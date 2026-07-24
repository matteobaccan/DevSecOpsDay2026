# Demo dal vivo: DevSecOps Day 2026

Tre esempi minimi, pensati per essere mostrati sul palco durante il talk "Oltre il Chatbot". Ogni cartella è indipendente e ha il proprio README con i comandi esatti.

| # | Slide corrispondente | Cosa mostra | Setup |
|---|---|---|---|
| 1 | Hardening DevSecOps: AI Gateway | Un singolo proxy centrale (LiteLLM) davanti a Claude, con virtual key, rate-limit e guardrail | [`01-ai-gateway/`](01-ai-gateway/README.md) |
| 2 | Hardening DevSecOps: Prompt Shields | Un classificatore locale (Meta PromptGuard 2) che assegna uno score di jailbreak a un prompt benigno vs uno ostile | [`02-prompt-shields/`](02-prompt-shields/README.md) |
| 3 | Hardening DevSecOps: Output Moderation | Blocco di un output che tenta di esfiltrare un segreto (AWS key / SSN), riusando lo stesso proxy del demo #1 | [`03-output-moderation/`](03-output-moderation/README.md) |

## Preparazione da fare PRIMA del talk (non il giorno stesso)

- **Demo #2**: richiede l'accettazione della licenza Llama su Hugging Face per scaricare `meta-llama/Llama-Prompt-Guard-2-22M` — il gating può richiedere da pochi minuti a 1-2 ore. Fallo con un giorno di anticipo ed esegui `huggingface-cli login`.
- **Demo #1 e #3**: serve una `ANTHROPIC_API_KEY` valida esportata come variabile d'ambiente.
- Tutti e tre girano in locale, senza account cloud da provisionare (Azure/Lakera/Purview citati in slide sono volutamente esclusi dai demo perché non self-hostable in 5 minuti).
