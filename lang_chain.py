from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from my_models import GEMINI_FLASH
from my_keys import GEMINI_API_KEY
from my_helper import encode_image


# Instanciamos el modelo de lenguaje de Gemini con la API Key y el modelo deseado
llm = ChatGoogleGenerativeAI(
    api_key=GEMINI_API_KEY,
    model=GEMINI_FLASH
)

# Codificamos la imagen a base64 para poder enviarla al modelo
imagen = encode_image("datos/ejemplo_grafico.jpg")

# Creamos el mensaje que se enviará al modelo
pregunta = "Describe la imagen: "

# Creamos un mensaje de tipo HumanMessage que contiene tanto el texto de la pregunta como la imagen codificada en base64
mensaje = HumanMessage(
    content = [
        {
            "type": "text", 
            "text": pregunta
        }, 
        {
            "type": "image_url", 
            "image_url": f'data:image/jpeg;base64,{imagen}'
        }
    ]
)

# Invocamos el modelo de lenguaje con el mensaje creado y obtenemos la respuesta
respuesta = llm.invoke([mensaje])

print(respuesta)
