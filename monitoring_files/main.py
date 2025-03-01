import os
from datetime import datetime

def get_files_sorted_by_modification_and_size(directory):
    # Lista para almacenar los archivos encontrados
    files = []

    # Recorrer el directorio y las subcarpetas
    for root, _, filenames in os.walk(directory):
        for file in filenames:
            # Obtener la ruta completa del archivo
            filepath = os.path.join(root, file)
            # Obtener la fecha de modificación y tamaño
            mod_time = os.path.getmtime(filepath)
            size = os.path.getsize(filepath) / (1024 * 1024)  # Convertir el tamaño a MB
            # Añadir solo si el tamaño es mayor a 1 MB
            if size > 1:
                files.append((filepath, mod_time, size))

    # Ordenar por fecha de modificación y luego por tamaño
    files_sorted = sorted(files, key=lambda x: (datetime.fromtimestamp(x[1]), x[2]), reverse=True)

    # Imprimir los archivos ordenados
    for file, mod_time, size in files_sorted:
        print(f"Archivo: {file} | Fecha de Modificación: {datetime.fromtimestamp(mod_time)} | Tamaño: {size:.2f} MB")


# Uso del script
directorio = r''  # Cambia esto por el directorio que deseas analizar
get_files_sorted_by_modification_and_size(directorio)
