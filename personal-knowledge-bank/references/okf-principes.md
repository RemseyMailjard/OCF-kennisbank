---
type: Reference
title: OKF principes
description: Samenvatting van de belangrijkste OKF-principes toegepast op Remsey OS.
tags: [okf, reference, kennisbeheer]
timestamp: 2026-06-14T18:43:13Z
---

# Kernidee

OKF staat voor een eenvoudige manier om kennis vast te leggen als een map met Markdown-bestanden en YAML-frontmatter.

# Waarom dit werkt

- Leesbaar voor mensen zonder speciale tooling.
- Parseerbaar door AI-agenten.
- Goed te versiebeheer met Git.
- Portable tussen tools en organisaties.
- Eenvoudig uit te breiden zonder centrale schema’s.

# Toepassing in deze bundel

Elk bestand beschrijft één concept, zoals een doel, routine, strategie, klanttype, training of prompt. De frontmatter maakt het concept vindbaar en filterbaar. De Markdown-body bevat de echte inhoud.

# Minimale regel

Elk conceptbestand heeft een YAML-frontmatter-blok met minimaal een niet-lege `type`.

# Praktische aanbeveling

Gebruik deze bundel als levende kennisbasis. Werk kleine bestanden regelmatig bij in plaats van grote documenten zelden.
