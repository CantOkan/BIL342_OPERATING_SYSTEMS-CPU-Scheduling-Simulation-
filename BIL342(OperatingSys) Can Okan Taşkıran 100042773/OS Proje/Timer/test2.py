import threading 
def mytimer(): 
   print("Python Program\n") 
my_timer = threading.Timer(3.0, mytimer) 
my_timer.start() 
print("Bye\n") 