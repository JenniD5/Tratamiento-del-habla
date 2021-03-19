#importar modulo

import speech_recognition as sr

#definir 
r = sr.Recognizer()

#definir archivo de audio
audio_file = sr.AudioFile('pato-el-pez.wav')

#speech reognition
with audio_file as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)
    result = r.recognize_google(audio, language="es-Mx")

#exportar resultados 
with open('resutado_pato_el_pez.txt', mode='w') as file:
    file.write("texto detectado:  ")
    file.write("")
    file.write(result)
    print("listo :)")