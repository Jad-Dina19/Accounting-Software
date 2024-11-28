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
            
    
    else:
        count = 0
        for line in file:
            
            data += [line.replace("\n","").split(",")]

        data.pop(0)
    
    new_data = []
    for row in data:
        for i in range(len(row)):
            
            if row[i].isnumeric():
                row[i] = float(row[i])    
        new_data.append(row)
   
    return new_data


def write_csv(file_name, data, overwrite):
    if overwrite:  
        file = open(f"data_files/{file_name}.csv", "w")
        
        for row in data:
            
            for i in range(len(row)):
            
                if i == (len(row) -1):
                
                    file.write(f"{row[i]}\n")
                else:

                    file.write(f"{row[i]},")
        file.close()
    
    else:
        file = open(f"data_files/{file_name}.csv", "w")
        count = 0
        for row in data:
            
            for i in range(len(row)):
                if i == (len(row) -1) and count == len(data) - 1:
                    
                    file.write(f"{row[i]}")
                elif i == (len(row) -1):
                
                    file.write(f"{row[i]}\n")
                else:

                    file.write(f"{row[i]},")
            count+=1
        file.close()

