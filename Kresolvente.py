from sympy import symbols, Eq, solve
import matplotlib.pyplot as plt
import numpy as np
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class CalculadoraPolinomios(App):
    def build(self):
        self.ventana = BoxLayout(orientation='vertical', padding=10, spacing=15)
        self.soluciones = []
        
        # Etiquetas y entradas para los coeficientes a, b y c
        self.a_label = Label(text="Coeficiente a:")
        self.a_entry = TextInput(size_hint=(None, None), size=(300, 50), padding=(10, 5))
        
        self.b_label = Label(text="Coeficiente b:")
        self.b_entry = TextInput(size_hint=(None, None), size=(300, 50), padding=(10, 5))
        
        self.c_label = Label(text="Coeficiente c:")
        self.c_entry = TextInput(size_hint=(None, None), size=(300, 50), padding=(10, 5))
             
        # Botón para calcular y mostrar las soluciones
        calcular_button = Button(text="Calcular Soluciones", background_color=(0, 0.7, 0.2, 1), size_hint=(None, None), size=(300, 50), padding=(10, 5))  # Estilo del botón
        calcular_button.bind(on_release=self.resolver_polinomio)
            
        # Botón para graficar polinomio
        graficar_button = Button(text="Graficar", background_color=(0, 0.2, 0.7, 1), size_hint=(None, None), size=(300, 50), padding=(10, 5))  # Estilo del botón
        graficar_button.bind(on_release=self.graficar_polinomio)
        
        # Etiqueta para mostrar las soluciones
        self.resultado_label = Label(text="")
        
        # Etiqueta para mostrar error de graficar.
        self.graficar_label = Label(text="")
        
        # Agregar widgets a la ventana principal
        self.ventana.add_widget(self.a_label)
        self.ventana.add_widget(self.a_entry)
        self.ventana.add_widget(self.b_label)
        self.ventana.add_widget(self.b_entry)
        self.ventana.add_widget(self.c_label)
        self.ventana.add_widget(self.c_entry)
        self.ventana.add_widget(calcular_button)
        self.ventana.add_widget(graficar_button)
        self.ventana.add_widget(self.resultado_label)
        self.ventana.add_widget(self.graficar_label)
        
        return self.ventana

    def resolver_polinomio(self, instance):
        try:
            # Obtener los coeficientes a, b y c desde las entradas del usuario
            a = float(self.a_entry.text) if self.a_entry.text else 0.0
            b = float(self.b_entry.text) if self.b_entry.text else 0.0
            c = float(self.c_entry.text) if self.c_entry.text else 0.0

            # Crear el símbolo 'x'
            x = symbols('x')

            # Crear la ecuación a resolver
            ecuacion = Eq(a*x**2 + b*x + c, 0)

            # Resolver la ecuación
            self.soluciones = solve(ecuacion, x)

            # Mostrar las soluciones en la etiqueta de resultados
            self.resultado_label.text = f"Soluciones: {self.soluciones}"
            self.graficar_label.text = f""
        except ValueError:
            self.resultado_label.text = f"Soluciones: Entrada no válida"
            return
    
    def graficar_polinomio(self,instance):
        if not self.soluciones:
            self.graficar_label.text = "Graficar: Primero calcula las soluciones"
            return
        
        a = float(self.a_entry.text) if self.a_entry.text else 0.0
        b = float(self.b_entry.text) if self.b_entry.text else 0.0
        c = float(self.c_entry.text) if self.c_entry.text else 0.0
        
        try:
            # Dibujar la gráfica del polinomio
            x_vals = np.linspace(-10, 10, 400)
            plt.xticks(np.arange(-10, 11, 1))
            y_vals = a * x_vals**2 + b * x_vals + c
            plt.plot(x_vals, y_vals, label='Polinomio')

            # Mostrar las soluciones en el gráfico
            for solucion in self.soluciones:
                if solucion.is_real:
                    plt.axvline(x=solucion, color='red', linestyle='--', label=f'Solución: {solucion:.2f}')
                    plt.axhline(y=a * solucion**2 + b * solucion + c, color='green', linestyle='-')
                    plt.axvline(x=a * solucion**2 + b * solucion + c, color='green', linestyle='-')
        except ValueError:
            self.graficar_label.text = "Primero calcula las soluciones"
        
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Gráfica del Polinomio')
        plt.grid(True)
        plt.legend()
        plt.show()

if __name__ == '__main__':
    CalculadoraPolinomios().run()
