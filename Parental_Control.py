import time
from datetime import datetime as dt

host_temp='hosts'

host_path=r'C:\Windows\System32\drivers\etc\hosts'
redirect='127.0.0.1'
#sites that  not need to allow children to use
sites_that_kill_me=['www.facebook.com','facebook.com']

print(dt.now())

while True:
    if(dt(dt.now().year,dt.now().month,dt.now().day,19)<dt.now()<(dt(dt.now().year,dt.now().month,dt.now().day,23))):
       print('Working hours:')
       with open(host_path,'r+') as file:
           content=file.read()
           for site in sites_that_kill_me:
               if site in content:
                   pass
               else:
                   file.write(redirect+' '+site+'\n')
    else:
       with open(host_path,'r+') as file:
           content =file.readlines()
           file.seek(0)
           for line in content:
               if not any(site in line for  site in sites_that_kill_me):
                   file.write(line)
           file.truncate()
       print('time to play...')
    time.sleep(5)   
    
       
       
       
           
       
       
       
                                                                
                                                                 
                                                                 
                                                                 
                                                                 

