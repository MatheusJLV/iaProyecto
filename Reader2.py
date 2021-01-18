import csv
import numpy as np
import pandas as pd
import time
from sklearn import preprocessing
import numpy as np


import csv
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import f_regression, SelectKBest
# example of correlation feature selection for numerical data
from sklearn.datasets import make_regression
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression

print("Pandas Read")
dataframe=pd.read_csv('DatosProcesados.csv',dtype={"Severidad":float,"Vehiculos":float,"Dia":int,
	"Hora":float,"TipoCalle":int,"Velocidad":float,"Iluminacion":int,"Clima":int,"CalleEstado":int,
	"Policias":int,"Heridos":int})

estadisticas=pd.read_csv('Estadisticas.csv',dtype={"mediaSeveridad":float,"varianzaSeveridad":float,
	"mediaVehiculos":float,"varianzaVehiculos":float,
	"mediaTiempo":float,"varianzaTiempo":float,
	"mediaVelocidad":float,"varianzaVelocidad":float})

#print(dataframe)
#print(estadisticas)

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

diasCate = [1,2]
TipoCalleCate = [1,2,3,4,5]
IluminacionCate = [1,2,3,4]
ClimaCate =[0,1,2,3,4]
CalleEstadoCate=[0,1,2,3,4]

enc = preprocessing.OneHotEncoder(categories=[diasCate, TipoCalleCate, IluminacionCate,ClimaCate,CalleEstadoCate])
fit=enc.fit(valores)
#print(fit)
arreglo=enc.transform(valores).toarray()
#print(arreglo)


OHE=pd.DataFrame({'DiaFinde': arreglo[:, 0], 'DiaLaboral': arreglo[:, 1],"Autopista": arreglo[:, 2],
	"AutopistaDoble": arreglo[:, 3],
	"1Via": arreglo[:, 4],"Redondel": arreglo[:, 5],"Entrada": arreglo[:, 6],
	"LuzDia": arreglo[:, 7],"LuzNoche": arreglo[:, 8],"LuzDesconocida": arreglo[:, 9],
	"LuzApagada": arreglo[:, 10],"Otro": arreglo[:, 11],
	"Despejado": arreglo[:, 12],"Lluvia": arreglo[:, 13],
	"Nieve": arreglo[:, 14],
	"Neblina": arreglo[:, 15],"Seca": arreglo[:, 16],"Inundada": arreglo[:, 17],
	"Humeda": arreglo[:, 18],"Nieve": arreglo[:, 19],"Congelada": arreglo[:, 20]})
#print(OHE)
#dataframe.drop('Dia', inplace=True, axis=1)
#dataframe.drop('TipoCalle', inplace=True, axis=1)
#dataframe.drop('Iluminacion', inplace=True, axis=1)
dataframe.drop('Clima', inplace=True, axis=1)
#dataframe.drop('CalleEstado', inplace=True, axis=1)

#DATOS PARA USAR
#en pandas
nuevodfpd=pd.concat([OHE,dataframe], axis=1)
#en numpy
nuevodfnp=np.array(nuevodfpd.values)
#DATOS PARA USAR


#print("Datos")
#print(nuevodfpd)
#print(nuevodfnp[0])

#print("verificando nombres y valores unicos")
#I=0
#for col in nuevodfpd.columns:
#	I=I+1
#	print(I)
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




dataframered=nuevodfpd[["Vehiculos","TipoCalle","Iluminacion","Velocidad","CalleEstado","Policias"]]
data=dataframered

X = data.iloc[:,0:5].values
Y = data.iloc[:,5:6].values
#print(X)
#print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=.2, random_state = 0)


grado=3

poly = PolynomialFeatures(degree = grado)
x_poly = poly.fit_transform(X_train)

features=1+5*grado
x_poly=x_poly[:,0:features]
print("x_poly")
print(x_poly)
#print(x_poly[0:1,:])
print(x_poly.shape)
print(x_poly.shape[0])

datos=x_poly
#print(datos[0])

mbatch=32
limite=np.full((features),6)
pesos=np.random.randint(1,limite)
totales=np.zeros(features)
contador=0
alpha=0.005
#print(datos[0:1,0:5][0])
#print(pesos)
for i in range(35000):
	print(i)
	print(pesos)
	totales=np.zeros(features)
	for j in range(mbatch):		
		datoxpeso=np.multiply(datos[contador:contador+1,0:features][0],pesos)
		#print("multiplicar")
		#print(datos[contador:contador+1,0:features][0])
		#print(pesos)
		#print(datoxpeso)
		esperado=np.full((features),datos[contador:contador+1,features-1:features][0])
		#print("esperado")
		#print(esperado)
		datodesper=np.subtract(datoxpeso,esperado)
		#print("resta")
		#print(datoxpeso)
		#print(esperado)
		#print(np.subtract(datoxpeso,esperado))
		datoxder=np.multiply(datodesper,datos[contador:contador+1,0:features][0])
		#print("resta")
		#print(datodesper)
		#print(datos[contador:contador+1,0:features][0])
		#print(np.multiply(datodesper,datos[contador:contador+1,0:features][0]))
		totales=np.add(totales,datoxder)
		#print("totales")
		#print(totales)
		contador=contador+1
	pesos=np.subtract(pesos,alpha/mbatch*totales)
	print(pesos)

