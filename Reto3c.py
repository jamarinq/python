def CrearDiccionarioEstudiante(Codigo: int, Nombre: str, Edad:int, promedio: float, Maestrias: list) -> dict:
    diccionarioEstudiante = {"Codigo":Codigo, "Nombre":Nombre, "Edad":Edad, "Promedio":promedio, "Maestrias":Maestrias}
    MostrarEstudiantesConMaestrias(diccionarioEstudiante)
    return diccionarioEstudiante

def MostrarEstudiantesConMaestrias (DiccionarioEstudiante:dict)->str:
    if DiccionarioEstudiante["Promedio"] >= 4.8:
        if len(DiccionarioEstudiante["Maestrias"]) > 2:
            M_gratis=[DiccionarioEstudiante["Maestrias"][0],DiccionarioEstudiante["Maestrias"][1]]
            M_pago=DiccionarioEstudiante["Maestrias"][2:len(DiccionarioEstudiante["Maestrias"])]
            listToStr1 = ', '.join([str(elem) for elem in M_gratis])
            listToStr2 = ', '.join([str(elem2) for elem2 in M_pago])
            master= "\nMaestrias Gratis: " + listToStr1 + "\nMaestrias: " + listToStr2
        elif len(DiccionarioEstudiante["Maestrias"]) == 2:
            M_gratis=[DiccionarioEstudiante["Maestrias"][0]]
            listToStr1 = ', '.join([str(elem) for elem in M_gratis])
            M_pago=[DiccionarioEstudiante["Maestrias"][1]]
            listToStr2 = ', '.join([str(elem2) for elem2 in M_pago])
            master= "\nMaestria Gratis: " + listToStr1 + "\nMaestrias: " + listToStr2
        else:
            M_gratis=[DiccionarioEstudiante["Maestrias"][0]]
            listToStr1 = ', '.join([str(elem) for elem in M_gratis])
            master= "\nMaestria Gratis: " + listToStr1
    else:
        M_pago=DiccionarioEstudiante["Maestrias"]
        listToStr2 = ', '.join([str(elem2) for elem2 in M_pago])
        master =  "\nMaestrias: " + listToStr2
    pal= "Codigo: " + str(DiccionarioEstudiante["Codigo"]) + "\nNombre: " + DiccionarioEstudiante["Nombre"] + "\nEdad: " + str(DiccionarioEstudiante["Edad"]) + "\nPromedio: " + str(DiccionarioEstudiante["Promedio"]) + master
    print(pal)
    #return pal

CrearDiccionarioEstudiante(123124,"Santiago",20, 4.8, ["mecatrónica","bioingeniería", "procesos","finanzas"])
CrearDiccionarioEstudiante(253255,"Carol",22, 5, ["informática","bioingeniería", "procesos","finanzas","ecología","química"])
CrearDiccionarioEstudiante(25354555,"Andrea",22, 3.8, ["mecatrónica","telemática"])
CrearDiccionarioEstudiante(525453,"Juank",25, 3.2, ["mecatrónica","bioingeniería", "procesos","finanzas","optimizacion"])
CrearDiccionarioEstudiante(235323,"Carolina",25, 4.9, ["informática","química"])
CrearDiccionarioEstudiante(121423,"Fransisco",22, 3.3, ["mecatrónica","telemática","finanzas","ecología"])
#print(".................")
#print(MostrarEstudiantesConMaestrias(CrearDiccionarioEstudiante(123124,"Santiago",20, 4.8, ["mecatrónica","bioingeniería", "procesos","finanzas"])))
#print(MostrarEstudiantesConMaestrias(CrearDiccionarioEstudiante(253255,"Carol",22, 5, ["informática","bioingeniería", "procesos","finanzas","ecología","química"])))
#print(MostrarEstudiantesConMaestrias(CrearDiccionarioEstudiante(25354555,"Andrea",22, 3.8, ["mecatrónica","telemática"])))