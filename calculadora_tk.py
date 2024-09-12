import tkinter
import math


root = tkinter.Tk()
root.title("Calculadora Científica")
root.configure(background='white')
root.resizable(width=False, height=False)
root.geometry("480x568+450+90")

calc = tkinter.Frame(root)
calc.grid()

class Calc():
    def __init__(self):
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False

    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def display(self, value):
        txtDisplay.delete(0, tkinter.END)
        txtDisplay.insert(0, value)

    def clear_entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def all_clear_entry(self):
        self.clear_entry()
        self.total = 0

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
        self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)
        
    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())
        self.display(self.total)
        self.input_value = True
        self.check_sum = False
        
    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)


added_value = Calc()

txtDisplay = tkinter.Entry(calc, font=('arial', 20, 'bold'), bg='white', bd=30, width=28, justify=tkinter.RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

numberpad = "789456123"
i = 0
btn = []
for j in range(2, 5):
    for k in range(3):
        btn.append(tkinter.Button(calc, width=6, height=2, font=('arial', 20, 'bold'), bd=4, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
        i += 1

btnClear = tkinter.Button(calc, text=chr(67), width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                    command=added_value.clear_entry).grid(row=1, column=0, pady=1)

btnAllClear = tkinter.Button(calc, text=chr(67) + chr(69), width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                    command=added_value.all_clear_entry).grid(row=1, column=1, pady=1)

btnAdd = tkinter.Button(calc, text="+", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                command=lambda: added_value.operation("add")).grid(row=1, column=3, pady=1)

btnSub = tkinter.Button(calc, text="-", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                command=lambda: added_value.operation("sub")).grid(row=2, column=3, pady=1)

btnMult = tkinter.Button(calc, text="*", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                command=lambda: added_value.operation("multi")).grid(row=3, column=3, pady=1)

btnDiv = tkinter.Button(calc, text=chr(247), width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                command=lambda: added_value.operation("divide")).grid(row=4, column=3, pady=1)

btnZero = tkinter.Button(calc, text="0", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                command=lambda: added_value.numberEnter(0)).grid(row=5, column=0, pady=1)

btnDot = tkinter.Button(calc, text=".", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                command=lambda: added_value.numberEnter(".")).grid(row=5, column=1, pady=1)

btnEquals = tkinter.Button(calc, text="=", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg='powder blue',
                    command=added_value.sum_of_total).grid(row=5, column=2, pady=1)


root.mainloop()