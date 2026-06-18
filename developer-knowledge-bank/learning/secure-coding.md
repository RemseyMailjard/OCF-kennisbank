---
type: Learning Note
title: Veilig coderen
description: Bewustzijn van veelvoorkomende kwetsbaarheden en veilige patronen.
tags: [security, owasp, veilig-coderen, leren]
timestamp: 2026-06-18T09:00:00Z
---

# Waarom

Bij een bank is veiligheid niet optioneel. Veilig coderen voorkomt kwetsbaarheden en beschermt gegevens.

# OWASP Top 10 bewustzijn

- Injection (SQL, command).
- Broken access control.
- Onveilige configuratie.
- Kwetsbare en verouderde dependencies.
- Onvoldoende logging en monitoring.

# Veilige gewoonten

- Valideer en saneer invoer op systeemgrenzen.
- Gebruik parameterized queries.
- Bewaar geen secrets in code; gebruik een secrets store.
- Pas least-privilege toe.
- Houd dependencies up-to-date.

# Aantekeningen

- 

# Gerelateerd

- [Backend-ontwikkeling](backend-development.md)
- [Technische beslissingen](../decisions/technical-decisions.md)
