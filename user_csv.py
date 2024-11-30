import numpy as np
# user_csv.py
# ENDG 233 F24
# Jad Dina, Shlok Bhatt

#this is just a function we made to check if a string is a float
def isfloat(num):
    """
    takes a number and checks if it is a float 

    parameters: num: any value

    returns: True if is float
             False if not float
    """
    #tries to cast value to float, if successful it returns True, if not it will produce a Value error
    try:
        float(num)
        return True
    
    #if this error is produced value is not a float and False will be returned
    except ValueError:
        return False
    

def read_csv(file_name, include_headers = True):
    """
    creates a 2D list of a csv file with or without headers

    parameters: file_name: string, name of the file being read
                include_headers(optional): boolean 

    returns: 2D list of data read from csv file
    """

    file = open(f"data_files/{file_name}.csv", "r") #opens file

    data =[]    #list which will hold data

    #checks if user wants headers to be included
    if(include_headers):
        
        #reads file line by line separating values into a list at the commas
        for line in file:

            data += [line.replace("\n","").split(",")] #appends list of a line to the 2D list
            
    
    else:
        #reads file line by line separating values into a list at the commas
        for line in file:
            
            data += [line.replace("\n","").split(",")] #appends list of a line to the 2D list

        data.pop(0) #removes headers
    

    new_data = [] #new list is created

    #iterates through every index value in the 2D list
    for row in data:
        for i in range(len(row)):
            
            #if is float is true the value gets casted to a float and put back into the row
            if isfloat(row[i]):
                row[i] = float(row[i])   

        new_data.append(row) #the updated row is appended to the new list
   
    return new_data #the 2D list is returned


def write_csv(file_name, data, overwrite):
    """
    writes a 2D list of data into a csv file

    parameters: file_name: string name of the csv file
                data: 2D list of data to be written
                overwrite: boolean 
    """

    #checks if file is to be overwritten
    if overwrite:  
        
        file = open(f"data_files/{file_name}.csv", "w") #opens file with w which overwrites
        
        #iterates through the index of each value in the 2D list
        for row in data:
            
            for i in range(len(row)):
                
                #adds new line rather than comma if value is the last in a row
                #this is done to maintain csv format
                if i == (len(row) -1):
                
                    file.write(f"{row[i]}\n") #writes the value to file
                else:

                    file.write(f"{row[i]},") #writes the value to file
        
        file.close()    #file is closed
    
    else:
        
        file = open(f"data_files/{file_name}.csv", "a")
    
        #iterates through the index of each value in the 2D list
        for row in data:
            
            for i in range(len(row)): #opens file with a which appends to existing data
                
                #adds new line rather than comma if value is the last in a row
                #this is done to maintain csv format
                if i == (len(row) -1):
                
                    file.write(f"{row[i]}\n") #writes the value to file
                else:

                    file.write(f"{row[i]},") #writes the value to file
        
        file.close()    #file is closed

