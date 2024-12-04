import numpy as np
import user_csv as csv      #imported user_csv as alias csv
import matplotlib.pyplot as plt
import random       #This is just used to display how our plotting works, isn't part of the project itself

# design_project.py
# ENDG 233 F24
# Jad Dina, Shlok Bhatt

def max(arr):
    """ 
    finds the maximum of a 2D array
    
    parameters: takes a 2D array, must have floats or ints
   
    returns: maximum number of  2D array as a float
    none if there are no floats  or ints
    """
    
    max_list=[]

    #iterates through each value in 2D array
    for row in arr:

        for col in row:

            #checks if value is a number and adds it a 2D array with only numbers
            if type(col) == float or type(col) == int:
                
                max_list.append(col)
    
    return np.max(max_list) #returns the maximum of the 2D array


def min(arr):
    """ 
    finds the minimum of a 2D array
    
    parameters: takes a 2D array, must have floats or ints
   
    returns: minimum number of  2D array as a float
    none if there are no floats or ints 
    """
    min_list=[]

    #iterates through each value in 2D array
    for row in arr:

        for col in row:

            #checks if value is a number and adds to array of only numbers
            if type(col) == float or type(col) == int:

                min_list.append(col)

    return np.min(min_list) #returns minimum of array 

def position(arr, position):
    """
    create a list of only specific job position requested from 2D array

    parameters: arr: 2D numpy array of data read from Employees.csv
    position: position to be searched for

    returns: 2D list containing lists of people who work a certain position, and their salary
    """
    
    position_list = []
    
    #iterates through the arrays within the 2D array
    for row in arr:
        
        #checks if the positions match and adds the row into an new array if they match
        if row[1] == position:
            
            position_list += [row]

    return position_list    #returns the new 2D array

def mean(arr):
    
    """ 
    finds the mean of a 2D array 
    
    parameters: takes a 2D array, must have floats or ints
   
    returns: mean number of 2D array as a float
    none if there are no floats or ints 
    """
    
    mean_list = []
   
    #iterates through each value in 2D array
    for row in arr:

        for col in row:

            #checks if value is a number, if so it appends to a list of only floats and ints
            if type(col) == float or type(col) == int:

                mean_list.append(col)

    return np.mean(mean_list) #returns the mean of the 2D array

def sum(arr):
    """
    finds the sum of a 2D array
    
    parameters: takes a 2D array, must have floats or ints
   
    returns: sum of 2D array as a float
    none if there are no floats or ints 
    """
    mean_list = []

    #iterates through every value in the 2D array
    for row in arr:

        for col in row:

            #checks if the value is a number and adds it to a list of only ints and floats
            if type(col) == float or type(col) == int:

                mean_list.append(col)

    return np.sum(mean_list)    #returns the sum of the 2D array


def search_wage(name, lst):
    """
    searches the wage of a person whose name is input

    parameters: name: must be a string of a person on the Employees.csv sheet
                lst: must be a 2D array read from the Employees.csv sheet
    
    returns: returns wage of a specific person who was input as a float
    """
    #iterates through each array in the 2D array
    for row in lst:
        
        #checks if the names match 
        if row[0] == name:

            return row[2]   #returns persons annual salary

def income_tax(wage):
    """
    based on a wage input, calculates income tax according to alberta 2024 tax bracket

    parameters: wage: float

    returns: income tax of the wage as a float
    """
  
   #taxes are based of gov alberta tax brackets less that $250000 
   #returns income tax based off tax bracket, checks if wage is within certian ranges
   #and multiplies by rate based off wage range
    if wage <= 148269:
                
        return 0.10 * wage
            
    elif 148269.01 <= wage <=177922:
                
        return 0.12 * wage
            
    elif 177922.01 <= wage <= 237230:

        return 0.13 * wage
            
    else:

        return 0.14 * wage


def net_income(income_tax, wage):
    """
    calculates net income

    parameters: income-tax float
                wage: float

    returns: income tax: float
    """
    
    return wage - income_tax #returns income tax subtracted from wage which is net income

def store_tax(name, income_tax, net_income, tax_arr):
    """
    modifies 2D array with updated tax information by storing it by name

    parameters: name: string of person
                income tax: float of income tax 
                net_income: float of net income
                tax_arr: 2D array read from Taxes.csv

    returns: updated tax_array as a 2D list
    """
    count = 0   #counter variable

    #iterates through the index values in each row the 2D array
    for row in tax_arr:

        for i in range(len(row)):

            #checks if the row matches the name and inputs the floats rounded to 1 decimal into the updated array
            if row[0] == name:
                
                row[2] = round(net_income, 1)
                row[3] = round(income_tax, 1)
                tax_arr[count] = row   #the purpose of the counter is to keep track of which row gets replaced
                
                return tax_arr     #returns the updated tax array
        
        count += 1  #counter increments by 1

def find_billable(name, data_arr):
    """
    finds the amount billed for a specific project

     parameter: name: string name of project
                data_arr: 2D array read from January_Billables.csv
    """
    #iterates through each row in the array
    for row in data_arr:
       
        #when the project matches its corresponding price is returned
        if row[0] == name:
            
            return row[1]   #price is returned


def menu():
    """
    prints main menu options until user chooses to exit the program, or enter valid input

    returns: option that user selected as a int
    """
    #infinite loop until value is returned
    while(True):    

        lst = ["Personal Details", "Company Billables", "Exit"] #creates list of menu options
        
        print("Welcome! Please select an option to view:\n") #prints welcome title
        
        #prints the enumerated menu options
        for index, option in enumerate(lst, start=1):
            print(f"\t{index}.  {option}")
    
        #error handling, checks if input is valid integer
        try:
            option = int(input(">>>")) #this may trigger the TypeError

            if(option not in[1, 2, 3, 4]):
                
                print("Invalid Input")  #prints error message
           
            else:

                return option   #returns valid integer if not returned loop continues
        
        #checks for value error which is detected when a value of another type is being casted to the wrong typw
        except ValueError:
            print("Invalid Input")  #prints error message


def path1():
    """
    prints path1 menu options until user chooses to exit the program, or enters valid input

    returns: option that user selected as a int
    """

    #infinite loop until value is returned
    while(True):
        print("\nPersonal Details: Select an option:")  #prints path1 title  

        lst = ["Personal Income", "Average Wage for Position", "Net Income", "Menu"]    #creates list of menu options

        #prints the enumerated menu options
        for index, option in enumerate(lst, start=1):
            print(f"\t{index}.  {option}")
    
    
        #error handling, checks if input is valid integer
        try:
            option = int(input(">>>")) #this may trigger the TypeError

            if(option not in[1, 2, 3, 4]):
                
                print("Invalid Input")  #prints error message
           
            else:

                return option   #returns valid integer if not returned loop continues
        
        #checks for value error which is detected when a value of another type is being casted to the wrong typw
        except ValueError:
            print("Invalid Input")  #prints error message



def path2():

    """
    prints path2 menu options until user chooses to exit the program, or enters valid input

    returns: option that user selected as a int
    """
    #infinite loop until value is returned
    while(True):   
        
        print("\nCompany Billables: Select an option:")   #prints path2 title   

        lst = ["Project Price", "Max Billable", "Revenue", "Profit", "Menu"]    #creates list of menu options

        #prints the enumerated menu options
        for index, option in enumerate(lst, start=1):
            print(f"\t{index}.  {option}")
        
        #error handling, checks if input is valid integer
        try:
            option = int(input(">>>")) #this may trigger the TypeError

            if(option not in[1, 2, 3, 4, 5]):
                
                print("Invalid Input")  #prints error message
           
            else:

                return option   #returns valid integer if not returned loop continues
        
        #checks for value error which is detected when a value of another type is being casted to the wrong typw
        except ValueError:
            print("Invalid Input")  #prints error message

        

#Runs the main program
if __name__ == "__main__":

    #Infinite loop until user exits the program
    while(True):    
        
        option = menu() #sets menu option

        #checks which menu option was selected and proceeds to the corresponding path
        if option == 1:
            
            #runs infinite loop until user wants to go back to main menu
            while(True):

                path_opt = path1() #sets path option to what user selection
                
                #checks what user chose and runs the code based off what they choose
                if path_opt == 1:
                    
                    name = input("Enter name of employee who's income you would like to view: ") #input name
                    
                    employee_array = csv.read_csv("Employees", False)    #reads Employees.csv and stores it
                    
                    wage = search_wage(name, employee_array) #searches for wage

                    print(f"\n{name}'s wage is ${wage:.2f}.\n")   #prints employee wage

                elif path_opt == 2:
                    
                    #user input 
                    posi = input("Enter the position you want to check average wage for Ex(Software Engineer): ") 

                    employee_array = csv.read_csv("Employees", False) #reads Employees.csv and stores it

                    average_wage = mean(position(employee_array, posi)) #calculates averagae wage

                    print(f"\nThe average wage for the {posi} position is ${average_wage:.2f}.") #prints average wage and position
                    
                    positions = ["Software Engineer", "Data Scientist", "Product Manager", "Cloud Architect", "AI/ML Engineer"]     #list of different positions
                    
                    average_wages = [] #empty list 
                    
                    #fills empty list with the average wages 
                    for pos in positions:
                        average_wages.append(mean(position(employee_array, pos)))
                    
                    #the wage and job ls are now used to plot a graph

                    plt.figure(figsize = [10,5])    #graph size
                    plt.bar(positions, average_wages, color = 'blue', width = 0.3 ) #bar graph
                    
                    #graph titles
                    plt.title("Average Wages for Job Positions", fontsize = 22) 
                    plt.xlabel("Jobs", fontsize = 16)
                    plt.ylabel("Average Wage", fontsize = 16)
                    
                    #saves to given directory and displays the graph
                    plt.savefig("final_plots/average_wages.png")
                    plt.show()
                
                elif path_opt == 3:
                    name = input("Enter name of employee who's income tax you would like to calculate: ") #user input
                    
                    employee_array = csv.read_csv("Employees", False) #reads Employees.csv
                    
                    #finds wage of employee, calculates income tax, and net income
                    wage = search_wage(name, employee_array)
                    tax = income_tax(wage)
                    net = net_income(tax, wage)

                    #prints the name of employee, wage, income tax and net income
                    print(f"\n{name} had a gross annual salary of {wage:.2f}, an income tax of ${tax:.2f}, and a net income of ${net:.2f}\n")

                    
                    #reads Taxes.csv and writes updates to it of the tax values that were calculated
                    
                    tax_array = csv.read_csv("Taxes")    #reads csv
                    updated_array = store_tax(name, tax, net, tax_array) #stores it in the 2D array 
                    csv.write_csv("Taxes", updated_array, True) #writes it to the csv file
                    print(f"\n{name}'s Tax sheet has been updataed\n") #prints that the update happened

                else:
                    break #takes user back to main menu
                
                    
        elif option == 2:

            #runs infinite loop until user wants to go back to main menu
            while(True):

                path_opt = path2() #path option variable is set
                
                #checks which option user entered and runs the code
                if path_opt == 1:
                    
                    billables = csv.read_csv("January_Billables")   #reads and stores values in csv file
                    
                    project = input("Enter a project whose price you would like to view: ")     #user input

                    #prints the amount billed for a specific project to 2 decimal places
                    print(f"\nFor the {project} project we billed the client ${find_billable(project, billables):.2f}")
                
                elif path_opt == 2:
                    
                    billables = csv.read_csv("January_Billables", False)    #reads csv file and stores value in 2D array
                    #prints the maximum the company billed a client for a project
                    print(f"\nThe max a client was charged was: ${max(billables)}")

                elif path_opt == 3:
                    
                    billables = csv.read_csv("January_Billables", False)    #reads csv file and stores value in 2D 
                    
                    print(f"\nCompany's Monthly Revenue: ${sum(billables)}")   #prints companys revenue for the month

                elif path_opt == 4:
                    
                    employee_array = csv.read_csv("Employees", False)    #reads csv file and stores value in 2D 
                    
                    billables = csv.read_csv("January_Billables", False)    #reads csv file and stores value in 2D 
                    
                    
                    revenue = sum(billables) #calculates revenue
                    
                    total_wages = sum(employee_array)/(12) #calculates the sum of the employees wages per month

                    profit = revenue - total_wages #calculates monthly profit


                    print(f"\nThe profit for the month is ${profit:.2f}.") #prints the monthly profit

                    #This code is not actually part of the project, it is just here so we can display how the data would look if we had the monthly profit for every month so this just fills a list rith random profit values within a range of 100,000 - 1,000,000 dollars
                    monthly_profits = [profit]
                    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
                    for month in range(0,11):
                        monthly_profits.append(random.randint(100000, 1000000))

                    #This plots random values with our actual january monthly profit value as a line graph
                    
                    #makes the graph
                    plt.figure(figsize=[10,5]) #graph size
                    plt.plot(months, monthly_profits, "rX--") #graph color and style

                    #labels axis and titles
                    plt.title("Profits per Month", fontsize = 22) 
                    plt.xlabel("Months", fontsize = 16)
                    plt.ylabel("Monthly Profit x 10^6 dollars", fontsize = 16)

                    #displays graph and saves it to directory given
                    plt.savefig("final_plots/monthly_profits.png")
                    plt.show()
                
                else:
                    break #back to main menu
        else:
            break #quits program