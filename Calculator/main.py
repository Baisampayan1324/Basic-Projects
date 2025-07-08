import math
import tkinter as tk
from tkinter import StringVar

# Global operator string
calc_operator = ""

def button_click(char):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)

def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")

def button_delete():
    global calc_operator
    calc_operator = calc_operator[:-1]
    text_input.set(calc_operator)

def factorial(n):
    return 1 if n in (0, 1) else n * factorial(n - 1)

def fact_func():
    global calc_operator
    try:
        result = str(factorial(int(calc_operator)))
        calc_operator = result
        text_input.set(result)
    except:
        text_input.set("ERROR")

def trig_sin():
    global calc_operator
    try:
        result = str(math.sin(math.radians(float(calc_operator))))
        calc_operator = result
        text_input.set(result)
    except:
        text_input.set("ERROR")

def trig_cos():
    global calc_operator
    try:
        result = str(math.cos(math.radians(float(calc_operator))))
        calc_operator = result
        text_input.set(result)
    except:
        text_input.set("ERROR")

def trig_tan():
    global calc_operator
    try:
        result = str(math.tan(math.radians(float(calc_operator))))
        calc_operator = result
        text_input.set(result)
    except:
        text_input.set("ERROR")

def trig_cot():
    global calc_operator
    try:
        result = str(1 / math.tan(math.radians(float(calc_operator))))
        calc_operator = result
        text_input.set(result)
    except:
        text_input.set("ERROR")

def square_root():
    global calc_operator
    try:
        val = float(calc_operator)
        if val >= 0:
            temp = str(val ** 0.5)
            calc_operator = temp
            text_input.set(temp)
        else:
            text_input.set("ERROR")
    except:
        text_input.set("ERROR")

def third_root():
    global calc_operator
    try:
        val = float(calc_operator)
        temp = str(val ** (1/3))
        calc_operator = temp
        text_input.set(temp)
    except:
        text_input.set("ERROR")

def sign_change():
    global calc_operator
    try:
        if calc_operator.startswith('-'):
            calc_operator = calc_operator[1:]
        else:
            calc_operator = '-' + calc_operator
        text_input.set(calc_operator)
    except:
        text_input.set("ERROR")

def percent():
    global calc_operator
    try:
        temp = str(eval(calc_operator + '/100'))
        calc_operator = temp
        text_input.set(temp)
    except:
        text_input.set("ERROR")

def button_equal():
    global calc_operator
    try:
        temp_op = str(eval(calc_operator))
        calc_operator = temp_op
        text_input.set(temp_op)
    except:
        text_input.set("ERROR")

def key_press(event):
    key = event.char
    if key.isdigit() or key in '+-*/.()':
        button_click(key)
    elif key == '\r':
        button_equal()
    elif key == '\b':
        button_delete()
    elif key.lower() == 'c':
        button_clear_all()

# Main window
tk_calc = tk.Tk()
tk_calc.title("Calculator")
tk_calc.geometry("480x700")
tk_calc.configure(bg="#121212")
tk_calc.resizable(False, False)

# For responsiveness
for i in range(10):
    tk_calc.grid_rowconfigure(i, weight=1)
for i in range(5):
    tk_calc.grid_columnconfigure(i, weight=1)

text_input = StringVar()

# Display frame
display_frame = tk.Frame(tk_calc, bg="#121212")
display_frame.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)

text_display = tk.Entry(
    display_frame,
    font=('Consolas', 24, 'bold'),
    textvariable=text_input,
    bd=0,
    insertwidth=2,
    bg='#1f1f1f',
    fg='#0ef',
    justify='right',
    relief='flat',
    highlightthickness=2,
    highlightcolor='#0ef',
    highlightbackground='#333',
)
text_display.pack(fill='both', expand=True, padx=5, pady=5)

tk_calc.bind('<Key>', key_press)
tk_calc.focus_set()

# Button style dictionaries
common_style = {
    'font': ('Segoe UI', 14, 'bold'),
    'bd': 0,
    'relief': 'flat',
    'cursor': 'hand2',
    'activebackground': '#2a2a2a'
}
sci_style = {**common_style, 'fg': '#fff', 'bg': '#3f51b5', 'activeforeground': '#fff'}
num_style = {**common_style, 'fg': '#fff', 'bg': '#333', 'activeforeground': '#fff'}
op_style = {**common_style, 'fg': '#fff', 'bg': '#00897b', 'activeforeground': '#fff'}
special_style = {**common_style, 'fg': '#fff', 'bg': '#b71c1c', 'activeforeground': '#fff'}

# Row 1
tk.Button(tk_calc, sci_style, text='abs', command=lambda: button_click('abs(')).grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, sci_style, text='mod', command=lambda: button_click('%')).grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, sci_style, text='div', command=lambda: button_click('//')).grid(row=1, column=2, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, sci_style, text='x!', command=fact_func).grid(row=1, column=3, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, sci_style, text='e', command=lambda: button_click(str(math.e))).grid(row=1, column=4, sticky="nsew", padx=2, pady=2)

# Row 2
tk.Button(tk_calc, sci_style, text='sin', command=trig_sin).grid(row=2, column=0, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, sci_style, text='cos', command=trig_cos).grid(row=2, column=1, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, sci_style, text='tan', command=trig_tan).grid(row=2, column=2, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, sci_style, text='cot', command=trig_cot).grid(row=2, column=3, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, sci_style, text='π', command=lambda: button_click(str(math.pi))).grid(row=2, column=4, sticky="nsew", padx=2, pady=2)

# Row 3
tk.Button(tk_calc, sci_style, text='x²', command=lambda: button_click('**2')).grid(row=3, column=0, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, sci_style, text='x³', command=lambda: button_click('**3')).grid(row=3, column=1, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, sci_style, text='x^n', command=lambda: button_click('**')).grid(row=3, column=2, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, sci_style, text='x⁻¹', command=lambda: button_click('**(-1)')).grid(row=3, column=3, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, sci_style, text='10^x', font=('Segoe UI', 12, 'bold'), command=lambda: button_click('10**')).grid(row=3, column=4, sticky="nsew", padx=2, pady=2)

# Row 4
tk.Button(tk_calc, sci_style, text='√', command=square_root).grid(row=4, column=0, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, sci_style, text='∛', command=third_root).grid(row=4, column=1, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, sci_style, text='ⁿ√', command=lambda: button_click('**(1/')).grid(row=4, column=2, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, sci_style, text='log', font=('Segoe UI', 12, 'bold'), command=lambda: button_click('log(')).grid(row=4, column=3, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, sci_style, text='ln', command=lambda: button_click('math.log(')).grid(row=4, column=4, sticky="nsew", padx=2, pady=2)

# Row 5
tk.Button(tk_calc, sci_style, text='(', command=lambda: button_click('(')).grid(row=5, column=0, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, sci_style, text=')', command=lambda: button_click(')')).grid(row=5, column=1, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, sci_style, text='±', command=sign_change).grid(row=5, column=2, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, sci_style, text='%', command=percent).grid(row=5, column=3, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, sci_style, text='e^x', command=lambda: button_click('math.e**')).grid(row=5, column=4, sticky="nsew", padx=2, pady=2)

# Row 6
tk.Button(tk_calc, num_style, text='7', command=lambda: button_click('7')).grid(row=6, column=0, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, num_style, text='8', command=lambda: button_click('8')).grid(row=6, column=1, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, num_style, text='9', command=lambda: button_click('9')).grid(row=6, column=2, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, special_style, text='DEL', command=button_delete).grid(row=6, column=3, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, special_style, text='AC', command=button_clear_all).grid(row=6, column=4, sticky="nsew", padx=2, pady=2)

# Row 7
tk.Button(tk_calc, num_style, text='4', command=lambda: button_click('4')).grid(row=7, column=0, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, num_style, text='5', command=lambda: button_click('5')).grid(row=7, column=1, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, num_style, text='6', command=lambda: button_click('6')).grid(row=7, column=2, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, op_style, text='×', command=lambda: button_click('*')).grid(row=7, column=3, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, op_style, text='÷', command=lambda: button_click('/')).grid(row=7, column=4, sticky="nsew", padx=2, pady=2)

# Row 8
tk.Button(tk_calc, num_style, text='1', command=lambda: button_click('1')).grid(row=8, column=0, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, num_style, text='2', command=lambda: button_click('2')).grid(row=8, column=1, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, num_style, text='3', command=lambda: button_click('3')).grid(row=8, column=2, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, op_style, text='+', command=lambda: button_click('+')).grid(row=8, column=3, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, op_style, text='−', command=lambda: button_click('-')).grid(row=8, column=4, sticky="nsew", padx=2, pady=2)

# Row 9
tk.Button(tk_calc, num_style, text='0', command=lambda: button_click('0')).grid(row=9, column=0, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, num_style, text='.', command=lambda: button_click('.')).grid(row=9, column=1, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, sci_style, text='EXP', font=('Segoe UI', 12, 'bold'), command=lambda: button_click('*10**')).grid(row=9, column=2, sticky="nsew", padx=2, pady=2)
tk.Button(tk_calc, op_style, text='=', command=button_equal).grid(row=9, column=3, columnspan=2, sticky="nsew", padx=2, pady=2)

# Status bar or instructions
status_frame = tk.Frame(tk_calc, bg="#121212", height=30)
status_frame.grid(row=10, column=0, columnspan=5, sticky="ew", padx=10, pady=5)
info_label = tk.Label(
    status_frame, 
    font=('Segoe UI', 9), 
    bg="#121212", 
    fg="#999"
)
info_label.pack()

tk_calc.mainloop()