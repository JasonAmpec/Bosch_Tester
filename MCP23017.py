import smbus
import time

flag = 1
 
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
bus.write_byte_data(OUT_DEVICE,IODIRA,0x00)
bus.write_byte_data(OUT_DEVICE,IODIRB,0x00)
bus.write_byte_data(IN_DEVICE,IODIRA,0xff)
bus.write_byte_data(IN_DEVICE,IODIRB,0xff)
bus.write_byte_data(IN_DEVICE,GPPUA,0xff)
bus.write_byte_data(IN_DEVICE,GPPUB,0xff)
 
# Loop until user presses CTRL-C
while True:
 
  # Read state of GPIOA register
  if (flag == 1):
    bus.write_byte_data(OUT_DEVICE,GPIOA,0xff)
    bus.write_byte_data(OUT_DEVICE,GPIOB,0x00)
    flag = 0
  elif (flag == 0):
    bus.write_byte_data(OUT_DEVICE,GPIOA,0x00)
    bus.write_byte_data(OUT_DEVICE,GPIOB,0xff)   
    flag = 1 

  Data = bus.read_byte_data(IN_DEVICE,GPIOA)
  
  print(bin(Data))
  time.sleep(2)
#TEST 1
#TEST 2
#Edit from webpage
