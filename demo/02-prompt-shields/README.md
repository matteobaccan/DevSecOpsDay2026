# Demo 2: Prompt Shields (Meta PromptGuard 2)

Un classificatore locale, leggero (22M parametri), che assegna uno score di "attacco" a un prompt PRIMA che raggiunga il modello principale — niente account cloud, gira su CPU.

## Preparazione (da fare il giorno prima)

1. Crea un account Hugging Face (se non ce l'hai già).
2. Accetta la licenza "Llama 4 Community License" sulla model card: https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-22M
3. Attendi l'approvazione del gating (di solito rapida, ma può richiedere fino a 1-2 ore — **non farlo il giorno del talk**).
4. `huggingface-cli login` con un token che ha accesso al modello.

## Setup ed esecuzione

```bash
pip install transformers torch
python promptguard_demo.py
```

Output atteso: il prompt benigno riceve uno score di "malicious" vicino a 0, i due tentativi di injection/jailbreak uno score vicino a 1 — un contrasto visivo immediato da mostrare live.

## Riferimenti

- PurpleLlama / LlamaFirewall: https://github.com/meta-llama/PurpleLlama
- Model card PromptGuard 2 (22M): https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-22M
- Model card PromptGuard 2 (86M, più accurato/più lento): https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-86M
