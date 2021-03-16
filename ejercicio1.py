import wave
import numpy as np
import matplotlib.pyplot as plt

#audio 
print('sonido de buho')
buho = wave.open('buho.WAV','r')
framesBuho=buho.readframes(-1)
print(framesBuho[:10])
ondaconvertidaBuho=np.frombuffer(framesBuho, dtype='int16')
print(ondaconvertidaBuho[:10])
framerateBuho= buho.getframerate()
print(framerateBuho)
time_Buho=np.linspace(start=0, stop=len(ondaconvertidaBuho)/framerateBuho, num=len(ondaconvertidaBuho))
print(time_Buho[:10])



#audio 2
print('sonido de pajaritos')
pajarito = wave.open('pajarito.WAV','r')
framesPajarito=pajarito.readframes(-1)
print(framesPajarito[:10])
ondaconvertidaPajarito=np.frombuffer(framesPajarito, dtype='int16')
print(ondaconvertidaPajarito[:10])
frameratePajarito= pajarito.getframerate()
print(frameratePajarito)
time_Pajarito=np.linspace(start=0, stop=len(ondaconvertidaPajarito)/frameratePajarito, num=len(ondaconvertidaPajarito))
print(time_Pajarito[:10])



plt.title('buho vs pajarito')
plt.xlabel('tiempo s')
plt.ylabel('amplitud')

#graficar juntos
plt.plot(time_Buho,ondaconvertidaBuho, label='buho')
plt.plot(time_Pajarito,ondaconvertidaPajarito, label='pajarito', alpha=0.5)

plt.legend()
plt.show()