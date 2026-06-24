import os
import time
from datetime import datetime


def parse_hora(hora_str):
    try:
        return datetime.strptime(hora_str, "%H:%M").time()
    except ValueError:
        raise ValueError("Formato inválido. Use HH:MM")


def esperar_hasta(hora_objetivo):
    while True:
        ahora = datetime.now().time()
        if ahora >= hora_objetivo:
            return
        segundos = (datetime.combine(datetime.today(), hora_objetivo) - datetime.combine(datetime.today(), ahora)).total_seconds()
        time.sleep(max(1, min(segundos, 60)))


def main():
    hora = input("Ingrese la hora para iniciar la aplicación (HH:MM): ")
    ruta_app = input("Ingrese la ruta completa de la aplicación a iniciar: ")
    hora_objetivo = parse_hora(hora)
    print(f"Esperando hasta las {hora_objetivo.strftime('%H:%M')}...")
    esperar_hasta(hora_objetivo)
    print("Hora alcanzada. Iniciando aplicación...")
    os.startfile(ruta_app)


if __name__ == "__main__":
    main()

