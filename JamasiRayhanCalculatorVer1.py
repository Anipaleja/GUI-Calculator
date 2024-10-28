# Rayhan Jamasi
# Dec 8th 2023
# Description: make the GUI placements for the calculator, none of the buttons
# have to call a method, but arrange them for how they will look in the
# final product

import tkinter

class calcGUI:
    def __init__(self):

        # Initializing self. variables so they can be used in other functions without there value being reset (many of these variables
        # need to keep a running total, but if I initalize in each function, it'll reset the value every time it is called)
        self.first_num = ""
        self.second_num = ""
        self.operator_count = 0
        self.number_checker = True
        self.operator_count = 0
        self.digit_counter = 0
        self.decimal_count = 0
        
        # Create the main window
        self.main_window = tkinter.Tk()

        # Create the dimensions for the main window
        self.main_window.minsize(340,380)
        self.main_window.maxsize(340,380)

        # Create the variable used for the display box
        self.display_box_var = tkinter.StringVar()

        # Create the display box at the top
        self.display_box = tkinter.Label(self.main_window,textvariable = self.display_box_var, bg="light blue",fg ="black",font="Times 18 bold")

        # Positioning the display box
        self.display_box.place(x=20,y=20,width=300,height=40)

        # Creating the buttons for the main window, row 1 starts at top and next rows are below
        # Create the first row buttons 
        self.square_root_button = tkinter.Button(self.main_window,text="√a",bg="light gray",fg="black",font="Times 15 bold")
        self.cubed_button = tkinter.Button(self.main_window,text="a³",bg="light gray",fg="black",font="Times 15 bold")
        self.squared_button = tkinter.Button(self.main_window,text="a²",bg="light gray",fg="black",font="Times 15 bold")
        self.clear_button = tkinter.Button(self.main_window,text="clear",bg="light gray",fg="dark red",font="Times 15 bold")

        # Create the second row buttons
        self.num_7_button = tkinter.Button(self.main_window,text="7",bg="light gray",fg="black",font="Times 15 bold",command=self.num7_input)
        self.num_8_button = tkinter.Button(self.main_window,text="8",bg="light gray",fg="black",font="Times 15 bold",command=self.num8_input)
        self.num_9_button = tkinter.Button(self.main_window,text="9",bg="light gray",fg="black",font="Times 15 bold",command=self.num9_input)
        self.division_button = tkinter.Button(self.main_window,text="/",bg="light gray",fg="black",font="Times 15 bold",command=self.division_input)

        # Create the third row of buttons
        self.num_4_button = tkinter.Button(self.main_window,text="4",bg="light gray",fg="black",font="Times 15 bold",command=self.num4_input)
        self.num_5_button = tkinter.Button(self.main_window,text="5",bg="light gray",fg="black",font="Times 15 bold",command=self.num5_input)
        self.num_6_button = tkinter.Button(self.main_window,text="6",bg="light gray",fg="black",font="Times 15 bold",command=self.num6_input)
        self.multiplication_button = tkinter.Button(self.main_window,text="x",bg="light gray",fg="black",font="Times 15 bold",command=self.multiplication_input)

        # Create the fourth row of buttons
        self.num_1_button = tkinter.Button(self.main_window,text="1",bg="light gray",fg="black",font="Times 15 bold",command=self.num1_input)
        self.num_2_button = tkinter.Button(self.main_window,text="2",bg="light gray",fg="black",font="Times 15 bold",command=self.num2_input)
        self.num_3_button = tkinter.Button(self.main_window,text="3",bg="light gray",fg="black",font="Times 15 bold",command=self.num3_input)
        self.addition_button = tkinter.Button(self.main_window,text="+",bg="light gray",fg="black",font="Times 15 bold",command=self.addition_input)

        # Create the fifth row of buttons
        self.num_0_button = tkinter.Button(self.main_window,text="0",bg="light gray",fg="black",font="Times 15 bold",command=self.num0_input)
        self.decimal_button = tkinter.Button(self.main_window,text=".",bg="light gray",fg="black",font="Times 15 bold")#command=self.decimal_input)
        self.equal_button = tkinter.Button(self.main_window,text="=",bg="light gray",fg="black",font="Times 15 bold")#command=self.equal_input
        self.subtraction_button = tkinter.Button(self.main_window,text="-",bg="light gray",fg="black",font="Times 15 bold",command=self.subtraction_input)

        # Positioning first row buttons
        self.square_root_button.place(x=20,y=80,width=60,height=40)
        self.cubed_button.place(x=100,y=80,width=60,height=40)
        self.squared_button.place(x=180,y=80,width=60,height=40)
        self.clear_button.place(x=260,y=80,width=60,height=40)

        # Positioning the second row buttons
        self.num_7_button.place(x=20,y=140,width=60,height=40)
        self.num_8_button.place(x=100,y=140,width=60,height=40)
        self.num_9_button.place(x=180,y=140,width=60,height=40)
        self.division_button.place(x=260,y=140,width=60,height=40)

        # Positioning the third row buttons
        self.num_4_button.place(x=20,y=200,width=60,height=40)
        self.num_5_button.place(x=100,y=200,width=60,height=40)
        self.num_6_button.place(x=180,y=200,width=60,height=40)
        self.multiplication_button.place(x=260,y=200,width=60,height=40)

        # Positioning the fourth row buttons
        self.num_1_button.place(x=20,y=260,width=60,height=40)
        self.num_2_button.place(x=100,y=260,width=60,height=40)
        self.num_3_button.place(x=180,y=260,width=60,height=40)
        self.addition_button.place(x=260,y=260,width=60,height=40)

        # Positioning the third row buttons
        self.num_0_button.place(x=20,y=320,width=60,height=40)
        self.decimal_button.place(x=100,y=320,width=60,height=40)
        self.equal_button.place(x=180,y=320,width=60,height=40)
        self.subtraction_button.place(x=260,y=320,width=60,height=40)

        # Start the tkinter.mainloop
        tkinter.mainloop()

    def num0_input(self):
        self.digit_counter += 1
        self.input_num(0)
        
    def num1_input(self):
        self.digit_counter += 1
        self.input_num(1)

    def num2_input(self):
        self.digit_counter += 1
        self.input_num(2)

    def num3_input(self):
        self.digit_counter += 1
        self.input_num(3)

    def num4_input(self):
        self.digit_counter += 1
        self.input_num(4)

    def num5_input(self):
        self.digit_counter += 1
        self.input_num(5)

    def num6_input(self):
        self.digit_counter += 1
        self.input_num(6)
    
    def num7_input(self):
        self.digit_counter += 1
        self.input_num(7)

    def num8_input(self):
        self.digit_counter += 1
        self.input_num(8)

    def num9_input(self):
        self.digit_counter += 1
        self.input_num(9)

    def addition_input(self):        
        self.operator_count += 1
        self.operator(" + ")
        
    def subtraction_input(self):        
        self.operator_count += 1
        self.operator(" - ")

    def division_input(self):        
        self.operator_count += 1
        self.operator(" / ")

    def multiplication_input(self):
        self.operator_count += 1
        self.operator(" x ")

    # Creating the function called once the user enters decimal. Raises decimal counter by 1 and calls add_decimal
    # function with passing a "." as the arguement
    def decimal_input(self):
        self.decimal_count += 1
        self.add_decimal(".")

    # Defining operator function with decimal_input as the parameter (along with self)
    def add_decimal(self,decimal_input):

        # determines whatever to add the decimal to the first number or second number, adds a decimal to self.first_num or self.second_ num.
        # Then display it in the display box
        if self.decimal_count == 1 and self.number_checker == True:
            self.first_num = str(self.first_num) + str(decimal_input)
            self.display_box_var.set(self.first_num)
        elif self.decimal_count == 1 and self.number_checker == False:
            self.second_num = str(self.second_num) + str(decimal_input)
            self.display_box_var.set(str(self.first_num) + self.operator_chosen + self.second_num)

    # Defining operator function with self and operator_input as the paramaters.
    def operator(self,operator_input):

        # This ensures that once they click the operator button, it displays the operator symbol in the display box and it sets the right variables back to default value
        if self.operator_count == 1:
            self.operator_chosen = operator_input
            self.display_box_var.set(str(self.first_num)+self.operator_chosen)
            self.number_checker = False
            self.digit_counter = 0
            self.decimal_count = 0
            self.decimal_divisor = 0.1

    def input_num(self,num_input):

        # self.number_checker figures out if it's apart of the first number or second number and displays it
        if self.number_checker == True:
            self.first_num = str(self.first_num) + str(num_input)
            self.display_box_var.set(self.first_num)

        # if it is apart of the second number, it will go to this elif statement. 
        elif self.number_checker == False:
            self.second_num = str(self.second_num) + str(num_input)
            self.display_box_var.set(str(self.first_num) + self.operator_chosen + self.second_num)


# Creating an instance of the calcGUI class
calculate = calcGUI()
