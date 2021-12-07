import mean_of_subjects as ms
import matplotlib.pyplot as plt
import pandas as pd

filelocation = input("Enter file location: ")
desired_filename = input("Enter desired filename : ")
paradigm = input("Enter the name of paradigm: ")
number_of_block = int(input("Enter the number of the blocks present in your dataset: "))

# filelocation = "C:\\Users\\duwad\\OneDrive - NJIT\\Academic\\JHU\\Sham and TBI\\MAT Files Shams\\sham csv\\3_days_in_noise"
# desired_filename = "testfile"
# paradigm = "3_days_in_noise"
# number_of_block = 5

combined = ms.operation(filelocation)
grouped = combined.sort_values(['Block number','dB'])
grouped.to_csv(desired_filename  +  '.csv' , index = False)

list_of_df = []

for i in range(1,number_of_block+1):
    df = grouped[grouped['Block number'] == i]
    list_of_df.append(df)             
    
list_of_means = []

for j in list_of_df: 
    A = j.groupby(['dB']).mean()
    B = j.groupby(['dB']).sem()
    A['SE'] = B['ASR val']
    list_of_means.append(A)
    
    
print(list_of_means)    

combined_means = pd.concat(list_of_means)

print(combined_means)

D = combined_means.sort_values(['dB'])
print(D)


index_1 = 0 #first row
index_2  = number_of_block
index_3 = 1 #dB column
index_4 = 3 # SE column

list_of_plottable = [ ]

for j in range(1,number_of_block+1):
    plotting_x = D.iloc[index_1:index_2,index_3:index_4]
    index_1 += number_of_block
    index_2 += number_of_block
    list_of_plottable.append(plotting_x)
print(list_of_plottable)

a = [i for i in range(1,number_of_block+1)]
x = (list(map(str, a)))
print(x)

intensities = ["70 dB SPL",'80 dB SPL','90 dB SPL','100 dB SPL','105 dB SPL'] #can be changed depending on user's need
colors = ['b','r','g','c','m'] #can be changed depending on user's need
ylimit = 1.5 #can be changed depending on user's need

for k in range(0,number_of_block):
    plt.plot(x,list_of_plottable[k]['ASR val'], color = colors[k], label = intensities[k])
    plt.errorbar(x,list_of_plottable[k]['ASR val'],yerr = list_of_plottable[k]['SE'] ,fmt =colors[k]+'o',capsize =5, ecolor = colors[k])
    plt.legend()
    plt.grid()
    plt.ylim([0 , ylimit])
    plt.xlabel("Trial block number")
    plt.ylabel("ASR amplitude in mV")
    plt.title("Average ASR across all subjects for " + paradigm)
    plt.savefig("Average ASR across all subjects for " + paradigm +".jpg")








