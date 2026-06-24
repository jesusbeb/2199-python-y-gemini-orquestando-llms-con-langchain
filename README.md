# Título del proyecto

2199 - Python y Gemini: Orquestando LLMs con LangChain

## 🔨 Funcionalidades del proyecto

En este proyecto, utilizaremos LangChain como framework principal para orquestar una solución integrada de análisis y organización de imágenes enriquecidas con anotaciones inteligentes. LangChain será empleado debido a su capacidad para conectar y gestionar flujos complejos que combinan IA multimodal y modelos de lenguaje, lo que permite un desarrollo más modular y escalable.

![](img/amostra.gif)

## ✔️ Técnicas y tecnologías utilizadas

Las técnicas y tecnologías utilizadas son:

- Programación en Python  
- Uso de la API Gemini  
- Uso del framework LangChain  
- Cadenas simples  
- Agente orquestador  
- Agente como herramientas  

## 🛠️ Abrir y ejecutar el proyecto

Después de descargar el proyecto, puedes abrirlo con Visual Studio Code. A continuación, es necesario preparar tu entorno. Para ello usamos la terminal cmd dentro VS Code:

### venv en Windows:

```bash
python -m venv .venv-gemini-3  --> Crea el ambiente virtual
.\.venv-gemini-3\Scripts\activate  --> Activa el ambiente virtual creado del directorio .venv
````

### venv en Mac/Linux:

```bash
python3 -m venv .venv-gemini-3
source .venv-gemini-3/bin/activate
```

Después, instala los paquetes utilizando (se debe estar dentro del mismo directorio en que se encuentra requirements.txt):

```bash
pip install -r requirements.txt
```


Si se tiene problemas por estar usando librerias desactualizadas, ejecutamos los siguientes comandos, teniendo activo el ambiente virtual:

python.exe -m pip install --upgrade pip   --> Actualiza el instalador de python
pip install -U langchain langchain-community langchain-cohere langchain-text-splitters langsmith   --> Actualiza los paquetes de LangChain


Despues de esto, es necesario cambiar la variable en my_models.py para asegurar que use la version mas reciente y estable:

GEMINI_FLASH = "gemini-flash-latest"


## 🔑 Generar API\_KEYs y asociarlas al archivo .env

```python
GEMINI_API_KEY = "TU_API_KEY_AQUÍ"
COHERE_API_KEY = "TU_API_KEY_AQUÍ"
```
