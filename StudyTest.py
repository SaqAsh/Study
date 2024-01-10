import psutil
import os


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
    #user_input_time = int(input("Enter the amount of time you want to run the timer (minutes): "))

    #timer_instance = Timer()
    terminator_instance = Terminator(["FaceTime", "Spotify"])

    while True:
        # Run the timer
        #timer_instance.RunTimer(user_input_time)
        # Call the terminate method
        terminator_instance.terminate()

        # Ask the user if they want to continue
        # user_input = input("Do you want to run the timer and termination again? (y/n): ").lower()
        # if user_input != 'y':
        #     print("Exiting program.")
        #     break


if __name__ == "__main__":
    main()
