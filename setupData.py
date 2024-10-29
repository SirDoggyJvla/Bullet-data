# Imports
import os
import numpy as np
import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd
import pyperclip


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


class SetupData():
    def __init__(self):
        path = r'C:\Users\simon\Documents\Perso\Jeux\Zomboid\Mods\Bullet data\bulletData.csv'
        
        # Load the CSV file into a DataFrame
        df = pd.read_csv(r'C:\Users\simon\Documents\Perso\Jeux\Zomboid\Mods\Bullet data\bulletData.csv',sep=';')
        self.df = df
        self.AmmoType = df['AmmoType'].values
        self.module = df['module'].values
        self.item = df['item'].values
        self.Emin = df['Emin'].values
        self.Emax = df['Emax'].values
        self.Diameter = df['Diameter'].values
        self.increaseHitTime = df['increaseHitTime'].values
        self.canKill = df['canKill'].values
        self.size = len(self.item)
        print(self.size)
        
        setup = input("Enter mod:")
        setup_method = getattr(self, f"Setup_{setup}", None)
        if setup_method:
            setup_method()  # Call the method
        else:
            print("Wrong entry")
        
    def Setup_IHR(self):
        str_format = '\t{0}]\t=\t{{ AmmoType = {1},\tEmin = {2},\tEmax = {3},\tDiameter = {4},\tCanKill = {5}, }},'

        output = ""

        df = self.df
        mod = df['mod'].values
        AmmoTypes = df['AmmoType'].values
        AmmoType = ['"{0}"'.format(AmmoTypes[i]) for i in range(len(df))]

        module = df['module'].values
        items = df['item'].values
        item = ['["{0}.{1}"'.format(module[i],items[i]) for i in range(len(df))]

        Emin = df['Emin'].values
        Emax = df['Emax'].values
        Diameter = df['Diameter'].values
        canKill = df['canKill'].values

        # Define the max lengths for each field to align them properly
        max_item_length = max(len(str(i)) for i in item)
        max_ammo_type_length = max(len(str(a)) for a in AmmoType)
        max_eminn_length = max(len(str(e)) for e in Emin)
        max_emax_length = max(len(str(e)) for e in Emax)
        max_diameter_length = max(len(str(d)) for d in Diameter)
        max_diameter_canKill = max(len(str(d)) for d in canKill)

        previousMod = ""
        for i in range(self.size):
            mod_i = mod[i]
            if mod_i != previousMod:
                previousMod = mod_i
                output += "\n"
                output += "--- {0}".format(mod_i)
                output += "\n"
                
            canKill_i = canKill[i]
            canKill_i = canKill_i == 1 and "true" or "false"
            
            output += str_format.format(
                item[i].ljust(max_item_length),
                AmmoType[i].ljust(max_ammo_type_length),
                str(Emin[i]).rjust(max_eminn_length),
                str(Emax[i]).rjust(max_emax_length),
                str(Diameter[i]).rjust(max_diameter_length),
                canKill_i.rjust(max_diameter_canKill)
            )
            output += "\n"
            
        print(output)
        
        # Copy the string to the clipboard
        pyperclip.copy(output)

SetupData()