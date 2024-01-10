import psutil
import time
import os
from selenium import webdriver

def clearTerminal():
    os.system('cls' if os.name== 'nt' else 'clear')
class Timer:
    def __init__(self, App_Name_List):
        self.TimeInMinutes = None
        self.TIMERISUP = 0
        self.App_Name_List = App_Name_List
        

    def RunTimer(self, TimeInMinutes):
        self.TIMERISUP = 0
        Terminator_instance = Terminator(self.App_Name_List)
        TimeInSeconds = TimeInMinutes * 60
        for x in range(TimeInSeconds, 0, -1):
            seconds = x % 60
            minutes = int(x / 60) % 60
            hours = int(x / 3600)
            print(f"{hours:02}:{minutes:02}:{seconds:02}")
            Terminator_instance.terminate()
            time.sleep(1)
            clearTerminal()

        print("TIME IS UP")
        self.TIMERISUP = 1  # Indicates that the timer has been up

        
class UserInputAndIO:
    def __init__(self):
        self.InputList = []
        self.InputTime = None
        self.InputPassword = None
        self.InputCounter = 0
        self.File_Path = "settings.txt"
        self.TimeFlag = None
    
    def PrintFile(self,list):
        if list is not None:
             print("Settings Loaded.")
             for items in list:
                 print(items)
        print("Existing settings displayed")
    
    def ReadFile(self):
        try:
            with open(self.File_Path, "r") as file:
                lines = file.readlines()
                self.PrintFile(lines)
            print("File has sucessfully been read")
        
        except FileNotFoundError:
            print(f"The filepath {self.File_Path} does NOT EXIST")
        except Exception as e:
            print(f"An unexpected exception has occured: {e}")  
    def GetUserInput(self):
        try:
            print("WELCOME TO STUDY!")
            print("_________________")
            print("Would you like to use existing settings for your current study session?")
            print("Please note that creating new settings will wipe old settings. Would you like to continue? [Y/N]")
            charSelect = input().lower()

            if charSelect == "y":
                #since the user is using the existing settings from the settings.txt, we can have it so the input list is set 
                #to the list in the function
                self.InputList = self.ReadFile()
                #printing the existing settings:
                print("The existing settings are")
                InputListWithoutNewline = [line.strip() for line in self.InputList]
                self.PrintFile(InputListWithoutNewline)
            else:
                #first thing that we want to do is open the file and clear that shit, and then we will move onto doing the rest of the shit
                with open(self.File_Path, "w") as file:
                    pass 
                with open (self.File_Path, "w") as file:
                    #now I must run a while loop until the user is done inputting strings into the input list
                    while (True):
                         self.InputList.append(input("Enter a website or application that makes you procrastinate: "))
                         print(f"The input from the user has sucessfully been recorded: {self.InputList[self.InputCounter]}")
                         self.InputCounter +=1
                         charInput = input("Would you like to add another app? [Y/N]").lower()
                         if (charInput == 'y'):
                             continue
                         else: break
                    for item in self.InputList:
                        file.write(str(item)+"\n")
                self.GetUserTimeInput()
                #now we must run an instance of the timer class 
                Timer_instance = Timer(self.InputList)
                Timer_instance.RunTimer(self.InputTime)
                self.TimeFlag = True
                    
        except ValueError as e:
            print(f"Error in getting user input: {e}")

    def GetUserTimeInput(self):
        try:
            self.InputTime = int(input("Enter the amount of time you want to study for (minutes): "))
            print(f"Goal time successfully stored: {self.InputTime}")
        except ValueError as e:
            print(f"Error in getting user input: {e}")
    

    def GetUserPassword(self):
        try:
            self.InputPassword = int(input("Enter the password to exit out of the study period: "))
            print(f"Password Successfully Stored: {self.InputPassword}")
        except ValueError as e:
            print(f"Error in getting user input: {e}")
    def PasswordVerification(self):
        
         exit()

class Terminator:
    def __init__(self, App_Name_List):
        self.App_Name_List = App_Name_List
        self.ProgramCounter = 0

    def terminate(self):
        if self.App_Name_List is None:
            raise ValueError("App Name List cannot be None")
        cur_processes = psutil.process_iter(['pid', 'name'])
        for each_process in cur_processes:
            for each_item in self.App_Name_List:
                
                # I added the lower function for a reason, if my pythonscript stops working this might be a reason why!
                if each_process.info.get('name').lower() == each_item.lower():
                    try:
                        # Check if the process is running before attempting to terminate
                        if psutil.pid_exists(each_process.info['pid']):
                            each_process.terminate()
                            self.ProgramCounter += 1
                            print(f"Terminated process with name: {each_item}")
                        else:
                            print(f"Process with name {each_item} not found.")
                    except psutil.NoSuchProcess as e:
                            print(f"Error terminating process: {e}")
    def terminateTabs(self):
        # if self.App_Name_List is None:
        #     raise ValueError("App Name List Cannot be None")
        # # now we will be making a variable that stores the list of tabs that are apart of the tabs
        # Chrome_instance = webdriver.Chrome()
        # Website_list = Chrome_instance.window_handles
        # for tabs in Website_list:
        #     #get the name of the tab that you are on.
        #     current_tab = tabs.title()
        #     for Apps in self.App_Name_List:
        #         if Apps.lower() == current_tab.lower():
        #             Chrome_instance.switch_to(tabs)
        #             self.ProgramCounter+=1
        #             Chrome_instance.close()
        #             print(f"Terminating process with name: {tabs}")
                    
                

def main():
    User = UserInputAndIO()
    while True:
        User.GetUserInput()
        if User.TimeFlag is True:
            break 
            
       

if __name__ == "__main__":
    main()
