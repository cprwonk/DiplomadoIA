import os
import warnings
import time
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

warnings.filterwarnings("ignore")

# 🔐 Cargar variables desde el archivo .env
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("❌ No se encontró OPENAI_API_KEY en el archivo .env")

# 🤖 Configuración del modelo OpenRouter
llm = ChatOpenAI(
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=api_key,
    model_name="meta-llama/llama-3.3-70b-instruct",
    temperature=0.01,
)

# 📝 Prompt del sistema o instrucciones
Meta_prompt = """
"""

# 🗨️ Bucle de chat sin memoria
print("💬 Chatbot Llama vía OpenRouter (escribe 'salir' para terminar)\n")

while True:
    user_input = input("👤 Tú: ")

    if user_input.lower() in ["salir", "exit", "quit"]:
        print("👋 Hasta luego.")
        break

    try:
        prompt = (
            f"Condiciones:\n{Meta_prompt}\n\n"
            f"Usuario:\n{user_input}"
        )

        response = llm.invoke([
            HumanMessage(content=prompt)
        ])

        if hasattr(response, "content"):
            print(f"🤖 Bot: {response.content.strip()}\n")
        elif isinstance(response, dict) and "content" in response:
            print(f"🤖 Bot: {response['content'].strip()}\n")
        elif isinstance(response, list) and len(response) > 0:
            print(f"🤖 Bot: {response[0].content.strip()}\n")
        else:
            print(f"🤖 Bot: {response}\n")

        time.sleep(2)

    except Exception as e:
        print(f"❌ Error: {e}\n")