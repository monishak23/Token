from google import genai

client = genai.Client(api_key="")


# Exercise 1 — count tokens of different inputs
texts = [
    "Hello",
    "Hello world how are you",
    "def fibonacci(n): return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)",
    "नमस्ते दुनिया",
    open("ai_report.txt").read()
]

for text in texts:
    result = client.models.count_tokens(
        model="gemini-2.0-flash-lite",
        contents=text
    )
    chars = len(text)
    ratio = round(chars / result.total_tokens, 1) if result.total_tokens else 0
    print(f"{text[:40]:<40} → {result.total_tokens:>5} tokens  ({ratio} chars/token)")