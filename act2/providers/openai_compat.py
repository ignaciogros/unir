import os
from openai import OpenAI


class OpenAICompatProvider:
    def __init__(self):
        self._client = OpenAI(
            base_url=os.environ["COMPAT_ENDPOINT"],
            api_key=os.environ["COMPAT_API_KEY"],
        )
        self._model = os.environ["COMPAT_MODEL"]

    def chat(self, messages: list[dict], temperature: float, max_tokens: int, top_p: float) -> str:
        response = self._client.chat.completions.create(
            model=self._model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
        )
        return response.choices[0].message.content
