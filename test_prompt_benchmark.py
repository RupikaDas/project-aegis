from src.evaluation.prompt_benchmark import (
    compare_prompt_versions
)

results = compare_prompt_versions()

print("\n=== PROMPT BENCHMARK ===\n")

for prompt, score in results.items():
    print(
        f"{prompt}: {score}%"
    )