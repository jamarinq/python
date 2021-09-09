def Cantidad_de_plantas(CadenaLugar: str, CadenaCultivo:str, LargoTerreno:float, AnchoTerreno:float, LargoCultivo:float, AnchoCultivo:float)->str:
    cantidad = (LargoTerreno*AnchoTerreno)//(LargoCultivo*AnchoCultivo)
    return "En "+ CadenaLugar + " se pueden plantar " + str(cantidad) + " de " + CadenaCultivo

print (Cantidad_de_plantas("chia","remolachas",6,6,2,2))
print (Cantidad_de_plantas("zipaquira","papas",90,90,10,10))
print (Cantidad_de_plantas("cajica","yucas",6500,6500,100,100))