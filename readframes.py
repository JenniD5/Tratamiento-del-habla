import wave
#cargar archivo wav en la variable 

godmorning=wave.open('good-morningMan.wav','r')

frames = godmorning.readframes(-1)
#obtener todos los frames del objeto wave

#mostrar el resultado de frames
print(frames[:100])


