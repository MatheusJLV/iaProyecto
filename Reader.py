import csv
import numpy as np
import pandas as pd
import time
from sklearn import preprocessing
import numpy as np

print("Pandas Read")
dataframe=pd.read_csv('DatosProcesados.csv',dtype={"Severidad":float,"Vehiculos":float,"Dia":int,
	"Hora":float,"TipoCalle":int,"Velocidad":float,"Iluminacion":int,"Clima":int,"CalleEstado":int,
	"Policias":int,"Heridos":int})

estadisticas=pd.read_csv('Estadisticas.csv',dtype={"mediaSeveridad":float,"varianzaSeveridad":float,
	"mediaVehiculos":float,"varianzaVehiculos":float,
	"mediaTiempo":float,"varianzaTiempo":float,
	"mediaVelocidad":float,"varianzaVelocidad":float})

print(dataframe)
print(estadisticas)