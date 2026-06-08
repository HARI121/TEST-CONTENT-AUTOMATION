import subprocess
import time
import pyautogui
import os
powershell_command = "tpm.msc"
output_folder = "C:\Adjustment Program"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Created folder: {output_folder}")
try:
    # Run the command
    result = subprocess.run(
        ["powershell", "-Command", powershell_command],
        capture_output=True,
        text=True,
        check=True
    )
    filename = "1.png"
    full_path = os.path.join(output_folder, filename)
    time.sleep(3)
    screenshot = pyautogui.screenshot()
    screenshot.save(full_path)
    # Print the output from PowerShell
    print("PowerShell Output:\n")
    print(result.stdout)

except subprocess.CalledProcessError as e:
    # Handle errors if the PowerShell command fails
    print("An error occurred while running the PowerShell script:")
    print(e.stderr)