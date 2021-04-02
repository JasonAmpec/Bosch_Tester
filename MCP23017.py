import smbus
import time

flag = 1
x = 0
Output_adr = 0b00000001
 
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

print ("Start Test Sequence")
 
# Loop until user presses CTRL-C
while True:
 
  # Read state of GPIOA register
  while (x <= 7): 
    bus.write_byte_data(OUT_DEVICE,GPIOA,Output_adr)
    Output_adr = Output_adr << 1
    x = x + 1

    Data = bus.read_byte_data(IN_DEVICE,GPIOA)
    print("Output:",format(Output_adr >> 1, '#010b'),"Readout",format(Data, '#010b'))
    time.sleep(1)

  x = 0
  Output_adr = 0b00000001
  
  print("**************END***************")
  time.sleep(5)
#TEST 1
#TEST 2
#Edit from webpage
