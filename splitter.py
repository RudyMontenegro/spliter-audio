import os
import sys
import glob
import subprocess

def main():
    # Determinar la ruta base (compatible con script .py y ejecutable .exe)
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    # Cambiar el directorio de trabajo a donde está el archivo
    os.chdir(base_path)

    # Buscar el primer archivo .mp3
    mp3_files = glob.glob("*.mp3")

    if not mp3_files:
        print("ERROR: No se encontró ningún archivo .mp3 en esta carpeta.")
        input("\nPresiona ENTER para salir...")
        return

    input_file = mp3_files[0]
    folder_name = os.path.splitext(input_file)[0]

    print(f"Archivo detectado: {input_file}")
    print(f"Creando carpeta: {folder_name}")

    # Crear carpeta (si existe no da error)
    os.makedirs(folder_name, exist_ok=True)

    # Patrón de salida: carpeta/fragment_001.mp3
    output_pattern = os.path.join(folder_name, "fragment_%03d.mp3")

    # Comando FFmpeg para dividir sin recodificar (-c copy)
    # -segment_time 60: duración de 60 segundos
    # -f segment: formato de segmentación
    # -reset_timestamps 1: reiniciar el reloj en cada corte
    # -segment_start_number 1: empezar en 001 en vez de 000
    cmd = [
        "ffmpeg",
        "-i", input_file,
        "-f", "segment",
        "-segment_time", "5",
        "-c", "copy",
        "-reset_timestamps", "1",
        "-segment_start_number", "1", 
        "-map", "0",
        output_pattern
    ]

    try:
        print("Procesando audio... Por favor espera.")
        # stdout y stderr a DEVNULL oculta el log técnico de ffmpeg, quítalo si quieres ver detalles
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"\n¡Éxito! Los fragmentos están en la carpeta: {folder_name}")
    except FileNotFoundError:
        print("\nERROR CRÍTICO: No se encontró 'ffmpeg'.")
        print("Asegúrate de que ffmpeg.exe esté en la misma carpeta que este programa.")
    except subprocess.CalledProcessError:
        print("\nERROR: Ocurrió un problema al procesar el audio.")
    except Exception as e:
        print(f"\nERROR inesperado: {e}")

    input("\nPresiona ENTER para cerrar...")

if __name__ == "__main__":
    main()