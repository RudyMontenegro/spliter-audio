# Spliter Audio

Herramienta para dividir archivos de audio MP3 en fragmentos de 5 segundos.

## Descripción

Este proyecto permite dividir archivos MP3 en fragmentos más pequeños de manera rápida y eficiente. El programa busca automáticamente el primer archivo `.mp3` en la carpeta donde se ejecuta y lo divide en fragmentos de 5 segundos cada uno.

## Características

- ✅ División automática de archivos MP3
- ✅ Fragmentos de 5 segundos
- ✅ Sin recodificación (copia directa para máxima velocidad)
- ✅ Organización automática en carpetas
- ✅ Interfaz de línea de comandos simple

## Requisitos

- Python 3.x
- FFmpeg (incluido como `ffmpeg.exe`)

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/RudyMontenegro/spliter-audio.git
cd spliter-audio
```

2. Asegúrate de tener FFmpeg disponible:
   - El proyecto incluye `ffmpeg.exe` en el repositorio
   - O instala FFmpeg desde [ffmpeg.org](https://ffmpeg.org/download.html)

## Uso

### Como script de Python

1. Coloca tu archivo `.mp3` en la misma carpeta que `splitter.py`
2. Ejecuta:
```bash
python splitter.py
```

3. El programa:
   - Buscará automáticamente el primer archivo `.mp3`
   - Creará una carpeta con el nombre del archivo
   - Generará fragmentos numerados: `fragment_001.mp3`, `fragment_002.mp3`, etc.

### Como ejecutable

1. Descarga `CortadorAudio.exe` desde la sección de releases
2. Coloca tu archivo `.mp3` en la misma carpeta que el ejecutable
3. Ejecuta `CortadorAudio.exe`
4. Los fragmentos se crearán automáticamente

## Estructura del Proyecto

```
spliter-audio/
├── splitter.py          # Script principal
├── CortadorAudio.spec   # Configuración de PyInstaller
├── README.md            # Este archivo
└── ffmpeg.exe           # Binario de FFmpeg (opcional)
```

## Configuración

Puedes modificar la duración de los fragmentos editando la línea 45 en `splitter.py`:

```python
"-segment_time", "5",  # Cambia "5" por el número de segundos deseado
```

## Construcción del Ejecutable

Para crear el ejecutable usando PyInstaller:

```bash
pyinstaller CortadorAudio.spec
```

El ejecutable se generará en la carpeta `dist/`.

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## Autor

Rudy Montenegro

