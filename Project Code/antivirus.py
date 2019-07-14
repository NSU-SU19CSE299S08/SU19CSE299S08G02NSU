import psutil
import os
import clamd

programs = psutil.pids()
virus_check = clamd.ClamdUnixSocket()
for program in programs:
    open('{]'.format(program.exe()), 'wb').write(clamd.EICAR)
    temp = virus_check.scan('{}'.format(program.exe()))
    if temp[0] == 'FOUND':
        program.terminate()

os.system('cd C:\\')
os.system('attrib -h -r -s autorun.inf')
try:
    os.system('del autorun.inf')
except FileNotFoundError:
    pass
