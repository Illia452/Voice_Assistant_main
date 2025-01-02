import time



start_time = time.time()
while True:
    if time.time() >= start_time + 4.8:
        print("good")
        break