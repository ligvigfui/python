import datetime
import pyautogui
import json
import os
import socket
import hash

def create_tcp_connection(ip_address, port) -> socket.socket:
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect the socket to the specified address and port
    client_socket.connect((ip_address, port))
    
    return client_socket

def send_get_request(client_socket, host, credentials):
    # Compose the GET request message
    request = "GET /login_neptun_fos HTTP/1.1\r\n"
    request += f"Host: {host}\r\n"
    request += f"Credentials: {credentials}\r\n\r\n"

    # Send the GET request message
    client_socket.send(request.encode())

def receive_response(client_socket) -> str:
    # Receive the response header
    header = ""
    while not header.endswith("\r\n\r\n"):
        header += client_socket.recv(1).decode()

    # Extract the content length from the header
    content_length = int(header.split("Content-Length: ")[1].split("\r\n")[0])

    # Receive the response body
    body = client_socket.recv(content_length).decode()

    return header + body

def login(credentials, host, port) -> bool:
    
    # Example usage
    credentials1 = hash.encode(credentials)

    # open client socket
    client_socket = create_tcp_connection(host, port)

    # Assume that client_socket is already connected
    send_get_request(client_socket, host, credentials1)

    # Example usage
    response = receive_response(client_socket)
    response = response.split("\r\n\r\n")[1]
    stuff = hash.decode(response, data["credentials"])
    if stuff == "Ok":
        print("Login successful")
        return False
    elif stuff == "Wc":
        print("Wrong credentials")
    elif stuff == "Nh":
        print("Server responded badly")
    elif stuff == "Nr":
        print("No response from server")
    else:
        print("Unknown error")
    return True
    



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
        "credentials": "email@something.com:password123",
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


host = "127.0.0.1"
port = 7878

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
        if login(data["credentials"], host, port):
            action = ''
            continue
        print('Neptun FOS/start neptun run')
        if data["start_method"] == 'at_time':
            # wait for start time
            print('Waiting for start time...')
            while True:
                if datetime.datetime.now().strftime("%H:%M:%S") >= data["start_time"]:
                    pyautogui.sleep(0.2)
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
