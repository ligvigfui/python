import datetime
import queue
import re
import pyautogui
import json
import os
import hash
import do_stuff

version = '0.3.0'

def auto_targetting_fix(data):
    if data["targetting"] == "auto":
        if data["course_or_exam"] == "exam":
            data["x_position"] = 1770
        elif data["course_or_exam"] == "course":
            data["x_position"] = 1240

def dark_gray_background(string: str) -> str:
    return '\033[100m' + string + '\033[0m'
def print_light(string: str):
    print(dark_gray_background(string))


def convert_time(time: str) -> int:
    # convert time from HH:MM:SS to seconds
    time = time.split(":")
    time = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
    return time
    
def now() -> str:
    # return current time in HH:MM:SS
    return datetime.datetime.now().strftime("%H:%M:%S")
    
def wait_for_time(ip: str, port: int, email: str, password: str, counter: list, que: queue.Queue, time: str) -> bool:
    sum = hash.login_queue(ip, port, email, password, counter, que)
    # convert time to seconds
    time2 = convert_time(time)
    # if time is tomorrow wait until tomorrow
    if time2 + 1 < datetime.datetime.now().hour * 3600 + datetime.datetime.now().minute * 60 + datetime.datetime.now().second:
        time_till_tomorrow = 86400 - (datetime.datetime.now().hour * 3600 + datetime.datetime.now().minute * 60 + datetime.datetime.now().second)
        count = 0
        while count < time_till_tomorrow:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("waiting for tomorrow: " + time + " will start at " + time)
            print(str(time_till_tomorrow - count) + " seconds left...")
            count += 1
            pyautogui.sleep(1)
    while True:
        # if time is in the next hour
        if time2 > convert_time(now()) and time2 < convert_time(now()) + 3600:
            # start logging in
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("waiting for time: " + time)
                print(str(time2 - convert_time(now())) + " seconds left...")
                #exit if sum is less then 5
                sum = hash.login_queue(ip, port, email, password, counter, que)
                if sum < 2:
                    return False
                # if time is in the next 4 seconds wait for it
                if time2 <= convert_time(now()) + 4:
                    while True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("waiting for time: " + time)
                        print(str(time2 - convert_time(now())) + " seconds left...")
                        if time2 <= convert_time(now()):
                            if not data["email"] == "ligvigfui@gmail.com":
                                print("starting...")
                                pyautogui.sleep(0.2)
                            return True
                pyautogui.sleep(0.999)
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
        # if data["port"] does not exist, add it 
        if not "port" in data:
            data["port"] = 80
        return data
    except Exception as e:
        # Handle any exceptions that might have been raised
        
        # The data you want to write to the file
        data = {
            "ip": "neptuncrf.freeddns.org",
            "port": 80,
            "email": "email@something.com",
            "password": "password123",
            "targetting": "auto",
            "x_position": 1240,
            "neptun_mode": "separate_windows",
            "start_time": "00:00:02",
            "start_method": "after_delay",
            "course_or_exam": "exam"
        }

        # Convert the data to a JSON string
        json_string = json.dumps(data, indent=4)

        # Open the file
        with open("cfg.json", "w") as file:
            # Write the JSON string to the file
            file.write(json_string)
        return data
    
def settings(data):
    settings = True
    while settings:
        os.system('cls' if os.name == 'nt' else 'clear')
        # settings
        print('NeptunCRF/settings')
        print('Type the number of the action you want to do: ')
        print('0. Change what you want to do  \t\tCurrently: ' + data["course_or_exam"])
        print_light('1. Change email                \t\tCurrently: ' + data["email"])
        print('2. Change password             \t\tCurrently: ' + data["password"])
        print_light('3. Change targetting mode      \t\tCurrently: ' + data["targetting"])
        print('4. Change x position           \t\tCurrently: ' + str(data["x_position"]))
        print_light('5. Change how you opened neptun\t\tCurrently: ' + data["neptun_mode"])
        print('6. Change when to start the run\t\tCurrently: ' + data["start_time"])
        print_light('7. How to start the run        \t\tCurrently: ' + data["start_method"])
        print('8. Save and return to main menu')
        print_light('9. Discard changes')
        actiona = input()
        if actiona == '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('NeptunCRF/settings/course_or_exam')
            print('Enter what you want the program to do: ')
            print('1. Course registration')
            print('2. Exam registration')
            what_to_do = input()
            if what_to_do == '1':
                data["course_or_exam"] = "course"
            elif what_to_do == '2':
                data["course_or_exam"] = "exam"
            else:
                input('Invalid input!\nPress a key to continue...')
                continue
        elif actiona == '1':
            # change email
            os.system('cls' if os.name == 'nt' else 'clear')
            print('NeptunCRF/settings/email')
            print('Enter your new email: \t\tCurrently: ' + data["email"])
            email = input('email: ')
            if email.find('@') == -1:
                input('Invalid email!\nPress a key to continue...')
                continue
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
            input('Hover your cursor above the desired button and press enter')
            x_position = pyautogui.position()[0]
            data["x_position"] = x_position
        elif actiona == '5':
            # change neptun mode
            os.system('cls' if os.name == 'nt' else 'clear')
            print('NeptunCRF/settings/neptun mode')
            print('Enter your new neptun mode: \t\tCurrently: ' + data["neptun_mode"])
            print('1. In browser')
            print('2. Separate window')
            hihi = input()
            if hihi == '1':
                data["neptun_mode"] = 'in_browser'
            elif hihi == '2':
                data["neptun_mode"] = 'separate_windows'
        elif actiona == '6':
            # change start time
            os.system('cls' if os.name == 'nt' else 'clear')
            print('NeptunCRF/settings/start time')
            print('Enter your new start time with the format (hh:mm:ss) \t\tCurrently: ' + data["start_time"])
            print('Time:') 
            time = input()
            # Check if the user input matches the pattern
            if not re.match(pattern, time):
                input("Invalid time format!\nPress a key to continue...")
                continue
            data["start_time"] = time
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
            auto_targetting_fix(data)
            settings = False
        elif actiona == '9':
            # discard changes
            # Open the file
            json_file = open("cfg.json", "r")
            
            data = json.load(json_file)
        else:
            input('Invalid action: ' + actiona + '\nPress a key to continue...')
    
    
    


# read cfg file
data = read_cfg()
auto_targetting_fix(data)

# Define the regular expression pattern
pattern = r'^\d{2}:\d{2}:\d{2}$'



# define targetting mode (1 = auto, 2 = manual)
# manual x positipon
# define neptun mode (1 = in browser, 2 = separate window)
# time to start looping (hh:mm:ss)


counter = [0]
que = queue.Queue()

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    # chose from settings or start neptun run countdown
    print('Welcome to NeptunCRF/main menu! Version: ' + version)
    print('Type the number of the action you want to do: ')
    print('1. Settings')
    print('2. Start the neptun run')
    print('3. Exit')
    action = input()
    if action == '1':
        settings(data)
    elif action == '2':
        print('NeptunCRF/start neptun run')
        if data["start_method"] == 'at_time':
            # wait for start time
            if not wait_for_time(data["ip"] , data["port"], data["email"], data["password"] , counter, que, data["start_time"]):
                input("Failed to login multiple times")
                continue
        elif data["start_method"] == 'after_delay':
            # wait for start time
            if not wait_time_amount(data["ip"] , data["port"], data["email"], data["password"] , counter, que, data["start_time"]):
                input("Failed to login multiple times")
                continue
        else:
            input("Invalid start method: " + data["start_method"] + "\nPress a key to continue...")
            continue
        do_stuff.do_stuff(data)
    elif action == '3':
        command = input('Are you sure you want to exit? (y/n): ')
        if command == 'y':
            # exit
            exit()
        else:
            continue
    else:
        input('Invalid input: ' + action + '\nPress enter to continue...')
        continue
