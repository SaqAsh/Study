import psutil

class Terminator:
    def __init__(self, App_Name):
        self.App_Name = App_Name

    def terminate(self):
        # Your termination logic here
        print(f"Terminating {self.App_Name}")

def main():
    # Create an instance of the Terminator class
    terminator_instance = Terminator("ExampleApp")

    # Call the terminate method
    terminator_instance.terminate()

if __name__ == "__main__":
    main()


    