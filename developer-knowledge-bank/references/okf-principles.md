---
type: Reference
title: OKF-principes
description: De uitgangspunten achter deze Open Knowledge Format kennisbundel.
timestamp: 2025-01-15T09:00:00
tags: [okf, kennisbeheer, principes]
---

# Wat is OKF?

OKF (Open Knowledge Format) is een eenvoudige, open manier om persoonlijke en
professionele kennis vast te leggen in platte Markdown-bestanden. De bundel is
zowel voor mensen als voor AI-tools goed leesbaar.

## Principes

1. **Platte tekst eerst** - alles is Markdown, geen database of propriëtair formaat.
2. **Frontmatter voor structuur** - elk inhoudelijk bestand begint met YAML
   frontmatter (`type`, `title`, `description`, `timestamp`, `tags`).
3. **Onderling gelinkt** - bestanden verwijzen naar elkaar met relatieve links,
   zodat kennis een navigeerbaar netwerk vormt.
4. **Mappen per thema** - `goals/`, `work/`, `learning/`, `decisions/`,
   `routines/`, `personal/`, `agents/`, `templates/` en `references/`.
5. **Index per map** - elke map heeft een `index.md` die de inhoud ontsluit.
6. **Klein en onderhoudbaar** - liever korte, actuele notities dan lange,
   verouderde documenten.

## Waarom OKF voor een developer?

* Je houdt grip op je doelen, beslissingen en leerpad op één plek.
* AI-assistenten kunnen jouw context gebruiken zonder dat je alles opnieuw uitlegt.
* De bundel groeit met je mee en blijft eigendom van jou.

Zie ook [HOW_TO_USE](../HOW_TO_USE.md) voor praktische werkwijzen.
