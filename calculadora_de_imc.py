import tkinter as tk


class BMICalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora de IMC")

        self.label_height = tk.Label(self.root, text="Altura (m):")
        self.label_height.pack()

        self.entry_height = tk.Entry(self.root)
        self.entry_height.pack()

        self.label_weight = tk.Label(self.root, text="Peso (kg):")
        self.label_weight.pack()

        self.entry_weight = tk.Entry(self.root)
        self.entry_weight.pack()

        self.button_calculate = tk.Button(
            self.root, text="Calcular IMC", command=self.calculate_bmi)
        self.button_calculate.pack()

        self.label_result = tk.Label(self.root, text="")
        self.label_result.pack()

    def calculate_bmi(self):
        try:
            height = float(self.entry_height.get())
            weight = float(self.entry_weight.get())

            bmi = weight / (height ** 2)

            self.label_result.config(text=f"Seu IMC é: {bmi:.2f}")

            self.show_bmi_category(bmi)
        except ValueError:
            self.label_result.config(
                text="Erro: Digite valores válidos para altura e peso")

    def show_bmi_category(self, bmi):
        if bmi < 18.5:
            category = "Abaixo do peso"
        elif bmi < 25:
            category = "Peso normal"
        elif bmi < 30:
            category = "Sobrepeso"
        else:
            category = "Obesidade"

        self.label_result.config(text=f"Seu IMC é: {bmi:.2f} ({category})")


if __name__ == "__main__":
    calculator = BMICalculator()
    calculator.root.mainloop()
