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
    #def terminateTabs(self)
#______________________________________________________________________________________________________________________________________   
                            
class Graphics:

    def __init__(self, root):

        #sets the background and appearance
        #_____________________________________
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.root = root 
        root.geometry("720x720")
        root.title("Welcome To STUDY!")
        #_____________________________________
        
        #these are the custom fonts that I made for tkinter, they are not used anymore, will delete soon
        #_______________________________________________________________________________________________
        self.customTitle = ctk.CTkFont( size=60, underline = True)
        self.customBody = ctk.CTkFont( size = 18)
        self.customBodySmall = ctk.CTkFont(family = "Courier New", size = 12)
        #_______________________________________________________________________________________________
        
        #Title
        #______________________________________________________________________________________________________________________
        # self.MainTitle = ctk.CTkLabel(master = root, text = "Welcome To STUDY!",font = self.customTitle, padx = 20, pady = 20)
        # self.MainTitle.pack()
        #______________________________________________________________________________________________________________________

        # Formatting the Tabs
        #______________________________________________________________________________________________________________________
        tabview = ctk.CTkTabview(master = root, width = 720, height = 800)
        tabview.pack()
        tab_1 = tabview.add("                                 tab 1                                 ")
        tab_2 = tabview.add("                                 tab 2                                ")
        tab_3 = tabview.add("                                 tab 3                                 ")

        #______________________________________________________________________________________________________________________

        #Items in tab #1
        #______________________________________________________________________________________________________________________
        self.label = ctk.CTkLabel(master = tab_1, text= "Enter Apps To Terminate:", font = self.customBody, padx = 10, pady = 15)
        self.label.grid(row=0, column=0, sticky="w")
        self.entry = ctk.CTkEntry(master =tab_1, width = 475)
        self.entry.grid(row=0, column=1)


        #______________________________________________________________________________________________________________________

        #Items in tab #2
        #______________________________________________________________________________________________________________________



        #______________________________________________________________________________________________________________________

        #Items in tab #3
        #______________________________________________________________________________________________________________________



        #______________________________________________________________________________________________________________________


        # self.entry = ctk.CTkEntry(master =root, width = 50)
        # self.entry.pack()

        # self.terminationButton = ctk.CTkButton(master = root, text = "Terminate Processes", command=self.terminateEvent)
        # self.terminationButton.pack()

    def terminateEvent(self):
        while True:
            terminateProcess = self.entry.get().split(",")
            terminator = Terminator(terminateProcess)
            terminator.terminateApps()
            #messagebox.showinfo("Termination Complete", f"Terminated {terminator.intTerminationCounter} processes.")


def main():
    root = ctk.CTk()
    app = Graphics(root)
    root.mainloop()

if __name__ == "__main__":
    main()
                            
                            
                            

        
        

