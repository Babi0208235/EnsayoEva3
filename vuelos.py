print("=== REGISTRO DE EQUIPAJE - VUELOSCHILE ===")
#1.- validar la cantidad total de equipaje a registrar 
total_equipaje = 0
while total_equipaje <= 0:
    try:
        entrada = input("¿Cuantos equipajes desea registrar?: ")
        total_equipaje = int(entrada)
        if total_equipaje <= 0:
           print("¡cantidad invalida! ingresa un entero positivo para continuar")
    except ValueError:
        print("¡Cantidad invalida! ingresa un entero positivo para continuar")
#inicializacion de contadores
equipajes_cabina = 0 
equipajes_bodega = 0
#ciclo de registro del equipaje
for i in range(total_equipaje):
    print(f"\n---Registro del equipaje n° {i+1} ---")
    #validacion del codigo del ticket 
    codigo_ticket = ""
    while True:
        codigo_ticket = input("ingrese codigo de ticket (min 5 caracteres, sin espacios)")
        #validar largo de codigo de ticket
        if len(codigo_ticket) < 5 :
            print("¡Error!, el codigo debe tener al menos 5 caracteres")
            continue
        #validar que no tenga espacios
        tiene_espacios = False
        for caracter in codigo_ticket:
            if caracter == " ":
                tiene_espacios = True
        if tiene_espacios:
            print("¡Error!, el codigo no debe incluir espacios")
            continue 
        break
    #validacion del peso 
    peso = -1
    while peso <= 0:
        try:
            entrada_peso = input("ingrese el peso del equipaje en KG (entero positivo")
            peso = int(entrada_peso)
            if peso <= 0:
                print("¡Error de pesaje! ingrese un numero positivo para el peso ")
        except ValueError:
            print("¡Error de pesaje! ingrese un numero positivo para el peso ") 
        #clasificacion del equipaje 
        if peso > 10:
            equipajes_bodega += 1
            print("clasificado como equipaje de bodega")
        else:
            equipajes_cabina += 1
            print("clasificado como equipaje de cabina ")
    #Salida final
print("\n================================================================================") 
print(f"¡el avion transportara {equipajes_cabina} equipajes en cabina y {equipajes_bodega} equipajes en bodega! ¡Manifiesto de carga listo!")
print("\n================================================================================")   


