import os
import time
i = 0
while i < 100000:
    os.system("python pushcommand.py")
    
    
    print("[+]================Pushing for {} times=====================[+]".format(i))
    time.sleep(120)
    i += 1