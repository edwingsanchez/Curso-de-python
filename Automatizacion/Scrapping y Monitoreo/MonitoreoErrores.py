import requests
import time
import logging
from datetime import datetime

# ---------------- CONFIGURACIÓN ----------------
URLS = [
    "https://Gmail.com",
    "https://sovm-frontend.vercel.app/"
]

CHECK_INTERVAL = 60  # segundos entre chequeos
TIMEOUT = 5          # segundos de espera por request

# ---------------- LOGGING ----------------
logging.basicConfig(
    filename="monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------- FUNCIONES ----------------
def check_url(url):
    try:
        response = requests.get(url, timeout=TIMEOUT)

        if response.status_code == 200:
            logging.info(f"OK: {url}")
            return True
        else:
            logging.warning(f"ERROR HTTP {response.status_code}: {url}")
            return False

    except requests.exceptions.Timeout:
        logging.error(f"TIMEOUT: {url}")
        return False

    except requests.exceptions.ConnectionError:
        logging.error(f"CONEXIÓN FALLIDA: {url}")
        return False

    except Exception as e:
        logging.error(f"ERROR DESCONOCIDO en {url}: {str(e)}")
        return False


def monitor():
    while True:
        print(f"\nChequeo: {datetime.now()}")

        for url in URLS:
            status = check_url(url)

            if not status:
                print(f"⚠️ Problema detectado en {url}")
            else:
                print(f"✅ {url} funcionando correctamente")

        time.sleep(CHECK_INTERVAL)


# ---------------- EJECUCIÓN ----------------
if __name__ == "__main__":
    monitor()