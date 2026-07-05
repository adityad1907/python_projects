import time 

my_time = int(input("Enter the Time in Seconds: "))

for x in range(my_time,0,-1):
    hours = int(x /3600) % 60
    minutes= int(x/60) % 60
    seconds = x % 60
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    time.sleep(1)