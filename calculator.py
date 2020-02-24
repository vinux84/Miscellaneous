# After you get the basics working, implement args, loop to display better, and number buttons to work
import os
#  import keyboard

class Calculator:

    def __init__(self, inp_1, inp_2):
        self.inp_1 = inp_1
        self.inp_2 = inp_2

    def addition(self):
        return self.inp_1 + self.inp_2

    def subtraction(self):
        return self.inp_1 - self.inp_2

    def multiplication(self):
        return self.inp_1 * self.inp_2

    def division(self):
        return self.inp_1 // self.inp_2

def ui():
    refresh()
    num_one = int(input(""))
    # for Key Logger, everytime this variable gets active, connect this with the key of enter?
    refresh()
    operand = input(f"{num_one} ")
    refresh()
    num_two = int(input(f"{num_one} {operand} "))
    refresh()
    calc = Calculator(num_one, num_two)
    if operand == "+":
        refresh()
        print(f"{num_one} {operand} {num_two} = {calc.addition()}\n")
    elif operand == "-":
        print(f"{num_one} {operand} {num_two} = {calc.subtraction()}\n")
    elif operand == "*":
        print(f"{num_one} {operand} {num_two} = {calc.multiplication()}\n")
    elif operand == "/":
        print(f"{num_one} {operand} {num_two} = {calc.division()}\n")
    else:
        print("Please Choose a Operand")

def refresh():

    while True:
        clear()
        print("Vincent's Calculator\n\n")
        break

def clear():
    os.system('clear')


ui()

