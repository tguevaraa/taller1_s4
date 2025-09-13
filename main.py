def base_de_datos():#funcion que simula una base de datos con usuarios y sus prestamos
    usuarios = {
        "pepitoPerez": {
            "libros": [{"titulo": "juan de la mancha", "dias": 6}, 
                       {"titulo": "el principito", "dias": 6}, 
                       {"titulo": "50 sombras de grey", "dias": 7}]
        },
        "juanPerez": {
            "libros": []
        }
    }
    return usuarios

#Aqui empieza el programa

db = base_de_datos() #variable que simula la base de datos

while True:
    print("-----Bienvenido a la biblioteca-----")
    print("\n1. Registrar usuario")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Ver estadisticas de usuario")
    print("5. Libros con préstamo mayor a 15 días")
    print("6. Salir")
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        nombre = input("\nIngrese su nombre de usuario: ")
        if nombre in db:
            print("El usuario ya existe")
        else:
            db[nombre] = {"libros": []}
            print("Usuario registrado exitosamente")
    
    elif opcion == "2":
        nombre = input("\nIngrese su nombre de usuario: ")
        if nombre not in db:
            print("El usuario no existe, por favor registrese primero")
            continue
            
        if len(db[nombre]["libros"]) >= 3:
            print("No puede prestar mas de 3 libros a la vez")
            continue
            
        libro = input("\nIngrese el nombre del libro: ")
        dias = int(input("Ingrese los dias de prestamo: "))
        
        for prestamo in db[nombre]["libros"]:
            if prestamo["titulo"] == libro:
                print(f"El libro '{libro}' ya esta prestado")
                break
        else:
            db[nombre]["libros"].append({"titulo": libro, "dias": dias})#agregar el libro a la lista de prestamos del usuario
            print(f"Libro '{libro}' prestado por {dias} dias a {nombre}")
    
    elif opcion == "3":
        nombre = input("\nIngrese su nombre de usuario: ")
        if nombre not in db:
            print("El usuario no existe, por favor registrese primero")
            continue
            
        libro = input("Ingrese el nombre del libro a devolver: ")
        for prestamo in db[nombre]["libros"]:
            if prestamo["titulo"] == libro:
                db[nombre]["libros"].remove(prestamo)
                print(f"Libro '{libro}' devuelto exitosamente por {nombre}")
                break
        else:
            print(f"El libro '{libro}' no esta prestado a {nombre}")
    
    elif opcion == "4":
        nombre = input("\nIngrese su nombre de usuario: ")
        if nombre not in db:
            print("El usuario no existe, por favor registrese primero")
            continue
        if db[nombre]["libros"]:
                total_prestamos = len(db[nombre]["libros"])
                promedio_dias = sum(p["dias"] for p in db[nombre]["libros"]) / total_prestamos
                print(f"\nTotal de préstamos actuales: {total_prestamos}")
                print(f"Promedio de días de préstamo: {int(promedio_dias)}")
    
    elif opcion == "5":
        print("\nLibros con préstamo mayor a 15 días:\n")
        encontrado = False
        for usuario, datos in db.items():
            for libro in datos["libros"]:
                if libro["dias"] > 15:
                    titulo = libro["titulo"]
                    dias = libro["dias"]
                    print(f"{titulo} prestado por {dias} días a {usuario}")
                    encontrado = True
        if not encontrado:
            print("No hay libros prestados por más de 15 días.")
    
    elif opcion == "6":
        print("\nGracias por usar la biblioteca. Hasta luego!")
        break
    
    else:
        print("\nOpcion no valida, por favor intente de nuevo.")