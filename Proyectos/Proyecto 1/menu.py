# Manuel Jarque

import app_ejercicios as ae

def main():
    df_semanal = None  # Inicialmente no hay DataFrame

    while True:
        print("\n--- Menú de Ejercicios ---")
        print("1. Crear plantilla de ejercicios\n2. Agregar ejercicio\n3. Eliminar ejercicio\n4. Completar repeticiones del día\n5. Graficar ejercicio\n6. Graficar proporción de ejercicios\n7. Salir")

        opcion = input("Selecciona una opción (1-7): ")

        if opcion == '1':
            lista_de_ejercicios = input("Ingresa los ejercicios (separados por comas): ").split(',')
            lista_de_ejercicios = [ej.strip() for ej in lista_de_ejercicios if ej.strip()]
            if len(lista_de_ejercicios) == 0:
                print("Error: Debes ingresar al menos un ejercicio.")
            else:
                df_semanal = ae.crear_plantilla_de_ejercicios_semanal(lista_de_ejercicios)
                print("Plantilla creada con los siguientes ejercicios:")
                print(df_semanal)

        elif opcion == '2':
            if df_semanal is None:
                print("Primero debes crear una plantilla de ejercicios (opción 1).")
                continue
            ejercicio_nuevo = input("Nombre del ejercicio a agregar: ")
            df_semanal = ae.agregar_ejercicio(ejercicio_nuevo, df_semanal)
            print(df_semanal)

        elif opcion == '3':
            if df_semanal is None:
                print("Primero debes crear una plantilla de ejercicios (opción 1).")
                continue
            ejercicio_a_eliminar = input("Nombre del ejercicio a eliminar: ")
            df_semanal = ae.eliminar_ejercicio(ejercicio_a_eliminar, df_semanal)
            print(df_semanal)

        elif opcion == '4':
            if df_semanal is None:
                print("Primero debes crear una plantilla de ejercicios (opción 1).")
                continue
            dia = input("Día de la semana: ").lower()
            repeticiones = input("Repeticiones (separadas por comas): ").split(',')
            try:
                repeticiones = [int(reps) for reps in repeticiones]
                df_semanal = ae.completar_dia(dia, repeticiones, df_semanal)
                print(df_semanal)
            except ValueError:
                print("Error: Todas las repeticiones deben ser números enteros.")

        elif opcion == '5':
            if df_semanal is None:
                print("Primero debes crear una plantilla de ejercicios (opción 1).")
                continue
            ejercicio = input("Nombre del ejercicio a graficar: ")
            ae.graficar_ejercicio(ejercicio, df_semanal)

        elif opcion == '6':
            if df_semanal is None:
                print("Primero debes crear una plantilla de ejercicios (opción 1).")
                continue
            ejercicio = input("Nombre del ejercicio para proporción: ")
            ae.graficar_proporcion_ejercicios(ejercicio, df_semanal)

        elif opcion == '7':
            print("Saliendo del menú.")
            break

        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
