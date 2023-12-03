import pygetwindow
import time
import bettercam

# Could be do with
# from config import *
# But we are writing it out for clarity for new devs
from config import screenShotHeight, screenShotWidth, autoGameDetection, gameName

def gameSelection() -> (bettercam.BetterCam, int, int | None):
    # Selecting the correct game window
    try:
        videoGameWindows = pygetwindow.getAllWindows()
        print("=== All Windows ===")
        for index, window in enumerate(videoGameWindows):
            # only output the window if it has a meaningful title
            if window.title != "":
                print("[{}]: {}".format(index, window.title))

        if autoGameDetection:
            # Filter windows by the specified game name
            filteredWindows = [window for window in videoGameWindows if gameName.lower() in window.title.lower()]

            if not filteredWindows:
                print(f"No windows found for the game '{gameName}'. Exiting.")
                return None

            if len(filteredWindows) == 1:
                videoGameWindow = filteredWindows[0]
            else:
                # If multiple windows match, let the user choose
                print("=== Matching Game Windows ===")
                for index, window in enumerate(filteredWindows):
                    print(f"[{index}]: {window.title}")
                try:
                    userInput = int(input("Please enter the number corresponding to the window you'd like to select: "))
                    videoGameWindow = filteredWindows[userInput]
                except ValueError:
                    print("You didn't enter a valid number. Please try again.")
                    return None
                except IndexError:
                    print("Invalid selection. Please try again.")
                    return None
        else:
            # Manual selection process
            try:
                userInput = int(input("Please enter the number corresponding to the window you'd like to select: "))
            except ValueError:
                print("You didn't enter a valid number. Please try again.")
                return
            # "save" that window as the chosen window for the rest of the script
            videoGameWindow = videoGameWindows[userInput]

    except Exception as e:
        print("Failed to select game window: {}".format(e))
        return None

    # Activate that Window
    activationRetries = 30
    activationSuccess = False
    while activationRetries > 0:
        try:
            videoGameWindow.activate()
            activationSuccess = True
            break
        except pygetwindow.PyGetWindowException as we:
            print("Failed to activate game window: {}".format(str(we)))
            print("Trying again... (you should switch to the game now)")
        except Exception as e:
            print("Failed to activate game window: {}".format(str(e)))
            print("Read the relevant restrictions here: https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setforegroundwindow")
            activationSuccess = False
            activationRetries = 0
            break
        # wait a little bit before the next try
        time.sleep(3.0)
        activationRetries = activationRetries - 1

    # if we failed to activate the window then we'll be unable to send input to it
    # so just exit the script now
    if not activationSuccess:
        return None

    print("Successfully activated the game window...")

    # Starting screenshoting engine
    left = ((videoGameWindow.left + videoGameWindow.right) // 2) - (screenShotWidth // 2)
    top = videoGameWindow.top + \
        (videoGameWindow.height - screenShotHeight) // 2
    right, bottom = left + screenShotWidth, top + screenShotHeight

    region: tuple = (left, top, right, bottom)

    # Calculating the center Autoaim box
    cWidth: int = screenShotWidth // 2
    cHeight: int = screenShotHeight // 2

    print(region)

    camera = bettercam.create(region=region, output_color="BGRA", max_buffer_len=512)
    if camera is None:
        print("Your Camera Failed! Ask @Wonder for help in our Discord in the #ai-aimbot channel ONLY: https://discord.gg/rootkitorg")
        return
    camera.start(target_fps=120, video_mode=True)

    return camera, cWidth, cHeight