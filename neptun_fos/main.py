import datetime
import pyautogui
import json
import os




    


# read cfg file
try:
    # Open the file in read mode
    with open("cfg.json", "r") as file:
        # Read the contents of the file
        data = json.load(file)
except Exception as e:
    # Handle any exceptions that might have been raised
    
    # The data you want to write to the file
    data = {
        "credentials": "username:password",
        "targetting": "auto",
        "x_position": 1240,
        "neptun_mode": "separate_windows",
        "start_time": "00:00:02",
        "start_method": "after_delay"
    }

    # Convert the data to a JSON string
    json_string = json.dumps(data, indent=4)

    # Open the file
    with open("cfg.json", "w") as file:
        # Write the JSON string to the file
        file.write(json_string)




# define targetting mode (1 = auto, 2 = manual)
# manual x positipon
# define neptun mode (1 = in browser, 2 = separate window)
# time to start looping (hh:mm:ss)





while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    # chose from settings or start neptun run countdown
    print('Welcome to Neptun FOS/main menu!')
    print('Type the number of the action you want to do: ')
    print('1. Settings')
    action = input('2. Start the neptun run')
    if action == '1':
        settings = True
        while settings:
            os.system('cls' if os.name == 'nt' else 'clear')
            # settings
            print('Neptun FOS/settings')
            print('Type the number of the action you want to do: ')
            print('1. Change credentials          \t\tCurrently: ' + data["credentials"])
            print('2. Change targetting mode      \t\tCurrently: ' + data["targetting"])
            print('3. Change x position           \t\tCurrently: ' + str(data["x_position"]))
            print('4. Change how you opened neptun\t\tCurrently: ' + data["neptun_mode"])
            print('5. Change when to start the run\t\tCurrently: ' + data["start_time"])
            print('6. How to start the run        \t\tCurrently: ' + data["start_method"])
            actiona = input('7. Save and return to main menu')
            if actiona == '1':
                # change credentials
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Neptun FOS/settings/credentials')
                print('Enter your new credentials: \t\tCurrently: ' + data["credentials"])
                username = input('Username: ')
                password = input('Password: ')
                data["credentials"] = username + ':' + password
            elif actiona == '2':
                # change targetting mode
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Neptun FOS/settings/targetting mode')
                print('Enter your new targetting mode: \tCurrently: ' + data["targetting"])
                print('1. Auto')
                hihi = input('2. Manual')
                if hihi == '1':
                    data["targetting"] = 'auto'
                elif hihi == '2':
                    data["targetting"] = 'manual'
            elif actiona == '3':
                # change x position
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Neptun FOS/settings/x position')
                input('Hover your cursor above the "Save" button and press enter')
                x_position = pyautogui.position()[0]
                data["x_position"] = x_position
            elif actiona == '4':
                # change neptun mode
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Neptun FOS/settings/neptun mode')
                print('Enter your new neptun mode: \t\tCurrently: ' + data["neptun_mode"])
                print('1. In browser')
                hihi = input('2. Separate window')
                if hihi == '1':
                    data["neptun_mode"] = 'in_browser'
                elif hihi == '2':
                    data["neptun_mode"] = 'separate_windows'
            elif actiona == '5':
                # change start time
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Neptun FOS/settings/start time')
                print('Enter your new start time with the format (hh:mm:ss) \t\tCurrently: ' + data["start_time"])
                data["start_time"] = input('Time: ')
            elif actiona == '6':
                # change start method
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Neptun FOS/settings/start method')
                print('Enter your new start method: \t\tCurrently: ' + data["start_method"])
                print('1. At time')
                hihi = input('2. After delay')
                if hihi == '1':
                    data["start_method"] = 'at_time'
                elif hihi == '2':
                    data["start_method"] = 'after_delay'
            elif actiona == '7':
                # save settings
                # Convert the data to a JSON string
                json_string = json.dumps(data, indent=4)

                # Open the file
                with open("cfg.json", "w") as file:
                    # Write the JSON string to the file
                    file.write(json_string)
                settings = False
            else:
                input('Invalid action: ' + actiona + '\nPress enter to continue...')
    elif action == '2':
        print('Neptun FOS/start neptun run')
        if data["start_method"] == 'at_time':
            # wait for start time
            print('Waiting for start time...')
            while True:
                if datetime.datetime.now().strftime("%H:%M:%S") >= data["start_time"]:
                    pyautogui.sleep(0.1)
                    break
        elif data["start_method"] == 'after_delay':
            # convert data["start_time"] to seconds
            delay = int(data["start_time"][0:2]) * 3600 + int(data["start_time"][3:5]) * 60 + int(data["start_time"][6:8])
            # wait for delay
            print('Waiting for delay: ' + str(delay) + ' seconds')
            for second in range(delay):
                os.system('cls' if os.name == 'nt' else 'clear')
                print(str(delay - second) + ' seconds left')
                pyautogui.sleep(1)
            pyautogui.sleep(0.1)
        runing = True
        found_neptuns = 0
        if data["targetting"] == 'manual':
            x_position = data["x_position"]
        elif data["targetting"] == 'auto':
            x_position = 1240
        else:
            input('Invalid targetting mode: ' + data["targetting"])
            runing = False
        while runing:
            steak = 0
            found = False
            screenshot = pyautogui.screenshot()
            # Search for the color FFFFFF from top to bottom, starting from x=1250
            for y in range(screenshot.size[1]):
                if screenshot.getpixel((x_position, y)) == (128, 128, 128):
                    steak = steak + 1
                else:
                    steak = 0
                if steak == 5:    
                    pyautogui.click(x_position, y+5)
                    pyautogui.moveTo(10,10)
                    if data["neptun_mode"] == 'separate_windows':
                        print('Switching to next desktop window')
                        pyautogui.hotkey('ctrl', 'win', 'right')
                    elif data["neptun_mode"] == 'in_browser':
                        print('Switching to next tab')
                        pyautogui.hotkey('ctrl', 'tab')
                    print('Found the color at y = ' + str(y+5))
                    found = True
                    break
            print('Broke out of loop: found: ' + str(found))
            runing = False
            if found:
                found_neptuns = found_neptuns + 1
                runing = True
        input('Found ' + str(found_neptuns) + ' neptuns')
    else:
        input('Invalid input: ' + action + '\nPress enter to continue...')
        continue


while False:
    # settings

    # take user input to a variable
    delay = input('Enter the delay in seconds: ')
    # convert the string to an integer
    delay = int(delay)

    # write code that waits 2 seconds
    print('Waiting ' + str(delay) + ' seconds...')
    pyautogui.sleep(delay)

    print('Taking screenshot now!')
    # Take a screenshot of the entire screen


    runing = True
    while runing:
        steak = 0
        found = False
        screenshot = pyautogui.screenshot()
        # Search for the color FFFFFF from top to bottom, starting from x=1250
        for y in range(screenshot.size[1]):
            if screenshot.getpixel((1240, y)) == (128, 128, 128):
                steak = steak + 1
            else:
                steak = 0
            if steak == 5:    
                pyautogui.click(1240, y+5)
                pyautogui.moveTo(10,10)
                if data("neptun_mode") == 'separate_window':
                    pyautogui.hotkey('ctrl', 'tab')
                elif data("neptun_mode") == 'in_browser':
                    pyautogui.hotkey('ctrl', 'win', 'right')
                print('Found the color at y = ' + str(y+5))
                found = True
                break
        print('Broke out of loop: found: ' + str(found))
        runing = False
        if found:
            runing = True
