import pandas as pd
import matplotlib.pyplot as plt
import time

print("Please make sure the file is in the same folder as this application and is in .csv format!")
file_name = input("Enter the file name: ")
df = pd.read_csv(f"{file_name}.csv")

original_number_of_trials = int(input("Enter the number of trials each that unique animal has in your dataset: "))
size_block = int(input("Enter the number of blocks you want in your analysis: "))
y_axis_upper_limit = float(input("Enter the upper limit of magnitude (mV) to be displayed on the plot for y-axis (1.5 recommended): "))
trials_in_block = original_number_of_trials / size_block

names_id = df['Animal'].unique().tolist() 
#print(len(names_id))

r = ['70 dB SPL','80 dB SPL','90 dB SPL',
         '100 dB SPL','105 dB SPL']

s = [70,80,90,100,105]

for name in names_id:
    block_number_list = []
    list_of_dataframes = []
    block_number = 0
    floor = 0 
    ceiling = trials_in_block
    while (ceiling<=original_number_of_trials):
        temp = (df[df['Animal'] == name][df['Trial'] > floor][df['Trial']<= ceiling])
        new_temp = temp[['dB', 'ASR val']]
        grouped = new_temp.groupby("dB")
        meaned = grouped.mean()
        meaned = meaned.reset_index()
        floor += trials_in_block
        ceiling += trials_in_block
        block_number += 1
        block_number_list.append(block_number)
        
        # plt.figure()
        # plt.plot(meaned['dB'],meaned['ASR val'],linestyle='-', marker='o', color='r')
        # plt.xlabel("Pulse intensity (dB SPL)")
        # plt.ylabel("Magnitude (mV)")
        # plt.ylim([0.0, y_axis_upper_limit])
        # #xlim,ylim,block number
        # plt.title("ASR amplitude within block " + str(block_number) + " for "  + str(name))
        # plt.savefig("ASR amplitude within block " + str(block_number) + " for " + str(name) +'.jpg')
        # plt.grid() 
        # # Combine all the operations and display
        # #plt.show()
        # #plt.close()
        # kali_format_data = meaned[['dB','ASR val']]
        # kali_format_data['Animal ID'] =  [name]*5
        # #kali_format_data['Block number'] = block_number_list
        # kali_format_data['Block number'] = [block_number]*5
        # list_of_dataframes.append(kali_format_data)

    combined_kali_format = pd.concat(list_of_dataframes)
    new_combined = combined_kali_format[['Animal ID','Block number','dB','ASR val']]
    grouped = new_combined.sort_values(["dB",'Block number'])
    grouped.to_csv("For "  + str(name) +  '.csv' , index = False)
    print(grouped)


print("Your program is successfully executed. Please check the running directory for freshly created csv datafiles and plots. :)")
print("Press 'e' and hit enter to exit the program.")
a = ""
while a != "e":
    a = input('').lower()
    time.sleep(5)
    
    
    
    
    