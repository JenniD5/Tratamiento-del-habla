#importar modulo

import speech_recognition as sr

#definir 
r = sr.Recognizer()

#definir archivo de audio
audio_file = sr.AudioFile('good-morningMan.wav')

#speech reognition
with audio_file as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)
    result = r.recognize_google(audio, language="en-Us")

#exportar resultados 
with open('resutl.txt', mode='w') as file:
    file.write("texto detectado:  ")
    file.write("/")
    file.write(result)
    print("listo :)")