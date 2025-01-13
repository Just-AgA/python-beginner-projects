#Print current time in milliseconds
from time import time
 
 #Find the time in milliseconds by using the time() function
milliseconds = int(time() * 1000)

print("Time in milliseconds is:")
print(milliseconds)