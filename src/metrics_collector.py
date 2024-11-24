import pandas as pd
import matplotlib.pyplot as plt
import os
import time

class MetricsCollector:
    def __init__(self, output_csv="../metrics/metrics.csv"):
        """
        Inicializa el recolector de métricas.
        """
        self.metrics = []
        self.output_csv = output_csv

    def add_metric(self, image_path, recognition_time, words_recognized, total_confidence):
        """
        Agrega una métrica al dataset.
        """
        metric = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "image_path": image_path,
            "recognition_time": recognition_time,
            "words_recognized": words_recognized,
            "total_confidence": total_confidence,
        }
        self.metrics.append(metric)

    def save_metrics_to_csv(self):
        """
        Guarda las métricas recopiladas en un archivo CSV.
        """
        df = pd.DataFrame(self.metrics)
        df.to_csv(self.output_csv, index=False)
        print(f"Métricas guardadas en: {self.output_csv}")

    def plot_metrics(self):
        """
        Genera gráficos a partir de las métricas recopiladas.
        """
        df = pd.DataFrame(self.metrics)

        if df.empty:
            print("No hay métricas para graficar.")
            return

        # Gráfico 1: Tiempo de reconocimiento por imagen
        plt.figure()
        df.plot(x="timestamp", y="recognition_time", kind="line", title="Tiempo de Reconocimiento")
        plt.xlabel("Timestamp")
        plt.ylabel("Tiempo (s)")
        plt.savefig("recognition_time.png")
        plt.show()

        # Gráfico 2: Palabras reconocidas por imagen
        plt.figure()
        df.plot(x="timestamp", y="words_recognized", kind="bar", title="Palabras Reconocidas")
        plt.xlabel("Timestamp")
        plt.ylabel("Palabras reconocidas")
        plt.savefig("words_recognized.png")
        plt.show()

        # Gráfico 3: Confianza promedio por imagen
        plt.figure()
        df.plot(x="timestamp", y="total_confidence", kind="line", title="Confianza Total")
        plt.xlabel("Timestamp")
        plt.ylabel("Confianza Total")
        plt.savefig("confidence_total.png")
        plt.show()
