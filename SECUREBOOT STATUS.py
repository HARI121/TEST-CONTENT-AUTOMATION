import subprocess
import time
import os
# command for accessing the secureboot status
powershell_command ="Confirm-SecureBootUEFI"
#folder where the result is saved
output_folder = "C:\\Adjustment Program"
#name of the file and combining the path with filename
filename = "securebootstatus.txt"
full_path = os.path.join(output_folder, filename)

# verification whether the folder exist and building a new one if it'snot available
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Created folder: {output_folder}")
elevated_command = (
    f"Start-Process powershell -ArgumentList '-Command \"{powershell_command} | "
    f"Out-File -FilePath ''{full_path}'' -Encoding utf8\"' -Verb RunAs -WindowStyle Hidden"
)
try:
    # Run the command
    result = subprocess.run(
        ["powershell", "-Command", elevated_command],
        capture_output=True,
        text=True,
        check=True
    )
    # for delay 
    time.sleep(1)
    if os.path.exists(full_path):
        # 1. Read the SecureBoot status that the admin process saved
        with open(full_path, "r", encoding="utf-8") as file:
            secureboot_result = file.read()
    # writing result to file
        with open(full_path, "w", encoding="utf-8") as file:
            file.write(f"{powershell_command}\n")
            file.write(secureboot_result)
            print(f"Success! Content successfully pasted into: {full_path}")

except subprocess.CalledProcessError as e:
    # Handle errors if the PowerShell command fails
    print("An error occurred while running the PowerShell script:")
    print(e.stderr)