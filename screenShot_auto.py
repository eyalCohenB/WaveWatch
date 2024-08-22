import pyautogui
import os
import time

def main():

    interval = 2 # 2 sec
    dir_name = "wave_pics"

    # Create a directory for screenies
    if dir_name in os.listdir() :
        print("dir for screenies already exists: " + dir_name)
    else:
        os.mkdir(dir_name)
        print("Created dir for screenies: " + dir_name)

    # Sleep to wait for screen change to waves video
    time.sleep(3) # 3 sec

    # Start screen capture loop.
    try:
        i = 1
        start_time = time.time()
        while time.time() - start_time < 300: # working for 5 min (60sec = min)
            img_name = "img"+ str(i) + ".png"
            img_path = dir_name + "/" + img_name
            image = pyautogui.screenshot(img_path)
            print("screenshot" + str(i))
            i+=1
            time.sleep(interval) # take screenie every interval secs.

    except KeyboardInterrupt:
        print("Finished Taking screenies at: " + dir_name)
        pass

    
if __name__ == "__main__":
    main()
