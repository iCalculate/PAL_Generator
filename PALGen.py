import pyautogui
import os
import sys
from ctypes import *
import numpy as np

def get_color(x, y):
	gdi32 = windll.gdi32
	user32 = windll.user32
	hdc = user32.GetDC(None)  # 获取颜色值
	pixel = gdi32.GetPixel(hdc, x, y)  # 提取RGB值
	r = pixel & 0x0000ff
	g = (pixel & 0x00ff00) >> 8
	b = pixel >> 16
	return [[r, g, b]]

Position = [[0,0]]
ColorList = get_color(Position[0][0],Position[0][1])

try:
	while True:
		Key = input("Enter to Add: ")
		if (Key == ""):
			x, y = pyautogui.position()
			New_Postion = [[x,y]]
			New_ColorList = get_color(New_Postion[0][0],New_Postion[0][1])
			Position.extend(New_Postion)
			ColorList.extend(New_ColorList)
			print("New_Postion = " + str(New_Postion))
			print("New_Color = " + str(New_ColorList))
			print(Key)
		elif (Key == "\\"):     #Use \ to finish Adding
			break
except KeyboardInterrupt:
	print('\nExit.')

print("Color = " + str(ColorList) )

filename = 'write_data.txt'
with open(filename,'w') as f:
	f.write("JASC-PAL\n")
	f.write("0100\n")
	f.write(str(len(Position)) + "\n")
	for j in range(len(Position)) :
		f.write(str(ColorList[j][0])+" "+ \
				str(ColorList[j][1])+" "+ \
				str(ColorList[j][2])+"\n")

if os.path.exists('./GetColor.pal'):
	Ans = input("Whether to overwrite the original file? (y/n) :")
	if (Ans == "y"):
		os.remove('./GetColor.pal')
		os.rename('./write_data.txt','./GetColor.pal')
		pass
	elif (Ans == "n"):
		NewFileName = input("Input New Name: ")
		os.rename('./write_data.txt','./' + NewFileName + '.pal')
else :
	os.rename('./write_data.txt','./GetColor.pal')

	