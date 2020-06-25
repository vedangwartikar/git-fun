import subprocess
import random

for i in range(1):
    for j in range(5, random.randint(5,9)):
        print('contributions: ', j, 'days ago: ', 49+i)
        file = open("bait.py", "a")
        file.write('i')
        subprocess.call("git init", shell = True)
        subprocess.call("git add .", shell = True)
        subprocess.call(''.join(['git commit --date="', str(49 + i), ' day ago" -m "updated"]']), shell = True)
        subprocess.call("git push origin master", shell = True)