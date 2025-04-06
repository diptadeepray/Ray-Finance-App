'''from openpyxl import load_workbook

wb = load_workbook("example.xlsx")  # Load the file
ws = wb.active

ws['C1'] = 100
ws['C2'] = 200
wb.save("example.xlsx")


print(ws['C1'].value)  # Output: Hello
print(ws['B1'].value)  # Output: World
'''


import pyautogui
pyautogui.typewrite("Hello, how are you?", interval=0.1)
'''💡 This will type:
H → e → l → l → o → , → → h → o → w → → a → r → e → → y → o → u → ?
(with a 0.1-second delay between each keystroke)
'''

pyautogui.press("enter")
#the Enter key is pressed, which might send the text in a chat, search bar, or command prompt.