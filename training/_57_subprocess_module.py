import os
import subprocess
import sys

#os.system() command is used to run the terminal commands. But it doesn't return output. Instead it returns the pass/fail status of the command.
#sp = subprocess.Popen(cmd, shell = True/False, stdout = subprocess.PIPE, stderr = subprocess.PIPE)  # Subprocess syntax
#rc = sp.wait()      # used to wait for the process 'sp' to complete
#out, err = sp.communicate() #used to get output and error message to out & err varibles respectively.
#shell = True => cmd = "ls -lrt" (command should be in form of string) (Command will be run in a new shell opened by python script)
#shell = False => cmd = ['ls', '-lrt'] (command should be in form of list) (Commad will be run in the same shell without opening new shell)

cmd = "ls -lrt"
sp = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
rc = sp.wait()
out, err = sp.communicate()

print(f'The return code is :{rc}')  #If return code is 0, it means that there is no error
print(f'Output is :{out}')          #Output and error is in binary format. To convert it to string format we have to assign .universal_newlines=True in subprocess
print(f'Err msg is :{err}')

print(f'===================================')

cmd = "ls -lrt"
sp = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, universal_newlines = True)
rc = sp.wait()
out, err = sp.communicate()
print(f'The return code is :{rc}')  #If return code is 0, it means that there is no error
print(f'Output is :{out}')          #Output and error is in string format as .universal_newlines=True in subprocess
print(f'Err msg is :{err}')

print(f'=====================================')

cmd = "ls -lrt".split() #Output of 'string'.split() will be list. In this eg, o/p will be ['ls', '-lrt']
sp = subprocess.Popen(cmd, shell = False, stdout = subprocess.PIPE, stderr = subprocess.PIPE, universal_newlines = True)
rc = sp.wait()
out, err = sp.communicate()
print(f'The return code is :{rc}')  #If return code is 0, it means that there is no error
print(f'Output is :{out}')          #Output and error is in string format as .universal_newlines=True in subprocess
print(f'Err msg is :{err}')

#INCASE, command depends on env variables of operating system, shell should always be true
#in windows os, shell should always be true
