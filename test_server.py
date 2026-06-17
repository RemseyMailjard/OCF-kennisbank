"""Smoke tests for the knowledge-bank MCP server logic."""

import pytest

import server


def test_lists_all_markdown_files():
    files = server._list()
    assert "index.md" in files
    assert "profile/professional-profile.md" in files
    assert all(file.endswith(".md") for file in files)


def test_reads_a_known_file():
    content = server._read("profile/professional-profile.md")
    assert "# Professional Profile" in content


def test_search_finds_mcp():
    hits = server._search("MCP")
    assert any(h["file"] == "learnings/mcp-notes.md" for h in hits)


def test_path_traversal_is_blocked():
    with pytest.raises(ValueError):
        server._read("../../etc/passwd")


def test_non_markdown_is_rejected():
    with pytest.raises(ValueError):
        server._read("../pyproject.toml")


def test_lists_frontmatter_tags_and_types():
    assert "training" in server._list_tags()
    assert "Template" in server._list_types()


def test_search_metadata_filters_by_tag_and_folder():
    hits = server._search_metadata(tag="training", folder="templates")
    assert any(hit["file"] == "templates/training-template.md" for hit in hits)


def test_knowledge_map_groups_files_by_folder():
    knowledge_map = server._knowledge_map()
    assert "business" in knowledge_map
    assert any(item["file"] == "business/tarieven.md" for item in knowledge_map["business"])


def test_validation_reports_current_bank_status():
    result = server._validate_knowledge_bank()
    assert result["valid"] is True
    assert result["errors"] == []


def test_frontmatter_parser_supports_yaml_timestamps():
    metadata = server._metadata_for(server.KB_ROOT / "profile" / "professional-profile.md")
    assert metadata["timestamp"]
    assert "profile" in metadata["tags"]


def test_context_bundle_includes_assignment_decision_notes():
    bundle = server._context_bundle("assignment")
    files = [item["file"] for item in bundle["files"]]
    assert "business/ideale-klant.md" in files
    assert "decisions/welke-opdrachten-aannemen.md" in files


def test_link_graph_finds_outgoing_links_and_backlinks():
    outgoing = server._list_outgoing_links("business/tarieven.md")
    assert any(link["target"] == "decisions/dagtarief-strategie.md" for link in outgoing)

    backlinks = server._find_backlinks("business/tarieven.md")
    assert any(backlink["source"] == "goals/skills4-it-groeien.md" for backlink in backlinks)


def test_related_notes_include_link_or_tag_reasons():
    related = server._find_related_notes("business/tarieven.md")
    assert related["file"] == "business/tarieven.md"
    assert any(item["reasons"] for item in related["related"])


def test_find_orphan_notes_returns_metadata():
    orphans = server._find_orphan_notes()
    assert all("file" in note and "title" in note for note in orphans)


def test_goal_alignment_context_and_signals():
    context = server._goal_alignment_context("AI agents training")
    files = [item["file"] for item in context["files"]]
    assert "goals/ai-agents-expert-worden.md" in files

    signals = server._check_goal_alignment("AI agents training")
    assert "context_files" in signals


def test_recent_notes_are_timestamp_ordered():
    recent = server._list_recent_notes(limit=3)
    assert len(recent) == 3
    assert all("timestamp" in note for note in recent)


def test_find_stale_notes_uses_frontmatter_timestamp(tmp_path, monkeypatch):
    old_note = tmp_path / "old.md"
    old_note.write_text(
        "---\ntype: Note\ntitle: Old\ndescription: Old note\ntags: [note]\ntimestamp: 2020-01-01T00:00:00Z\n---\n\n# Old\n",
        encoding="utf-8",
    )
    fresh_note = tmp_path / "fresh.md"
    fresh_note.write_text(
        "---\ntype: Note\ntitle: Fresh\ndescription: Fresh note\ntags: [note]\ntimestamp: 2999-01-01T00:00:00Z\n---\n\n# Fresh\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(server, "KB_ROOT", tmp_path.resolve())

    stale = server._find_stale_notes(days_old=90)

    assert [note["file"] for note in stale] == ["old.md"]


def test_find_placeholder_text_reports_unfinished_lines(tmp_path, monkeypatch):
    note = tmp_path / "note.md"
    note.write_text("# Note\n\n- \n\nTODO: finish this\n", encoding="utf-8")
    monkeypatch.setattr(server, "KB_ROOT", tmp_path.resolve())

    findings = server._find_placeholder_text()

    assert any(finding["text"] == "TODO: finish this" for finding in findings)
    assert any(finding["text"] == "-" for finding in findings)


def test_validate_index_coverage_finds_missing_links(tmp_path, monkeypatch):
    folder = tmp_path / "business"
    folder.mkdir()
    (folder / "index.md").write_text("# Business\n", encoding="utf-8")
    (folder / "tarieven.md").write_text("# Tarieven\n", encoding="utf-8")
    monkeypatch.setattr(server, "KB_ROOT", tmp_path.resolve())

    result = server._validate_index_coverage()

    assert result["valid"] is False
    assert result["errors"] == ["business/index.md: missing link to business/tarieven.md"]


def test_validate_index_coverage_accepts_linked_notes(tmp_path, monkeypatch):
    folder = tmp_path / "business"
    folder.mkdir()
    (folder / "index.md").write_text("# Business\n\n- [Tarieven](tarieven.md)\n", encoding="utf-8")
    (folder / "tarieven.md").write_text("# Tarieven\n", encoding="utf-8")
    monkeypatch.setattr(server, "KB_ROOT", tmp_path.resolve())

    result = server._validate_index_coverage()

    assert result["valid"] is True
    assert result["checked_indexes"] == ["business/index.md"]


def test_training_context_includes_training_materials():
    context = server._training_context("Power Automate")
    files = [item["file"] for item in context["files"]]
    assert "templates/training-template.md" in files
    assert "routines/trainingsvoorbereiding.md" in files
    assert "business/trainingsdomeinen.md" in files


def test_capture_inbox_note_creates_frontmatter_safe_inbox(tmp_path, monkeypatch):
    monkeypatch.setattr(server, "KB_ROOT", tmp_path.resolve())

    result = server._capture_inbox_note("Idea for a governance workshop", "meeting", ["idea"])
    content = (tmp_path / "inbox.md").read_text(encoding="utf-8")

    assert result["file"] == "inbox.md"
    assert "type: Inbox" in content
    assert "Idea for a governance workshop" in content
    assert server._validate_knowledge_bank()["valid"] is True


def test_template_listing_and_preview_do_not_write(tmp_path, monkeypatch):
    templates = tmp_path / "templates"
    templates.mkdir()
    (templates / "training-template.md").write_text(
        "---\ntype: Template\ntitle: Training template\ndescription: Demo\ntags: [template]\ntimestamp: 2026-06-17T00:00:00Z\n---\n\n# Old title\n\nBody",
        encoding="utf-8",
    )
    monkeypatch.setattr(server, "KB_ROOT", tmp_path.resolve())

    templates_list = server._list_templates()
    preview = server._preview_note_from_template(
        "training-template",
        "Previewed Training",
        "learning/previewed-training.md",
    )

    assert templates_list[0]["file"] == "templates/training-template.md"
    assert preview["content"].count("# Previewed Training") == 1
    assert not (tmp_path / "learning" / "previewed-training.md").exists()


def test_append_to_log_writes_only_log_file(tmp_path, monkeypatch):
    (tmp_path / "log.md").write_text("# Log\n", encoding="utf-8")
    monkeypatch.setattr(server, "KB_ROOT", tmp_path.resolve())

    result = server._append_to_log("- captured insight", "Test entry")

    assert result["file"] == "log.md"
    assert "Test entry" in (tmp_path / "log.md").read_text(encoding="utf-8")
    assert "captured insight" in (tmp_path / "log.md").read_text(encoding="utf-8")


def test_create_note_from_template_creates_markdown_inside_bank(tmp_path, monkeypatch):
    templates = tmp_path / "templates"
    templates.mkdir()
    (templates / "training-template.md").write_text("# Old title\n\nBody", encoding="utf-8")
    monkeypatch.setattr(server, "KB_ROOT", tmp_path.resolve())

    result = server._create_note_from_template(
        "training-template",
        "learning/copilot-finance.md",
        "Copilot Finance",
    )

    created = tmp_path / "learning" / "copilot-finance.md"
    assert result["file"] == "learning/copilot-finance.md"
    assert created.read_text(encoding="utf-8").startswith("# Copilot Finance")


def test_create_note_from_template_refuses_path_traversal(tmp_path, monkeypatch):
    templates = tmp_path / "templates"
    templates.mkdir()
    (templates / "training-template.md").write_text("# Old title\n", encoding="utf-8")
    monkeypatch.setattr(server, "KB_ROOT", tmp_path.resolve())

    with pytest.raises(ValueError):
        server._create_note_from_template("training-template", "../outside.md", "Nope")


def test_specific_create_helpers_choose_safe_default_paths(tmp_path, monkeypatch):
    templates = tmp_path / "templates"
    templates.mkdir()
    (templates / "training-template.md").write_text("# Old title\n", encoding="utf-8")
    (templates / "business-client-template.md").write_text("# Old title\n", encoding="utf-8")
    (templates / "concept-template.md").write_text("# Old title\n", encoding="utf-8")
    monkeypatch.setattr(server, "KB_ROOT", tmp_path.resolve())

    training = server._create_training_note("Power Automate Basics")
    client = server._create_client_note("Contoso Bank")
    decision = server._create_decision_note("Accept Managed Services")

    assert training["file"] == "learning/power-automate-basics.md"
    assert client["file"] == "business/clients/contoso-bank.md"
    assert decision["file"] == "decisions/accept-managed-services.md"
