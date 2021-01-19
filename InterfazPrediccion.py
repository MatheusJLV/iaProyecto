import tkinter as tk
from tkinter import ttk
import numpy as np
import pickle
from sklearn.preprocessing import PolynomialFeatures

def Predecir():
    
    estadoC=comboEstadoCalle.get()

    if estadoC=="Seca": 
        estadoC=0
    elif estadoC=="Inundada" :
        estadoC=1
    elif estadoC=="Humeda" :
        estadoC=2
    elif estadoC=="Con nieve" :
        estadoC=3
    elif estadoC=="Congelada" :
        estadoC=4

    iluminacion=comboIluminacion.get()

    if iluminacion=="Día": 
        iluminacion=1
    elif iluminacion=="Noche con luces prendidas" :
        iluminacion=2
    elif iluminacion=="Noche con luces desconocidas" :
        iluminacion=3
    elif iluminacion=="Noche con luces apagadas" :
        iluminacion=4

    tipoCalle=comboTipoCalle.get()

    if tipoCalle=="Autopista": 
        tipoCalle=1
    elif tipoCalle=="Autopista doble" :
        tipoCalle=2
    elif tipoCalle=="Calle de una via" :
        tipoCalle=3
    elif tipoCalle=="Redondel" :
        tipoCalle=4
    elif tipoCalle=="Carril de acceso" :
        tipoCalle=5
    
    resM= np.zeros(shape=(1,5))
    resM[0][0]=vehiculos.get()
    resM[0][1]=estadoC
    resM[0][2]=iluminacion
    resM[0][3]=Velocidad.get()
    resM[0][4]=tipoCalle
    

    filename = 'model degree.sav'
    elasticReg = pickle.load(open(filename, 'rb'))
    Poly = PolynomialFeatures(degree = 3, include_bias = False)
    xFitPoly = Poly.fit_transform(resM)
    yFit = elasticReg.predict(xFitPoly)
    pol.set(round(yFit[0]))


window=tk.Tk()
window.title("Predicción de numero de policias")
window.geometry('600x600')

titulo=tk.Label(window,text="Sistema de predicción de numero de policias", font=('​Helvetica', 18, 'bold'))
titulo.pack()


titulo=tk.Label(window,text="Estado de la calle", font=('​Helvetica', 16, 'bold'))
titulo.pack()
comboEstadoCalle = ttk.Combobox(window, 
                            values=[
                                    "Seca", 
                                    "Inundada",
                                    "Humeda",
                                    "Con nieve",
                                    "Congelada"], font=('​Helvetica', 14))
comboEstadoCalle.current(0)
comboEstadoCalle.pack()


tituloVelocidad=tk.Label(window,text="Velocidad limite de la calle", font=('​Helvetica', 16, 'bold'))
tituloVelocidad.pack()
Velocidad=tk.Spinbox(window,from_ =0, to=250, font=('​Helvetica', 14))
Velocidad.pack()


tituloIluminacion=tk.Label(window,text="Tipo de iluminación", font=('​Helvetica', 16, 'bold'))
tituloIluminacion.pack()
comboIluminacion = ttk.Combobox(window, 
                            values=[
                                    "Día", 
                                    "Noche con luces prendidas",
                                    "Noche con luces desconocidas",
                                    "Noche con luces apagadas",], font=('​Helvetica', 14))
comboIluminacion.current(0)
comboIluminacion.pack()

tituloTipoCalle=tk.Label(window,text="Tipo de calle", font=('​Helvetica', 16, 'bold'))
tituloTipoCalle.pack()
comboTipoCalle = ttk.Combobox(window, 
                            values=[
                                    "Autopista",
                                    "Autopista doble", 
                                    "Calle de una via",
                                    "Redondel",
                                    "Carril de acceso",], font=('​Helvetica', 14))
comboTipoCalle.current(0)
comboTipoCalle.pack()


tituloVehiculos=tk.Label(window,text="Cantidad de vehiculos accidentados", font=('​Helvetica', 16, 'bold'))
tituloVehiculos.pack()
vehiculos=tk.Spinbox(window,from_ =0, to=30, font=('​Helvetica', 14))
vehiculos.pack()

button=tk.Button(window,text="Predecir",width=30, command=Predecir, font=('​Helvetica', 16, 'bold'))
button.pack()



tituloPolicias=tk.Label(window,text="Cantidad de policias requerido", font=('​Helvetica', 16, 'bold'))
tituloPolicias.pack()

pol= tk.IntVar(window,0)
Policias=tk.Spinbox(window,from_ =0, to=200, font=('​Helvetica', 14), state = tk.DISABLED, textvariable=pol)
Policias.pack()

window.mainloop()