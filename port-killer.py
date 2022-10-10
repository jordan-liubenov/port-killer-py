# Script intended to make the termination of in-use ports easy
import os

def receiveInput():
  target_port = input('Enter desired port to kill:\n')
  # check to make sure the port that was input is not a reserved port (0 - 1023)
  if int(target_port) <= 1023:
    decision = input('Sorry, that port is reserved, (retry) or (exit)?\n')
    if decision == 'exit':
     os.system('exit')
    elif decision == 'retry':
     receiveInput()


def main():
  receiveInput()

main()