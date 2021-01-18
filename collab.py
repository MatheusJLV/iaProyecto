import csv
import numpy as np
import pandas as pd
import time
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
# example of correlation feature selection for numerical data
from sklearn.datasets import make_regression
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression

import matplotlib.pyplot as plt
import scipy.linalg
from sklearn.preprocessing import MinMaxScaler


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

print("verificando nombres y valores unicos")
for col in dataframe.columns:
	print(col)
	print(dataframe[col].unique())




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
print(valores)





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
print(OHE)
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

print("verificando nombres y valores unicos")
for col in nuevodfpd.columns:
	print(col)
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




#data = pd.read_csv("data.csv")
data=nuevodfpd
#X = data.iloc[:,0:2].values
#Y = data.iloc[:,4:5].values
X = data.iloc[1:10,17:23].values
Y = data.iloc[1:10,25:26].values

#scale = StandardScaler()
#X = scale.fit_transform(X)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=.2, random_state = 0)

poly = PolynomialFeatures(degree = 3)
x_poly = poly.fit_transform(X_train)
print(x_poly)
poly.fit(X_train,Y_train)

model = LinearRegression()
model.fit(x_poly, Y_train,batch_size=10)
print(model)

y_pred = model.predict(poly.fit_transform(X_test))
print(y_pred)



