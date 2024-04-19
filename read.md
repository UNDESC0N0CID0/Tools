# Scripts de PowerShell y Python

Este repositorio contiene scripts de PowerShell y Python para obtener la duración de los videos y ejecutar todos los scripts de Python en el directorio actual, respectivamente.

## Uso

### Script de PowerShell para obtener la duración de los videos

1. Abre PowerShell.
2. Navega al directorio donde guardaste el archivo `.ps1` utilizando el comando `cd`. Por ejemplo, si guardaste el archivo en el directorio `C:\Scripts`, escribirías `cd C:\Scripts`.
3. Ejecuta el script escribiendo `.\GetVideoDuration.ps1 -Directory "Ruta del directorio"` y presionando Enter. Reemplaza `"Ruta del directorio"` con la ruta del directorio que contiene tus videos. Si no proporcionas un valor para `-Directory`, el script se ejecutará en la ruta actual del archivo.

### Script de Python para ejecutar todos los scripts de Python en el directorio actual

1. Abre la terminal.
2. Navega al directorio donde guardaste el archivo `execute.py` utilizando el comando `cd`. Por ejemplo, si guardaste el archivo en el directorio `C:\Scripts`, escribirías `cd C:\Scripts`.
3. Ejecuta el script escribiendo `python execute.py` y presionando Enter.

## Parámetros

### Script de PowerShell

- `-Directory`: La ruta del directorio que contiene los videos. Si no se proporciona, se usará la ruta actual del archivo.

## Salida

### Script de PowerShell

El script genera una lista de todos los videos en el directorio especificado, junto con su duración.

### Script de Python

El script ejecuta todos los scripts de Python en el directorio actual.

## Notas

### Script de PowerShell

Este script solo funcionará para archivos de video que Windows pueda leer la duración. Si tienes videos en un formato no estándar, es posible que necesites una herramienta adicional para leer la duración.

### Script de Python

Este script solo ejecutará los scripts de Python en el directorio actual. Asegúrate de que todos los scripts de Python en el directorio sean seguros para ejecutar.
