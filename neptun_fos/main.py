import datetime
import queue
import pyautogui
import json
import os
import hash




def convert_time(time: str) -> int:
    # convert time from HH:MM:SS to seconds
    time = time.split(":")
    time = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
    return time
    
    
def wait_for_time(ip: str, port: int, email: str, password: str, counter: list, que: queue.Queue, time: str) -> bool:
    sum = hash.login_queue(ip, port, email, password, counter, que)
    # convert time to seconds
    time2 = convert_time(time)
    # if time is in the past add 24 hours
    if time2 - 1 < datetime.datetime.now().hour * 3600 + datetime.datetime.now().minute * 60 + datetime.datetime.now().second:
        # wait till tomorrow
        time_till_tomorrow = 86400 - (datetime.datetime.now().hour * 3600 + datetime.datetime.now().minute * 60 + datetime.datetime.now().second)
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("waiting for tomorrow: " + time)
            print(str(time_till_tomorrow) + " seconds left...")
            sum = hash.login_queue(ip, port, email, password, counter, que)
            #exit if sum is less then 5
            if sum < 2:
                return False
            if time_till_tomorrow <= 0:
                break
            time_till_tomorrow -= 1
            pyautogui.sleep(0.9)
    # if time is in the next hour
    if time2 < datetime.datetime.now().hour * 3600 + 3600:
        # start logging in
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("waiting for time: " + time)
            print(str(time2 - (datetime.datetime.now().hour * 3600 + datetime.datetime.now().minute * 60 + datetime.datetime.now().second)) + " seconds left...")
            sum = hash.login_queue(ip, port, email, password, counter, que)
            #exit if sum is less then 5
            if sum < 2:
                return False
            # if time is in the next 4 seconds wait for it
            if time2 <= datetime.datetime.now().hour * 3600 + datetime.datetime.now().minute * 60 + datetime.datetime.now().second +4:
                while True:
                    if time2 <= datetime.datetime.now().hour * 3600 + datetime.datetime.now().minute * 60 + datetime.datetime.now().second:
                        return True
            pyautogui.sleep(0.999)

def wait_time_amount(ip: str , port: int, email: str, password: str, counter: list, que: queue.Queue, time: str) -> bool:
    # add time to current time
    time = convert_time(time)
    time = datetime.datetime.now() + datetime.timedelta(seconds=time)
    return wait_for_time(ip, port, email, password, counter, que, time.strftime("%H:%M:%S"))
    

def read_cfg() -> dict:
    # read cfg file
    try:
        # Open the file in read mode
        with open("cfg.json", "r") as file:
            # Read the contents of the file
            data = json.load(file)
        return data
    except Exception as e:
        # Handle any exceptions that might have been raised
        
        # The data you want to write to the file
        data = {
            "ip": "ligvigfui.ddns.net:7878",
            "email": "email@something.com",
            "password": "password123",
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
        return data


# read cfg file
data = read_cfg()



# define targetting mode (1 = auto, 2 = manual)
# manual x positipon
# define neptun mode (1 = in browser, 2 = separate window)
# time to start looping (hh:mm:ss)


port = 7878
counter = [0]
que = queue.Queue()

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    # chose from settings or start neptun run countdown
    print('Welcome to NeptunCRF/main menu!')
    print('Type the number of the action you want to do: ')
    print('1. Settings')
    print('2. Start the neptun run')
    print('3. Exit')
    action = input()
    if action == '1':
        settings = True
        while settings:
            os.system('cls' if os.name == 'nt' else 'clear')
            # settings
            print('NeptunCRF/settings')
            print('Type the number of the action you want to do: ')
            print('1. Change email                \t\tCurrently: ' + data["email"])
            print('2. Change password             \t\tCurrently: ' + data["password"])
            print('3. Change targetting mode      \t\tCurrently: ' + data["targetting"])
            print('4. Change x position           \t\tCurrently: ' + str(data["x_position"]))
            print('5. Change how you opened neptun\t\tCurrently: ' + data["neptun_mode"])
            print('6. Change when to start the run\t\tCurrently: ' + data["start_time"])
            print('7. How to start the run        \t\tCurrently: ' + data["start_method"])
            print('8. Save and return to main menu')
            print('9. Discard changes')
            actiona = input()
            if actiona == '1':
                # change email
                os.system('cls' if os.name == 'nt' else 'clear')
                print('NeptunCRF/settings/email')
                print('Enter your new email: \t\tCurrently: ' + data["email"])
                email = input('email: ')
                data["email"] = email
            elif actiona == '2':
                # change password
                os.system('cls' if os.name == 'nt' else 'clear')
                print('NeptunCRF/settings/password')
                print('Enter your new password: \tCurrently: ' + data["password"])
                password = input('password: ')
                data["password"] = password
            elif actiona == '3':
                # change targetting mode
                os.system('cls' if os.name == 'nt' else 'clear')
                print('NeptunCRF/settings/targetting mode')
                print('Enter your new targetting mode: \tCurrently: ' + data["targetting"])
                print('1. Auto')
                print('2. Manual')
                hihi = input()
                if hihi == '1':
                    data["targetting"] = 'auto'
                elif hihi == '2':
                    data["targetting"] = 'manual'
            elif actiona == '4':
                # change x position
                os.system('cls' if os.name == 'nt' else 'clear')
                print('NeptunCRF/settings/x position')
                input('Hover your cursor above the "Save" button and press enter')
                x_position = pyautogui.position()[0]
                data["x_position"] = x_position
            elif actiona == '5':
                # change neptun mode
                os.system('cls' if os.name == 'nt' else 'clear')
                print('NeptunCRF/settings/neptun mode')
                print('Enter your new neptun mode: \t\tCurrently: ' + data["neptun_mode"])
                print('1. In browser')
                hihi = input('2. Separate window')
                if hihi == '1':
                    data["neptun_mode"] = 'in_browser'
                elif hihi == '2':
                    data["neptun_mode"] = 'separate_windows'
            elif actiona == '6':
                # change start time
                os.system('cls' if os.name == 'nt' else 'clear')
                print('NeptunCRF/settings/start time')
                print('Enter your new start time with the format (hh:mm:ss) \t\tCurrently: ' + data["start_time"])
                data["start_time"] = input('Time: ')
            elif actiona == '7':
                # change start method
                os.system('cls' if os.name == 'nt' else 'clear')
                print('NeptunCRF/settings/start method')
                print('Enter your new start method: \t\tCurrently: ' + data["start_method"])
                print('1. At time')
                hihi = input('2. After delay')
                if hihi == '1':
                    data["start_method"] = 'at_time'
                elif hihi == '2':
                    data["start_method"] = 'after_delay'
            elif actiona == '8':
                # save settings
                # Convert the data to a JSON string
                json_string = json.dumps(data, indent=4)

                # Open the file
                with open("cfg.json", "w") as file:
                    # Write the JSON string to the file
                    file.write(json_string)
                settings = False
            elif actiona == '9':
                # discard changes
                # Open the file
                json_file = open("cfg.json", "r")
                
                data = json.load(json_file)
            else:
                input('Invalid action: ' + actiona + '\nPress a key to continue...')
    elif action == '2':
        print('NeptunCRF/start neptun run')
        if data["start_method"] == 'at_time':
            # wait for start time
            if not wait_for_time(data["ip"] , port, data["email"], data["password"] , counter, que, data["start_time"]):
                input("Failed to login multiple times")
                actiona = ""
                continue
        elif data["start_method"] == 'after_delay':
            # wait for start time
            if not wait_time_amount(data["ip"] , port, data["email"], data["password"] , counter, que, data["start_time"]):
                input("Failed to login multiple times")
                actiona = ""
                continue
            pyautogui.sleep(0.2)
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
            # Search for the color 888888 from top to bottom, starting from x=1250
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
    elif action == '3':
        command = input('Are you sure you want to exit? (y/n): ')
        if command == 'y':
            # exit
            exit()
        elif command == 'n':
            continue
    else:
        input('Invalid input: ' + action + '\nPress enter to continue...')
        continue
