import psutil
import time


#this is the class for the timer, on how long the user will be 

#class Timer

# this is the class for the basic user input for what program they want termianted, expand on the user input class at a later date
class UserInputAndIO:
    def __init__(self):
        self.InputString = None
        self.InputTime = None
        self.InputPassword = None
        self.InputCounter = 0
    def GetUserInput(self):
        try:
            if (self.InputCounter <1):
                print("WELCOME TO STUDY!")
                print("_________________")
                print("Would you like to use existing settings for your current study session")
                print("Please note that creating new settings will wipe old settings, would you like to continue? [Y/N]")
                charSelect = input()
                charSelect = charSelect.lower()
                # I want this to be the cross roads, if the user presses yes then there is a new bit of information created, if the user 
                #does not press yes, then it reads shit from the file
                
                self.InputString = input("Enter a program that makes you procrasinate!")
                print(f"Input from user has successfully been recorded {self.InputString}")
                charInput = input("Would you like to add another app?! [Y/N]")
                charInput = charInput.lower() #allows it so no matter what the userinputs, the reading of the string will be the same
                self.InputCounter +=1
                print(f"The number of apps that you have currently schedculed to terminate{self.InputCounter}")
                self.GetUserInput() if charInput == "y" else None 
        except ValueError as e:
            print (f"Error in getting user input:{e}")
    def GetUserTimeInput(self):
        try:
            self.InputTime = float(input("Enter the amount of time you want to study for (minutes)"))
            print(f"Goal time successfully stored {self.InputTime}")
        except ValueError as e:
            print(f"Error in getting user input: {e}")
    def GetUserPassword(self):
        try:
            self.InputPassword = int(input("Enter the password to exit out of study period"))
            print(f"Password Successfully Stored: {self.InputPassword}")
        except ValueError as e:
            print(f"Error in getting user input: {e}")
            
class Terminator:
    def __init__(self, App_Name_List):
        self.App_Name_List = App_Name_List
        self.ProgramCounter = -1

    def terminate(self):
        if self.App_Name is None:
            raise ValueError("App Name cannot be None")
        cur_processes = psutil.process_iter(['pid', 'name'])
        for each_process in cur_processes:
            for each_item in self.App_Name_List:
                if each_process.info.get('name') == each_item:
                    try:
                        # Check if the process is running before attempting to terminate
                        if psutil.pid_exists(each_process.info['pid']):
                            each_process.terminate()
                            ProgramCounter+=1 # this is the counter that tracks how many times the user tries to log back onto something to procrasinate
                            print(f"Terminated process with name: {self.App_Name}")
                        else:
                            print(f"Process with name {self.App_Name} not found.")
                    except psutil.NoSuchProcess as e:
                        print(f"Error terminating process: {e}")


def main():
    # Create an instance of the Terminator class
    user_instance = UserInputAndIO
    Input = user_instance.GetUserInput()
    terminator_instance = Terminator(Input)
    terminator_instance2 = Terminator("FaceTime")

    # Call the terminate method
    while True:
        terminator_instance.terminate()
        terminator_instance2.terminate()
        time.sleep(10)


if __name__ == "__main__":
    main()
