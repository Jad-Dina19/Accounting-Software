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

file_name = input("Enter file name")
M = csv.read_csv(file_name, False)
print(mean(position(M, "Software Engineer")))
