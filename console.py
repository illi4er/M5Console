from m5stack import *
from m5stack_ui import *
from uiflow import *

line = 0

def clear(name = "Console"):
  global line
  line = 0
  for i in range(2):
    lcd.clear()
    lcd.fill(0x000000)
  lcd.print(name, 5, 5, 0xffc800)
  
def extraline(number):
  if number > 0:
    return 1
  else:
    return 0
  
def write(text, typ = 0):
  global line
  color = 0
  if typ == 0:
    color = 0xffffff
  elif typ == 1:
    color = 0xc80000
  elif typ == 2:
    color = 0x00c800
  elif typ == 3:
    color = 0x0000c8
  for i in range((len(text) // 36 + extraline(len(text)%36))):
    lcd.print(text[36*i:36*(i+1)], 5, 20+15*i+15*line,color)
  line = line + int((len(text) // 36 + extraline(len(text)%36)))
