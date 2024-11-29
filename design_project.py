import numpy as np
import user_csv as csv

# design_project.py
# ENDG 233 F24
# STUDENT NAME(S)
# GROUP NAME
# A terminal-based data analysis and visualization program in Python.
# You must follow the specifications provided in the project description.
# Remember to include docstrings and comments throughout your code.
def max(data_list):
    max_list=[]
    for row in data_list:
        for col in row:
            if type(col) == float:
                max_list.append(col)
    return np.max(max_list)


def min(data_list):
    min_list=[]
    for row in data_list:
        for col in row:
            if type(col) == float:
                min_list.append(col)
    return np.min(min_list)

def position(data_list, position):
    
    position_list = []
    
    for row in data_list:
        
        if row[1] == position:
            
            position_list += [row]    
    return position_list

def mean(data_list):
    mean_list = []
    for row in data_list:
        for col in row:
            if type(col) == float:
                mean_list.append(col)
    return np.mean(mean_list)

def sum(data_list):
    mean_list = []
    for row in data_list:
        for col in row:
            if type(col) == float:
                mean_list.append(col)
    return np.sum(mean_list)

def search_wage(name, lst):
    for row in lst:
        for i in range(len(row)):
            if row[i] == name:
                return row[2]

def income_tax(wage):
    
   #taxes are based of gov alberta tax brackets less that $250000
    if wage <= 148269:
                
        return 0.10 * wage
            
    elif 148269.01 <= wage <=177922:
                
        return 0.12 * wage
            
    elif 177922.01 <= wage <= 237230:

        return 0.13 * wage
            
    else:

        return 0.14 * wage

def net_income(income_tax, wage):
    return wage - income_tax

def store_tax(name, income_tax, net_income, tax_list):
    count = 0
    for row in tax_list:
        for i in range(len(row)):
            if row[0] == name:
                row[2] = round(net_income, 1)
                row[3] = round(income_tax, 1)
                tax_list[count] = row
                return tax_list
        count += 1

def find_billable(name, data):

    for row in data:
       
        if row[0] == name:
            
            return row[1]

def menu():
    while(True):    
        lst = ["Personal Details", "Company Billables", "Exit"]
        print("Welcome! Please select an option to view:\n")
        for index, option in enumerate(lst, start=1):
            print(f"\t{index}.  {option}")
    
    
        try:
            option = int(input())
            if(option not in[1, 2, 3, 4]):
                print("Invalid Input")
            else:
                return option

        
        except ValueError:
            print("Invalid Input")

def path1():
    while(True):
        print("\nPersonal Details: Select an option:")    
        lst = ["Personal Income", "Average Wage for Position", "Net Income", "Exit"]

        for index, option in enumerate(lst, start=1):
            print(f"\t{index}.  {option}")
    
    
        try:
            option = int(input())
            if(option not in[1, 2, 3, 4]):
                print("Invalid Input")
            else:
                return option

        
        except ValueError:
            print("Invalid Input")
    
def path2():
    while(True):   
        
        print("\nCompany Billables: Select an option:")    
        lst = ["Project Price", "Max Billable", "Revenue", "Profit", "Exit"]

        for index, option in enumerate(lst, start=1):
            print(f"\t{index}.  {option}")
        
        try:
            option = int(input())
            if(option not in[1, 2, 3, 4, 5]):
                print("Invalid Input")
            else:
                return option

        
        except ValueError:
            print("Invalid Input")
        

#Runs the main program
if __name__ == "__main__":
    while(True):    
        option = menu()
        if option == 1:

            while(True):

                path_opt = path1()
                if path_opt == 1:
                    
                    name = input("Enter name of employee who's income you would like to view: ")
                    employee_list = csv.read_csv("Employees", False)
                    wage = search_wage(name, employee_list)

                    print(f"{name}'s wage is ${wage:.2f}.\n")

                elif path_opt == 2:
                    posi = input("Enter the position you want to check average wage for Ex(Software Engineer): ")
                    employee_list = csv.read_csv("Employees", False)
                    average_wage = mean(position(employee_list, posi))

                    print(f"\nThe average wage for the {posi} position is ${average_wage:.2f}.")
                
                elif path_opt == 3:
                    name = input("Enter name of employee who's income tax you would like to calculate")
                    employee_list = csv.read_csv("Employees", False)
                    
                    wage = search_wage(name, employee_list)

                    tax = income_tax(wage)

                    net = net_income(tax, wage)

                    print(f"\n{name} had a gross annual salary of {wage:.2f}, an income tax of ${tax:.2f}, and a net income of ${net:.2f}\n")

                    tax_list = csv.read_csv("Taxes")
                    updated_list = store_tax(name, tax, net, tax_list)
                    csv.write_csv("Taxes", updated_list, True)
                    print(f"\n{name}'s Tax sheet has been updataed\n")
                else:
                    break
                
                continue

        elif option == 2:
            while(True):
                path_opt = path2()
                
                if path_opt == 1:
                    
                    billables = csv.read_csv("Monthy_Billables")
                    
                    project = input("Enter a project whose price you would like to view: ")

                    print(f"\nFor the {project} project we billed the client${find_billable(project, billables):.2f}")
                
                elif path_opt == 2:
                    
                    billables = csv.read_csv("Monthly_Billables", False)
                    print(f"\nThe max a client was charged was ${max(billables)}")

                elif path_opt == 3:
                    
                    billables = csv.read_csv("Monthly_Billables", False)
                    print(f"\nCompany's Monthly Earnings ${sum(billables)}")
                elif path_opt == 4:
                    
                    employee_list = csv.read_csv("Employees", False)
                    billables = csv.read_csv("Monthly_Billables", False)
                    
                    revenue = sum(billables)
                    total_wages = sum(employee_list)/(12)

                    profit = revenue - total_wages

                    print(f"\nThe profit for the month is ${profit:.2f}.")

                else:
                    break

    
