---
type: Guide
title: Hoe gebruik je deze developer-kennisbundel?
description: Praktische handleiding om deze generieke developer-kennisbundel dagelijks te gebruiken voor werk, leren, beslissingen en persoonlijk leven.
tags: [okf, handleiding, kennisbank, developer, productiviteit]
timestamp: 2026-06-18T09:00:00Z
---

# Hoe gebruik je deze developer-kennisbundel?

Deze map is jouw persoonlijke kennisbasis als ontwikkelaar. Elk `.md`-bestand beschrijft één concept: een doel, project, routine, beslissing, leerpad of persoonlijk inzicht.

Zie de bundel niet als "een map met documenten", maar als jouw **persoonlijke besturingssysteem** voor werk, groei, keuzes en balans.

# De kern: Capture, Curate, Consult, Create

```text
1. Capture  → snel vastleggen
2. Curate   → ordenen en aanscherpen
3. Consult  → raadplegen bij keuzes
4. Create   → gebruiken om output te maken
```

- **Capture**: leg taken, inzichten, bugs en ideeën direct vast in [inbox.md](inbox.md), zonder ze perfect te maken.
- **Curate**: werk losse notities later uit tot nette concepten met frontmatter en duidelijke koppen.
- **Consult**: gebruik je bundel als spiegel bij keuzes (past dit bij mijn doelen, team, werkwijze?).
- **Create**: gebruik je kennis als input voor Copilot of ChatGPT bij standups, documentatie of e-mails.

# Aanbevolen workflow

1. **Dagelijks**: leg losse notities vast in `inbox.md`; werk ze op een rustig moment uit.
2. **Per sprint**: werk `work/current-projects.md` en `decisions/` bij.
3. **Wekelijks**: doe een review met het template in `templates/weekly-review-template.md`.
4. **Per kwartaal**: herzie je `goals/` en `learning/learning-plan.md`.
5. **Bij AI-gebruik**: laat een agent eerst relevante bestanden lezen voordat die output maakt.

# Waar zet je wat?

| Situatie | Waar zet je het? |
|---|---|
| Nieuwe taak of bug | `inbox.md` of `work/current-projects.md` |
| Technische keuze | `decisions/technical-decisions.md` |
| Iets nieuws geleerd | `learning/` |
| Inzicht over energie/focus | `personal/health.md` |
| Loopbaanwens | `goals/career-growth.md` |
| 1-op-1 met je lead | `templates/one-on-one-template.md` |
| Reflectie op de week | `log.md` of `personal/reflection-questions.md` |

# Minimale frontmatter

Elk conceptbestand bevat minimaal:

```yaml
---
type: Concept
title: Titel
description: Korte omschrijving
tags: [tag1, tag2]
timestamp: 2026-06-18T00:00:00Z
---
```

# Tip

Gebruik korte, duidelijke bestanden. Liever tien kleine bestanden dan één groot document.
