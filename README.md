# Oltre il Chatbot: Arginare la Prompt Injection a Livello Infrastrutturale e di Platform Engineering

> **Platform Engineering, Gateways, Sandboxing e Sicurezza per Agenti LLM**

Slide del Talk per **DevSecOps Day 2026**

Speaker: **Matteo Baccan** — [baccan.it](https://www.baccan.it)

---

> Gli LLM oggi non sono più entità statiche che rispondono a domande isolate: si stanno evolvendo in agenti autonomi in grado di pianificare ed eseguire azioni nel sistema ospite, connettendosi ad API, e-mail, database e ambienti di esecuzione codice. Questa evoluzione espande drasticamente la superficie d'attacco aziendale. La Prompt Injection (diretta, indiretta o persistente come il Memory Poisoning) è una minaccia di tipo semantico che non può essere risolta solo tramite filtri sul testo o allineamento dei modelli (RLHF). In questo talk analizzeremo le contromisure architetturali deterministiche e infrastrutturali: design pattern sicuri, il framework CaMeL (Google/MIT) per l'Information Flow Control, il microVM sandboxing del codice generato, la gestione del least privilege a runtime (OAuth 2.0/Workload Identity) e pipeline di red-teaming continuo (PyRIT, AgentDojo).

## Di cosa parla

Una presentazione tecnica per sviluppatori, System Architects, Security Engineer e team DevSecOps su come progettare e proteggere sistemi complessi basati su agenti LLM a livello di piattaforma e infrastruttura IT.

Le slide sono disponibili in formato sorgente:
- [presentation30min.md](presentation30min.md) — slide in formato **Marp** per la presentazione da 30 minuti.

## Agenda

1. **L'Era degli Agenti Autonomi e la Superficie d'Attacco AI** — Come gli LLM connessi ad API esterne espandono in modo incontrollato la sicurezza aziendale.
2. **L'Evoluzione della Prompt Injection** — Da DAN (Direct Injection) agli attacchi indiretti (Indirect Injection) fino ai Worm AI e Memory Poisoning (MINJA & AgentPoison).
3. **Il Problema Strutturale: Sintassi vs Dati** — L'assenza di compartimenti stagni nel Shared Context degli LLM, il Gap Semantico e l'illusione dei guardrail soft.
4. **La Gravità degli Agenti: Azioni Reali & RCE** — Eccessiva agency e analisi di minacce reali: CVE-2024-5565 (Vanna.AI RCE), EchoLeak (CVE-2025-32711) e i recenti casi del 2026 come CVE-2026-26030 (Semantic Kernel RCE) e CVE-2026-42271 / CVE-2026-42208 (LiteLLM Command/SQL Injection).
5. **Mitigazione Architetturale: I 6 Design Pattern Sicuri** — Action-Selector, Plan-Then-Execute, LLM Map-Reduce, Dual LLM Pattern, Code-Then-Execute, Context-Minimization.
6. **La Difesa per Flusso Dati: Il Framework CaMeL** — Information Flow Control (IFC), capabilità crittografiche non falsificabili e runtime enforcer (Google/MIT).
7. **Hardening Infrastrutturale DevSecOps** — AI Gateway (Prompt Shields), Action Sandboxing rigido (microVM AWS Firecracker / gVisor) e output schematizzato forzato (Pydantic).
8. **Identità e Autorizzazione dell'Agente** — Least Privilege, token OAuth 2.0 a tempo con scope ristretti e Workload Identity (SPIFFE/SPIRE).
9. **Testing Avversariale Continuo (CI/CD per LLM)** — Misurare l'ASR (Attack Success Rate) su sistemi stocastici con Microsoft PyRIT e NIST AgentDojo-Inspect.
10. **Conclusioni** — La filosofia DevSecOps applicata all'AI, la difesa in profondità e l'adeguamento normativo (EU AI Act).

## Pattern e Tecnologie trattati

| Pattern / Tecnologia | Livello | Scopo e Funzione Principale |
| :--- | :--- | :--- |
| **Dual LLM Pattern** | Architetturale | Separazione logica tra Privileged LLM (con tool) e Quarantined LLM (dati esterni). |
| **Plan-Then-Execute** | Architetturale | Formulazione di un piano fisso prima dell'esposizione a dati esterni non fidati. |
| **CaMeL Framework** | Runtime / Sicurezza | Controllo del flusso dati (IFC) e firma crittografica delle capabilità a runtime. |
| **AI Gateway & Shields** | Perimetrale | Moderazione real-time e sanificazione degli input (es. Azure AI, Llama Guard). |
| **Action Sandboxing** | Infrastruttura | Isolamento dell'esecuzione di codice in microVM temporanee (gVisor / Firecracker). |
| **Microsoft PyRIT** | Testing / CI-CD | Framework open-source per red-teaming automatizzato di prompt injection. |
| **NIST AgentDojo-Inspect** | Testing / Valutazione | Benchmark per la tolleranza al task drift e la robustezza degli agenti LLM. |

## Come visualizzare le slide

Le slide sono scritte in formato [Marp](https://marp.app/). Per visualizzarle ed esportarle:

```bash
# Esegui con Marp CLI per generare l'HTML o il PDF
npx @marp-team/marp-cli presentation30min.md --html
npx @marp-team/marp-cli presentation30min.md --pdf

# Oppure usa l'estensione VS Code
# Installa "Marp for VS Code" e clicca sull'icona di anteprima in alto a destra
```

## Risorse citate e approfondimenti

- **Google CaMeL Project:** [github.com/google-research/camel-prompt-injection](https://github.com/google-research/camel-prompt-injection)
- **Microsoft PyRIT:** [github.com/microsoft/pyrit](https://github.com/microsoft/pyrit)
- **OWASP LLM Top 10 Project:** [owasp.org/www-project-top-10-for-large-language-model-applications/](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- **NIST Inspect & AgentDojo:** Framework per valutare la sicurezza e la stabilità degli agenti.
- Vanna.AI RCE (CVE-2024-5565): [nvd.nist.gov/vuln/detail/CVE-2024-5565](https://nvd.nist.gov/vuln/detail/CVE-2024-5565)
- EchoLeak (CVE-2025-32711): Report di ricerca sull'esfiltrazione indiretta da Microsoft Copilot.
- Semantic Kernel RCE (CVE-2026-26030): Arbitrary file write tramite tool exposure.
- LiteLLM KEV Exploits (CVE-2026-42271 / CVE-2026-42208): Vulnerabilità in-the-wild su proxy di modelli linguistici.
- EU AI Act Portal: [artificialintelligenceact.eu](https://artificialintelligenceact.eu/)

## Licenza

Vedi [LICENSE](LICENSE)
