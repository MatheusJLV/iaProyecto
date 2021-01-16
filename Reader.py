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

#print("verificando nombres y valores unicos")
#for col in dataframe.columns:
#	print(col)
#	print(dataframe[col].unique())

dias=np.array(dataframe.Dia.values)
#print(dias)

TipoCalle=np.array(dataframe.TipoCalle.values)
#print(TipoCalle)

Iluminacion=np.array(dataframe.Iluminacion.values)
#print(Iluminacion)

Clima=np.array(dataframe.Clima.values)
#print(Clima)

CalleEstado=np.array(dataframe.CalleEstado.values)
#print(CalleEstado)

subset=dataframe[["Dia","TipoCalle","Iluminacion","Clima","CalleEstado"]]
#print(subset)
valores=np.array(subset.values)
#print(valores)

diasCate = [1,2,3,4,5,6,7]
TipoCalleCate = [1,2,3,4,5]
IluminacionCate = [1,2,3,4,5]
ClimaCate =[0,1,2,3,4,5,6,7]
CalleEstadoCate=[0,1,2,3,4]

enc = preprocessing.OneHotEncoder(categories=[diasCate, TipoCalleCate, IluminacionCate,ClimaCate,CalleEstadoCate])
fit=enc.fit(valores)
#print(fit)
arreglo=enc.transform(valores).toarray()
#print(arreglo)


OHE=pd.DataFrame({'Doming': arreglo[:, 0], 'Lunes': arreglo[:, 1],"Martes": arreglo[:, 2],
	"Miercoles": arreglo[:, 3],"Jueves": arreglo[:, 4],"Viernes": arreglo[:, 5],
	"Sabado": arreglo[:, 6],"Autopista": arreglo[:, 7],"AutopistaDoble": arreglo[:, 8],
	"1Via": arreglo[:, 9],"Redondel": arreglo[:, 10],"Entrada": arreglo[:, 11],
	"LuzDia": arreglo[:, 12],"LuzNoche": arreglo[:, 13],"LuzDesconocida": arreglo[:, 14],
	"LuzApagada": arreglo[:, 15],"NoLuz": arreglo[:, 16],"Otro": arreglo[:, 17],
	"Despejado": arreglo[:, 18],"DespejadoViento": arreglo[:, 19],"Lluvia": arreglo[:, 20],
	"LluviaViento": arreglo[:, 21],"Nieve": arreglo[:, 22],"NieveViento": arreglo[:, 23],
	"Neblina": arreglo[:, 24],"Seca": arreglo[:, 25],"Inyndada": arreglo[:, 26],
	"Humeda": arreglo[:, 27],"Nieve": arreglo[:, 28],"Congelada": arreglo[:, 29]})
#print(OHE)
dataframe.drop('Dia', inplace=True, axis=1)
dataframe.drop('TipoCalle', inplace=True, axis=1)
dataframe.drop('Iluminacion', inplace=True, axis=1)
dataframe.drop('Clima', inplace=True, axis=1)
dataframe.drop('CalleEstado', inplace=True, axis=1)

#DATOS PARA USAR
#en pandas
nuevodfpd=pd.concat([OHE,dataframe], axis=1)
#en numpy
nuevodfnp=np.array(nuevodfpd.values)
#DATOS PARA USAR


print("Datos")
print(nuevodfpd)
#print(nuevodfnp[0])

#print("verificando nombres y valores unicos")
#for col in nuevodfpd.columns:
#	print(col)
#	print(nuevodfpd[col].unique())


#DATOS PARA USAR
mediaSeveridad=estadisticas["mediaSeveridad"].values[0]
varianzaSeveridad=estadisticas["varianzaSeveridad"].values[0]
mediaVehiculos=estadisticas["mediaVehiculos"].values[0]
varianzaVehiculos=estadisticas["varianzaVehiculos"].values[0]
mediaTiempo=estadisticas["mediaTiempo"].values[0]
varianzaTiempo=estadisticas["varianzaTiempo"].values[0]
mediaVelocidad=estadisticas["mediaVelocidad"].values[0]
varianzaVelocidad=estadisticas["varianzaVelocidad"].values[0]
#DATOS PARA USAR

print("Stats")
print(mediaSeveridad)
print(varianzaSeveridad)
print(mediaVehiculos)
print(varianzaVehiculos)
print(mediaTiempo)
print(varianzaTiempo)
print(mediaVelocidad)
print(varianzaVelocidad)