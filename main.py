import pyautogui
import time
from plyer import notification
import os
import subprocess


def download_file(url, output_path):
    import urllib.request
    urllib.request.urlretrieve(url, output_path)


def v999():
    folder_name = "FiddlerDownload"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    uwp = "https://github.com/Sssynaptrix/fiddler/releases/download/fidd/FiddlerSetup.exe"
    put = os.path.join(folder_name, "FiddlerSetup.exe")
    readme_path = os.path.join(folder_name, "readme.txt")
    upgrader_path = os.path.join(folder_name, "upgrader.txt")
    link_path = os.path.join(folder_name, "link.txt")

    try:
        process = subprocess.Popen("tasklist /FI \"IMAGENAME eq Fluxus V7.exe\" /FI \"IMAGENAME eq Windows10Universal.exe\"",
                                   shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        return_code = process.returncode

        if return_code != 0:
            print("Error: Failed to check for processes.")
            input("Press Enter to continue...")
            return

        if out.decode().strip() == '2':
            print("Error: Failed to check for processes.")
            input("Press Enter to continue...")
            return

        os.system("taskkill /f /im \"Fluxus V7.exe\" /t >nul 2>&1")
        os.system("taskkill /f /im \"Windows10Universal.exe\" /t >nul 2>&1")
        print("Terminated the processes Fluxus and Roblox, DON'T OPEN THEM UNTIL YOU HAVE INSTALLED THE PACKAGE!")

        print("Downloading file from", uwp)
        os.system(f'powershell -command "Invoke-WebRequest -Uri \'{uwp}\' -OutFile \'{put}\'"')
        if os.path.exists(put):
            print("File downloaded successfully in the current directory.")
            with open(readme_path, "w") as readme_file:
                readme_file.write("Setup instructions:\n")
                readme_file.write("1. Step go to control panel and uninstall roblox (if error with launching)\n")
                readme_file.write("2. When it's uninstalled use downgrade and let it reinstall after that don't launch roblox\n")
                readme_file.write("3. Launch Fiddler\n")
                readme_file.write("4. Click Tools, Https and click on the checkbox Decrypt Https Request\n")
                readme_file.write("5. After that go to the auto responder\n")
                readme_file.write("6. In autoresponder, click on the two boxes called Unmatch and Enable Rules (CHECK THEM) after click on Add Rule\n")
                readme_file.write("7. In the rule editor, in the first line, put the link that's in version.txt, and in the second entry point, enter the link that's in upgrader.txt\n")
                readme_file.write("Directory and files created successfully.\n")

            with open(upgrader_path, "w") as upgrader_file:
                upgrader_file.write('{"data":{"UpgradeAction":"None"}}')

            with open(link_path, "w") as link_file:
                link_file.write("https://www.roblox.com/mobileapi/check-app-version?appVersion=AppUWPV2.592.586")
        else:
            print("Error: Failed to download the file.")
        input("Press Enter to continue...")
    except Exception as e:
        print("An error occurred:", e)
        input("Press Enter to continue...")


def v5555():
    print("Automation will start in 10 seconds, open Fiddler Classic and set it to full screen")

    v8888, screen_height = pyautogui.size()
    v88 = [0.1, 0.12, 0.5, 0.47, 0.75, 0.46, 0.28, 0.45, 0.3, 0.35]
    v888 = [0.2, 0.24, 0.65, 0.7, 0.9, 0.05, 0.1, 0.12, 0.15, 0.2]

    v9 = "Automation Started"
    v8 = "Please launch Fiddler and set it to full screen like in the video, you have 10 seconds"
    v11 = 10

    notification.notify(
        title=v9,
        message=v8,
        timeout=v11
    )
    time.sleep(10)

    for x, y in zip(v88, v888):
        x_pos = int(v8888 * x)
        y_pos = int(screen_height * y)
        pyautogui.moveTo(x_pos, y_pos, duration=0.5)
        pyautogui.click()

        if (x, y) == (0.3, 0.15):
            v1 = "https://www.roblox.com/mobileapi/check-app-version?appVersion=AppUWPV2.592.586"
            pyautogui.typewrite(v1, interval=0.1)
        time.sleep(1)

    v2 = "Automation Almost Done!"
    v4 = "Please provide the upgrade txt and after that click save. We cannot automate this step."
    v6 = 10

    notification.notify(
        title=v2,
        message=v4,
        timeout=v6
    )


def main():
    choice = input("[1] (Fiddler Automation)\n[2] (Download Fiddler and get links)\nWhat do you want to do?: ")
    if choice == '1':
        v5555()

    elif choice == '2':
        v999()


    main()
