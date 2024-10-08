# Librería de funciones

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Funciones 

def crear_plantilla_de_ejercicios_semanal(lista_de_ejercicios):
    """
    Crea un DataFrame con ceros para los ejercicios indicados en la lista.
    
    Parámetros:
    lista_de_ejercicios (list): Lista de nombres de los ejercicios.
    
    Retorna:
    DataFrame: DataFrame con los días de la semana como columnas y los ejercicios como índices.
    """
    df_semanal = pd.DataFrame(0,
               index= lista_de_ejercicios,
               columns= ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo'])
    return df_semanal


def agregar_ejercicio(ejercicio_nuevo, df_base):
    """
    Agrega un nuevo ejercicio al DataFrame si no existe ya.
    
    Parámetros:
    ejercicio_nuevo (str): Nombre del ejercicio a agregar.
    df_base (DataFrame): DataFrame original.
    
    Retorna:
    DataFrame: Nuevo DataFrame con el ejercicio agregado.
    """
    df_nuevo = df_base.copy()
    if ejercicio_nuevo not in df_nuevo.index:
        df_nuevo.loc[ejercicio_nuevo] = 0
    else:
        print(f'El ejercicio "{ejercicio_nuevo}" ya existe en el DataFrame.')
    return df_nuevo


def eliminar_ejercicio(ejercicio_a_eliminar, df_base):
    """
    Elimina un ejercicio del DataFrame si existe.
    
    Parámetros:
    ejercicio_a_eliminar (str): Nombre del ejercicio a eliminar.
    df_base (DataFrame): DataFrame original.
    
    Retorna:
    DataFrame: Nuevo DataFrame con el ejercicio eliminado.
    """
    df_nuevo = df_base.copy()
    if ejercicio_a_eliminar in df_nuevo.index:
        df_nuevo = df_nuevo.drop(ejercicio_a_eliminar)
    else:
        print(f'El ejercicio "{ejercicio_a_eliminar}" no existe o ya ha sido eliminado.')
    return df_nuevo


def completar_dia(dia, arreglo_de_repeticiones):
    """
    Completa las repeticiones de un día específico en el DataFrame.
    
    Parámetros:
    dia (str): Día de la semana a completar (e.g., 'lunes').
    arreglo_de_repeticiones (array): Array con las repeticiones para cada ejercicio.
    
    Retorna:
    DataFrame: Nuevo DataFrame con las repeticiones cargadas.
    """
    df_semanal = df_semanal_sin_cargar.copy()
    if len(arreglo_de_repeticiones) == len(df_semanal.index):
        df_semanal.loc[:, dia] = arreglo_de_repeticiones
    else:
        print('El arreglo de repeticiones no coincide con el número de ejercicios cargados.')

    return df_semanal


def graficar_ejercicio(ejercicio, df_base):
    """
    Grafica la evolución de un ejercicio a lo largo de la semana.
    
    Parámetros:
    ejercicio (str): Nombre del ejercicio a graficar.
    df_base (DataFrame): DataFrame que contiene las repeticiones.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(df_base.columns, df_base.loc[ejercicio], color= "grey")
    plt.title(f"Evolución de {ejercicio} a lo largo de la semana")
    plt.xlabel('Días de la semana')
    plt.ylabel('Repeticiones')
    plt.show()


def graficar_proporcion_ejercicios(ejercicio, df_base):
    """
    Grafica la proporción de repeticiones de cada ejercicio a lo largo de la semana.
    
    Parámetros:
    ejercicio (str): Nombre del ejercicio a resaltar en el gráfico.
    df_base (DataFrame): DataFrame que contiene las repeticiones.
    """
    suma_repeticiones = df_base.sum(axis=1)
    total_repeticiones = suma_repeticiones.sum()
    proporciones = round((suma_repeticiones / total_repeticiones), 4) * 100

    colores = ['orange' if ej == ejercicio else 'skyblue' for ej in proporciones.index] #Usé un for, no me maten :)
    plt.figure(figsize=(8, 8))
    plt.pie(proporciones, labels=proporciones.index, autopct='%1.1f%%', colors=colores, wedgeprops=dict(edgecolor='black'))
    plt.title('Proporción de repeticiones de cada ejercicio a lo largo de la semana')
    plt.show()