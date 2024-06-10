import tkinter as tk


class Stopwatch:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cronômetro")

        self.time = 0
        self.running = False

        self.label = tk.Label(self.root, text="Tempo: 00:00:00")
        self.label.pack()

        self.button_start = tk.Button(
            self.root, text="Iniciar", command=self.start)
        self.button_start.pack()

        self.button_stop = tk.Button(
            self.root, text="Parar", command=self.stop)
        self.button_stop.pack()

        self.button_reset = tk.Button(
            self.root, text="Resetar", command=self.reset)
        self.button_reset.pack()

        self.update_time()

    def update_time(self):
        if self.running:
            self.time += 1
            minutes = self.time // 60
            seconds = self.time % 60
            self.label.config(text=f"Tempo: {minutes:02d}:{seconds:02d}:00")

        self.root.after(1000, self.update_time)

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def reset(self):
        if not self.running:
            self.time = 0
            self.label.config(text="Tempo: 00:00:00")


if __name__ == "__main__":
    stopwatch = Stopwatch()
    stopwatch.root.mainloop()
