Reseñas = int(input("Reseñas: "))
PrecioApp = int(input("PrecioApp: "))
Meses = int(input("Meses: "))

Ganacia = Reseñas * PrecioApp
GanaciaPorMes = int(Ganacia / Meses)

print("Ganacia total:", Ganacia , "MXN")
print("Ganacia por mes:", GanaciaPorMes, "MXN" )
