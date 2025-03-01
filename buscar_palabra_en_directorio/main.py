import os

def buscar_palabra_en_archivos(directorio, palabra):
    """
    Busca una palabra dentro de todos los archivos de texto en un directorio.

    :param directorio: Ruta del directorio donde buscar.
    :param palabra: Palabra a buscar.
    """
    resultados = []

    # Recorrer todos los archivos en el directorio
    for root, _, files in os.walk(directorio):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
    
                try:
                    # Leer cada archivo
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        for num_linea, linea in enumerate(f, start=1):
                            if palabra in linea:
                                resultados.append((file_path, num_linea, linea.strip()))
                except Exception as e:
                    print(f"No se pudo leer el archivo: {file_path}. Error: {e}")

    # Mostrar resultados
    if resultados:
        print(f"Se encontró la palabra '{palabra}' en los siguientes archivos:")
        for archivo, linea, contenido in resultados:
            print(f"Archivo: {archivo}, Línea: {linea}, Contenido: {contenido}")
    else:
        print(f"No se encontró la palabra '{palabra}' en ningún archivo.")

# Directorio y palabra a buscar
directorio = ""  # Cambia a tu directorio
palabra = "cosmosDBTrigger"  # Cambia a la palabra que quieres buscar

buscar_palabra_en_archivos(directorio, palabra)
