from selenium import webdriver
import time

# Replace this list with the names of the apps you want to terminate
app_name_list = ["Spotify", "Discord", "Youtube"]

# Create a single instance of Chrome
chrome_instance = webdriver.Chrome()

while True:
    for app_name in app_name_list:
        app_found = False

        # Get the handles of all open tabs
        website_list = chrome_instance.window_handles

        for tab_handle in website_list:
            # Switch to the tab
            # Get the title of the current tab
            current_tab_title = chrome_instance.title
            if app_name.lower() == current_tab_title.lower():
                chrome_instance.switch_to.window(tab_handle)
                app_found = True
                # Close the tab directly without switching to it
                chrome_instance.execute_script(f"window.close();")
                print(f"Terminating process with name: {current_tab_title}")

        if not app_found:
            print(f"{app_name} is not open.")

    # Add a 2-second delay before the next iteration
    time.sleep(2)  # Sleep for 2 seconds
