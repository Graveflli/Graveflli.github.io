 ### lj code for rfid

big brother is watching you...

```python
import numpy as np 
import pandas as pd 
import os


#!! convert RFID file to standard file(pyEcoHAB txt)
def convert_file(folder_path, p, date, idx_num):
    date1 = date 
    date = date[: 4] + '.' + date[4: 6] + '.' + date[6: ]
    
    f = open(p, encoding='unicode_escape')
    data = f.readlines()

    print(len(data))
    data_std = []
    for i,j in enumerate(data):
        data_time = j[j.find('[')+1 : j.find(']')]
        rfid = j[j.find('$')+1 : j.find('#')]
        if data_time != '':
            data_std.append((data_time, rfid))
    
    tt = data_std[0][0]
    tt = tt[: tt.find(':')]
    tt = int(tt)
    
    savedata = [] 
    for i,j in enumerate(data_std):
        ti = j[0][: j[0].find(':')]
        ti = int(ti)

        if ti != tt or i == len(data_std)-1:
            
            savepath = folder_path + '/' + date1 + '_' + str(tt) + '0000.txt'
            if int(ti) < int(tt):
                date1 = str(int(date1) + 1)
            name=['idx','date','time', 'mapidx', 'duration', 'rfid']
            test = pd.DataFrame(columns=name,data=savedata)

            test.to_csv(savepath, sep='\t', index=False) #, encoding='gbk')
            
            savedata = []
            tt = ti
            

        l = [str(i+1), date, j[0], str(idx_num), '211', j[1]]
        savedata.append(l) 
    
    
def rfid_1folder(config):
    folder_path = config['folder_path'] 
    if not os.path.exists(folder_path):
        raise ValueError("RFID文件夹不存在")
    
    date = folder_path[: folder_path.rfind('-')]
    date = date[date.rfind('/')+1 : date.rfind('-')]
    
    paths = os.listdir(folder_path)
    for p in paths:
        if 'COM' not in p: 
            continue
        idx = p[p.find('M')+1 : p.find('.')] #!! 必须得COMxxx.txt (命名格式)
        p = folder_path + '/' + p
        idx_num = idx_map[idx]
        
        print(folder_path, p, date, idx_num)
        convert_file(folder_path, p, date, idx_num)
        break
    
    


if __name__ == "__main__":
    
    idx_map = {'28' : 7, '29' : 1, '45' : 3, '30': 4, '31' : 5, '42': 6, '43': 7, '44': 9, '45': 10} #!! COM29-7 : 27 -> 7
    idx_map['30'] = 1
    
    config = {
        # "folder_path" : "./20210917-20210921-RFID",
        "folder_path" : "/run/media/arch/A/Workspace_/rfid/20210917-20210921-RFID",
        'idx_map' : idx_map
    }
    
    rfid_1folder(config)
    
```