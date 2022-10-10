# Script intended to make the termination of in-use ports easy
from operator import indexOf
import os

def formatPortResults(found_ports):
  found_ports = found_ports.split('\n')
  for i in found_ports:
    current_index = found_ports.index(i)
    print(i)
    if i != '':
      formatted_cell = i.split()
      found_ports[current_index] = formatted_cell
  return found_ports

def searchAndDestroy(port):
  output = os.popen('netstat -ano | findstr :' + port).read()
  output = formatPortResults(output)
  # print(output)

def receiveInput():
  target_port = input('Enter desired port to kill:\n')
  
  if int(target_port) <= 1023:
  # check to make sure the port that was input is not a reserved port (0 - 1023)
    decision = input('Sorry, that port is reserved, (retry) or (exit)?\n')
    decision = decision.strip()
    if decision == 'exit':
     os.system('exit')
    elif decision == 'retry':
     receiveInput()

  searchAndDestroy(target_port)

def main():
  receiveInput()

main()