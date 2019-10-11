
import time

localtime=int(time.time())
print("enter "+str(localtime))

time.sleep(2)

sonlocal=int(time.time())
print("moved "+str(sonlocal))


gecensure=int(sonlocal-localtime)

print("Gecen süre :{}".format(gecensure))