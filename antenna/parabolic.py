#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 23:53:48 2026

@author: ramel
"""

import tkinter as tk
from tkinter import messagebox
import math

def calculate_gain():
    try:
        # Constant updated as requested
        c = 3e8  # Speed of light in m/s (3.0 * 10^8)

        # Get values from entries
        freq_ghz = float(entry_freq.get())
        efficiency_pct = float(entry_eff.get())
        diameter = float(entry_diam.get())

        # Validation
        if freq_ghz <= 0 or efficiency_pct <= 0 or diameter <= 0:
            messagebox.showerror("Input Error", "All values must be greater than zero.")
            return

        # Unit conversions
        freq_hz = freq_ghz * 1e9
        efficiency = efficiency_pct / 100.0
        
        # Calculations
        wavelength = c / freq_hz
        # Gain formula: G = e * (pi * D / lambda)^2
        gain_linear = efficiency * ( (math.pi * diameter) / wavelength )**2
        
        # Convert to dBi
        gain_dbi = 10 * math.log10(gain_linear)

        # Update result label
        label_result.config(text=f"{gain_dbi:.2f} dBi", fg="#2e7d32")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# Setup the main window
root = tk.Tk()
root.title("Parabolic Antenna Gain Calculator")
root.geometry("350x320")
root.resizable(False, False)

# Styling configuration
padding = {'padx': 15, 'pady': 8}

# UI Layout
tk.Label(root, text="Frequency (GHz):").grid(row=0, column=0, sticky="e", **padding)
entry_freq = tk.Entry(root)
entry_freq.insert(0, "2.4")
entry_freq.grid(row=0, column=1, **padding)

tk.Label(root, text="Efficiency (%):").grid(row=1, column=0, sticky="e", **padding)
entry_eff = tk.Entry(root)
entry_eff.insert(0, "55")
entry_eff.grid(row=1, column=1, **padding)

tk.Label(root, text="Dish Diameter (m):").grid(row=2, column=0, sticky="e", **padding)
entry_diam = tk.Entry(root)
entry_diam.insert(0, "1")
entry_diam.grid(row=2, column=1, **padding)

# Calculate Button
btn_calc = tk.Button(root, text="Calculate Gain", command=calculate_gain, 
                     bg="#1565c0", fg="white", font=('Arial', 10, 'bold'), height=2)
btn_calc.grid(row=3, column=0, columnspan=2, pady=15, sticky="we", padx=40)

# Results Section
tk.Label(root, text="Antenna Gain:", font=('Arial', 10)).grid(row=4, column=0, columnspan=2)
label_result = tk.Label(root, text="-- dBi", font=('Arial', 18, 'bold'))
label_result.grid(row=5, column=0, columnspan=2)

tk.Label(root, text="Ramel Recentes").grid(row=8, column=1, sticky="e", **padding)


# Start application
root.mainloop()