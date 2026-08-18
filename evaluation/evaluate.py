import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


import json
import time
from pathlib import Path

from app.retriever import retrieve
from app.generator import generate_answer


QUESTIONS_FILE = Path("evaluation/questions.json")
RESULTS_FILE = Path("evaluation/results.json")


def main():
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        questions = json.load(f)

    results = []
    passed = 0
    total_latency = 0

    for item in questions:
        question = item["question"]
        expected = item["expected_answer"]

        start = time.perf_counter()

        retrieved = retrieve(question, k=3)

        context = "\n".join(
            result["text"] for result in retrieved
        )

        answer = generate_answer(question, context)

        latency = time.perf_counter() - start
        total_latency += latency

        expected_words = set(expected.lower().split())
        answer_words = set(answer.lower().split())

        overlap = len(expected_words & answer_words)
        accuracy = overlap / len(expected_words)

        is_pass = accuracy >= 0.5

        if is_pass:
            passed += 1

        results.append({
            "question": question,
            "expected_answer": expected,
            "generated_answer": answer,
            "latency_seconds": round(latency, 4),
            "accuracy": round(accuracy, 4),
            "passed": is_pass
        })

        print("\nQuestion:", question)
        print("Answer:", answer)
        print("Accuracy:", f"{accuracy:.2%}")
        print("Latency:", f"{latency:.4f}s")
        print("Passed:", is_pass)

    average_latency = total_latency / len(questions)

    summary = {
        "total_tests": len(questions),
        "passed": passed,
        "accuracy": round((passed / len(questions)) * 100, 2),
        "average_latency_seconds": round(average_latency, 4),
        "results": results
    }

    with open(RESULTS_FILE, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print("\n==============================")
    print("EVALUATION SUMMARY")
    print("==============================")
    print("Tests:", len(questions))
    print("Passed:", passed)
    print("Accuracy:", summary["accuracy"], "%")
    print("Average latency:", summary["average_latency_seconds"], "seconds")
    print("==============================")


if __name__ == "__main__":
    main()