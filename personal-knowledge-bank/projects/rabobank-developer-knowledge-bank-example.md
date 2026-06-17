---
type: Training Example
title: Rabobank developer knowledge bank example
description: Voorbeeld van hoe Rabobank-ontwikkelaars een eigen OKF-kennisbank kunnen bouwen voor trainingen, projecten en kennisdeling.
tags: [training, rabobank, knowledge-bank, example]
timestamp: 2026-06-17T00:00:00Z
---

# Rabobank developer knowledge bank example

## Doel

Dit document laat zien hoe Rabobank-ontwikkelaars een eigen persoonlijke kennisbank kunnen gebruiken om:

- technische kennis vast te leggen
- trainingsmateriaal te structureren
- projectcontext te bewaren
- AI-ondersteuning te laten werken op eigen kennis
- keuzes te maken op basis van strategie en energie

## Structuur

Gebruik deze mappen als uitgangspunt:

- `business/` — commerciële onderwerpen, klanttypes, tarieven en proposities
- `goals/` — strategische doelen, leerdoelen en werkweekvoorkeuren
- `learning/` — technische notities, architectuurinzichten en trainingsonderwerpen
- `decisions/` — beslisregels, keuzecriteria en belangrijke besluiten
- `routines/` — weekplanning, trainingsvoorbereiding en reviewroutines
- `personal/` — energie, waarden, reflectie en focusinzichten
- `agents/` — prompts en agentinstructies voor AI-assistenten
- `templates/` — herbruikbare notitietemplates voor trainingen, klanten en projecten
- `projects/` — project- of trainingsspecifieke context en evaluaties

## Gebruik in training

1. Laat ontwikkelaars hun eigen map kopiëren als startpunt.
2. Vraag hen om drie concrete notities te maken:
   - een `goals/`-doel voor een persoonlijk leertraject of project
   - een `learning/`-notitie over een technisch onderwerp of tool
   - een `projects/`-notitie met een trainings- of projectevaluatie
3. Laat ze één AI-prompt in `agents/` gebruiken om een voorstel of samenvatting te genereren.
4. Bespreek welke tags en metadata helpen om de kennis later terug te vinden.

## Voorbeeldworkflow

### Stap 1: noteer een leerdoel

Maak een bestand `goals/ai-agents-expert-worden.md` met:

- type: Learning Goal
- titel: wat je wil bereiken
- beschrijving: waarom dit belangrijk is
- tags: [ai, agents, learning]

### Stap 2: noteer een trainingsidee

Maak een bestand `learning/mcp-workshop-rabobank.md` met:

- doel
- doelgroep
- leerdoelen
- praktische cases
- demo's
- oefeningen

### Stap 3: noteer een projectevaluatie

Maak een bestand `projects/rabobank-mcp-training-evaluation.md` waarin je:

- beschrijft wat wel en niet werkte
- benoemt welke tooling en toegang nodig was
- geeft concrete aanbevelingen voor een volgende keer

### Stap 4: gebruik een AI-agent

Laat de ontwikkelaar `assistant-instructions.md` en één of twee relevante bestanden gebruiken als context voor een prompt die:

- een trainingsplan maakt
- een korte samenvatting schrijft
- een voorstel of e-mail opstelt

## Tips

- Houd bestanden kort en concreet.
- Gebruik tags om vergelijkbare notities te vinden.
- Werk `log.md` wekelijks bij.
- Gebruik `personal/energie-focus.md` om terugkerende werkpatronen te herkennen.
- Maak na elke training een korte evaluatie in `projects/`.

## Waarom dit werkt

Een persoonlijke kennisbank maakt kennis herbruikbaar, helpt bij training en projectwork, en zorgt dat AI-tools zoals Copilot of ChatGPT beter aansluiten op de eigen context. Voor Rabobank-ontwikkelaars is het vooral handig omdat de kennisbank:

- lokaal kan draaien
- veilig als Markdown wordt opgeslagen
- overzichtelijk is voor het team
- direct bruikbaar is voor hands-on training en agentontwikkeling
