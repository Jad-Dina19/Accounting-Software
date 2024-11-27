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

def menu():
    while(True):    
        lst = ["Personal Income", "Company Billables", "Company Payments", "Exit"]
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
        print("What would you like to view?")    
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
    pass
def path3():
    pass


while(True):    
    option = menu()
    if option == 1:
        while(True):
            path1_opt = path1()
            if path1_opt == 1:
                name = input("Enter name of employee who's income you would like to view:")

    elif option == 2:
        path2()
    elif option == 3:
        path3()
    else:
        break
    
