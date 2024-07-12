import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
class CalculatorApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        self.window = BoxLayout(orientation='vertical', padding=10, spacing=10)
        input_layout = GridLayout(cols=2, size_hint=(1, 0.3))
        input_layout.add_widget(Label(text="Number 1:", color=(0, 0, 0, 1), font_size=32))
        self.num1 = TextInput(multiline=False, halign="right", font_size=32)
        input_layout.add_widget(self.num1)
        input_layout.add_widget(Label(text="Number 2:", color=(0, 0, 0, 1), font_size=32))
        self.num2 = TextInput(multiline=False, halign="right", font_size=32)
        input_layout.add_widget(self.num2)
        self.window.add_widget(input_layout)
        self.operations = GridLayout(cols=4, size_hint=(1, 0.3), spacing=10)
        self.add_button = Button(text="+", background_color=(0.6, 0.7, 0.8, 1), font_size=48)
        self.add_button.bind(on_press=self.calculate)
        self.operations.add_widget(self.add_button)
        self.subtract_button = Button(text="-", background_color=(0.6, 0.7, 0.8, 1), font_size=48)
        self.subtract_button.bind(on_press=self.calculate)
        self.operations.add_widget(self.subtract_button)
        self.multiply_button = Button(text="*", background_color=(0.6, 0.7, 0.8, 1), font_size=48)
        self.multiply_button.bind(on_press=self.calculate)
        self.operations.add_widget(self.multiply_button)
        self.divide_button = Button(text="/", background_color=(0.6, 0.7, 0.8, 1), font_size=48)
        self.divide_button.bind(on_press=self.calculate)
        self.operations.add_widget(self.divide_button)
        self.window.add_widget(self.operations)
        result_layout = GridLayout(cols=2, size_hint=(1, 0.3))
        result_layout.add_widget(Label(text="Result:", color=(0, 0, 0, 1), font_size=32))
        self.result = Label(text="", font_size=32, halign="center", color=(0, 0, 0, 1))
        result_layout.add_widget(self.result)
        self.window.add_widget(result_layout)
        return self.window
    def calculate(self, instance):
        num1 = float(self.num1.text)
        num2 = float(self.num2.text)
        operation = instance.text
        if operation == "+":
            res = num1 + num2
        elif operation == "-":
            res = num1 - num2
        elif operation == "*":
            res = num1 * num2
        elif operation == "/":
            if num2 != 0:
                res = num1 / num2
            else:
                res = "Error (Div by 0)"
        else:
            res = "Unknown operation"
        self.result.text = str(res)
if __name__ == "__main__":
    CalculatorApp().run()
