from typing import Protocol


class Provider(Protocol):
    def chat(self, messages: list[dict], temperature: float, max_tokens: int, top_p: float) -> str: ...


def get_provider(name: str) -> Provider:
    if name == "azure":
        from .azure import AzureProvider
        return AzureProvider()
    if name == "ollama":
        from .ollama import OllamaProvider
        return OllamaProvider()
    if name == "openai_compat":
        from .openai_compat import OpenAICompatProvider
        return OpenAICompatProvider()
    raise ValueError(f"Unknown provider: {name!r}. Choose from: azure, ollama, openai_compat")
