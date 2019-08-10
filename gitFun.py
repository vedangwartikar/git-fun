import subprocess
import random

for i in range(random.randint(1,8)):
    for j in range(1,6):
        file = open("bait.py", "a")
        file.write('i')
        subprocess.call("git init", shell = True)
        subprocess.call("git add .", shell = True)
        subprocess.call(''.join(['git commit --date="', str(365 + j), ' day ago" -m "updated"]']), shell = True)
        subprocess.call("git push origin master", shell = True)