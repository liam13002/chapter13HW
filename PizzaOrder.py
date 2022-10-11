import tkinter
import tkinter.messagebox
 
class Pizza:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry('500x300')
 
        self.topframe = tkinter.Frame(self.main_window)
        self.midframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)
 
 
        self.main_window.title("Pizza Order")
 
        self.label = tkinter.Label(self.main_window, text="Pizza Order")
        self.label.pack()
 
        self.name_label = tkinter.Label(self.topframe, text="Name:")
        self.name_label.pack()
 
        self.name_entry = tkinter.Entry(self.topframe)
        self.name_entry.pack()
 
        self.crust_label = tkinter.Label(self.midframe, text="Crust:")
        self.crust_label.pack()
 
        self.crust_var = tkinter.StringVar(self.main_window)
        self.crust_var.set("Thin")
        self.crust_option = tkinter.OptionMenu(self.midframe, self.crust_var, "Thin", "Thick", "Stuffed")
        self.crust_option.pack()
 
        self.toppings_label = tkinter.Label(self.bottomframe, text="Toppings:")
        self.toppings_label.pack()
 
        self.pepperoni_var = tkinter.IntVar()
        self.pepperoni_check = tkinter.Checkbutton(self.bottomframe, text="Pepperoni", variable=self.pepperoni_var)
        self.pepperoni_check.pack()
 
        self.olives_var = tkinter.IntVar()
        self.olives_check = tkinter.Checkbutton(self.bottomframe, text="Olives", variable=self.olives_var)
        self.olives_check.pack()
 
        self.pineapple_var = tkinter.IntVar()
        self.pineapple_check = tkinter.Checkbutton(self.bottomframe, text="Pineapple", variable=self.pineapple_var)
        self.pineapple_check.pack()
 
        self.calculate_button = tkinter.Button(self.bottomframe, text="Calculate", command=self.price)
        self.calculate_button.pack()
 
        self.quit_button = tkinter.Button(self.bottomframe, text="Quit", command=self.main_window.quit)
        self.quit_button.pack()
 
        self.topframe.pack()
        self.midframe.pack()
        self.bottomframe.pack()
        tkinter.mainloop()
 
    def price(self):
        name = self.name_entry.get()
        crust = self.crust_var.get()
        pepperoni = self.pepperoni_var.get()
        olives = self.olives_var.get()
        pineapple = self.pineapple_var.get()
 
        total = 0
        if crust == "Thin":
            total += 10
        elif crust == "Thick":
            total += 12
        elif crust == "Stuffed":
            total += 15
 
        if pepperoni == 1:
            total += 2
        if pineapple == 1:
            total += 1
        if olives == 1:
            total += 1
 
        tkinter.messagebox.showinfo("Total", "Total: $" + str(total) + "\nName: " + name)
 
 
my_gui = Pizza()