from src.utils.functions.selfInput import *;
from src.utils.functions.clear import *;
import os;
import psutil;

pid = os.getpid()
py = psutil.Process(pid)

def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)

battery = psutil.sensors_battery()

batteryResume = "\033[1;32m%s%%\033[0;0m, tempo restante: %s" % (battery.percent, secs2hours(battery.secsleft))

message = f'''
            nome de usuario: {os.getlogin()}
            cpu usada: {psutil.cpu_percent(interval=1)}
            memoria usada: {py.memory_info()[0]/2.**30}
            psycal memoria use: {psutil.virtual_memory()}
            net stats: {psutil.net_if_stats()}
            rede: {psutil.net_io_counters()}
            bateria: {batteryResume}
            other: {psutil.cpu_times()}
        '''
def run():
    Sair = False;
    while(Sair == False):
        clear();
    
        try:
            print(message)
        except:
            a = 0;

        choice = selfInput('Aperte enter para ir ao menu...');
        
        if True:
            clear();
            Sair = True;