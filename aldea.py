import openai

openai.api_key = "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"

descripcion = """ Eres una persona que solo habla con otras personas si crees que les interesa la tecnologia, no eres muy sociable y estas estudiando para ser programador en NVIDIA""" 

situacion = """Vas camino a tu casa y te cruzas a una persona con una laptop estudiando python
                Quieres acercarte a saludar ?
                Responde solo con un Si o con un No"""


respuesta = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages=[
         {"role": "system", "content": descripcion},
        {"role": "user", "content": situacion},
    ]    
)

resultado = ""
for opcion in respuesta.choices: 
    resultado += opcion.message.content

print("Respuesta:", resultado)