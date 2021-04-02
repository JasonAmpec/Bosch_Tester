import smbus
import time
import MCP_lib
import numpy as np

f = open("results.txt","w")

y = 0
B_string = 0
arraysize = 0

Learn = np.array([])
 
#bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1
 
OUT_DEVICE = 0x20 # Device address (A0-A2)
IN_DEVICE = 0X21
IODIRA = 0x00 # Pin direction register
IODIRB = 0x01
GPIOA  = 0x12 # Register for inputs
GPIOB = 0x13
GPPUA = 0x0C
GPPUB = 0x0D
 
# Set first 7 GPA pins as outputs and
# last one as input.
MCP_lib.init()

print ("Start Test Sequence")
 
# Loop until user presses CTRL-C
while True:
 
  # Read state of GPIOA register
  Learn = MCP_lib.scan()

  #print("results are:",Learn) 
  for z in Learn:
    print(z)

  f.write("Learning Results: \n12345678\n")
  arraysize = Learn.size
  while (y < arraysize):
    B_string = Learn[y]
    f.write(B_string)
    f.write("\n")
    y= y+1
    
  f.close()
  Learn = np.delete(Learn,1)

  
  print("**************END***************")
  time.sleep(5)
#TEST 1
#TEST 2
#Edit from webpage
