from src.utils.functions.selfInput import *;
from src.utils.functions.clear import *;
import os;
import psutil;

pid = os.getpid()
py = psutil.Process(pid)

battery = psutil.sensors_battery()

batteryResume = f"\033[1;32m{battery.percent}\033[0;0m"

message = f'''
            nome de usuario: {os.getlogin()}
            cpu usada: {psutil.cpu_percent(interval=1)}
            memoria usada: {py.memory_info()[0]/2.**30}
            psycal memoria use: {psutil.virtual_memory()}
            net stats: {psutil.net_if_stats()}
            rede: {psutil.net_io_counters()}
            bateria: {batteryResume}🔋
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