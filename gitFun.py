import subprocess
import random

for i in range(5):
    for j in range(1, random.randint(3,8)):
        print(j, 17+i)
        file = open("bait.py", "a")
        file.write('i')
        subprocess.call("git init", shell = True)
        subprocess.call("git add .", shell = True)
        subprocess.call(''.join(['git commit --date="', str(17 + i), ' day ago" -m "updated"]']), shell = True)
        subprocess.call("git push origin master", shell = True)