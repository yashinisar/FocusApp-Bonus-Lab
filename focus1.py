import time

start_time = time.time()

for i in range(5):
    print("Focus on the task at hand!")
    time.sleep(1)

end_time = time.time()
print(f"Task completed in {end_time - start_time} seconds")

