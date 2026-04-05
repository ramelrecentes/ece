

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 21:32:30 2026

@author: ramel
"""
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation

class StandingWaveApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Standing Waves Visualizer rev 0.1 - Engr. Ramel Recentes ")
       
        # --- Matplotlib Setup (Top) ---
        self.fig, self.ax = plt.subplots(figsize=(8, 4))
        self.pi = np.pi
        self.t = np.linspace(0, 2 * self.pi, 1000)
        self.ax.set_xlim(0, 2 * self.pi)
        self.ax.set_ylim(-4, 4)
        self.ax.grid(True, linestyle='--', alpha=0.6)
        self.ax.set_title("Standing Wave Visualization Tool")

        self.line1, = self.ax.plot([], [], color='b', lw=1.5, label="Incident")
        self.line2, = self.ax.plot([], [], color='g', lw=1.5, label="Reflected")
        self.line,  = self.ax.plot([], [], color='r', lw=2.5, label="Standing")

        # Embed Matplotlib in Tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # --- UI Layout (Bottom) ---
        control_frame = ttk.Frame(root, padding="15")
        control_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Vi Input
        ttk.Label(control_frame, text="Vi:").grid(row=0, column=0, padx=2)
        self.vi_entry = ttk.Entry(control_frame, width=7)
        self.vi_entry.insert(0, "1.0")
        self.vi_entry.grid(row=0, column=1, padx=5)

        # Vr Input
        ttk.Label(control_frame, text="Vr:").grid(row=0, column=2, padx=2)
        self.vr_entry = ttk.Entry(control_frame, width=7)
        self.vr_entry.insert(0, "1.0")
        self.vr_entry.grid(row=0, column=3, padx=5)

        # Toggle Button (Start/Stop)
        self.is_running = True
        self.btn_toggle = ttk.Button(control_frame, text="Stop Simulation", command=self.toggle_anim)
        self.btn_toggle.grid(row=0, column=4, padx=20)

        # Legend Labels
        ttk.Label(control_frame, text="Blue: Incident", foreground="blue").grid(row=0, column=5, padx=5)
        ttk.Label(control_frame, text="Green: Reflected", foreground="green").grid(row=0, column=6, padx=5)
        ttk.Label(control_frame, text="Red: Standing", foreground="red").grid(row=0, column=7, padx=5)

        # --- Animation Control ---
        self.ani = animation.FuncAnimation(
            self.fig, self.animate, init_func=self.init_plot,
            frames=500, interval=50, blit=True
        )

    def toggle_anim(self):
        if self.is_running:
            self.ani.event_source.stop()
            self.btn_toggle.config(text="Start Simulation")
        else:
            self.ani.event_source.start()
            self.btn_toggle.config(text="Stop Simulation")
        self.is_running = not self.is_running

    def init_plot(self):
        self.line1.set_data([], [])
        self.line2.set_data([], [])
        self.line.set_data([], [])
        return self.line1, self.line2, self.line

    def animate(self, phi):
        try:
            vi = float(self.vi_entry.get())
            vr = float(self.vr_entry.get())
        except ValueError:
            vi, vr = 0.0, 0.0

        y1 = vi * np.sin(6 * self.t - phi / 10.0)
        y2 = vr * np.sin(6 * self.t + phi / 10.0)
        y = y1 + y2

        self.line1.set_data(self.t, y1)
        self.line2.set_data(self.t, y2)
        self.line.set_data(self.t, y)
       
        return self.line1, self.line2, self.line

if __name__ == "__main__":
    root = tk.Tk()
    app = StandingWaveApp(root)
    root.mainloop()