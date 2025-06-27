import time

arquivo = open("log.txt","w")

while True:
    #print(time.strftime("%a, %d, %b %Y %H:%M:%S", time.gmtime()))
    arquivo.writelines(time.strftime("%H:%M:%S\n"), time.gmtime())
    time.sleep(5)
    