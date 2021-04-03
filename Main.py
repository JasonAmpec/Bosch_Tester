import smbus
import time
import MCP_lib
import numpy as np

f = open("results.txt","w")

y = 0
B_string = 0
arraysize = 0

Learn = np.array([])
 

#initial
MCP_lib.init()

print ("Start Test Sequence")
 
# Loop until user presses CTRL-C
while True:
 
  #Scan through all input port and return results 
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
    
  #f.close()
  Learn = np.delete(Learn,1)

  
  print("**************END***************")
  
#TEST 1
#TEST 2
#Edit from webpage
