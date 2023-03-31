import time

seconds = int(input('How much seconds do you want? '))

def count_down_time(seconds):
    while seconds>0:
        mins = seconds//60
        secs = seconds%60
        timer = f'{mins}:{secs}   '
        
        print(timer, end='\r')
        time.sleep(1)
        seconds-=1
    print("Time's gone!")
    
count_down_time(seconds)