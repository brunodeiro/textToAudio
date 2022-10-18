
# Maneira alternativa de transformar o texto em áudio com Python

import pyttsx3

# Carrega a biblioteca
engine = pyttsx3.init()

# O texto que a engine vai usar
engine.say("Olá, como vai ?")
engine.say("Esse é o meu segundo áudio gerado com Python") 

#Executa
engine.runAndWait()