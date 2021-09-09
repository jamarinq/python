import pandas as pd
import numpy as np

from pandas.core.arrays.sparse import dtype


doc1="https://raw.githubusercontent.com/jamarinq/imaster/main/cotizacion.csv"

def resumen_cotizaciones(fichero:str) -> pd.DataFrame:
    df=pd.read_csv(fichero,sep=";",decimal=",",thousands=".")
    #df["Final"]=df["Final"].replace(',','.',regex=True).astype(float)	
    #df=df.replace('.','',regex=True)
    #df["Final"].astype("float")
    #P_final=df2["Final"].mean()
    #print(P_final)
    columnas=["Final","Máximo", "Mínimo", "Volumen", "Efectivo"]
    filas=["Mínimo","Máximo","Media"]
    df2=pd.DataFrame([df.min(),df.max(),df.mean()], columns=columnas,index=filas)
    #print(df2)
    return df2

def HacerMatrizN(fichero:str) -> np.load:
    #df=pd.read_csv(fichero,sep=";",decimal=",",thousands=".")
    #mat=df.to_numpy
    mat=np.loadtxt(fichero,delimiter=";",dtype="str",skiprows=2)
    #print(mat)
    return mat

def ObtenerInfo(fichero: str, Buscar: str) -> pd.DataFrame:
    columnas=["Nombre","Final","Máximo", "Mínimo", "Volumen", "Efectivo"]
    filas=Buscar
    df=pd.read_csv(fichero,sep=";",decimal=",",thousands=".")
    df2=df[df["Nombre"]==Buscar]
    #print(df2)
    return df2
    #df2=pd.DataFrame(["hola"], columns=columnas,index=filas)

doc1="https://raw.githubusercontent.com/jamarinq/imaster/main/cotizacion.csv"
print(resumen_cotizaciones(doc1))
print(HacerMatrizN(doc1))
print(ObtenerInfo(doc1, "ACCIONA"))
print(ObtenerInfo(doc1, "BBVA"))