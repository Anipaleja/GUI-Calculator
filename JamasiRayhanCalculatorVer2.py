# Rayhan Jamasi
# Dec 8th 2023
# Description: Second version of the calculator, make the basic math functions work

import tkinter

class calcGUI:
    def __init__(self):

        # Initalizing variables
        self.first_num = ""
        self.second_num = ""
        self.final_num_value = 0
        self.first_num_value = 0
        self.second_num_value = 0
        self.operator_count = 0
        self.input_button = True
        self.digit_counter = 0
        self.decimal_divisor = 0.1
        self.operator_chosen = ""
        self.decimal_count = 0
        self.equal_count = 0
        
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

        # Creating the buttons for the buttons_frame, row 1 starts at top and next rows are below
        # Create the first row buttons 
        self.square_root_button = tkinter.Button(self.main_window,text="√a",bg="light gray",fg="black",font="Times 15 bold")#command=self.sq_input)
        self.cubed_button = tkinter.Button(self.main_window,text="a³",bg="light gray",fg="black",font="Times 15 bold")#command=self.cubed_input)
        self.squared_button = tkinter.Button(self.main_window,text="a²",bg="light gray",fg="black",font="Times 15 bold")#,command=self.squared_input)
        self.clear_button = tkinter.Button(self.main_window,text="clear",bg="light gray",fg="dark red",font="Times 15 bold",command=self.clear_input)

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
        self.decimal_button = tkinter.Button(self.main_window,text=".",bg="light gray",fg="black",font="Times 15 bold",command=self.decimal_input)
        self.equal_button = tkinter.Button(self.main_window,text="=",bg="light gray",fg="black",font="Times 15 bold",command=self.equal_input)
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

    # defining the function for the buttons 0-9 (with self as paramter )and calling the input num function with passing the number
    # chosen as an arguement. Also adding digit counter by 1 so that in the input_num
    # function, it goes through correct if statement
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

    # Creating the function that is called once the user clicks the equal button. This increases equal count by 1
    # and calls the self.last_input
    def equal_input(self):
        self.equal_count = 0
        self.equal_count += 1
        self.last_input()

    # Creating the function (self as a paramter) that is called once the user clicks the clear button. This resets all variables to
    # their original state and clears the display box of numbers. Without this, old values for variables would
    # create problems when the user is trying to enter a new equation. 
    def clear_input(self):
        self.equal_count = 0
        self.decimal_count = 0
        self.operator_count = 0
        self.digit_counter = 0
        self.first_num = ""
        self.second_num = ""
        self.first_num_value = 0
        self.second_num_value = 0
        self.final_num_value = 0
        self.operator_chosen = ""
        self.input_button = True
        self.decimal_divisor = 0.1
        self.display_box_var.set("")

    # Creating the function called once the user enters decimal. Raises decimal counter by 1 and calls add_decimal
    # function with passing a "." as the arguement
    def decimal_input(self):
        self.decimal_count = 0
        self.decimal_count += 1
        self.add_decimal(".")

    # Creating the basic math functions with self as the paramater. Adds 1 to the operator_count
    # aond passes a " + ", " - ", " / ", or " x " depending on which button is clciked. It will pass it as
    # an argument to the operator function
    
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

    # Creating the function with self and num_input as the two paramaters. num_input recieves the number chosen by the user (depending on what
    # button they click)
    def input_num(self,num_input):

        # self.input_button figures out if it's apart of the first number or second number and displays it
        if self.input_button == True:
            self.first_num = str(self.first_num) + str(num_input)
            self.display_box_var.set(self.first_num)
            
            # Checks if its a decimal number and goes to this statement if it is not a decimal number
            if self.decimal_count == 0:
                
                # Checks if its only a 1 digit number or not. If 1 digit, first_num_value = the digit inputted, else multiply
                # original value by 10 and adds the new num_input
                if self.digit_counter == 1:
                    self.first_num_value = num_input
                else:
                    self.first_num_value = 10*self.first_num_value + num_input
                    
            # Goes to this else statment if it is a decimal number
            else:

                # Checks if its only a 1 digit number or not. If 1 digit, first_num_value = the digit inputted, else it
                # adds the new number inputted to self.first_num_value and divides it by self.decimal_divisor.
                # Decimal divisor becomes 10x smaller each time they add a new number to a DECIMAL NUMBER. This is
                # because it has to follow the rule of 0.1 (tenth), 0.01 (hundreth), 0.001 (thousandth). As you go to the right
                # of a decimal number's digits, it becomes 10x smaller.   
                if self.digit_counter == 1:
                    self.first_num_value = num_input 
                else:
                    self.first_num_value +=(num_input*self.decimal_divisor)
                    self.decimal_divisor /= 10
                    
        # Goes to this elif statement if it is for the second number and displays the first number, operator, and
        # second number.
        elif self.input_button == False:
            self.second_num = str(self.second_num) + str(num_input)
            self.display_box_var.set(str(self.first_num) + self.operator_chosen + self.second_num)

            # Checking if there are decimals
            if self.decimal_count == 0:

                # Following the same process as above as it checks the digits and assigns new values. The difference is that
                # instead of first_num and first_num_value, it uses second_num and second_num_value. 
                if self.digit_counter == 1:
                    self.second_num_value = num_input
                else:
                    self.second_num_value = 10*self.second_num_value + num_input

            # Goes to this else statement if a decimal number. if 1 digit, assigns self.second_num_value = num_input, else follows
            # the same pattern as above with self.second_num_value. adds (num_input*self.decimal divisor) to itself and decimal divisor
            # becomes 10x smaller each time)
            else:
                if self.digit_counter == 1:
                    self.second_num_value = num_input 
                else:
                    self.second_num_value += (num_input*self.decimal_divisor)
                    self.decimal_divisor /= 10

    # Defining operator function with self and operator_input as the paramaters.
    def operator(self,operator_input):

        # This ensures that once they click the operator button, it displays the operator symbol in the display box and it sets the right variables back to default value
        if self.operator_count == 1:
            self.operator_chosen = operator_input
            self.display_box_var.set(str(self.first_num)+self.operator_chosen)
            self.input_button = False
            self.digit_counter = 0
            self.decimal_count = 0
            self.decimal_divisor = 0.1

    # Defining operator function with decimal_input as the parameter (along with self)
    def add_decimal(self,decimal_input):

        # determines whatever to add the decimal to the first number or second number, adds a decimal to self.first_num or self.second_ num.
        # Then display it in the display box
        if self.decimal_count == 1 and self.input_button == True:
            self.first_num = str(self.first_num) + str(decimal_input)
            self.display_box_var.set(self.first_num)
        elif self.decimal_count == 1 and self.input_button == False:
            self.second_num = str(self.second_num) + str(decimal_input)
            self.display_box_var.set(str(self.first_num) + self.operator_chosen + self.second_num)
    
    # Defining the last_input function with self as a paramater
    def last_input(self):

        # Depending on the operation the user chosen, the program will run a specific calculation with the numbers inputted and assign
        # the value of this calculation to self.final_num_value
        if self.input_button == False and self.equal_count == 1:
            if self.operator_chosen == " + ":
                self.final_num_value = self.first_num_value + self.second_num_value
            elif self.operator_chosen == " - ":
                self.final_num_value = self.first_num_value - self.second_num_value
            elif self.operator_chosen == " / ":
                self.final_num_value = self.first_num_value / self.second_num_value
            elif self.operator_chosen == " x ":
                self.final_num_value = self.first_num_value * self.second_num_value
        
        # Sets the display box to the final value calculated by the program
        self.display_box_var.set(str(self.final_num_value))

        # Resetting specific variables back to there original value
        self.equal_count = 0
        self.operator_count = 0
        self.operator_chosen = ""
        self.second_num = ""
        self.second_num_value = 0
        self.input_button = True

        # Making the self.final_num_value now equal to the self.first_num and self.first_num_value. This is because the user can choose to perform more
        # functions with this new final value. (they do not need to clear the calculator and retype in the answer to perform operations to it)
        self.first_num = self.final_num_value
        self.first_num_value = self.final_num_value

        # Creating a remainder checker variable, assigning it a value, so that it can be used in the if statment below
        # to check if the final number is decimal or not
        remainder_checker = 0
        remainder_checker = self.first_num_value % 1
        self.final_num_value = 0

        # Determining if the number is decimal (using remainder_checker variabl)e and if the decimal_count and decimal_divisor needs to be reset or not
        if remainder_checker != 0:
            self.decimal_count = 1
        else:
            self.decimal_count = 0
            self.decimal_divisor = 0.1

# Creating an instance of the calcGUI class
calculate = calcGUI()
