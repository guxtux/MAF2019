#!/bin/bash

# Verifica que se haya proporcionado al menos un archivo
if [ "$#" -eq 0 ]; then
    echo "Uso: $0 archivo1.tex archivo2.tex ..."
    exit 1
fi

# Itera sobre todos los argumentos (archivos .tex)
for file in "$@"; do
    if [ -f "$file" ]; then
        (
            echo "Compilando $file..."
            pdflatex -interaction=nonstopmode "$file" > /dev/null 2>&1
            echo "Terminado: $file"
        ) &
    else
        echo "Archivo no encontrado: $file"
    fi
done

# Espera a que todos los procesos terminen
wait

echo "Compilación finalizada para todos los archivos proporcionados."
