##Notes:
It is advised that one should keep copies of all the original files somewhere else before running any of these protocols to prevent file corruption in case some errors occur.  
This protocol is specific to the Lauer lab data format.  

#Steps to get raw data into excel file format:

- Run matlab_to_excel.exe program.
- Enter the location of the folder/directory where raw files are located and hit enter. 
- Example of the file name is TBI_1_day.FILE [.File format]
- Example of directory/folder name is C:\Academic\JHU\Test_for_kali
- Go to the directory/folder where the application is located. “matlab_batch.File” should be generated there. Move this file to the folder where the raw files are located.
- Use “Bulk Rename Utility” software to rename all of the files in the directory that contains raw files and the “matlab_batch file.” 
	
#Following are the steps required to perform the batch renaming.

Download and install (from the attached .exe application in the folder/shared drive or website) ‘Bulk rename Utility.’
Select the folder that contains all the files you desire to rename or change the extension by clicking on the button with folder icon on top right. You can find the folder icon on the right side of the directory bar/tab. 
Select your desired folder once the dialogue box titled ‘Browse files’ appears. 
A list of all the files should appear on the topmost box right under the folder location bar.
Select all the files in the list by pressing ‘Ctrl+A’. Left column shows the current name and extension of the file and the middle column shows the new name and extension of the files in green color.
From the ‘Extension (11)’ tab on the bottom right, select fixed from the menu. (Default might be ‘same’ instead of ‘fixed.’
On the box next to the fixed menu, type the desired file extension. 
For example,

		Current name column: TBI_1_day.FILE
New file name column: TBI_1_day.

After selecting fixed from the menu and typing ‘m’ on the box to the right, 
New file name column: TBI_1_day.m

“Move matlab_batch.m” in some other folder of your choice. 
Copy and paste “ASR_preproc.m” file to the directory/folder with freshly name changed .m data files (initially where the raw data files were located). 
Make sure the only files in the directory are raw data files with extension changed into “.m” format and the “ASR_preproc.m” file.
Go back to the folder where you moved the “matlab_batch.m” file and open this in matlab.
Change the running directory of matlab to the folder/directory where .m data files and “ASR_preproc.m” files are located. (Matlab may prompt asking if you want to change the folder or add to the path. Select “Add to the Path.”)
Hit Run button on the top of the editor page (as you would normally run any matlab script).
File named “Kalidatafuntime.xlsx” is generated in the same directory.

Steps to run habituation analysis:


Open “Kalidatafuntime.xlsx” in excel. 
Save a copy of the file in csv format by following the steps below:
File > Save as > 
Name the file as you desire.
Click on the drop down menu below the naming box and select “CSV (Comma delimited)(*.csv)” option and hit save.
Locate application “ASR_amplitude_plotter.exe” and move the freshly created CSV data file to the directory with the application.
Run the application and enter the filename on the console. (Please only enter the filename without the extension.) 
For example: Enter just “Custom_block” if the csv data file name with extension is “Custom_block.csv”
Follow the instructions on the program console window.
All of the segregated data files in .csv format and the analysis plots are generated in the same directory.


