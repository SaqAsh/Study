import psutil
import time

class UserInput:
    def __init__(self, InputString):
        self.InputString = InputString
    def GetUserInput(self):
        try:
            self.InputString = input()
            print(f"Input from user has successfully been recorded {self.InputString}")
        except ValueError as e:
            print (f"Error in getting userinput:{e}")
        

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
    terminator_instance = Terminator(user_instance.GetUserInput)
    terminator_instance2 = Terminator("FaceTime")

    # Call the terminate method
    while True:
        terminator_instance.terminate()
        terminator_instance2.terminate()
        time.sleep(10)


if __name__ == "__main__":
    main()
