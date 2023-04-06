import tkinter as tk
from main import *

# Primary Window
root = tk.Tk()

# Const Configs
FONT = ("Arial", 14)
UPPER_FONT = ("Arial", 21)
WHITE = "#ffffff"
LIGHT = "#e1e1e1"
DARK = "#262626"
BLACK = "#000000"
SWITCH_BG = "#3c3c3c"
SPECIAL_BG = "#323232"

# Configs
root.config(background=DARK)
root.title("PyCalculator")
root.iconbitmap("icon.ico")
root.resizable(False, False)

# Buffers
buffer_min_view = "0"
buffer_view = "0"

# Widgets
frame = tk.Label(root, text="PyCalculator  -  By EcWolf",bg=DARK, font=FONT, fg=LIGHT, width="28", height="1")
min_view = tk.Label(root, text="", font=FONT, fg=LIGHT, bg=DARK, width="31", height="2")
view = tk.Label(root, text="0", font=UPPER_FONT, fg=LIGHT, bg=DARK, width="21", height="3")

b_undo = tk.Button(root, text="<<", font=FONT, fg=LIGHT, bg=SPECIAL_BG, width="7", height="3", command=bUndo)
b_clean = tk.Button(root, text="CLR", font=FONT, fg=LIGHT, bg=SPECIAL_BG, width="7", height="3", command=bClean)
b_multiply = tk.Button(root, text="X", font=FONT, fg=LIGHT, bg=SPECIAL_BG, width="7", height="3", command=bMultiply)
b_split = tk.Button(root, text="%", font=FONT, fg=LIGHT, bg=SPECIAL_BG, width="7", height="3", command=bSplit)
b_add = tk.Button(root, text="+", font=FONT, fg=LIGHT, bg=SPECIAL_BG, width="7", height="3", command=bAdd)
b_subtract = tk.Button(root, text="-", font=FONT, fg=LIGHT, bg=SPECIAL_BG, width="7", height="3", command=bSubtact)
b_equal = tk.Button(root, text="=", font=FONT, fg=LIGHT, bg=SPECIAL_BG, width="7", height="7", command=bEqual)
b_deny = tk.Button(root, text="+/-", font=FONT, fg=LIGHT, bg=SPECIAL_BG, width="7", height="3", command=bDeny)
b_point = tk.Button(root, text=",", font=FONT, fg=LIGHT, bg=SPECIAL_BG, width="7", height="3", command=bPoint)
b0 = tk.Button(root, text="0", font=FONT, fg=LIGHT, bg=SWITCH_BG, width="7", height="3", command=b0)
b1 = tk.Button(root, text="1", font=FONT, fg=LIGHT, bg=SWITCH_BG, width="7", height="3", command=b1)
b2 = tk.Button(root, text="2", font=FONT, fg=LIGHT, bg=SWITCH_BG, width="7", height="3", command=b2)
b3 = tk.Button(root, text="3", font=FONT, fg=LIGHT, bg=SWITCH_BG, width="7", height="3", command=b3)
b4 = tk.Button(root, text="4", font=FONT, fg=LIGHT, bg=SWITCH_BG, width="7", height="3", command=b4)
b5 = tk.Button(root, text="5", font=FONT, fg=LIGHT, bg=SWITCH_BG, width="7", height="3", command=b5)
b6 = tk.Button(root, text="6", font=FONT, fg=LIGHT, bg=SWITCH_BG, width="7", height="3", command=b6)
b7 = tk.Button(root, text="7", font=FONT, fg=LIGHT, bg=SWITCH_BG, width="7", height="3", command=b7)
b8 = tk.Button(root, text="8", font=FONT, fg=LIGHT, bg=SWITCH_BG, width="7", height="3", command=b8)
b9 = tk.Button(root, text="9", font=FONT, fg=LIGHT, bg=SWITCH_BG, width="7", height="3", command=b9)

# Positions
frame.grid(row=0, column= 0, columnspan=4, sticky="nw")
min_view.grid(row=1, column= 0, columnspan=4, sticky="w")
view.grid(row=2, column= 0, columnspan=4, sticky="w")

b_split.grid(row=3, column=0, padx=0, pady=0)
b_multiply.grid(row=3, column=1, padx=0, pady=0)
b_undo.grid(row=3, column=2, padx=0, pady=0)
b_clean.grid(row=3, column=3, padx=0, pady=0)

b7.grid(row=4, column=0, padx=0, pady=0)
b8.grid(row=4, column=1, padx=0, pady=0)
b9.grid(row=4, column=2, padx=0, pady=0)
b_add.grid(row=4, column=3, padx=0, pady=0)

b4.grid(row=5, column=0, padx=0, pady=0)
b5.grid(row=5, column=1, padx=0, pady=0)
b6.grid(row=5, column=2, padx=0, pady=0)
b_subtract.grid(row=5, column=3, padx=0, pady=0)

b1.grid(row=6, column=0, padx=0, pady=0)
b2.grid(row=6, column=1, padx=0, pady=0)
b3.grid(row=6, column=2, padx=0, pady=0)
b_equal.grid(row=6, column=3, padx=0, pady=0, rowspan=8)

b_deny.grid(row=7, column=0, padx=0, pady=0)
b0.grid(row=7, column=1, padx=0, pady=0)
b_point.grid(row=7, column=2, padx=0, pady=0)