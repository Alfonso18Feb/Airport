import random
from datetime import datetime, timedelta
import threading

class Vuelo:
    def __init__(self, numero, destino, hora_salida):
        self.numero = numero
        self.destino = destino
        self.hora_salida = hora_salida
        self.retraso = timedelta(hours=random.randint(0, 4))
        self.hora_embarque = self.hora_salida + self.retraso

    def __str__(self):
        return (f"Vuelo {self.numero} a {self.destino}:\n"
                f"Hora de salida: {self.hora_salida}\n"
                f"Retraso: {self.retraso}\n"
                f"Hora de embarque: {self.hora_embarque}\n")

class GestionVuelos:
    def __init__(self):
        self.vuelos = []
        self.lock = threading.Lock()

    def agregar_vuelo(self, numero, destino, hora_salida):
        with self.lock:
            vuelo = Vuelo(numero, destino, hora_salida)
            self.vuelos.append(vuelo)

    def mostrar_vuelos(self):
        for vuelo in self.vuelos:
            print(vuelo)

def agregar_vuelos_concurrentemente(gestion_vuelos, vuelos):
    threads = []
    for vuelo in vuelos:
        t = threading.Thread(target=gestion_vuelos.agregar_vuelo, args=vuelo)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

# Ejemplo de uso
if __name__ == "__main__":
    gestion_vuelos = GestionVuelos()
    vuelos = [
        ("IB1234", "Madrid", datetime(2023, 10, 25, 14, 30)),
        ("IB5678", "Barcelona", datetime(2023, 10, 25, 16, 45)),
        ("IB9101", "Valencia", datetime(2023, 10, 25, 18, 0)),
        ("IB1121", "Sevilla", datetime(2023, 10, 25, 19, 15)),
        ("IB3141", "Bilbao", datetime(2023, 10, 25, 20, 30)),
        ("IB5161", "Malaga", datetime(2023, 10, 25, 21, 45)),
        ("IB7181", "Granada", datetime(2023, 10, 25, 22, 0)),
        ("IB9201", "Alicante", datetime(2023, 10, 25, 23, 15)),
        ("IB1222", "Zaragoza", datetime(2023, 10, 26, 0, 30)),
        ("IB3242", "Santander", datetime(2023, 10, 26, 1, 45)),
        ("IB5262", "Vigo", datetime(2023, 10, 26, 3, 0))
    ]
    agregar_vuelos_concurrentemente(gestion_vuelos, vuelos)
    gestion_vuelos.mostrar_vuelos()