# Path to the hosts file
hosts_path = 'C:\Windows\System32\drivers\etc\hosts'

youtubeLine = 26

# Read the hosts file
with open(hosts_path, 'r') as file:
    lines = file.readlines()

# Check if the 17th line starts with '# '
if lines[youtubeLine - 1].startswith('# '):
    # If it does, remove '# '
    lines[youtubeLine - 1] = lines[youtubeLine - 1][2:]
    isEnable = True
else:
    # If it doesn't, add '# '
    lines[youtubeLine - 1] = '# ' + lines[youtubeLine - 1]
    isEnable = False

# Write the modified lines back to the hosts file
with open(hosts_path, 'w') as file:
    file.writelines(lines)
    
if isEnable:
    print('Youtube is disabled')
else:
    print('Youtube is enabled')
    
import os
import threading
import time

def exit_on_input():
    input('Press enter to exit')
    os._exit(0)

# Start a separate thread that waits for the user's input
threading.Thread(target=exit_on_input).start()

# Wait for 3 seconds
time.sleep(3)

# If the user hasn't pressed enter after 3 seconds, exit the script
os._exit(0)