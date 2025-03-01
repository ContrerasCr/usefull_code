from openai import OpenAI
import os
from pathlib import Path
import json
from pydub import AudioSegment


def transcribe_audio(file_path, output_path):

    client = OpenAI()
    print(f"Transcribing {file_path}")
    audio_file = open(file_path, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        language="es",
        file=audio_file,
        response_format="text"
    )
    datos = {
        "texto": transcription
    }
    
    with open(output_path, 'w', encoding='utf-8') as archivo_json:
        json.dump(datos, archivo_json, ensure_ascii=False, indent=4)
    
    
    return output_path

def convertir_audio_a_mp3(ruta_archivo, ruta_salida):
    # Detecta el formato del archivo original
    extension = os.path.splitext(ruta_archivo)[-1].lower()

    # Cargar el archivo de audio
    audio = AudioSegment.from_file(ruta_archivo, format=extension[1:])

    # Exportar el archivo como MP3
    audio.export(ruta_salida, format="mp3")
    return ruta_salida

def split_audio(file_path, output_dir):
    
    audio_dir = []
    
    # Cargar el archivo de audio
    audio = AudioSegment.from_file(file_path)
    
    # Definir la duración de cada parte (en milisegundos)
    part_duration = 20 * 60 * 1000  # 20 minutos
    
    # Dividir el archivo de audio en partes
    for i, part in enumerate(range(0, len(audio), part_duration)):
        audio_path = f"{output_dir}\part_{i + 1}.mp3"
        part_audio = audio[part:part + part_duration]
        part_audio.export(f"{output_dir}\part_{i + 1}.mp3", format="mp3")
        audio_dir.append(audio_path)
    
    return audio_dir
# Configure api_key

api_key = ''
os.environ["OPENAI_API_KEY"] = api_key

# Ruta al archivo de audio
location = r""
output_path = r""

tamano_archivo = os.path.getsize(location)
tamano_archivo_mb = tamano_archivo / (1024 * 1024)

formato = location.split(".")[-1]

if formato != "mp3":
    salida = location.split(".")[0]
    salida = f"{salida}.mp3"
    location = convertir_audio_a_mp3(location, salida)

if tamano_archivo_mb > 25:
    location = split_audio(location, output_path)
else:
    location = [location]

for audio in location:
    output_file = audio.split("\\")[-1].split(".")[0]
    output_path_i = fr"{output_path}\{output_file}.json"
    au_dir = transcribe_audio(audio, output_path_i)
    print(au_dir)







