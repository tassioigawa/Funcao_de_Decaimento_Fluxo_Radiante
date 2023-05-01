import math as m
import pandas as pd

##altitude = float(input("Insira o intervalo de ocorrência de aerossóis marinhos: "))
Irradiancia = [315.49, 313.28, 178.30, 261.13]
coef_abs_band_marine_aerossols = [0.066, 0.041, 0.039, 0.079] ## (Coef. Marine Aerossols (VAXELEIRE, 1991)
coef_abs_band_pure_water_cdom = [0.0904, 0.0588, 0.3315, 2.2932] ##(Coef. Pure Water (BUITEVELD; DONZE, 1994); Coef. CDOM (KIRK, 1976))

################################################## Decaimento ###########################################################
# Função de Decaimento do Fluxo Radiante
def Decaimento (Irrad,a, x):
    Fluxo = Irrad*m.e**(-a*x)
    return Fluxo

### Atmosfera (Aerossóis Marinhos)
for i in range(0,10,1):
    Irradiancia_mar_aero_azul = [Decaimento(Irradiancia[0], coef_abs_band_marine_aerossols[0], i)]

for i in range(0,10,1):
    Irradiancia_mar_aero_verde = [Decaimento(Irradiancia[1], coef_abs_band_marine_aerossols[1], i)]

for i in range(0,10,1):
    Irradiancia_mar_aero_verm = [Decaimento(Irradiancia[2], coef_abs_band_marine_aerossols[2], i)]

for i in range(0,10,1):
    Irradiancia_mar_aero_infrprox = [Decaimento(Irradiancia[3], coef_abs_band_marine_aerossols[3], i)]


df = pd.DataFrame(zip(Irradiancia_mar_aero_azul,Irradiancia_mar_aero_verde,Irradiancia_mar_aero_verm,Irradiancia_mar_aero_infrprox),
                  columns=['Azul', 'Verde','Vermelho','Infravermelho'])
print(df)

### Oceano (Água Pura; CDOM)
for i in range(0,100,1):
    Irradiancia_oceano_azul = [Decaimento(Irradiancia_mar_aero_azul[-1], coef_abs_band_pure_water_cdom[0], i)]

for i in range(0,100,1):
    Irradiancia_oceano_verde = [Decaimento(Irradiancia_mar_aero_verde[-1], coef_abs_band_pure_water_cdom[1], i)]

for i in range(0,100,1):
    Irradiancia_oceano_verm = [Decaimento(Irradiancia_mar_aero_verm[-1], coef_abs_band_pure_water_cdom[2], i)]

for i in range(0,100,1):
    Irradiancia_oceano_infrprox = [Decaimento(Irradiancia_mar_aero_infrprox[-1], coef_abs_band_pure_water_cdom[3], i)]


df2 = pd.DataFrame(zip(Irradiancia_oceano_azul,Irradiancia_oceano_verde,Irradiancia_oceano_verm ,Irradiancia_oceano_infrprox),
                  columns=['Azul', 'Verde','Vermelho','Infravermelho'])
print(df2)