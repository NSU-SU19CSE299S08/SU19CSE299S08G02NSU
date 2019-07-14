import psutil
import os

# li = psutil.pids()
# print(li)
# p = psutil.Process(272)
# print(p.name())
os.system('cd C:\\')
os.system('attrib -h -r -s autorun.inf')
try:
    os.system('del autorun.inf')
except FileNotFoundError:
    pass
