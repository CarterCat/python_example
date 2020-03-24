import time


i = 0
while True:
    print(f"i={i}")
    i += 1
    time.sleep(0.001)
    if i == 10000:
        break
