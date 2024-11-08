# Manuel Jarque

from PIL import Image, ImageFilter, ImageOps, ImageEnhance
import cv2
import matplotlib.pyplot as plt
import numpy as np


#Ejercicio 1
def redimensionar_imagen(ruta, nombre, plataforma):
    """
    Redimensiona una imagen a las dimensiones recomendadas para una plataforma específica, manteniendo la relación de aspecto.

    Parámetros:
    ruta (str): Ruta del directorio donde se encuentra la imagen.
    nombre (str): Nombre del archivo de la imagen a redimensionar.
    plataforma (str): Nombre de la plataforma objetivo ('Instagram', 'Facebook', 'Twitter', 'Youtube').

    Retorna:
    Image: Objeto de la imagen redimensionada en el tamaño recomendado para la plataforma especificada.
          Si la plataforma no está reconocida, se retorna la imagen original sin cambios.

    Raises:
    FileNotFoundError: Si la ruta o el archivo de la imagen no es válido.

    Notas:
    Las dimensiones objetivo por plataforma son:
    - Instagram: 1080x1080
    - Facebook: 1200x630
    - Twitter: 1024x512
    - Youtube: 1280x720

    La imagen se guarda con un nuevo nombre basado en la plataforma seleccionada.
    """


    img = Image.open(ruta + nombre)
    print(f"Dimensiones originales de la imagen: {img.size}")

    plataforma = plataforma.capitalize()
    dimensiones = {
        "Instagram": (1080, 1080),
        "Facebook": (1200, 630),
        "Twitter": (1024, 512),
        "Youtube": (1280, 720)
    }

    if plataforma not in dimensiones:
        print("Plataforma no reconocida. Usa: 'Instagram', 'Facebook', 'Twitter' o 'Youtube'.")
        return img

    ancho_objetivo, alto_objetivo = dimensiones[plataforma]

    img.thumbnail((ancho_objetivo, alto_objetivo))
    
    nombre_redimensionada = input("Ingrese el nombre para la imagen redimensionada (separando las palabras con _): ")

    print(f"Imagen redimensionada a {img.size} para {plataforma}")
    img.save(ruta + f"{nombre_redimensionada.lower()}_para_{plataforma.lower()}.png")
    print(f"Imagen guardada como '{nombre_redimensionada.lower()}_para_{plataforma.lower()}.png'")
    
    return img


#-------------------------------------------------------

#Ejercicio 2
def ajustar_contraste(ruta, nombre):
    """
    Ajusta el contraste de una imagen utilizando la ecualización de histograma y muestra los resultados.

    Parámetros:
    ruta (str): Ruta del directorio donde se encuentra la imagen.
    nombre (str): Nombre del archivo de la imagen a procesar.

    Retorna:
    None: La función guarda la imagen ecualizada en el directorio especificado y muestra el histograma original y ecualizado.

    Raises:
    FileNotFoundError: Si la ruta o el archivo de la imagen no es válido.

    Notas:
    La función realiza los siguientes pasos:
    - Lee la imagen en escala de grises.
    - Muestra el histograma original junto con su función de distribución acumulativa (CDF).
    - Realiza la ecualización del histograma de la imagen para mejorar el contraste.
    - Muestra la imagen ecualizada y su histograma correspondiente.
    - La imagen ecualizada se guarda con el nombre proporcionado por el usuario.
    """

    img = cv2.imread(ruta + nombre, 0)
    img_np = np.array(img)

    hist, bins = np.histogram(img_np.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()

    plt.figure(figsize=(12, 6))
    plt.subplot(2, 2, 1)
    plt.imshow(img_np, cmap='gray')
    plt.title("Imagen original")
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.plot(cdf_normalized, color='b')
    plt.hist(img_np.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.legend(('CDF', 'Histograma'), loc='upper left')
    plt.title("Histograma original")

    equ = cv2.equalizeHist(img_np)

    hist_eq, bins_eq = np.histogram(equ.flatten(), 256, [0, 256])
    cdf_eq = hist_eq.cumsum()
    cdf_eq_normalized = cdf_eq * hist_eq.max() / cdf_eq.max()

    plt.subplot(2, 2, 3)
    plt.imshow(equ, cmap='gray')
    plt.title("Imagen ecualizada")
    plt.axis("off")

    plt.subplot(2, 2, 4)
    plt.plot(cdf_eq_normalized, color='b')
    plt.hist(equ.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.legend(('CDF', 'Histograma'), loc='upper left')
    plt.title("Histograma ecualizado")

    nombre_ecualizada = input("Ingrese el nombre para la imagen ecualizada (separando las palabras con _): ")
    Image.fromarray(equ).save(ruta + f"{nombre_ecualizada.lower()}_ecualizada.png")
    print(f"Imagen guardada como '{nombre_ecualizada.lower()}_ecualizada.png'")

    plt.tight_layout()
    plt.show()

#-------------------------------------------------------

#Ejercicio 3
def aplicar_filtro(ruta, nombre, filtro_seleccionado):
    """
    Aplica un filtro seleccionado a una imagen y guarda tanto la imagen filtrada como una imagen con todos los filtros aplicados.

    Parámetros:
    ruta (str): Ruta del directorio donde se encuentra la imagen.
    nombre (str): Nombre del archivo de la imagen a procesar.
    filtro_seleccionado (str): El nombre del filtro a aplicar. Puede ser uno de los siguientes: 
                                'Blur', 'Contour', 'Detail', 'Edge Enhance', 'Edge Enhance More', 
                                'Emboss', 'Find Edges', 'Sharpen', 'Smooth'.

    Retorna:
    None: La función guarda la imagen filtrada con el filtro seleccionado y una imagen con todos los filtros aplicados en el directorio especificado.

    Raises:
    FileNotFoundError: Si la ruta o el archivo de la imagen no es válido.

    Notas:
    La función realiza los siguientes pasos:
    - Aplica el filtro seleccionado a la imagen y la guarda con un nombre proporcionado por el usuario.
    - Muestra la imagen original y las versiones con todos los filtros aplicados en una cuadrícula.
    - Guarda la imagen con todos los filtros aplicados.
    - Si el filtro seleccionado no es válido, se mostrará una lista de filtros disponibles.
    """

    img = Image.open(ruta + nombre)

    filtro_seleccionado = filtro_seleccionado.capitalize()
    filtros = {
        "Blur": ImageFilter.BLUR,
        "Contour": ImageFilter.CONTOUR,
        "Detail": ImageFilter.DETAIL,
        "Edge Enhance": ImageFilter.EDGE_ENHANCE,
        "Edge Enhance More": ImageFilter.EDGE_ENHANCE_MORE,
        "Emboss": ImageFilter.EMBOSS,
        "Find Edges": ImageFilter.FIND_EDGES,
        "Sharpen": ImageFilter.SHARPEN,
        "Smooth": ImageFilter.SMOOTH
    }

    if filtro_seleccionado not in filtros:
        print("Filtro no válido. Elige uno de los siguientes:")
        for nombre in filtros:
            print(f"- {nombre}")
        return

    img_filtro_seleccionado = img.filter(filtros[filtro_seleccionado])
    nombre_filtrada = input("Ingrese el nombre para la imagen con filtro (separando las palabras con _): ")
    img_filtro_seleccionado.save(ruta + f"{nombre_filtrada.lower()}_con_filtro_{filtro_seleccionado.lower()}.png")
    print(f"Imagen con filtro '{filtro_seleccionado.lower()}' guardada como '{nombre_filtrada.lower()}_con_filtro_{filtro_seleccionado.lower()}.png'.")

    plt.figure(figsize=(15, 8))

    plt.subplot(3, 4, 1)
    plt.imshow(img)
    plt.title("Original")
    plt.axis("off")

    for i, (nombre_filtro, filtro) in enumerate(filtros.items(), start=2):
        img_filtrada = img.filter(filtro)
        plt.subplot(3, 4, i)
        plt.imshow(img_filtrada)
        plt.title(nombre_filtro, color='red' if nombre_filtro == filtro_seleccionado else 'black')
        plt.axis("off")

    plt.savefig(ruta + f"{nombre_filtrada.lower()}_todos_los_filtros.png")
    print(f"Imagen con todos los filtros guardada como '{nombre_filtrada.lower()}_todos_los_filtros.png'.")

    plt.tight_layout()
    plt.show()


#-------------------------------------------------------

#Ejercicio 4
def crear_boceto(ruta, nombre, persona = True):
    """
    Convierte una imagen en un boceto en blanco y negro con bordes realzados. Si la imagen no es de una persona, el efecto de boceto no se aplica.

    Parámetros:
    ruta (str): Ruta del directorio donde se encuentra la imagen.
    nombre (str): Nombre del archivo de la imagen a procesar.
    persona (bool, opcional): Indica si la imagen es de una persona. Si es False, no se aplicará el efecto de boceto. El valor por defecto es True.

    Retorna:
    None: La función guarda la imagen procesada como un boceto realzado con bordes en el directorio especificado.

    Raises:
    FileNotFoundError: Si la ruta o el archivo de la imagen no es válido.

    Notas:
    La función realiza los siguientes pasos:
    - Convierte la imagen a escala de grises.
    - Aplica un filtro de suavizado (desenfoque gaussiano).
    - Detecta los bordes de la imagen.
    - Realza los bordes con un ajuste de nitidez y contraste.
    - Si `persona` es False, la función no aplica el efecto y muestra un mensaje indicando que no es una imagen de persona.
    - Guarda la imagen resultante como un archivo con el nombre proporcionado por el usuario.
    """

    if not persona:
        print("La imagen no es de una persona. No se aplicará el efecto de boceto.")
        return

    img = Image.open(ruta + nombre).convert("L")

    img_suavizada = img.filter(ImageFilter.GaussianBlur(radius= 1.7))

    img_bordes = img_suavizada.filter(ImageFilter.FIND_EDGES)


    img_realzada =ImageEnhance.Sharpness(img_bordes).enhance(3.0)


    img_realzada = ImageEnhance.Contrast(img_realzada).enhance(2.5)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(img_realzada, cmap='gray')
    plt.title("Boceto con bordes realzados")
    plt.axis("off")

    nombre_boceto = input("Ingrese el nombre para el boceto (separando las palabras con _): ")
    img_realzada.save(ruta + f"{nombre_boceto.lower()}_realzado.png")
    print(f"Imagen de boceto guardada como '{nombre_boceto.lower()}_realzado.png'.")

    plt.tight_layout()
    plt.show()