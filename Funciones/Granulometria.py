import pandas as pd
import matplotlib.path as mpath
import numpy as np
import matplotlib.pyplot as plt 
from scipy.interpolate import interp1d


#valores de entrada
Malla= pd.Series([
    "#4", #Tamiz #4
    "#10", #Tamiz #10
    "#20", #Tamiz #20
    "#40", #Tamiz #40
    "#60", #Tamiz #60
    "#140", #Tamiz #140
    "#200", #Tamiz #200
    "fondo", #Fondo
])

Abertura= pd.Series([
    "4.750", #Abertura Tamiz #4
    "2.000", #Abertura Tamiz #10
    "0.850", #Abertura Tamiz #20
    "0.425", #Abertura Tamiz #40
    "0.250", #Abertura Tamiz #60
    "0.106", #Abertura Tamiz #140
    "0.075", #Abertura Tamiz #200
    "0", #fondo
])



Retenido= pd.Series([
    95, #Tamiz #4
    80, #Tamiz #10
    51, #Tamiz #20
    33, #Tamiz #40
    13, #Tamiz #60
    6, #Tamiz #140
    3, #Tamiz #200
    67, #Fondo
  
])

Acum=[] #Matriz donde se guardan los datos 
#Realizar calculo de datos, valor retenidido mas valor acumulado 
Acum.append(Retenido[0]+0)
Acum.append(Retenido[1]+Acum[0])
Acum.append(Retenido[2]+Acum[1])
Acum.append(Retenido[3]+Acum[2])
Acum.append(Retenido[4]+Acum[3])
Acum.append(Retenido[5]+Acum[4])
Acum.append(Retenido[6]+Acum[5])
Acum.append(Retenido[7]+Acum[6])
Ret_Acu =pd.Series(Acum)


AcuP=[] 
#Realizar Calculo, valor Acumulado total - valor retenido el el primer tamiz
AcuP.append(Acum[7]-Retenido[0])

#Valor acumulado menos el valor retenido en cada tamiz
AcuP.append(AcuP[0]-Retenido[1])
AcuP.append(AcuP[1]-Retenido[2])
AcuP.append(AcuP[2]-Retenido[3])
AcuP.append(AcuP[3]-Retenido[4])
AcuP.append(AcuP[4]-Retenido[5])
AcuP.append(AcuP[5]-Retenido[6])
AcuP.append(AcuP[6]-Retenido[7])
Pasa = pd.Series(AcuP)

Granulometria = pd.DataFrame({  #Se crea la tabla con los valores que se deben ingresar en cada columna 
    'Malla': Malla,
    'Abertura': Abertura,
    'Retenido': Retenido,
    'Retenido Acumulado': Ret_Acu,
    'Pasa': Pasa
})


Peso_Total = Granulometria["Retenido"].sum() #Obtenemos el peso total de la muestra de suelo 
Peso_Total

Porpasa=[] #Obtenemos el porcentaje que pasa en cada tamiz, con el peso que pasa y el peso total
Porpasa.append((Pasa[0]*100)/Peso_Total)
Porpasa.append((Pasa[1]*100)/Peso_Total)
Porpasa.append((Pasa[2]*100)/Peso_Total)
Porpasa.append((Pasa[3]*100)/Peso_Total)
Porpasa.append((Pasa[4]*100)/Peso_Total)
Porpasa.append((Pasa[5]*100)/Peso_Total)
Porpasa.append((Pasa[6]*100)/Peso_Total)
Porpasa.append((Pasa[7]*100)/Peso_Total)
Porcen_Pasa = pd.Series(Porpasa)

Granulometria = pd.DataFrame({ #Tabla con la nueva columna de %Pasa
    'Malla': Malla,
    'Abertura': Abertura,
    'Retenido': Retenido,
    'Retenido Acumulado': Ret_Acu,
    'Pasa': Pasa,
    '% Pasa': Porcen_Pasa
})

print(Granulometria)

#valores de entrada
Malla= pd.Series([
    "#4", #Tamiz #4
    "#10", #Tamiz #10
    "#20", #Tamiz #20
    "#40", #Tamiz #40
    "#60", #Tamiz #60
    "#140", #Tamiz #140
    "#200", #Tamiz #200
    "fondo", #Fondo
])

Abertura= pd.Series([
    "4.750", #Abertura Tamiz #4
    "2.000", #Abertura Tamiz #10
    "0.850", #Abertura Tamiz #20
    "0.425", #Abertura Tamiz #40
    "0.250", #Abertura Tamiz #60
    "0.106", #Abertura Tamiz #140
    "0.075", #Abertura Tamiz #200
    "0", #fondo
])



Retenido= pd.Series([
    95, #Tamiz #4
    80, #Tamiz #10
    51, #Tamiz #20
    33, #Tamiz #40
    13, #Tamiz #60
    6, #Tamiz #140
    3, #Tamiz #200
    67, #Fondo
  
])

Acum=[] #Matriz donde se guardan los datos 
#Realizar calculo de datos, valor retenidido mas valor acumulado 
Acum.append(Retenido[0]+0)
Acum.append(Retenido[1]+Acum[0])
Acum.append(Retenido[2]+Acum[1])
Acum.append(Retenido[3]+Acum[2])
Acum.append(Retenido[4]+Acum[3])
Acum.append(Retenido[5]+Acum[4])
Acum.append(Retenido[6]+Acum[5])
Acum.append(Retenido[7]+Acum[6])
Ret_Acu =pd.Series(Acum)


AcuP=[] 
#Realizar Calculo, valor Acumulado total - valor retenido el el primer tamiz
AcuP.append(Acum[7]-Retenido[0])

#Valor acumulado menos el valor retenido en cada tamiz
AcuP.append(AcuP[0]-Retenido[1])
AcuP.append(AcuP[1]-Retenido[2])
AcuP.append(AcuP[2]-Retenido[3])
AcuP.append(AcuP[3]-Retenido[4])
AcuP.append(AcuP[4]-Retenido[5])
AcuP.append(AcuP[5]-Retenido[6])
AcuP.append(AcuP[6]-Retenido[7])
Pasa = pd.Series(AcuP)

Granulometria = pd.DataFrame({  #Se crea la tabla con los valores que se deben ingresar en cada columna 
    'Malla': Malla,
    'Abertura': Abertura,
    'Retenido': Retenido,
    'Retenido Acumulado': Ret_Acu,
    'Pasa': Pasa
})


Peso_Total = Granulometria["Retenido"].sum() #Obtenemos el peso total de la muestra de suelo 
Peso_Total

Porpasa=[] #Obtenemos el porcentaje que pasa en cada tamiz, con el peso que pasa y el peso total
Porpasa.append((Pasa[0]*100)/Peso_Total)
Porpasa.append((Pasa[1]*100)/Peso_Total)
Porpasa.append((Pasa[2]*100)/Peso_Total)
Porpasa.append((Pasa[3]*100)/Peso_Total)
Porpasa.append((Pasa[4]*100)/Peso_Total)
Porpasa.append((Pasa[5]*100)/Peso_Total)
Porpasa.append((Pasa[6]*100)/Peso_Total)
Porpasa.append((Pasa[7]*100)/Peso_Total)
Porcen_Pasa = pd.Series(Porpasa)

Granulometria = pd.DataFrame({ #Tabla con la nueva columna de %Pasa
    'Malla': Malla,
    'Abertura': Abertura,
    'Retenido': Retenido,
    'Retenido Acumulado': Ret_Acu,
    'Pasa': Pasa,
    '% Pasa': Porcen_Pasa
})

print(Granulometria)