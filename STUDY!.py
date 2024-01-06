import psutil
import time


class Terminator:
    def __init__(self, App_Name):
        self.App_Name = App_Name

    def terminate(self):
        if self.App_Name is None:
                raise ValueError("App Name cannot be None")
        # Your termination logic here
        print(f"Terminating {self.App_Name}")
        curProccesses = psutil. process_iter(['pid', 'name'])
        for eachProcess in curProccesses:
            if eachProcess.info['name'] == self.App_Name:
                eachProcess.terminate()
                print(f"Terminated process with name: {self.App_Name}")
        
def main():
    # Create an instance of the Terminator class
    terminator_instance = Terminator("ExampleApp")

    # Call the terminate method
    while True:
        terminator_instance.terminate()
        time.sleep(10)
        
if __name__ == "__main__":
    main()


    