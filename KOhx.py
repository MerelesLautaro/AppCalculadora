from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton

class CalculadoraHexadecimal(App):
    def build(self):             
        self.ventana = BoxLayout(orientation='vertical')

        # Entrada para el primer número hexadecimal
        self.entry_num1 = TextInput(hint_text="Primer número hexadecimal", multiline=False)

        # Entrada para el segundo número hexadecimal
        self.entry_num2 = TextInput(hint_text="Segundo número hexadecimal", multiline=False)

        # Operación predeterminada
        self.operacion_var = '+'
        # Selección de operación
        self.operaciones = ['+', '-', 'x', '/']

        operacion_label = Label(text="Operación:")

        self.botones_operacion = []
        for operacion in self.operaciones:
            boton_operacion = ToggleButton(text=operacion, group='operaciones')
            boton_operacion.bind(on_release=self.actualizar_seleccion)
            self.botones_operacion.append(boton_operacion)

        # Botón para calcular
        calcular_button = Button(text="Calcular")
        calcular_button.bind(on_release=self.calcular)

        # Etiqueta para mostrar el resultado
        self.resultado_label = Label(text="Resultado:")

        # Agregar widgets al diseño
        self.ventana.add_widget(self.entry_num1)
        self.ventana.add_widget(self.entry_num2)
        self.ventana.add_widget(operacion_label)
        for boton in self.botones_operacion:
            self.ventana.add_widget(boton)
        self.ventana.add_widget(calcular_button)
        self.ventana.add_widget(self.resultado_label)

        return self.ventana

    def actualizar_seleccion(self, instance):
        self.operacion_var = instance.text

    def calcular(self, instance):
        try:
            num1 = int(self.entry_num1.text, 16)
            num2 = int(self.entry_num2.text, 16)

            if self.operacion_var == '+':
                resultado = num1 + num2
            elif self.operacion_var == '-':
                resultado = num1 - num2
            elif self.operacion_var == 'x':
                resultado = num1 * num2
            elif self.operacion_var == '/':
                resultado = num1 // num2
            else:
                resultado = "Operación no válida"

            resultado = hex(resultado)[2:].upper()
            self.resultado_label.text = f"Resultado: {resultado}"
        except ValueError:
            self.resultado_label.text = "Entrada no válida"

if __name__ == '__main__':
    CalculadoraHexadecimal().run()
