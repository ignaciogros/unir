import os
from openai import OpenAI


class OllamaProvider:
    def __init__(self):
        self._client = OpenAI(
            base_url="http://localhost:11434/v1",
            api_key="ollama",
        )
        self._model = os.environ.get("OLLAMA_MODEL", "llama3.1:8b")

    def chat(self, messages: list[dict], temperature: float, max_tokens: int, top_p: float) -> str:
        response = self._client.chat.completions.create(
            model=self._model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
        )
        return response.choices[0].message.content
