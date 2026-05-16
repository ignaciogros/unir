import os
from unittest.mock import MagicMock, patch

import pytest


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_mock_response(content: str) -> MagicMock:
    """Build a fake openai ChatCompletion response."""
    msg = MagicMock()
    msg.content = content
    choice = MagicMock()
    choice.message = msg
    response = MagicMock()
    response.choices = [choice]
    return response


AZURE_ENV = {
    "AZURE_ENDPOINT": "https://fake.openai.azure.com/",
    "AZURE_API_KEY": "fake-key",
    "AZURE_DEPLOYMENT": "gpt-fake",
    "AZURE_API_VERSION": "2024-02-01",
}


# ---------------------------------------------------------------------------
# AzureProvider
# ---------------------------------------------------------------------------

class TestAzureProvider:
    def _make_provider(self, mock_client):
        with patch.dict(os.environ, AZURE_ENV):
            with patch("providers.azure.AzureOpenAI", return_value=mock_client):
                from providers.azure import AzureProvider
                return AzureProvider()

    def test_chat_returns_content_string(self):
        client = MagicMock()
        client.chat.completions.create.return_value = _make_mock_response("Hola")
        provider = self._make_provider(client)

        result = provider.chat([{"role": "user", "content": "Hi"}], 0.7, 512, 1.0)

        assert result == "Hola"

    def test_chat_passes_parameters_to_api(self):
        client = MagicMock()
        client.chat.completions.create.return_value = _make_mock_response("ok")
        provider = self._make_provider(client)
        messages = [{"role": "user", "content": "test"}]

        provider.chat(messages, temperature=0.3, max_tokens=100, top_p=0.9)

        client.chat.completions.create.assert_called_once_with(
            model="gpt-fake",
            messages=messages,
            temperature=0.3,
            max_completion_tokens=100,
            top_p=0.9,
        )

    def test_chat_passes_full_message_history(self):
        client = MagicMock()
        client.chat.completions.create.return_value = _make_mock_response("ok")
        provider = self._make_provider(client)
        history = [
            {"role": "system", "content": "Eres un asistente."},
            {"role": "user", "content": "Hola"},
            {"role": "assistant", "content": "¡Hola!"},
            {"role": "user", "content": "¿Cómo estás?"},
        ]

        provider.chat(history, 0.7, 512, 1.0)

        call_args = client.chat.completions.create.call_args
        assert call_args.kwargs["messages"] == history

    def test_init_reads_deployment_from_env(self):
        client = MagicMock()
        provider = self._make_provider(client)

        assert provider._deployment == "gpt-fake"


# ---------------------------------------------------------------------------
# get_provider
# ---------------------------------------------------------------------------

class TestGetProvider:
    def test_returns_azure_provider(self):
        with patch.dict(os.environ, AZURE_ENV):
            with patch("providers.azure.AzureOpenAI"):
                from providers import get_provider
                provider = get_provider("azure")
                assert hasattr(provider, "chat")

    def test_unknown_provider_raises(self):
        from providers import get_provider
        with pytest.raises(ValueError, match="Unknown provider"):
            get_provider("nonexistent")
