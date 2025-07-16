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
                print("\nRegistrar estudiante")
                cantidad_estudiantes = int(input("Cuantos estudiantes desea registrar: "))
                for i in range(cantidad_estudiantes):
                    carnet = input(f"Ingresa el carnet del estudiante No.{i+1}: ")
                    if carnet in estudiantes:
                        print("El carnet ya esta registrado en el sistema")
                    else:
                        nombre_estudiante = input(f"Ingresa el nombre del estudiante No.{i+1}: ")
                        edad_estudiante = input(f"Ingresa la edad del estudiante No.{i+1}: ")
                        carrera_estudiante = input(f"Ingresa la carrera del estudiante No.{i+1}: ")
                        cantidad_cursos = int(input(f"Cuantos cursos desea registrar al estudiante No.{i+1} (Limite 10 cursos): "))
                        if cantidad_cursos > 0 and cantidad_cursos<=10:
                            for curso in range(cantidad_cursos):
                                nombre_curso = input(f"Ingresa el nombre del curso {curso + 1} del estudiante No.{i + 1}: ")
                                nota_tarea = int(input(f"Ingrese la nota de tareas del curso {curso + 1} del estudiante No.{i + 1}: "))
                                if nota_tarea <= 0 or nota_tarea > 100:
                                    print("Un curso no puede tener una nota menor a 0 o mayor a 100")
                                else:
                                    nota_parcial = int(input(f"Ingrese la nota del parcial del curso {curso + 1} del estudiante No.{i + 1}: "))
                                    if nota_parcial <= 0 or nota_parcial > 100:
                                        print("Un curso no puede tener una nota menor a 0 o mayor a 100")
                                    else:
                                        nota_proyecto = int(input(f"Ingrese la nota del proyecto del curso {curso + 1} del estudiante No.{i + 1}: "))
                                        if nota_proyecto <= 0 or nota_proyecto > 100:
                                            print("Un curso no puede tener una nota menor a 0 o mayor a 100")
                                        else:
                                            estudiantes[carnet]={
                                                "nombre_estudiante":nombre_estudiante,
                                                "edad_estudiante":edad_estudiante,
                                                "carrera_estudiante":carrera_estudiante,
                                                "cursos":{
                                                    "nombre_curso":nombre_curso,
                                                    "nota_tarea":nota_tarea,
                                                    "nota_parcial": nota_parcial,
                                                    "nota_proyecto":nota_proyecto
                                                }
                                            }
                        else:
                            print("Cursos deben ser mayor a 0 y tambien no puede superar 10 cursos por estudiante")

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