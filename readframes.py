import wave
import numpy as np 
#cargar archivo wav en la variable 

godmorning=wave.open('good-morningMan.wav','r')

frames = godmorning.readframes(-1)
#obtener todos los frames del objeto wave
ondaconvertida = np.frombuffer(frames, dtype='int16')
#mostrar el resultado de frames
print(ondaconvertida[:10])


