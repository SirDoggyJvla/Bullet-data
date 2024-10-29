# Imports
import os
import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd


def ask_for_repository(title,extension=None):
    while True:
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        path = filedialog.askdirectory(title=title)
        if path:
            if extension:
                txt_files = [file for file in os.listdir(path) if file.endswith(extension)]
                if txt_files:
                    return path, txt_files
                else:
                    print("No txt files.")
            else:
                return path
        else:
            print("No directory selected.")



# Load the CSV file into a DataFrame
df = pd.read_csv(r'C:\Users\simon\Documents\Perso\Jeux\Zomboid\Mods\Bullet data\bulletData.csv',sep=';')
item = df['item'].values

# Prompt user to chose a folder
path_script,txt_files = ask_for_repository("Select Scripts folder",'.txt')

os.chdir(path_script)

bullets = {}

for script_files in txt_files:
    with open(script_files, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            if not "AmmoType" in line:
                continue 

            line = line.replace('\t', '').replace('\n', '').replace(',', '').replace(' ','')
            parts = line.split('=')
            
            bullet = parts[1]

            parts = bullet.split('.')

            if 2 > len(parts):
                # print("no module for ",parts)
                module = "Base"
                bullet = parts[0]
            else:
                module = parts[0]
                bullet = parts[1]

            if bullet not in bullets and bullet not in item:
                bullets[bullet] = module
                
                
for bullet in bullets:
    print(bullets[bullet])

print("\n")
    
for bullet in bullets:
    print(bullet)