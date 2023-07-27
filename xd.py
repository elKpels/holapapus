def final():
    print("Agarro mi mochila")
    print("Me subo al carro")
    print("A chambear")

print("Me levanto")
respuesta_banho = input("¿Me bañé?: 'Y/N' ")

if respuesta_banho == "Y":
    print("Me cambio")
    respuesta_media_hora = input("¿Tengo más de media hora?: 'Y/N' ")
    if respuesta_media_hora == "Y":
        print("Desayuno")
    final()
else:
    print("Me baño")
    print("Me cambio")
    respuesta_media_hora = input("¿Tengo más de media hora?: 'Y/N' ")
    if respuesta_media_hora == "Y":
        print("Desayuno")
    final()
