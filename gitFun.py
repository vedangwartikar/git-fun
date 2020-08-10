import subprocess

file = open("bait.py", "a")
file.write('i')
#subprocess.call("C:/Users/Vedant Wartikar/Desktop/GitHub/git-fun", shell = True)
subprocess.call("git init", shell = True)
subprocess.call("git add .", shell = True)
subprocess.call('git commit -m "updated"', shell = True)
subprocess.call("git push origin master", shell = True)