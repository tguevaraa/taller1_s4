def base_de_datos():
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

db = base_de_datos()

while True:
    print("Bienvenido a la biblioteca")
    print("1. Registrar usuario")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Salir")
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        nombre = input("Ingrese su nombre de usuario: ")
        if nombre in db:
            print("El usuario ya existe")
        else:
            db[nombre] = {"libros": []}
            print("Usuario registrado exitosamente")
    
    elif opcion == "2":
        nombre = input("Ingrese su nombre de usuario: ")
        if nombre not in db:
            print("El usuario no existe, por favor registrese primero")
            continue
            
        if len(db[nombre]["libros"]) >= 3:
            print("No puede prestar mas de 3 libros a la vez")
            continue
            
        libro = input("Ingrese el nombre del libro: ")
        dias = int(input("Ingrese los dias de prestamo: "))
        
        for prestamo in db[nombre]["libros"]:
            if prestamo["titulo"] == libro:
                print(f"El libro '{libro}' ya esta prestado")
                break
        else:
            db[nombre]["libros"].append({"titulo": libro, "dias": dias})
            print(f"Libro '{libro}' prestado por {dias} dias a {nombre}")
    
    elif opcion == "3":
        nombre = input("Ingrese su nombre de usuario: ")
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
        print("Gracias por usar la biblioteca. Hasta luego!")
        break
    
    else:
        print("Opcion no valida, por favor intente de nuevo.")