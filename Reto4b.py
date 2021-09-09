def CrearDiccionarioEstudiante(Informacion: str) -> dict:
    val=Informacion.split("%")
    d2={}
    for x in val:
        if x.startswith("TLI"):
            claves1=(x.split(";"))
            claves1.pop(0)
            #print(type(claves1))
            #print(claves1)
        else:
            valores1=x.split(";")
            clave2=valores1[0]
            valores1.pop(0)
            d1 = dict(zip(claves1,valores1))
            d2[clave2]=d1
            #print(clave2)
    #print(d2)
    return d2

def PromedioMayorMenor(diccionarioE: dict)->list:
    listaPro=[]
    for key in diccionarioE:
        listaPro.append(float(diccionarioE[key]["Promedio"]))
        #print(x[key].get("Promedio"))
    promedio=sum(listaPro)/len(listaPro)
    pal="El promedio de notas de los {nE} estudiantes es: {pr}, la nota mas alta es: {Nmayor} y la nota menor es: {Nmenor}".format(nE=len(listaPro),
    pr=promedio,Nmayor=max(listaPro),Nmenor=min(listaPro))
    #print(pal)
    return pal
    
def ImprimirLaInfo(diccionarioEp: dict) ->str:
    for key1 in diccionarioEp:
        for key2 in diccionarioEp[key1]:
            palEst=(str(key2)+" : "+ str(diccionarioEp[key1][key2]))
            print(palEst)
        print("")


lis1=CrearDiccionarioEstudiante("TLI;Nombre;CC;Teléfono;Promedio%234jj234d2;Santiago Perez;1006614805;30139020352;4.5%fff342345d;Carol Martinez;111234882;3213213214;4.9%fgfg3333d2;Juan Felacio;11124992;3092404231;2.2")
lis2=CrearDiccionarioEstudiante("TLI;Nombre;CC;Teléfono;Promedio%dg8288wj3;Alejandra Gonzales;11112342;3002431243;3.2%ee23553mmd;Andrea Garcia;1002341242;3013090222;1.2")
#print("...............")
#print(lis1)
#PromedioMayorMenor([lis1,lis2])
#print("...............")
ImprimirLaInfo(lis1)
ImprimirLaInfo(lis2)
#infor=list(map(PromedioMayorMenor,[lis1,lis2]))