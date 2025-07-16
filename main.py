def Menu():
    print("---Menu---")
    print("1. Registrar estudiante")
    print("2. Mostrar todos los estudiantes y cursos")
    print("3. Buscar estudiante por carnet")
    print("4. Salir")
estudiantes = {}
while True:
    Menu()
    try:
        opcion=int(input("Selecciona una opcion: "))
        match opcion:
            case 1:
                print("Registrar estudiante")

            case 2:
                print("Mostrar todos los estudiantes y cursos")
            case 3:
                print("Buscar estudiante por carnet")
            case 4:
                print("Gracias por utilizar el programa")
                break
            case _:
                print("Opcion invalida")
    except Exception:
        print("Solo es permitido ingresar numeros")