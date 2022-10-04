from symtable import Symbol

class Menu:
    def displayMenu(self):
        print("You will be able to choose from the following options: ")
        print("\n1-Addition\n2-Subtraction\n3-Multiplication\n4-Division\n5-Power\n")

class Integers:
    def integerOne(self):
        integerOne = input("Enter your first integer: ")
        return int(integerOne)
                                                           
    def integerTwo(self):
        integerTwo = input("Enter your second integer: ")
        return int(integerTwo)

class userChoice:
    def userOperation(self,x_input,y_input):
        opChoice = input("Choose an operation:\n[A]ddition\n[S]ubtraction\n[M]ultiplication\n[D]ivision\n[P]ower\n").upper()
        dict = {"A" : x_input+y_input,
                "S" : x_input-y_input,
                "M" : x_input*y_input,
                "D" : x_input/y_input,
                "P" : x_input**y_input}

        symb = {"A" : "+",
                "S" : "-",
                "M" : "*",
                "D" : "/",
                "P" : "^"}

        return [symb[opChoice],dict[opChoice]]

class Mainclass:
    def mainFunction(self):
        flag = True
        while(flag):

            Menu().displayMenu()                                               
            num1 = Integers().integerOne()
            num2 = Integers().integerTwo()
            choice = userChoice().userOperation(num1,num2)

            if(choice != None):
                print(num1,choice[0], num2,"=",choice[1])   
               
            else:
                print("Error, invalid input.")
            
            question = input("enter [Y]es to continue, [N]o to quit").upper()  
            
            if( question == "Y"):
                flag = True
            elif(question == "N"):
                flag = False
            else:
                print ("error, please input valid values")
                flag = False

Mainclass().mainFunction()