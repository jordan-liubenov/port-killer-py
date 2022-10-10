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
 
  if not output:
    decision = input("Port is not active, (retry) or (exit)?\n")
    decision = decision.strip().lower()
    if decision == 'exit':
     os.system('exit')
     return
    elif decision == 'retry':
     receiveInput()
    else:
      searchAndDestroy(port)

  for i in output:
    host = i[1].split(':')
    current_port = host[1]
    pid = i[4]
    
    if not checkEstablished(i) or current_port != port:
      continue
    
    result = os.popen('taskkill /PID ' + pid + ' /F').read()
    print(result)
    return
  
def receiveInput():
  target_port = input('Enter desired port to kill:\n')  
  target_port = target_port.strip()

  if not target_port.isnumeric():
    print('That doesn\'t seem right... try again')
    receiveInput()
    return

  # check to make sure the port that was input is not a reserved port
  if int(target_port) <= 1023:
    decision = input('Sorry, that port is reserved, (retry) or (exit)?\n')
    decision = decision.strip().lower()
    if decision == 'exit':
     os.system('exit')
     return
    elif decision == 'retry':
     receiveInput()

  searchAndDestroy(target_port)


def main():
  receiveInput()

main()