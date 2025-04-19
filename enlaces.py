import requests
import json
import pandas as pd
import os
import pyfiglet

<<<<<<< HEAD
# Arte ASCII
def mostrar_banner():
    banner = pyfiglet.figlet_format("URL MASKER")
    print(banner)
    print("Sígueme en Twitter: @ivancastl")
    print("Únete al grupo de Telegram: t.me/OSINTube")
    print("-" * 60)
=======
# 🎨 Mostrar banner ASCII
def mostrar_banner():
    banner = pyfiglet.figlet_format("FakeNlaces")
    print(banner)
    print("🔗 Herramienta para ofuscar/acortar enlaces ")
   
>>>>>>> 023f09a (actualizacion)

# Función para acortar una URL usando encurtador.dev
def acortar_url(url_original):
    url_acortador = "https://api.encurtador.dev/encurtamentos"
    payload = {"url": url_original}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url_acortador, data=json.dumps(payload), headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["urlEncurtada"]
    except requests.exceptions.RequestException as e:
        print(f"❌ Error al acortar la URL: {e}")
        return None

# Leer archivo de enlaces (Excel o TXT)
def obtener_enlaces_archivo(nombre_archivo):
    ruta_archivo = os.path.join(os.path.dirname(__file__), nombre_archivo)

    if not os.path.exists(ruta_archivo):
        print("❌ El archivo no existe en la misma carpeta.")
        return None

    try:
        if nombre_archivo.endswith(".txt"):
            with open(ruta_archivo, "r", encoding="utf-8") as f:
                enlaces = [line.strip().replace("https://", "") for line in f if line.strip()]
        elif nombre_archivo.endswith(".xlsx"):
            df = pd.read_excel(ruta_archivo)
            enlaces = [link.replace("https://", "") for link in df["Links"]]
        else:
            print("❌ El archivo debe ser .txt o .xlsx con una columna 'Links'.")
            return None
        return enlaces
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        return None

# Programa principal
def main():
    mostrar_banner()

    print("¿Qué deseas hacer?")
    print("1️⃣ Acortar un solo enlace manualmente")
    print("2️⃣ Acortar varios enlaces desde un archivo (txt o xlsx)")
    opcion = input("Selecciona 1 o 2: ").strip()

    if opcion == "1":
        dominio_original = input("🌍 Ingresa el dominio que deseas mantener (ej: misitio.com): ").strip()
        enlace_usuario = input("🌐 Ingresa el enlace que deseas acortar (ej: https://google.com): ").strip()

        enlace_limpio = enlace_usuario.replace("https://", "")
        url_acortada = acortar_url(enlace_limpio)

        if url_acortada:
            nueva_url = f"https://{dominio_original}@{url_acortada}"
            print(f"✅ URL final: {nueva_url}")
        else:
            print("❌ No se pudo acortar la URL.")

    elif opcion == "2":
        nombre_archivo = input("📄 Ingresa el nombre del archivo con enlaces (ej: enlaces.txt o enlaces.xlsx): ").strip()
        dominio_original = input("🌍 Ingresa el dominio que deseas mantener (ej: misitio.com): ").strip()

        enlaces = obtener_enlaces_archivo(nombre_archivo)

        if enlaces:
            for enlace in enlaces:
                url_acortada = acortar_url(enlace)
                if url_acortada:
                    nueva_url = f"https://{dominio_original}@{url_acortada}"
                    print(f"✅ URL final: {nueva_url}")
                else:
                    print(f"❌ No se pudo acortar: {enlace}")
                print("─" * 40)
        else:
            print("❌ No se pudieron procesar los enlaces.")

    else:
        print("❌ Opción no válida. Intenta con 1 o 2.")

if __name__ == "__main__":
    main()
