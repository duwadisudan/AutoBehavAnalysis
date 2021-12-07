import pandas as pd
import os

list_of_dataframes = []

def file_command(filepath):
    
    df = pd.read_csv(filepath)
    list_of_dataframes.append(df)
    
def operation(filelocation):
    a_directory = filelocation
    for filename in os.listdir(a_directory):
        filepath = os.path.join(a_directory, filename)
        file_command(filepath)
    
    combined_kali_format = pd.concat(list_of_dataframes)
    return combined_kali_format 
    

                         
                         