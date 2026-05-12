import os
from dotenv import load_dotenv
from providers import get_provider

load_dotenv()

provider = get_provider(os.environ.get("PROVIDER", "azure"))

temperature = float(os.environ.get("TEMPERATURE", 0.7))
max_tokens  = int(os.environ.get("MAX_TOKENS", 512))
top_p       = float(os.environ.get("TOP_P", 1.0))

system_prompt = os.environ.get("SYSTEM_PROMPT", "Eres un asistente útil y conciso.")

messages: list[dict] = [{"role": "system", "content": system_prompt}]

print("Chatbot iniciado. Escribe 'salir' para terminar.\n")

while True:
    user_input = input("Tú: ").strip()
    if not user_input:
        continue
    if user_input.lower() == "salir":
        print("¡Hasta luego!")
        break

    messages.append({"role": "user", "content": user_input})

    response = provider.chat(messages, temperature, max_tokens, top_p)

    messages.append({"role": "assistant", "content": response})
    print(f"Asistente: {response}\n")
