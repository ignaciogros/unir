import os
from openai import AzureOpenAI


class AzureProvider:
    def __init__(self):
        self._client = AzureOpenAI(
            azure_endpoint=os.environ["AZURE_ENDPOINT"],
            api_key=os.environ["AZURE_API_KEY"],
            api_version=os.environ.get("AZURE_API_VERSION", "2024-02-01"),
        )
        self._deployment = os.environ["AZURE_DEPLOYMENT"]

    def chat(self, messages: list[dict], temperature: float, max_tokens: int, top_p: float) -> str:
        response = self._client.chat.completions.create(
            model=self._deployment,
            messages=messages,
            temperature=temperature,
            max_completion_tokens=max_tokens,
            top_p=top_p,
        )
        return response.choices[0].message.content
