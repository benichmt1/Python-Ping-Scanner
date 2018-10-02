#A single-threaded Python Ping Scanner - Michael Benich @benichmt1 
#To do - work on the multithreading capabilities. Right now the output is being parsed which prevents the other thread from firing?

#!/usr/bin/python
import subprocess
import threading

def main():
        target = 200
        up = 0
        down = 0
        threads = []
        while (target < 255):
                startThreads(threads, target, up, down)
                target += 1
                
        checkIfThreadsAreAllTerminated(up, down)

        

def startThreads(threads, target, up, down):
        t = threading.Thread(target=scan, args=(target, up, down))
        threads.append(t)
        t.start()

def checkIfThreadsAreAllTerminated(up, down):
        allFinished = False
        while(allFinished == False):
            count = int(threading.activeCount())
            if(count == 1):
                allFinished = True
                print ("A total of " + str(up+down) + " hosts were scanned.")
                print (str(up) + " hosts were alive, and " + str(down) + " hosts were unreachable. ")
                quit()

def scan(target, up, down):
        ip = "192.168.31." +str(target)
        '''
        output = subprocess.Popen(["ping","-c","1",ip],stdout = subprocess.PIPE).communicate()[0]
        if ('Unreachable' in str(output)):
                print ('Host ' + ip + " is offline or unavailable")
                down+= 1
        else:
                print ("Host " + ip + " is online")
                up+= 1
        '''

        toPing = subprocess.Popen(['ping','-c','3',ip], stdout=subprocess.PIPE)
        output = toPing.communicate()[0]
        hostAlive = toPing.returncode
        if(hostAlive == 0):
                print(ip+" is reachable")   
                up += 1
        else:
                down += 1
        
main()