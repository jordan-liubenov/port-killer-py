# Script intended to make the finding and termination of leftover in-use ports easy
import os

def formatPortResults(found_ports):
  formatted_ports = []
  found_ports = found_ports.split('\n')
  for i in found_ports:
    if i != '':
      formatted_cell = i.split()
      formatted_ports.append(formatted_cell)
  return formatted_ports

def checkEstablished(port):
  isEstablished = False
  if port[3] == 'ESTABLISHED':
    isEstablished = True
  return isEstablished

def searchAndDestroy(port):
  output = os.popen('netstat -ano | findstr :' + port).read()
  output = formatPortResults(output)

  for i in output:
    host = i[1].split(':')
    current_port = host[1]
    pid = i[4]
    
    if not checkEstablished(i) or current_port != port:
      continue
    
    # TODO execute termination command:
    # taskkill /PID 39304 /F




def receiveInput():
  target_port = input('Enter desired port to kill:\n')  
  target_port = target_port.strip()

  if int(target_port) <= 1023:
  # check to make sure the port that was input is not a reserved port
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