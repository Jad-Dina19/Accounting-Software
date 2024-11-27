import numpy as np
# user_csv.py
# ENDG 233 F24
# STUDENT NAME(S)
# GROUP NAME
# A terminal-based data analysis and visualization program in Python.
# You must follow the specifications provided in the project description.
# Remember to include docstrings and comments throughout your code.
def read_csv(file_name, include_headers = True):
    file = open(f"data_files/{file_name}.csv", "r")
    data =[]
    if(include_headers):
        for line in file:
            data += [line.replace("\n","").split(",")]
            data[len(data)-1] = float(data[len(data)-1])
    
    else:
        count = 0
        for line in file:
            
            data += [line.replace("\n","").split(",")]

            if count != 0:
                data[len(data)-1][2] = float(data[len(data)-1][2])
            
            count+= 1
        data.pop(0)

    return data


def write_csv():
    pass


