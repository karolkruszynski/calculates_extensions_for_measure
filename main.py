import tkinter as tk
import time
import sys
import os

# Tworzenie okna głównego
root = tk.Tk()
root.title("Program obliczający doczepy dla miarki")
root.geometry("550x300")

# Funkcja do obliczania wymiarów zwykłego mebla
def calculate_normal_measurement():
    os_x_cale = str(entry_os_x.get())
    os_x_cale = os_x_cale.replace(",", ".")
    os_x_cale_f = float(os_x_cale)
    wynik_os_x = os_x_cale_f * 2.54
    wynik_cm_os_x = wynik_os_x / 2
    # Czyścimy pole tekstowe, a następnie wprowadzamy do niego wynik funkcji.
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, "KIND LEFT dla X: -" + str(wynik_cm_os_x) + "\n" + "KIND RIGHT dla X: " + str(wynik_cm_os_x))


# Funkcja do obliczania wymiarów rotacyjnego mebla
def calculate_rotational_measurement():
    os_x_cale = str(entry_os_x.get())
    os_x_cale = os_x_cale.replace(",", ".")
    os_x_cale_f = float(os_x_cale)
    wynik_os_x = os_x_cale_f * 2.54
    os_z_cale = str(entry_os_z.get())
    os_z_cale = os_z_cale.replace(",", ".")
    os_z_cale_f = float(os_z_cale)
    wynik_os_z = os_z_cale_f * 2.54
    wynik_cm_os_z = wynik_os_z / 2
    wynik_cm_os_x = wynik_os_x / 2
    # Czyścimy pole tekstowe, a następnie wprowadzamy do niego wynik funkcji.
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, "KIND LEFT dla Z: -" + str(wynik_cm_os_z) + "\n" + "KIND RIGHT dla X: " + str(wynik_cm_os_x))


# Funkcja do wyświetlania treści dokumentacji programu
def dokumentacja():
    dokumentacja_text.config(text="Program służy do obliczania z Cali na Centymetry, miarki do mebli zawierajacych sectional builder. \n ")
    dokumentacja_text2.config(text="Wartości wyliczone przez program wpisujemy w PE danego modułu w kategorii: \n ")
    dokumentacja_text3.config(text="MEASUREMENT ATTACHMENTS  ==> DEFAULTS \n")

def insert_text(text):
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, text)


# Tworzenie instancji dla dokumentacji
dokumentacja_text = tk.Label(root, text=" ")
dokumentacja_text2 = tk.Label(root, text=" ")
dokumentacja_text3 = tk.Label(root, text=" ")

# Tworzenie etykiet
label_os_x = tk.Label(root, text="Podaj szerokość ( X ) w Calach:")
label_os_z = tk.Label(root, text="Podaj głębokość ( Z ) w Calach:")
label_dokumentacja = tk.Label(root, text=" Dokumentacja Programu ")
result_text = tk.Text(root, height=5, width=30)

# Tworzenie pola tekstowego
entry_os_x = tk.Entry(root)
entry_os_z = tk.Entry(root)

# Tworzenie przycisków
calculate_normal_button = tk.Button(root, text="Oblicz wymiar dla zwykłego mebla", command=calculate_normal_measurement)
calculate_rotational_button = tk.Button(root, text="Oblicz wymiar dla rotacyjnego mebla", command=calculate_rotational_measurement)
dokumentacja_button = tk.Button(root, text=" Wyświetl ", command=dokumentacja)

# Umieszczanie elementów w oknie
label_os_x.grid(column=0, row=0)
entry_os_x.grid(column=1, row=0)
label_os_z.grid(column=0, row=1)
entry_os_z.grid(column=1, row=1)
label_dokumentacja.grid(column=0, row=2)
dokumentacja_button.grid(column=1, row=2)
result_text.grid(column=0, row=4, columnspan=2)
calculate_normal_button.grid(column=0, row=3)
calculate_rotational_button.grid(column=1, row=3)
dokumentacja_text.grid(row=6,columnspan=2)
dokumentacja_text2.grid(row=7,columnspan=2)
dokumentacja_text3.grid(row=8,columnspan=2)
root.mainloop()
