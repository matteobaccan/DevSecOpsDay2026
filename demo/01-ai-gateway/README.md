# Demo 1: AI Gateway (LiteLLM Proxy)

Un proxy centrale davanti a Claude: un solo punto per policy, audit, rate-limit e virtual key — invece di ogni app/agente con la propria chiave API diretta.

## Setup (2 minuti)

```bash
pip install 'litellm[proxy]'
export ANTHROPIC_API_KEY=sk-ant-...
litellm --config config.yaml
# proxy attivo su http://localhost:4000, compatibile OpenAI
```

## Momento 1 — far passare Claude Code attraverso il gateway

Aggiungi al `settings.json` di Claude Code (o esportale come env var):

```json
{ "env": { "ANTHROPIC_BASE_URL": "http://localhost:4000", "ANTHROPIC_API_KEY": "sk-1234" } }
```

Lancia una query `claude` qualsiasi: la richiesta passa dal proxy locale, non da Anthropic direttamente — mostralo nei log del terminale dove gira `litellm`.

## Momento 2 — virtual key con rate-limit/budget

```bash
curl http://localhost:4000/key/generate \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{"models":["claude-sonnet-5"],"max_budget":1,"rpm_limit":2,"duration":"1h"}'
```

Usa la chiave generata per due richieste consecutive rapide: la terza viene rifiutata (rate limit) — dimostra il controllo centralizzato che un accesso diretto all'API non avrebbe.

## Riferimenti

- LiteLLM Docker Quick Start: https://docs.litellm.ai/docs/proxy/docker_quick_start
- LiteLLM Proxy CLI Quick Start: https://docs.litellm.ai/docs/proxy/quick_start
- LiteLLM Virtual Keys: https://docs.litellm.ai/docs/proxy/virtual_keys
- Claude Code settings (env vars): https://code.claude.com/docs/en/settings
