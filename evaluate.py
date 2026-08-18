@'
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
        accuracy = overlap / len(expected_words) if expected_words else 0

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

        print(f"\nQuestion: {question}")
        print(f"Answer: {answer}")
        print(f"Accuracy: {accuracy:.2%}")
        print(f"Latency: {latency:.4f}s")
        print(f"Passed: {is_pass}")

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
    print(f"Tests: {len(questions)}")
    print(f"Passed: {passed}")
    print(f"Accuracy: {summary['accuracy']}%")
    print(f"Average latency: {summary['average_latency_seconds']} seconds")
    print("==============================")


if __name__ == "__main__":
    main()
'@ | Set-Content evaluation\evaluate.py