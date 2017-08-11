import subprocess
import random

for i in range(6):
    for j in range(1, random.randint(3,8)):
        print('contributions: ', j, 'days ago: ', 1095+i)
        file = open("bait.py", "a")
        file.write('i')
        subprocess.call("git init", shell = True)
        subprocess.call("git add .", shell = True)
        subprocess.call(''.join(['git commit --date="', str(1095 + i), ' day ago" -m "updated"]']), shell = True)
        subprocess.call("git push origin master", shell = True)