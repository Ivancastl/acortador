# Acortador de Enlaces con Dominio Personalizado

Este script te permite **acortar enlaces** utilizando la API de [encurtador.dev](https://www.encurtador.dev/) y combinar el enlace resultante con un dominio personalizado, útil por ejemplo para crear enlaces disfrazados o con propósito de redireccionamiento creativo.

Además, permite trabajar con múltiples enlaces almacenados en un archivo `.txt` o `.xlsx`.

## 🔧 Requisitos

- Tener **Python** instalado.
- Conexión a internet.
- Archivo `.txt` o `.xlsx` en la misma carpeta que el script si vas a procesar múltiples enlaces.

## 🧠 ¿Cómo funciona?

- Puedes elegir entre acortar un solo enlace o varios desde un archivo.
- Combina el dominio personalizado con la URL acortada usando el formato

## Instalación 

### **Paso 1:**
# Clona este repositorio 
```bash
git clone https://github.com/Ivancastl/acortador.git
```

### **Paso 2:**
# Accede al directorio del proyecto.
```bash
cd enlaces
```

### **Paso 3:**
# Instala las dependencias necesarias.
```bash
pip install -r requirements.txt
```

### **Paso 4:**
# Instala las dependencias necesarias.
```bash
python enlace.py
```

📌 Salida del script
El script imprimirá en consola todas las URLs generadas en el siguiente formato:
https://tudominio@url-acortada
