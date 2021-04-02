import os
import time
i = 0
while i < 100000:
    os.system("python pushcommand.py")
    time.sleep(20)
    i += 1
    print("Pushing for {} times".format(i))
