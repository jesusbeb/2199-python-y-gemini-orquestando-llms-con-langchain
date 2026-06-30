from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage
from my_models import GEMINI_FLASH
from my_keys import GEMINI_API_KEY, COHERE_API_KEY
from my_helper import encode_image
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


"""
# Instanciamos el modelo de lenguaje de Cohere con la API Key
llm = ChatCohere(
    cohere_api_key=COHERE_API_KEY,
)

respuesta = llm.invoke([HumanMessage(content="Cuales canales mexicanos de Youtube me recomiendas para aprender a programar en Python?")])
print(f"Respuesta de Cohere: ", respuesta.content)
"""


# Instanciamos el modelo de lenguaje de Gemini con la API Key y el modelo deseado
llm = ChatGoogleGenerativeAI(
    api_key=GEMINI_API_KEY,
    model=GEMINI_FLASH
)

"""
respuesta = llm.invoke("Cuales canales mexicanos de Youtube me recomiendas para aprender a programar en Python?")
print(f"Respuesta de Gemini: ", respuesta.content)
"""

# Codificamos la imagen a base64 para poder enviarla al modelo
imagen = encode_image("datos/ejemplo_grafico.jpg")

# Creamos el template para el análisis de la imagen con la imagen codificada en base64
# El template contiene un mensaje del sistema que indica al modelo que debe actuar como analista de imágenes y un mensaje del usuario que contiene la imagen codificada en base64.
template_analisis = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            Asume que eres analista de imagenes. Tu principal tarea consiste en: analizar una imagen
            para extraer las informaciones mas relevantes de manera objetiva.
            """
        ),
        (
            "user",
            [
                {
                    "type": "texto",
                    "text": "Describe la imagen: "
                },
                {
                    "type": "image_url",
                    "image_url": "data:image/jpeg;base64,{imagen_informada}"
                }
            ]
        )
    ]
)

# Creamos la cadena de análisis que combina el template, el modelo de lenguaje y un parser de salida para obtener la respuesta en formato de texto.
cadena_analisis = template_analisis | llm | StrOutputParser()

# Invocamos la cadena de análisis con la imagen codificada en base64 y obtenemos la respuesta del modelo.
respuesta_analisis = cadena_analisis.invoke({"imagen_informada": imagen})

print(f"Respuesta de Gemini: ", respuesta_analisis)