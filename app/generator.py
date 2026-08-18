import re


def generate_answer(question, context):
    question_words = {
        word.lower()
        for word in re.findall(r"\b\w+\b", question)
        if len(word) > 2
    }

    sentences = re.split(r"(?<=[.!?])\s+", context.strip())

    relevant = []

    for sentence in sentences:
        words = {
            word.lower()
            for word in re.findall(r"\b\w+\b", sentence)
            if len(word) > 2
        }

        score = len(question_words & words)

        if score > 0:
            relevant.append((score, sentence.strip()))

    if not relevant:
        return "I couldn't find that information in the provided documents."

    relevant.sort(key=lambda item: item[0], reverse=True)

    return " ".join(
        sentence for _, sentence in relevant[:2]
    )