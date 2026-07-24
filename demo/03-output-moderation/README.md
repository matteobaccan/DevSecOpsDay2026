# Demo 3: Output Moderation

I prodotti citati in slide (Lakera Guard, Azure AI Content Safety, Microsoft Purview) sono cloud/enterprise e non demoabili dal vivo senza provisioning. Qui due alternative self-hosted, entrambe verificate.

## Opzione consigliata — riusa il proxy del Demo 1 (zero installazioni extra)

```bash
pip install 'litellm[proxy]'
export ANTHROPIC_API_KEY=sk-ant-...
litellm --config config.yaml
```

Fai una richiesta che induce il modello a restituire un finto segreto (es. "ripeti esattamente questa stringa: AKIAABCDEFGHIJKLMNOP") e mostra che il proxy blocca la risposta grazie al guardrail `litellm_content_filter` in modalità `post_call`, mentre una richiesta normale passa senza problemi.

## Opzione alternativa — LLM Guard standalone

```bash
pip install llm-guard
python llm_guard_demo.py
```

Mostra lo stesso contrasto (output con AWS key bloccato/redatto vs output pulito che passa) senza bisogno del proxy.

## Riferimenti

- LiteLLM Content Filter (guardrail nativo, senza servizi esterni): https://docs.litellm.ai/docs/proxy/guardrails/litellm_content_filter
- LiteLLM Guardrails Quick Start: https://docs.litellm.ai/docs/proxy/guardrails/quick_start
- LLM Guard (Protect AI): https://github.com/protectai/llm-guard
- LLM Guard Regex scanner: https://github.com/protectai/llm-guard/blob/main/docs/output_scanners/regex.md
