from tkinter import *
from tkinter import ttk

# A dogs list will be used to save or load dogs
# Not yet implemented
dogs = []

"""
Dog class initializes variables name, weight, age, allergies and diet
Set and get methods for each member variable
A dog object is used to find dietary needs based on weight
"""


class Dog:

    def __init__(self):
        self.name = None
        self.weight = 0
        self.age = 0
        self.allergies = False
        self.diet = None

    def set_name(self, name):
        self.name = name

    def set_weight(self, weight):
        self.weight = weight

    def set_age(self, age):
        self.age = age

    def set_allergies(self, allergy):
        self.allergies = allergy

    def set_diet(self, diet):
        self.diet = diet

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def get_age(self):
        return self.age

    def get_allergies(self):
        return self.allergies

    def get_diet(self):
        return self.diet


"""
The App class takes the root Tkinter window, sets the title and options/style
The class creates the labels, text, entry, checkbox and button objects
And packs them into the two frames created within the master window
"""


class App:

    def __init__(self, master):
        master.title('Raw Dog Food Calculator')
        master.resizable(False, False)

        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Arial', 11))
        self.style.configure('Header.TLabel', font=('Arial', 18, 'bold'))

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        ttk.Label(self.frame_header,
                  text='B.A.R.F. Diet Calculator',
                  style='Header.TLabel').grid(row=0, column=0, columnspan=2, padx=15)

        ttk.Label(self.frame_header, wraplength=300,
                  text=("Please enter your dog's name and weight and the calculator will display the dietary"
                        " requirements for your pet's raw food diet")).grid(row=1, column=1, padx=15)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text='Dog\'s Name:').grid(row=0, column=0, padx=5, sticky='sw')
        ttk.Label(self.frame_content, text='Weight:').grid(row=0, column=1, padx=5, sticky='sw')
        ttk.Label(self.frame_content, text='Age:').grid(row=2, column=0, padx=5, sticky='sw')
        ttk.Label(self.frame_content, text='Allergies:').grid(row=2, column=1, padx=5, sticky='sw')
        ttk.Label(self.frame_content, text='Comments:').grid(row=4, column=0, padx=5, sticky='sw')

        self.entry_name = ttk.Entry(self.frame_content, width=24, font=('Arial', 10))
        self.entry_weight = ttk.Entry(self.frame_content, width=24, font=('Arial', 10))
        self.entry_age = ttk.Entry(self.frame_content, width=24, font=('Arial', 10))
        self.text_comments = Text(self.frame_content, width=50, height=10, font=('Arial', 10))

        self.allergies = IntVar()
        self.check_allergies = ttk.Checkbutton(self.frame_content, onvalue=1, offvalue=0,
                                               variable=self.allergies)

        self.entry_name.grid(row=1, column=0, padx=5)
        self.entry_weight.grid(row=1, column=1, padx=5)
        self.entry_age.grid(row=3, column=0, padx=5)
        self.check_allergies.grid(row=3, column=1, padx=5, sticky='w')
        self.text_comments.grid(row=5, column=0, columnspan=2, padx=5)

        ttk.Button(self.frame_content, text='Submit',
                   command=self.submit).grid(row=6, column=0, padx=5, pady=5, sticky='e')
        ttk.Button(self.frame_content, text='Clear',
                   command=self.clear).grid(row=6, column=1, padx=5, pady=5, sticky='w')

    """
    The submit function takes no parameters
    Creates a dog object and sets the name, weight and age
    Also checks if allergy checkbox has been checked
    Creates a new diet object with the dog as input
    Currently only prints to console
     TODO: save list of dogs to file and create window to dispay selected dog
    """

    def submit(self):
        dog = Dog()
        dog.set_name(self.entry_name.get())
        dog.set_weight(self.entry_weight.get())
        dog.set_age(self.entry_age.get())

        if self.allergies.get() == 1:
            dog.set_allergies(True)
        else:
            dog.set_allergies(False)

        diet = Diet(dog)
        dog.set_diet(diet)
        dogs.append(dog)

        print('Dog\'s name: ', dog.get_name())
        print('Dog\'s age: ', dog.get_age())
        print('Allergies: ', dog.get_allergies())
        print('Pounds per day: ', diet.get_pounds_per_day())
        print('Ounces per day: ', diet.to_ounces(diet.get_pounds_per_day()))
        print('Muscle meat: ', diet.get_muscle_meat())
        print('Raw meaty bones: ', diet.get_raw_meaty_bones())
        print('Liver: ', diet.get_liver())
        print('Secreting organs: ', diet.get_secreting_organs())
        print('Fruits and vegetables: ', diet.get_fruit_vegetables())
        print('Other: ', diet.get_other())
        self.clear()

    # Clear method clears all GUI entries

    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_weight.delete(0, 'end')
        self.entry_age.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')


"""
The diet class takes a dog object as a parameter in its constructor
The weight variable is set and all calculations are down with this
Get functions are included for all dietary needs and the to ounces function
changes the weight to ounces
TODO: create an option that allows the user to choose pounds or ounces
"""


class Diet:
    def __init__(self, dog):
        self.weight = dog.get_weight()
        self.pounds_per_day = int(self.weight) * 0.025
        self.muscle_meat = self.pounds_per_day * 0.70
        self.raw_meaty_bones = self.pounds_per_day * 0.10
        self.liver = self.pounds_per_day * 0.05
        self.secreting_organs = self.pounds_per_day * 0.05
        self.fruit_vegetables = self.pounds_per_day * 0.09
        self.other = self.pounds_per_day * 0.01

    def get_pounds_per_day(self):
        return self.pounds_per_day

    def get_muscle_meat(self):
        return self.muscle_meat

    def get_raw_meaty_bones(self):
        return self.raw_meaty_bones

    def get_liver(self):
        return self.liver

    def get_secreting_organs(self):
        return self.secreting_organs

    def get_fruit_vegetables(self):
        return self.fruit_vegetables

    def get_other(self):
        return self.other

    def to_ounces(self, pounds):
        return pounds * 16


def main():
    root = Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__": main()
