import csv
import numpy as np
import pandas as pd
import time
from sklearn import preprocessing
import numpy as np

print("Pandas process")
dataframe1=pd.read_csv('accidents_2007.csv',dtype={"Police_Force":int,"Accident_Severity":int,"Number_of_Vehicles":int,"Number_of_Casualties":int,"Day_of_Week":
	int,"Time":"string","Road_Type":"string","Speed_limit":int,"Light_Conditions":"string","Weather_Conditions":"string",
	"Road_Surface_Conditions":"string","Year":int})
dataframe2=pd.read_csv('accidents_2011.csv',dtype={"Police_Force":int,"Accident_Severity":int,"Number_of_Vehicles":int,"Number_of_Casualties":int,"Day_of_Week":
	int,"Time":"string","Road_Type":"string","Speed_limit":int,"Light_Conditions":"string","Weather_Conditions":"string",
	"Road_Surface_Conditions":"string","Year":int})
dataframe3=pd.read_csv('accidents_2014.csv',dtype={"Police_Force":int,"Accident_Severity":int,"Number_of_Vehicles":int,"Number_of_Casualties":int,"Day_of_Week":
	int,"Time":"string","Road_Type":"string","Speed_limit":int,"Light_Conditions":"string","Weather_Conditions":"string",
	"Road_Surface_Conditions":"string","Year":int})
frames = [dataframe1, dataframe2, dataframe3]
dataframe=pd.concat(frames)
#print(dataframe)
print("eliminando columnas innecesarias (No aplican)")
dataframe.drop('Accident_Index', inplace=True, axis=1)
dataframe.drop('Location_Easting_OSGR', inplace=True, axis=1)
dataframe.drop('Longitude', inplace=True, axis=1)
dataframe.drop('Latitude', inplace=True, axis=1)
dataframe.drop('Location_Northing_OSGR', inplace=True, axis=1)
dataframe.drop('Date', inplace=True, axis=1)
dataframe.drop('Local_Authority_(District)', inplace=True, axis=1)
dataframe.drop('Local_Authority_(Highway)', inplace=True, axis=1)
dataframe.drop('1st_Road_Number', inplace=True, axis=1)
dataframe.drop('Junction_Detail', inplace=True, axis=1)
dataframe.drop('Junction_Control', inplace=True, axis=1)
dataframe.drop('2nd_Road_Class', inplace=True, axis=1)
dataframe.drop('2nd_Road_Number', inplace=True, axis=1)
dataframe.drop('Pedestrian_Crossing-Human_Control', inplace=True, axis=1)
dataframe.drop('Special_Conditions_at_Site', inplace=True, axis=1)
dataframe.drop('Carriageway_Hazards', inplace=True, axis=1)
dataframe.drop('Urban_or_Rural_Area', inplace=True, axis=1)
dataframe.drop('Did_Police_Officer_Attend_Scene_of_Accident', inplace=True, axis=1)
dataframe.drop('LSOA_of_Accident_Location', inplace=True, axis=1)
dataframe.drop('Pedestrian_Crossing-Physical_Facilities', inplace=True, axis=1)
dataframe.drop('1st_Road_Class', inplace=True, axis=1)

print("eliminando filas innecesarias (Blanks/Nulls)")
dataframe.dropna(subset=['Road_Surface_Conditions'], inplace=True)
dataframe.dropna(subset=['Weather_Conditions'], inplace=True)
dataframe.dropna(subset=['Time'], inplace=True)

indexNames = dataframe[ dataframe['Road_Type'] == "Unknown" ].index
dataframe.drop(indexNames , inplace=True)
indexNames = dataframe[ dataframe['Weather_Conditions'] == "Unknown" ].index
dataframe.drop(indexNames , inplace=True)

#print("verificando nombres y valores unicos")
#for col in dataframe.columns:
#	print(col)
#	print(dataframe[col].unique())


print("Policias enviados")
Policias=np.array(dataframe.Police_Force.values)
print(Policias)

print("Heridos")
Heridos=np.array(dataframe.Number_of_Casualties.values)
print(Heridos)

mediaSeveridad=0
varianzaSeveridad=0
severidadNormal=[]
print("procesando severidad")
severidad=np.array(dataframe.Accident_Severity.values)
mediaSeveridad=np.mean(severidad)
varianzaSeveridad=np.std(severidad)
print("media")
print(mediaSeveridad)
print("varianza")
print(varianzaSeveridad)
severidad=severidad.reshape(-1, 1)
scaler = preprocessing.StandardScaler().fit(severidad)
X_scaled = scaler.transform(severidad)
for i in range(len(X_scaled)):
	severidadNormal.append(X_scaled[i][0])
severidadNormal=np.array(severidadNormal)
print("severidad normalizada")
print(severidadNormal)
#print(X_scaled.mean(axis=0))
#print(X_scaled.std(axis=0))


mediaVehiculos=0
varianzaVehiculos=0
vehiculosNormal=[]
print("procesando Num de vehiculos")
vehiculos=np.array(dataframe.Number_of_Vehicles.values)
mediaVehiculos=np.mean(vehiculos)
varianzaVehiculos=np.std(vehiculos)
print("media")
print(mediaVehiculos)
print("varianza")
print(varianzaVehiculos)
vehiculos=vehiculos.reshape(-1, 1)
scaler = preprocessing.StandardScaler().fit(vehiculos)
X_scaled = scaler.transform(vehiculos)
for i in range(len(X_scaled)):
	vehiculosNormal.append(X_scaled[i][0])
vehiculosNormal=np.array(vehiculosNormal)
print("vehiculos normalizado")
print(vehiculosNormal)
#print(X_scaled.mean(axis=0))
#print(X_scaled.std(axis=0))

print("procesando dia de semana")
print("Domingo:1")
dia=np.array(dataframe.Day_of_Week.values)
print(dia)
#dia=dia.reshape(-1, 1)
#scaler = preprocessing.StandardScaler().fit(dia)
#X_scaled = scaler.transform(dia)
#diaNormal=X_scaled
#print("dia normalizado")
#print(X_scaled)
#print(X_scaled.mean(axis=0))
#print(X_scaled.std(axis=0))


mediaTiempo=0
varianzaTiempo=0
print("procesando tiempo")
#print("hora")
#print(dataframe.Time.values)
tiempo=[]
tiempoNormal=[]
for i in range(len(dataframe.Time.values)):
	#print((dataframe.Time.values))
	try:
		time_object = time.strptime(dataframe.Time.values[i], '%H:%M')
		hora=(time_object.tm_hour)
		minuto=(time_object.tm_min)
		#print("minuto del dia")
		minutoT=hora*60+minuto
		#print(minutoT)
		tiempo.append(minutoT)
	except ValueError as e:
		print('ValueError:', e)
#print("hora nueva")
#print(len(tiempo))
tiempo=np.array(tiempo)
mediaTiempo=np.mean(tiempo)
varianzaTiempo=np.std(tiempo)
print("media")
print(mediaTiempo)
print("varianza")
print(varianzaTiempo)
tiempo=tiempo.reshape(-1, 1)
scaler = preprocessing.StandardScaler().fit(tiempo)
X_scaled = scaler.transform(tiempo)
for i in range(len(X_scaled)):
	tiempoNormal.append(X_scaled[i][0])
print("tiempo normalizado")
tiempoNormal=np.array(tiempoNormal)
print(tiempoNormal)
#print(X_scaled.mean(axis=0))
#print(X_scaled.std(axis=0))


print("procesando tipo de calle")
print("""
	AUTOPISTA:1
	AUTOPISTA DOBLE (SEPARACION):2
	CALLE DE UNA VIA:3
	REDONDEL:4
	CARRIL DE ACCESO:5""")
calleT=np.array(dataframe.Road_Type.values)
calleT = np.where(calleT == "Single carriageway", 1, calleT)
calleT = np.where(calleT == 'Dual carriageway', 2, calleT)
calleT = np.where(calleT == 'One way street', 3, calleT)
calleT = np.where(calleT == 'Roundabout', 4, calleT)
calleT = np.where(calleT == 'Slip road', 5, calleT)
print(calleT)



mediaVelocidad=0
varianzaVelocidad=0
print("procesando limite de velocidad")
velocidadNormal=[]
velocidad=np.array(dataframe.Speed_limit.values)
mediaVelocidad=np.mean(velocidad)
varianzaVelocidad=np.std(velocidad)
print("media")
print(mediaVelocidad)
print("varianza")
print(varianzaVelocidad)
velocidad=velocidad.reshape(-1, 1)
scaler = preprocessing.StandardScaler().fit(velocidad)
X_scaled = scaler.transform(velocidad)
for i in range(len(X_scaled)):
	velocidadNormal.append(X_scaled[i][0])
velocidadNormal=np.array(velocidadNormal)
print("velocidad normalizada")
print(velocidadNormal)



print("procesando iluminacion")
print("""
	DIA:1
	NOCHE CON LUCES PRENDIDAS:2
	NOCHE LUCES DESCONOCIDAS:3
	NOCHE CON LUCES APAGDAS:4
	NOCHE SIN LUCES:5""")
luz=np.array(dataframe.Light_Conditions.values)
luz = np.where(luz == 'Daylight: Street light present', 1, luz)
luz = np.where(luz == 'Darkness: Street lights present and lit', 2, luz)
luz = np.where(luz == 'Darkness: Street lighting unknown', 3, luz)
luz = np.where(luz == 'Darkness: Street lights present but unlit', 4, luz)
luz = np.where(luz == 'Darkeness: No street lighting', 5, luz)
print(luz)


print("procesando clima")
print("""
	OTRO:0
	DESPEJADO:1
	DESPEJADO CON VIENTO:2
	LLOVIENDO:3
	LLOVIENDO CON VIENTO:4
	NEVANDO:5
	NEVANDO CON VIENTO:6
	NEBLINA:7""")
clima=np.array(dataframe.Weather_Conditions.values)
clima = np.where(clima == 'Other', 0, clima)
clima = np.where(clima == 'Fine without high winds', 1, clima)
clima = np.where(clima == 'Fine with high winds', 2, clima)
clima = np.where(clima == 'Raining without high winds', 3, clima)
clima = np.where(clima == 'Raining with high winds', 4, clima)
clima = np.where(clima == 'Snowing without high winds', 5, clima)
clima = np.where(clima == 'Snowing with high winds', 6, clima)
clima = np.where(clima == 'Fog or mist', 7, clima)
print(clima)

print("procesando estado de la calle")
print("""
	SECA:0
	INUNDADA:1
	HUMEDA:2
	CON NIEVE:3
	CONGELADA:4
	""")
calleE=np.array(dataframe.Road_Surface_Conditions.values)
calleE = np.where(calleE == 'Dry', 0, calleE)
calleE = np.where(calleE == 'Flood (Over 3cm of water)', 1, calleE)
calleE = np.where(calleE == 'Wet/Damp', 2, calleE)
calleE = np.where(calleE == 'Snow', 3, calleE)
calleE = np.where(calleE == 'Frost/Ice', 4, calleE)
print(calleE)




dfSave=pd.DataFrame({"Severidad":severidadNormal,"Vehiculos":vehiculosNormal,"Dia":dia,
	"Hora":tiempoNormal,"TipoCalle":calleT,"Velocidad":velocidadNormal,"Iluminacion":luz,
	"Clima":clima,"CalleEstado":calleE,"Policias":Policias,"Heridos":Heridos})
print(dfSave)


dfSave.to_csv('DatosProcesados.csv', index=True)



dfSave2=pd.DataFrame({"mediaSeveridad":[mediaSeveridad],"varianzaSeveridad":[varianzaSeveridad],
	"mediaVehiculos":[mediaVehiculos],"varianzaVehiculos":[varianzaVehiculos],
	"mediaTiempo":[mediaTiempo],"varianzaTiempo":[varianzaTiempo],
	"mediaVelocidad":[mediaVelocidad],"varianzaVelocidad":[varianzaVelocidad]})
print(dfSave2)


dfSave2.to_csv('Estadisticas.csv', index=False)