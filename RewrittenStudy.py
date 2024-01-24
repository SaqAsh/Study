#_______________________________________________
# Author: Saqib Ashraf
# Date: January 17th 2024
# Purpose: To stop students from procrasinating
#_______________________________________________
import psutil
from selenium import webdriver
import tkinter as tk
from tkinter import messagebox
from tkinter import font
import customtkinter as ctk
import time
filepath = "settings.txt"
#Purpose: To handle the termination of apps
#TO-DO: To make terminator for terminating tabs that user opens
#___________________________________________________________________________________________________________________________________
class Terminator:
    def __init__(self, listInput):
        self.listInput = listInput
        self.intTerminationCounter = 0 #this is how many times apps got terminated, 
        #this will allow for user to know how foucsed they were during the study session
    
    #this function is used to terminate apps
    def terminateApps(self):
        if self.listInput is None:
            raise ValueError("List cannot be NONE")
        list_cur_processes = psutil.process_iter(['pid','name'])
        for each_process in list_cur_processes:
            for each_item in self.listInput:
                
                # I added the lower function for a reason, if my pythonscript stops working this might be a reason why!
                if each_process.info.get('name').lower() == each_item.lower():
                    try:
                        # Check if the process is running before attempting to terminate
                        if psutil.pid_exists(each_process.info['pid']):
                            each_process.terminate()
                            self.intTerminationCounter += 1
                            print(f"Terminated process with name: {each_item}")
                        else:
                            print(f"Process with name {each_item} not found.")
                    except psutil.NoSuchProcess as e:
                            print(f"Error terminating process: {e}")

    #implement the tab termination code in order to run selenium based tab terminator       
    #def terminateTabs(self):
#______________________________________________________________________________________________________________________________________   

#______________________________________________________________________________________________________________________________________
class Graphics:

    def __init__(self, root):
        self.File_Path = "settings.txt"
        self.elapsed_time =0
        #sets the background and appearance initialization
        #_____________________________________
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.root = root 
        root.geometry("720x720")
        root.title("Welcome To STUDY!")
        #_____________________________________

        #custom fonts
        #_______________________________________________________________________________________________
        self.customTitle = ctk.CTkFont( size=90, underline = False)
        self.customBody = ctk.CTkFont( size = 40)
        self.customBodyU = ctk.CTkFont( size = 18, underline = False)
        self.customBodySmall = ctk.CTkFont(family = "Courier New", size = 12)
        #_______________________________________________________________________________________________
        # Formatting the Tabs
        #______________________________________________________________________________________________________________________
        tabview = ctk.CTkTabview(master = root, width = 720, height = 800)
        tabview.pack()
        tab_1 = tabview.add("                                       Termination                                       ")
        tab_2 = tabview.add("                                        Progress                                        ")
        #______________________________________________________________________________________________________________________

        #Items in tab #1
        #______________________________________________________________________________________________________________________
        #label for termination
        self.label = ctk.CTkLabel(master=tab_1, text="Enter Apps To Terminate:", font=self.customBodyU, padx=10, pady=15)
        self.label.grid(row=0, column=0, sticky="w")

        # Entry widget for app termination
        self.entry = ctk.CTkEntry(master=tab_1, width=317)
        self.entry.grid(row=0, column=1, sticky="ew", padx=5)

        # Button to save to file
        self.writeFileButton = ctk.CTkButton(master=tab_1, text="Save File")
        self.writeFileButton.grid(row=0, column=2, padx=5, sticky="w")

        #label to show the existing settings
        self.label2 = ctk.CTkLabel(master=tab_1, text="Existing Settings:", font=self.customBodyU, padx=10, pady=0)
        self.label2.grid(row=1, column=0, sticky="w")

        #the scrolling textboox that will be getting all the input from the file and adding to it
        self.scroll_text_ = ctk.CTkTextbox(master= tab_1, activate_scrollbars=True, width=675, height = 500)
        self.scroll_text_.grid(row = 2, column = 0, columnspan = 3)

        #this clears all the information from the files
        self.clear = ctk.CTkButton(master=tab_1, text="Clear Settings", width=300, font = self.customBody)
        self.clear.grid(row=20, column=1, padx=10, sticky="w")


        # Configure row weights for vertical spacing
        for i in range(20):
            tab_1.grid_rowconfigure(i, weight=1)
  
      

        #______________________________________________________________________________________________________________________

        #Items in tab #2
        #______________________________________________________________________________________________________________________
        self.label2 = ctk.CTkLabel(master=tab_2, text="Enter a study time (minutes):", font=self.customBodyU, padx=10, pady=15 )
        self.label2.grid(row=0, column=0, sticky = 'w')

        # Entry widget for study time
        self.entry2 = ctk.CTkEntry(master=tab_2, width=300)
        self.entry2.grid(row=0, column=1)

        self.writeFileButton1 = ctk.CTkButton(master=tab_2, text="Save Time")
        self.writeFileButton1.grid(row=0, column=2, padx = 5)

        # Label for displaying time
        self.time_label = ctk.CTkLabel(master=tab_2, text="00:00:00", font=self.customTitle, padx=20, pady=20)
        self.time_label.grid(row=19, column=0, columnspan=3)
        
        #Termination Log Label
        self.label3 = ctk.CTkLabel(master=tab_2, text="Termination Log:", font=self.customBodyU, padx=10, pady=15)
        self.label3.grid(row=1, column=0, sticky="w")

        # Start button
        self.start_button = ctk.CTkButton(master=tab_2, text="Start STUDY!", font=self.customBody, width=330, command=self.start_time)
        self.start_button.grid(row=20, column=0, columnspan=3, pady = 20)

        self.scroll_text = ctk.CTkTextbox(master= tab_2, activate_scrollbars=True, width=675, height = 350)
        self.scroll_text.grid(row = 3, column = 0, columnspan = 3)

        # Configure the columns and rows for centering
        for i in range(20):
            tab_2.grid_rowconfigure(i, weight=1)


    def start_time(self):
        self.update_clock()
    def terminateEvent(self):
        while True:
            terminateProcess = self.entry.get().split(",")
            terminator = Terminator(terminateProcess)
            terminator.terminateApps()
    def Writefile(self):
        input_text = self.entry.get()  # Get the text from the entry widget
        try:
            with open(self.File_Path, "w") as file:  # Open the file in write mode
                file.write(input_text)  # Write the input text to the file
            messagebox.showinfo("Success", "Input saved to file successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    #clock code generated by gpt4
    def update_clock(self):
        hours, remainder = divmod(self.elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"
        
        self.time_label.configure(text=formatted_time)
        self.elapsed_time += 1  # Increment the timer
        self.root.after(1000, self.update_clock)





def main():
    root = ctk.CTk()
    app = Graphics(root)
    root.mainloop()

if __name__ == "__main__":
    main()
                            
                            
                            

        
        

