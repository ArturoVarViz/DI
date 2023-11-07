import tkinter as tk
from tkinter import filedialog
from text_to_midi import text_to_midi  # Asegúrate de que text_to_midi esté en el mismo directorio

def save_midi(text_entry):
    text = text_entry.get("1.0", tk.END)

    for i, line in enumerate(text.split('\n')):
        if line.strip():
            mid = text_to_midi(line)
            file_path = filedialog.asksaveasfilename(defaultextension=".mid")
            if file_path:
                mid.save(file_path)

def create_gui():
    root = tk.Tk()

    text_entry = tk.Text(root)
    text_entry.pack()

    save_button = tk.Button(root, text="Guardar como MIDI", command=lambda: save_midi(text_entry))
    save_button.pack()

    root.mainloop()
