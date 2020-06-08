# Fahrenheit til Celsius
import tkinter

def convert_to_celsius():
    fahrenheit = float(input_box.get())
    celsius = (fahrenheit-32)*5/9
    output_label.config(text=round(celsius, 2))


window = tkinter.Tk()
window.title("C til F konvertering")
window.minsize(width=250, height=50)

lable_c = tkinter.Label(text="Indtast i C")
input_box = tkinter.Entry(justify=tkinter.RIGHT)
output_label = tkinter.Label(text="", justify=tkinter.RIGHT, width=8)
action_button = tkinter.Button(text='Konverter', command=convert_to_celsius)

lable_c.grid(row=0, padx=20, pady=10)
input_box.grid(row=0, column=1)

action_button.grid(row=1, padx=20, pady=10)
output_label.grid(row=1, column=1)

window.mainloop()


