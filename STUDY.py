import psutil
import time


#this is the class for the timer, on how long the user will be 

#class Timer




# this is the class for the basic user input for what program they want termianted, expand on the user input class at a later date
# add a function to start the timer, and how many hours you want to study for, this is the end time for this program, once this timer has eneded, that is where the 
class UserInput:
    def __init__(self):
        self.InputString = None
        self.InputTime = None
        self.InputPassword = None
    def GetUserInput(self):
        try:
            self.InputString = input("Enter a program that makes you procrasinate!")
            print(f"Input from user has successfully been recorded {self.InputString}")
        except ValueError as e:
            print (f"Error in getting user input:{e}")
    def GetUserTimeInput(self):
        try:
            self.InputTime = float(input("Enter the amount of time you want to study for"))
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
    def __init__(self, App_Name):
        self.App_Name = App_Name

    def terminate(self):
        if self.App_Name is None:
            raise ValueError("App Name cannot be None")
        cur_processes = psutil.process_iter(['pid', 'name'])
        for each_process in cur_processes:
            if each_process.info.get('name') == self.App_Name:
                try:
                    # Check if the process is running before attempting to terminate
                    if psutil.pid_exists(each_process.info['pid']):
                        each_process.terminate()
                        print(f"Terminated process with name: {self.App_Name}")
                    else:
                        print(f"Process with name {self.App_Name} not found.")
                except psutil.NoSuchProcess as e:
                    print(f"Error terminating process: {e}")


def main():
    # Create an instance of the Terminator class
    user_instance = UserInput
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
