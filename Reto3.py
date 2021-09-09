def CrearDiccionarioEstudiante(Codigo: int, Nombre: str, Edad:int, promedio: float, Maestrias: list) -> dict:
    diccionarioEstudiante = {"Codigo":Codigo, "Nombre":Nombre, "Edad":Edad, "Promedio":promedio, "Maestrias":Maestrias}
    return diccionarioEstudiante

def MostrarEstudiantesConMaestrias (DiccionarioEstudiante:dict)->str:
    if DiccionarioEstudiante["Promedio"] >= 4.8:
        if len(DiccionarioEstudiante["Maestrias"]) > 2:
            M_gratis=[DiccionarioEstudiante["Maestrias"][0],DiccionarioEstudiante["Maestrias"][1]]
            M_pago=DiccionarioEstudiante["Maestrias"][2:len(DiccionarioEstudiante["Maestrias"])]
            listToStr1 = ', '.join([str(elem) for elem in M_gratis])
            listToStr2 = ', '.join([str(elem2) for elem2 in M_pago])
            master= "\nMaestrias Gratis: " + listToStr1 + "\nMaestrias: " + listToStr2
        else:
            M_gratis=[DiccionarioEstudiante["Maestrias"][0]]
            listToStr1 = ', '.join([str(elem) for elem in M_gratis])
            master= "\nMaestrias Gratis: " + listToStr1
    else:
        M_pago=DiccionarioEstudiante["Maestrias"]
        listToStr2 = ', '.join([str(elem2) for elem2 in M_pago])
        master =  "\nMaestrias: " + listToStr2
    pal= "Codigo: " + str(DiccionarioEstudiante["Codigo"]) + "\nNombre: " + DiccionarioEstudiante["Nombre"] + "\nEdad: " + str(DiccionarioEstudiante["Edad"]) + "\nPromedio: " + str(DiccionarioEstudiante["Promedio"]) + master
    return pal

#print(CrearDiccionarioEstudiante(123124,"Santiago",20, 4.8, ["mecatrónica","bioingeniería", "procesos","finanzas"]))
#print(CrearDiccionarioEstudiante(253255,"Carol",22, 5, ["informática","bioingeniería", "procesos","finanzas","ecología","química"]))
#print(CrearDiccionarioEstudiante(25354555,"Andrea",22, 3.8, ["mecatrónica","telemática"]))
#print(".................")
print(MostrarEstudiantesConMaestrias(CrearDiccionarioEstudiante(123124,"Santiago",20, 4.8, ["mecatrónica","bioingeniería", "procesos","finanzas"])))
#print(MostrarEstudiantesConMaestrias(CrearDiccionarioEstudiante(253255,"Carol",22, 5, ["informática","bioingeniería", "procesos","finanzas","ecología","química"])))
#print(MostrarEstudiantesConMaestrias(CrearDiccionarioEstudiante(25354555,"Andrea",22, 3.8, ["mecatrónica","telemática"])))