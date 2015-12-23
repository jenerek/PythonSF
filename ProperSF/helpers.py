import time

def printl(lines, sleep=True):
    for line in lines:
        print(line)
        if  sleep:
            sleep_time = len(line.split(" "))/4
            time.sleep(sleep_time)
        
        
def compare(right, user_ans):
    fine = right.replace("\"", "'").lower().strip() == user_ans.replace("\"", "'").lower().strip()
    return fine
    
def printa(lines):
    for line in lines:
        print(line)
        
        
def print_set(lines):
    for line in lines:
        print ""
        print ""
        return sleep.time(2)