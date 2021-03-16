import wave
import numpy as np 
import matplotlib.pyplot as plt 
#cargar archivo wav en la variable 

goodmorning=wave.open('good-morningMan.wav','r')
print("good morning")
frames = goodmorning.readframes(-1)
print(frames[:10])
#obtener todos los frames del objeto wave
ondaconvertida = np.frombuffer(frames, dtype='int16')

#mostrar el resultado de frames
print(ondaconvertida[:10])

framerate_gm= goodmorning.getframerate()
print(framerate_gm)

time_gom=np.linspace(start=0, stop=len(ondaconvertida)/framerate_gm, num=len(ondaconvertida))
print(time_gom[:10])


goodafter = wave.open('good-afternoon.wav', 'r')
frames_after= goodafter.readframes(-1)
ondaconvertidaafter= np.frombuffer(frames_after, dtype='int16')
framerate_ga= goodafter.getframerate()
time_ga=np.linspace(start=0,stop=len(ondaconvertidaafter)/framerate_ga, num=len(ondaconvertidaafter))
print("good after")
print(frames_after[:10])
print(ondaconvertidaafter[:10])
print(framerate_ga, time_ga[:10])


#generacion de la grafica
plt.title('good morning vs good afternoon')
plt.xlabel('tiempo s')
plt.ylabel('amplitud')

plt.plot(time_ga, ondaconvertidaafter, label="good afternoon")
plt.plot(time_gom, ondaconvertida, label="good morning", alpha=0.5)
plt.legend()
plt.show()
