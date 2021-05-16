#!/usr/bin/python3

import spidev
import time

# Fuehrt aus, gibt Ausgabe nach stdout und in die Datei.
# ./datareader.py | tee out.log

delay = 0.2

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

def readChannel(channel):
  val = spi.xfer([1,(8+channel)<<4,0])
  data = ((val[1]&3) << 8) + val[2]
  return data

if __name__ == "__main__":
# try:
    t_end = time.time()+30
    while time.time() <= t_end:
      val = readChannel(0)
      print(str(val))  
  #print("C0 \t C1 \t C2 \t C3 \t C4 \t C5 \t C6 \t C7")
#   while True:
#     val = readChannel(0)  
  #for x in range(0, 8):
      # val = readChannel(x)
      # print str(val) + "\t",          
      #print("")  
#     time.sleep(delay)
# except KeyboardInterrupt:
#   print "Cancel."
