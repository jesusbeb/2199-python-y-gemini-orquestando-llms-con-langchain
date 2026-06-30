from langchain_google_genai import ChatGoogleGenerativeAI
from my_keys import GEMINI_API_KEY

# En este ejemplo, vamos a probar la conexión con Google Gemini utilizando la API Key y el modelo "gemini-1.5-flash-002".

# Vamos a probar inyectando el nombre directamente
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-002", 
    google_api_key=GEMINI_API_KEY
)

print("Conectando con Google Gemini...")

try:
    respuesta = llm.invoke("Hola, responde solo con la palabra: Funciona.")
    print("¡ÉXITO! La respuesta es:", respuesta.content)
except Exception as e:
    print("Sigue fallando. El error exacto es:", e)