from tkinter import Tk, Entry, Button, StringVar, Frame, X, LEFT, SUNKEN
import scientificCalculator

def cal(event):
    global expression
    text = event.widget.cget("text")
    if expression.get()=='SyntaxError' or expression.get()=='ERROR':
        expression.set("")
        panel.update()
    print(text)
    if text == '=':
        try:
            text = scientificCalculator.scientifi_calculator(expression.get())
        except :
            text = "ERROR"
        expression.set(text)
        panel.update()
    elif text == 'C':
        expression.set("")
        panel.update()
    else:
        expression.set(expression.get()+text)
        panel.update()

root = Tk()
root.title("Calculator")
root.maxsize(305, 500)
root.minsize(305, 500)
expression = StringVar()
expression.set("")
k = 1
m = ['C', '(', ')', '%', '^']
l = ['=', '0', '/', '*', '-', '+']
# panel
panel = Entry(root, textvariable=expression, font="arial 19 bold", borderwidth=4, relief=SUNKEN)
panel.pack(fill=X, ipady=10, padx=5)
for i in range(3):
    fr = Frame(root, bg="grey")
    for j in range(3):
        btn = Button(fr, text=f"{k}", padx=28, pady=28)
        btn.pack(side=LEFT, padx=1)
        btn.bind("<Button-1>", cal)
        k += 1
    btn = Button(fr, text=m[i], padx=28, pady=28)
    btn.pack(side=LEFT, padx=1)
    btn.bind("<Button-1>", cal)
    fr.pack(pady=4)
for i in range(2):
    fr = Frame(root, bg="grey")
    for j in range(3):
        btn = Button(fr, text=l[9 - k], padx=28, pady=28)
        btn.pack(side=LEFT, padx=1)
        btn.bind("<Button-1>", cal)
        k += 1
    btn = Button(fr, text=m[3 + i], padx=28, pady=28)
    btn.pack(side=LEFT, padx=1)
    btn.bind("<Button-1>", cal)
    fr.pack(pady=4)


root.mainloop()
