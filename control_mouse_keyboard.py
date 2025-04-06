import pyautogui


# Find an image on the screen (must provide an image file)
'''position = pyautogui.locateOnScreen("WindowsButton.png")  # Replace with your image

if position:
    print("Image found at:", position)
    pyautogui.click(position)  # Click on the found image
else:
    print("Image not found!")'''

# force use of ImageNotFoundException
pyautogui.useImageNotFoundException()

try:
    location = pyautogui.locateOnScreen("WindowsButton.png")
    left, top, width, height = location  # Unpack values


    pyautogui.click(left+(width*.8), top+(height*.5), button='left')  # Right-click at (400,400)
    # Cannot understand very small images


except pyautogui.ImageNotFoundException:
    print('ImageNotFoundException: image not found')
