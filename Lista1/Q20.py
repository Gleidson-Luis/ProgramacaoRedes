import time

arquivo = open("log.txt","w")

while True:
    #print(time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))
    #print(time.strftime("%H:%M:%S", time.gmtime()))
    arquivo.write(time.strftime("%H:%M:%S\n", time.gmtime()))
    time.sleep(1)
    