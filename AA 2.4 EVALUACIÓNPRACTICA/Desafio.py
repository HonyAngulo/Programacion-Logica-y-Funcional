import tkinter as tk  # Módulo para crear interfaces gráficas
from tkinter import ttk, messagebox  # Widgets estilizados y ventanas de mensajes
from functools import reduce  # Función de orden superior para acumulaciones
from typing import List, Dict  # Tipado para mejorar claridad

# Tipos personalizados para organizar los datos
Valoraciones = Dict[str, List[int]]
Materias = Dict[str, Valoraciones]

class EncuestaApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Encuesta de Evaluación de Asignaturas")  # Título de la ventana

        # Estructura de datos para guardar todas las materias y valoraciones
        self.materias: Materias = {}

        # Lista de aspectos a evaluar
        self.aspectos = ["Contenido", "Actividades", "Herramientas", "Docente", "Dificultad"]

        # Configura la interfaz de usuario
        self.setup_ui()

    def setup_ui(self):
        # Crea el contenedor principal con padding
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Campo para escribir el nombre de la materia
        ttk.Label(self.main_frame, text="Materia:", font=('Segoe UI', 10, 'bold')).grid(row=0, column=0, sticky=tk.W)
        self.materia_entry = ttk.Entry(self.main_frame, width=30)
        self.materia_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

        # Crear spinboxes para cada aspecto usando map y zip (sin bucles)
        self.valoraciones_entries = dict(
            zip(
                self.aspectos,
                list(map(
                    lambda idx: self._crear_spinbox(idx + 1),
                    range(len(self.aspectos))
                ))
            )
        )

        # Botón para guardar los datos ingresados
        ttk.Button(self.main_frame, text="Guardar Valoración", command=self.guardar_valoracion)\
            .grid(row=6, column=0, columnspan=2, pady=10)

        # Botón para mostrar resultados procesados
        ttk.Button(self.main_frame, text="Ver Resultados", command=self.mostrar_resultados)\
            .grid(row=7, column=0, columnspan=2, pady=5)

        # Botón para limpiar el área de resultados
        ttk.Button(self.main_frame, text="Limpiar Resultados", command=self.limpiar_resultados)\
            .grid(row=8, column=0, columnspan=2, pady=5)

        # Área de texto donde se muestran los resultados
        self.resultados_text = tk.Text(self.main_frame, height=15, width=60, state=tk.DISABLED)
        self.resultados_text.grid(row=9, column=0, columnspan=2, pady=10)

    def _crear_spinbox(self, row):
        # Crea un Spinbox para un aspecto específico en una fila dada
        ttk.Label(self.main_frame, text=f"{self.aspectos[row-1]} (1-5):").grid(row=row, column=0, sticky=tk.W)
        spin = ttk.Spinbox(self.main_frame, from_=1, to=5, width=5)
        spin.set(" ")  # Valor por defecto
        spin.grid(row=row, column=1, sticky=tk.W)
        return spin

    def guardar_valoracion(self):
        # Obtiene la materia y guarda sus valoraciones si son válidas
        materia = self.materia_entry.get().strip()
        if not materia:
            messagebox.showerror("Error", "Debe ingresar el nombre de la materia")
            return

        try:
            # Obtiene los valores ingresados desde los spinboxes
            valoraciones = dict(
                map(lambda item: (item[0], int(item[1].get())), self.valoraciones_entries.items())
            )

            # Verifica que todos los valores estén entre 1 y 5
            if any(not (1 <= v <= 5) for v in valoraciones.values()):
                raise ValueError("Las valoraciones deben estar entre 1 y 5")

            # Inicializa la materia si no existe
            if materia not in self.materias:
                self.materias[materia] = dict(
                    map(lambda aspecto: (aspecto, []), self.aspectos)
                )

            # Agrega las valoraciones al diccionario
            _ = list(map(lambda item: self.materias[materia][item[0]].append(item[1]), valoraciones.items()))

            messagebox.showinfo("Éxito", "Valoración guardada correctamente")
            self.limpiar_formulario()

        except ValueError as e:
            messagebox.showerror("Error", f"Valor inválido: {e}")

    def limpiar_formulario(self):
        # Limpia el formulario de entrada para otra valoración
        self.materia_entry.delete(0, tk.END)
        _ = list(map(lambda e: (e.delete(0, tk.END), e.insert(0, " ")), self.valoraciones_entries.values()))

    def limpiar_resultados(self):
        # Limpia el área de resultados en pantalla
        self.resultados_text.config(state=tk.NORMAL)
        self.resultados_text.delete(1.0, tk.END)
        self.resultados_text.config(state=tk.DISABLED)

    def mostrar_resultados(self):
        # Muestra los resultados procesados en la interfaz
        if not self.materias:
            messagebox.showinfo("Información", "No hay datos para mostrar")
            return

        resultados = self.procesar_resultados()
        self.resultados_text.config(state=tk.NORMAL)
        self.resultados_text.delete(1.0, tk.END)

        # Muestra cada materia y sus métricas
        def mostrar_materia(materia_resultado):
            materia, datos = materia_resultado
            self.resultados_text.insert(tk.END, f"\n📚 Materia: {materia}\n")
            suma_total = 0
            total_items = 0

            # Muestra cada aspecto con su promedio y estadísticas
            def mostrar_aspecto(aspecto_datos):
                nonlocal suma_total, total_items
                aspecto, valores = aspecto_datos
                if isinstance(valores, dict):
                    self.resultados_text.insert(
                        tk.END,
                        f"  • {aspecto}: Promedio={valores['promedio']:.2f}, "
                        f"Mín={valores['min']}, Máx={valores['max']}, "
                        f"Total={valores['total']}, Altas={valores['altas']}\n"
                    )
                    suma_total += valores['promedio']
                    total_items += 1

            list(map(mostrar_aspecto, datos.items()))

            if total_items > 0:
                promedio_general = suma_total / total_items
                self.resultados_text.insert(tk.END, f"  😉 Promedio general: {promedio_general:.2f}\n")

        list(map(mostrar_materia, resultados.items()))
        self.resultados_text.config(state=tk.DISABLED)

    def procesar_resultados(self) -> Dict[str, Dict[str, Dict[str, float]]]:
        # Procesa los resultados de todas las materias usando map y funciones
        return dict(
            map(
                lambda item: (
                    item[0],
                    dict(map(lambda aspecto: (aspecto[0], self.calcular_metricas(aspecto[1])), item[1].items()))
                ),
                self.materias.items()
            )
        )

    def calcular_metricas(self, valores: List[int]) -> Dict[str, float]:
        # Calcula promedio, mínimo, máximo y total de una lista de valores
        if not valores:
            return {"promedio": 0, "min": 0, "max": 0, "total": 0, "altas": 0}

        suma = reduce(lambda x, y: x + y, valores)
        total = len(valores)
        promedio = suma / total
        min_val = reduce(lambda x, y: x if x < y else y, valores)
        max_val = reduce(lambda x, y: x if x > y else y, valores)
        altas = self.contar_valoraciones_altas(valores)

        return {
            "promedio": promedio,
            "min": min_val,
            "max": max_val,
            "total": total,
            "altas": altas
        }

    def contar_valoraciones_altas(self, valores: List[int], umbral: int = 4) -> int:
        # Cuenta cuántas valoraciones están por encima de cierto umbral
        return len(list(filter(lambda x: x >= umbral, valores)))

# Punto de entrada del programa
def main():
    root = tk.Tk()  # Crea la ventana principal
    app = EncuestaApp(root)  # Crea la app
    root.mainloop()  # Inicia el bucle de eventos

# Llama a main si este archivo se ejecuta directamente
if __name__ == "__main__":
    main()
