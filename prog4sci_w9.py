from tkinter import*
window = Tk()
window.title('Task 1')
label = Label(window, text = "Hello world! Let's get active!")
label.pack(side = 'top')

def quitting():
    window.destroy()
    return
btn_quitting = Button(window, text = 'Close the window', command=quitting)
btn_quitting.pack(padx=200, pady = 50)

def change_color1():
    window.cget('bg') == 'pink'
    window.configure(bg='pink')
    return
def change_color2():
    window.cget('bg') == 'blue'
    window.configure(bg='blue')
    return
btn_change_color = Button(window, text='Switch background colour to pink', command= change_color1)
btn_change_color.pack(padx=200, pady=100)
btn_change_color = Button(window, text='Switch background colour to blue', command= change_color2)
btn_change_color.pack(padx=200, pady=100)
window.mainloop()



window.mainloop()
