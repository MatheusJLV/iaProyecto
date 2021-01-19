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

from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error
import pickle

dataframe=pd.read_csv('DatosProcesados.csv',dtype={"Severidad":float,"Vehiculos":float,"Dia":int,
	"Hora":float,"TipoCalle":int,"Velocidad":float,"Iluminacion":int,"Clima":int,"CalleEstado":int,
	"Policias":int,"Heridos":int})

estadisticas=pd.read_csv('Estadisticas.csv',dtype={"mediaSeveridad":float,"varianzaSeveridad":float,
	"mediaVehiculos":float,"varianzaVehiculos":float,
	"mediaTiempo":float,"varianzaTiempo":float,
	"mediaVelocidad":float,"varianzaVelocidad":float})


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

arreglo=enc.transform(valores).toarray()



OHE=pd.DataFrame({'DiaFinde': arreglo[:, 0], 'DiaLaboral': arreglo[:, 1],"Autopista": arreglo[:, 2],
	"AutopistaDoble": arreglo[:, 3],
	"1Via": arreglo[:, 4],"Redondel": arreglo[:, 5],"Entrada": arreglo[:, 6],
	"LuzDia": arreglo[:, 7],"LuzNoche": arreglo[:, 8],"LuzDesconocida": arreglo[:, 9],
	"LuzApagada": arreglo[:, 10],"Otro": arreglo[:, 11],
	"Despejado": arreglo[:, 12],"Lluvia": arreglo[:, 13],
	"Nieve": arreglo[:, 14],
	"Neblina": arreglo[:, 15],"Seca": arreglo[:, 16],"Inundada": arreglo[:, 17],
	"Humeda": arreglo[:, 18],"Nieve": arreglo[:, 19],"Congelada": arreglo[:, 20]})

dataframe.drop('Clima', inplace=True, axis=1)


#DATOS PARA USAR
#en pandas
nuevodfpd=pd.concat([OHE,dataframe], axis=1)
#en numpy
nuevodfnp=np.array(nuevodfpd.values)
#DATOS PARA USAR




#DATOS PARA USAR
mediaSeveridad=estadisticas["mediaSeveridad"].values[0]
varianzaSeveridad=estadisticas["varianzaSeveridad"].values[0]
mediaVehiculos=estadisticas["mediaVehiculos"].values[0]
varianzaVehiculos=estadisticas["varianzaVehiculos"].values[0]
mediaTiempo=estadisticas["mediaTiempo"].values[0]
varianzaTiempo=estadisticas["varianzaTiempo"].values[0]
mediaVelocidad=estadisticas["mediaVelocidad"].values[0]
varianzaVelocidad=estadisticas["varianzaVelocidad"].values[0]


columnas=["CalleEstado"]

dataframered=nuevodfpd[["Vehiculos","TipoCalle","Iluminacion","Velocidad","CalleEstado","Policias"]]
data=dataframered


X= data.iloc[:,0:5].values
Y = data.iloc[:,5:6].values


X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=.2, random_state = 0)

#Lo hacemos polinomial

degree=3
Poly = PolynomialFeatures(degree = degree, include_bias = False)
xTrainPoly = Poly.fit_transform(X_train)

# Con elastico
elasticReg = ElasticNet(alpha = 0.1, l1_ratio = 0.85)
elasticReg.fit(xTrainPoly, Y_train )


#Prediccion
xFitPoly = Poly.transform(X_test)
xFit=xFitPoly
# yFit = sgd.predict(xFitPoly)
yFit = elasticReg.predict(xFitPoly)


mse = mean_squared_error(Y_test, yFit)
rmse = np.sqrt(mse)
print("RMSE")
print(rmse)

#Grafico de espejo para comparar Y prueba con Y predicho
x = np.linspace(0,100,num=1000)
plt.plot(yFit, Y_test,marker='o', linestyle = '', zorder = 1, color='b')
plt.plot(x, x, linestyle = '-',color='red',zorder=2,lw=3)
plt.xlabel('Numero de policias predicho', fontsize = 18)
plt.ylabel('Numero de policias reales', fontsize = 18)
plt.show()

filename = 'model degree.sav'
pickle.dump(elasticReg, open(filename, 'wb'))