# create class
class IOString():


    # constructor to set default value
    def __init__(self):
        self.str1 = ""


        # function to get input from user
    def get_String(self):
         self.str1 = input ("Enter String : ")
    def print_String(self):
        print("Result is :", self.str1.upper())

str1 = IOString()
str1.get_String()
str1.print_String()
    
            
        