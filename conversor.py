from gtts import gTTS
from playsound import playsound

# Transformando texto em áudio com Python

audio = 'audio.mp3'
idioma = 'pt-br'

sp = gTTS(
    text='Meu primeiro áudio gerado com Python!',
    lang=idioma
)

sp.save(audio)
playsound(audio)


