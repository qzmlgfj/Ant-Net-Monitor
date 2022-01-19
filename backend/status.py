import psutil

#TODO 封装对象

def get_status():
    psutil.cpu_percent(interval=1)
    #a = psutil.cpu_times_percent(interval=1)
    
