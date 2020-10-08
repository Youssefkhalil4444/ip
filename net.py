import socket
import sys
import os
os.system ("clear")
print ("welcome....................................!")
print ("welcome....................................!")
print ("welcome....................................!")
def login (name) :
    name = input ("Type Password please: ")
    if name == ("Dos") :
        print ("Iam stanlee welcome in my script....!")
        hostname = input('Enter Your DNS Or Target: ')
        ip=socket.gethostbyname(hostname)
        print ('Host Name Is: ',hostname, '\n' 'Target Ip Is: ',ip)
    else :
        print ("$&$&$$$&$$$$&$$&$$$&$&Error$&$&$&$&$&$&$&&&&$&$&$&$")
        login ("tag")
login ("")
# صنع StanLee حتى لا يتم تغيره 
