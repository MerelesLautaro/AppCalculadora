from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton

class CalculadoraBinaria(App):
    def build(self):
        self.ventana = BoxLayout(orientation='vertical')
        
        # Entrada para el primer valor binario
        self.etiqueta_binario1 = Label(text="Primer Valor Binario:")
        self.entrada_binario1 = TextInput()
        
        # Entrada para el segundo valor binario
        self.etiqueta_binario2 = Label(text="Segundo Valor Binario:")
        self.entrada_binario2 = TextInput()
        
        # Selector de operación
        self.operaciones = ['+', '-', 'x', '/']
        self.botones_operacion = []
        self.seleccion_operacion = '+'

        for operacion in self.operaciones:
            boton_operacion = ToggleButton(text=operacion, group='operaciones')
            boton_operacion.bind(on_press=self.actualizar_seleccion)
            self.botones_operacion.append(boton_operacion)

        # Botón para realizar la operación
        self.boton_calcular = Button(text="Calcular")
        self.boton_calcular.bind(on_press=self.realizar_operacion)
        
        # Etiqueta para mostrar el resultado
        self.etiqueta_resultado = Label(text="")
        
        # Agregar widgets a la ventana principal
        self.ventana.add_widget(self.etiqueta_binario1)
        self.ventana.add_widget(self.entrada_binario1)
        self.ventana.add_widget(self.etiqueta_binario2)
        self.ventana.add_widget(self.entrada_binario2)
        for boton in self.botones_operacion:
            self.ventana.add_widget(boton)
        self.ventana.add_widget(self.boton_calcular)
        self.ventana.add_widget(self.etiqueta_resultado)
        
        return self.ventana

    def actualizar_seleccion(self, instance):
        self.seleccion_operacion = instance.text

    def binario_sin_prefijo(self, numero):
        if numero.startswith('-'):
            return '-' + numero[3:]
        else:
            return numero[2:]

    def realizar_operacion(self, instance):
        valor_binario_1 = self.entrada_binario1.text
        valor_binario_2 = self.entrada_binario2.text

        if self.seleccion_operacion == '+':
            resultado = self.binario_sin_prefijo(bin(int(valor_binario_1, 2) + int(valor_binario_2, 2)))
        elif self.seleccion_operacion == '-':
            resultado = self.binario_sin_prefijo(bin(int(valor_binario_1, 2) - int(valor_binario_2, 2)))
        elif self.seleccion_operacion == 'x':
            resultado = self.binario_sin_prefijo(bin(int(valor_binario_1, 2) * int(valor_binario_2, 2)))
        elif self.seleccion_operacion == '/':
            resultado = self.binario_sin_prefijo(bin(int(valor_binario_1, 2) // int(valor_binario_2, 2)))

        self.etiqueta_resultado.text = f"Resultado: {resultado}"

if __name__ == '__main__':
    CalculadoraBinaria().run()
