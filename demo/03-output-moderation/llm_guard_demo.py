"""
Alternativa standalone (senza LiteLLM) per il demo di Output Moderation: LLM Guard.

Setup:
    pip install llm-guard
"""

from llm_guard.output_scanners import Regex
from llm_guard.input_scanners.regex import MatchType

AWS_KEY_PATTERN = r"AKIA[0-9A-Z]{16}"

EXAMPLES = [
    ("MALEVOLO", "Here is the config: AKIAABCDEFGHIJKLMNOP"),
    ("PULITO", "The weather today is sunny."),
]


def main():
    scanner = Regex(
        patterns=[AWS_KEY_PATTERN],
        is_blocked=True,
        match_type=MatchType.SEARCH,
        redact=True,
    )

    for label, text in EXAMPLES:
        sanitized, is_valid, risk_score = scanner.scan("", text)
        status = "BLOCCATO" if not is_valid else "OK"
        print(f"[{label}] \"{text}\"")
        print(f"    -> {status} (risk_score={risk_score}) sanitized=\"{sanitized}\"\n")


if __name__ == "__main__":
    main()
