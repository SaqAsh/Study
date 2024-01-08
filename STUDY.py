import psutil
import time

class UserInputAndIO:
    def __init__(self):
        self.InputList = []
        self.InputTime = None
        self.InputPassword = None
        self.InputCounter = 0

    def GetUserInput(self):
        try:
            print("WELCOME TO STUDY!")
            print("_________________")
            print("Would you like to use existing settings for your current study session?")
            print("Please note that creating new settings will wipe old settings. Would you like to continue? [Y/N]")
            charSelect = input().lower()

            if charSelect == "n":
                # Read settings from file
                with open("settings.txt", "r") as file:
                    lines = file.readlines()
                    self.InputList = lines[0].strip().split(',')
                    self.InputTime = float(lines[1].strip())
                    self.InputPassword = int(lines[2].strip())
                    self.InputCounter = len(self.InputList.split(','))
                    print("Existing settings loaded.")
            else:
                # Append new settings without overwriting existing ones
                with open("settings.txt", "a") as file:
                    while True:
                        self.InputList.append(input("Enter a program that makes you procrastinate: "))
                        print(f"Input from the user has successfully been recorded: {self.InputList[-1]}")
                        charInput = input("Would you like to add another app? [Y/N]").lower()
                        self.InputCounter += 1
                        print(f"The number of apps that you have currently scheduled to terminate: {self.InputCounter}")
                        if charInput != "y":
                            break

                    # Save new settings to file
                    file.write(','.join(self.InputList) + '\n')
                    file.write(str(self.InputTime) + '\n')
                    file.write(str(self.InputPassword) + '\n')

        except ValueError as e:
            print(f"Error in getting user input: {e}")

    def GetUserTimeInput(self):
        try:
            self.InputTime = float(input("Enter the amount of time you want to study for (minutes): "))
            print(f"Goal time successfully stored: {self.InputTime}")
        except ValueError as e:
            print(f"Error in getting user input: {e}")

    def GetUserPassword(self):
        try:
            self.InputPassword = int(input("Enter the password to exit out of the study period: "))
            print(f"Password Successfully Stored: {self.InputPassword}")
        except ValueError as e:
            print(f"Error in getting user input: {e}")

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
                if each_process.info.get('name') == each_item:
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

def main():
    # Create an instance of the UserInputAndIO class
    user_instance = UserInputAndIO()
    user_instance.GetUserInput()
    user_instance.GetUserTimeInput()
    user_instance.GetUserPassword()

    # Create an instance of the Terminator class
    terminator_instance = Terminator(user_instance.InputList)

    # Call the terminate method
    while True:
        terminator_instance.terminate()
        time.sleep(10)

if __name__ == "__main__":
    main()
