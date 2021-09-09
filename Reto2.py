def CrearDiccionario(Codigo: int, Nombre: str, Edad : int, promedio: float, Colegiatura: float) -> dict:
    diccionarioEstudiante = {"Codigo":Codigo, "Nombre":Nombre, "Edad":Edad, "Promedio":promedio, "Colegiatura":Colegiatura}
    return diccionarioEstudiante

def AplicarColegiatura(Diccionarios: dict) -> str:
    if Diccionarios["Promedio"] >= 4.6:
        val_colegiatura = Diccionarios["Colegiatura"]*0.8
    else:
        val_colegiatura = Diccionarios["Colegiatura"]*1.1
    val="{0:.1f}".format(val_colegiatura)
    diccionarioEstudiante2 = {"Codigo":Diccionarios["Codigo"], "Nombre":Diccionarios["Nombre"], "Edad":Diccionarios["Edad"], "Promedio":Diccionarios["Promedio"], "Colegiatura":val_colegiatura}
    palabra = "Codigo: " + str(Diccionarios["Codigo"]) + ", Nombre: " + Diccionarios["Nombre"] + ", Edad: " + str(Diccionarios["Edad"]) + ", Promedio: " + str(Diccionarios["Promedio"]) + ", Colegiatura: " + val
    return palabra

print(CrearDiccionario(3001254,"Santiago",20, 4.0, 1000000))
print(CrearDiccionario(3599392,"Andres",17, 4.8, 23488000))
print(CrearDiccionario(3000045,"Carol",19, 3.2, 30000000445))
print(".................")
print(AplicarColegiatura(CrearDiccionario(3001254,"Santiago",20, 4.0, 1000000)))
print(type(AplicarColegiatura(CrearDiccionario(3001254,"Santiago",20, 4.0, 1000000))))
print(AplicarColegiatura(CrearDiccionario(3599392,"Andres",17, 4.8, 23488000)))
print(AplicarColegiatura(CrearDiccionario(3000045,"Carol",19, 3.2, 30000000445)))
