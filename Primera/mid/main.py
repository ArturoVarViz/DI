import tkinter as tk
from tkinter import filedialog
from mido import Message, MidiFile, MidiTrack

# Mapeo de letras a notas
note_map = {
    'A': 57,  # A en la 4ª octava
    'B': 58,  # Bb en la 4ª octava
    'C': 60,  # C en la 5ª octava
    'D': 62,  # D en la 5ª octava
    'E': 63,  # Eb en la 5ª octava
    'F': 64,  # E en la 5ª octava
    'G': 66,
    'H': 67,
    'I': 68,
    'J': 69,
    'K': 70,
    'L': 71,
    'M': 72,
    'N': 73,
    'Ñ': 73,
    'O': 74,
    'P': 75,
    'Q': 76,
    'R': 77,
    'S': 78,
    'T': 79,
    'U': 80,
    'V': 81,
    'W': 82,
    'X': 83,
    'Y': 84,
    'Z': 85
}


def text_to_midi(text):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    for char in text:
        if char == " ":
            track.append(Message('note_off', note=note, velocity=64, time=64))  # tiempo de silencio
        else:
            note = note_map.get(char.upper())
            if note:
                track.append(Message('note_on', note=note, velocity=64, time=32))
                track.append(Message('note_off', note=note, velocity=64, time=32))

    return mid


def save_midi():
    text = text_entry.get("1.0", tk.END)

    for i, line in enumerate(text.split('\n')):
        if line.strip():  # Verifica si la línea no está vacía
            mid = text_to_midi(line)
            file_path = filedialog.asksaveasfilename(defaultextension=f"_line{i + 1}.mid")
            if file_path:
                mid.save(file_path)


root = tk.Tk()

text_entry = tk.Text(root)
text_entry.pack()

save_button = tk.Button(root, text="Guardar como MIDI", command=save_midi)
save_button.pack()

root.mainloop()
