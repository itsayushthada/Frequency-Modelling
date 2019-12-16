"""
This script is hard coded and was used in certain state of the system.
This particular method is not applicalble for simulating the similar experiment.
"""

import pyautogui as pg
import time

pg.PAUSE = 1.5

skipfiles = [1, 22, 86, 97, 122, 156]

def action(fname):
        # Loading Geometry
	pg.rightClick(380, 232)
	pg.moveTo(480, 280)
	pg.click(680, 280)
	pg.typewrite("{}.x_t".format(fname))
	pg.click(510, 470)

	# Edit Model
	pg.rightClick(380, 250)
	pg.click(390, 260)
	pg.click(750, 415)
	time.sleep(30)

	# Generate Report
	pg.click(350, 30)
	time.sleep(10)

	# Save Report as .htm
	pg.click(550, 690)
	time.sleep(2)
	pg.click(280, 160)
	pg.typewrite("{}".format(fname))
	pg.hotkey("tab")
	pg.press("p")
	pg.hotkey("enter")

	# Close the Window
	pg.click(1350, 10)

	
def getdata(lbound, ubound):
        for x in range(lbound, ubound+1):
                if x not in skipfiles:
                        action(x)
