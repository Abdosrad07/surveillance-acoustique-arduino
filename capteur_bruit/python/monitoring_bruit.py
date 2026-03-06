import serial
import matplotlib.pyplot as plt
from collections import deque

# --- Configuration ---
PORT = "COM5"
BAUD = 9600
SEUIL = 100 # Valeur seuil pour alerte
TAILLE_FENETRE = 20 # Pour moyenne glissante

# --- Initialisation ---
ser = serial.Serial(PORT, BAUD)
signal = deque(maxlen=100) # dernier 100 points
moyenne_glissante = deque(maxlen=TAILLE_FENETRE)

plt.ion() # mode interactif
fig, ax = plt.subplots()

# --- Boucle principale ---
while True:
    line = ser.readline().decode(errors="ignore").strip()
    if line.isdigit():
        val = int(line)
        signal.append(val)
        moyenne_glissante.append(val)

        # Calcul moyenne glissante
        if len(moyenne_glissante) > 0:
            moyenne = sum(moyenne_glissante) / len(moyenne_glissante)
        else :
            moyenne = val
        
        # Alerte si seuil dépassé
        if val > SEUIL:
            print(f"ALERTE ! Niveau bruit élevé : {val}")

        # Affichage graphique
        ax.clear()
        ax.plot(signal, label="Signal")
        ax.plot([moyenne]*len(signal), "--", label=f"Moyenne glissante({TAILLE_FENETRE})")
        ax.set_title("Station acoustique")
        ax.set_xlabel("Echantillons")
        ax.set_ylabel("Amplitude")
        ax.legend()
        plt.pause(0.01)