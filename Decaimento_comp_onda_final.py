import math as m
import pandas as pd
import matplotlib.pyplot  as plt
import numpy as np

##altitude = float(input("Insira o intervalo de ocorrência de aerossóis marinhos: "))
Irradiancia = [315.39, 313.18, 178.24, 261.05]
coef_abs_band_marine_aerossols = [0.066, 0.041, 0.039, 0.079] ## (Coef. Marine Aerossols (VAXELEIRE, 1991)
coef_abs_band_pure_water_cdom = [0.0904, 0.0588, 0.3315, 2.2932] ##(Coef. Pure Water (BUITEVELD; DONZE, 1994); Coef. CDOM (KIRK, 1976))

################################################## Decaimento ###########################################################
# Função de Decaimento do Fluxo Radiante
def Decaimento (Irrad,a, x):
    Fluxo = Irrad*m.e**(-a*x)
    return Fluxo

### Atmosfera (Aerossóis Marinhos)
arazul=[]
arverde=[]
arvermelho=[]
arinfrprox=[]

for i in range(0,11,1):
    Irradiancia_mar_aero_azul = [Decaimento(Irradiancia[0], coef_abs_band_marine_aerossols[0], i)]
    arazul.append(Irradiancia_mar_aero_azul)
for i in range(0,11,1):
    Irradiancia_mar_aero_verde = [Decaimento(Irradiancia[1], coef_abs_band_marine_aerossols[1], i)]
    arverde.append(Irradiancia_mar_aero_verde)
for i in range(0,11,1):
    Irradiancia_mar_aero_verm = [Decaimento(Irradiancia[2], coef_abs_band_marine_aerossols[2], i)]
    arvermelho.append(Irradiancia_mar_aero_verm)
for i in range(0,11,1):
    Irradiancia_mar_aero_infrprox = [Decaimento(Irradiancia[3], coef_abs_band_marine_aerossols[3], i)]
    arinfrprox.append(Irradiancia_mar_aero_infrprox)
    print(Irradiancia_mar_aero_infrprox)

df = pd.DataFrame(zip(Irradiancia_mar_aero_azul,Irradiancia_mar_aero_verde,Irradiancia_mar_aero_verm,Irradiancia_mar_aero_infrprox),
                  columns=['Azul', 'Verde','Vermelho','Infravermelho'])
print(df)

### Oceano (Água Pura; CDOM)
oceanoazul=[]
oceanoverde=[]
oceanovermelho=[]
oceanoinfrprox=[]

for i in range(0,100,1):
    Irradiancia_oceano_azul = [Decaimento(Irradiancia_mar_aero_azul[-1], coef_abs_band_pure_water_cdom[0], i)]
    oceanoazul.append(Irradiancia_oceano_azul)
for i in range(0,100,1):
    Irradiancia_oceano_verde = [Decaimento(Irradiancia_mar_aero_verde[-1], coef_abs_band_pure_water_cdom[1], i)]
    oceanoverde.append(Irradiancia_oceano_verde)
for i in range(0,100,1):
    Irradiancia_oceano_verm = [Decaimento(Irradiancia_mar_aero_verm[-1], coef_abs_band_pure_water_cdom[2], i)]
    oceanovermelho.append(Irradiancia_oceano_verm)
for i in range(0,100,1):
    Irradiancia_oceano_infrprox = [Decaimento(Irradiancia_mar_aero_infrprox[-1], coef_abs_band_pure_water_cdom[3], i)]
    oceanoinfrprox.append(Irradiancia_oceano_infrprox)
    print(Irradiancia_oceano_infrprox)

df2 = pd.DataFrame(zip(Irradiancia_oceano_azul,Irradiancia_oceano_verde,Irradiancia_oceano_verm ,Irradiancia_oceano_infrprox),
                  columns=['Azul', 'Verde','Vermelho','Infravermelho'])
print(df2)

x=np.arange(0,100,1)
x2=['10','9','8','7','6','5','4','3','2','1','0']
x3=np.arange(10,-100,-1)
x4 = []
for val in x3:
    x4.append(str(val))
plt.style.use('ggplot')


plt.title('Irradiância por Profundidade - Água Pura + CDOM')
plt.xlabel('Profundidade (m)')
plt.ylabel('Irradiância (W/m²)')
plt.plot(x,oceanoazul, label='Banda do Azul', color='blue')
plt.plot(x,oceanoverde, label='Banda do Verde', color='green')
plt.plot(x,oceanovermelho, label='Banda do Vermelho', color='red')
plt.plot(x,oceanoinfrprox, label='Banda do Infravermelho Proxímo', color='purple')
plt.legend()
plt.show()

plt.title('Irradiância por Altitude - Aerossóis Marinhos')
plt.xlabel('Altitude (m)')
plt.ylabel('Irradiância (W/m²)')
plt.plot(x2,arazul, label='Banda do Azul', color='blue')
plt.plot(x2,arverde, label='Banda do Verde', color='green')
plt.plot(x2,arvermelho, label='Banda do Vermelho', color='red')
plt.plot(x2,arinfrprox, label='Banda do Infravermelho Proxímo', color='purple')
plt.legend()
plt.show()

del arazul[-1]
del arverde[-1]
del arvermelho[-1]
del arinfrprox[-1]
combiazul=[]
combiazul.extend(arazul)
combiazul.extend(oceanoazul)
combiverde=[]
combiverde.extend(arverde)
combiverde.extend(oceanoverde)
combivermelho=[]
combivermelho.extend(arvermelho)
combivermelho.extend(oceanovermelho)
combiinfrprox=[]
combiinfrprox.extend(arinfrprox)
combiinfrprox.extend(oceanoinfrprox)


print(len(x4))
print(len(combiazul))

plt.title('Irradiância por Altitude/ - (Aerossóis Marinhos) (Água Pura + CDOM)')
plt.xlabel('Altitude (m)')
plt.ylabel('Irradiância (W/m²)')
plt.plot(x4,combiazul, label='Banda do Azul', color='blue')
plt.plot(x4,combiverde, label='Banda do Verde', color='green')
plt.plot(x4,combivermelho, label='Banda do Vermelho', color='red')
plt.plot(x4,combiinfrprox, label='Banda do Infravermelho Proxímo', color='purple')
plt.legend()
plt.show()

