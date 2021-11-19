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



2021-11-19: new requests:

```python
import numpy as np 
import pandas as pd 
import os


#!! convert RFID file to standard file(pyEcoHAB txt)
def convert_file(folder_path, p, date, idx_num):
    COMp = p[p.rfind('/')+1 : p.find('.')]

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
            
            savepath = folder_path + '/' + COMp + '_' + date1 + '_' + str(tt) + '0000.txt'
            if int(ti) < int(tt):
                date1 = str(int(date1) + 1)
            name=['idx','date','time', 'mapidx', 'duration', 'rfid']
            test = pd.DataFrame(columns=name,data=savedata)

            # test.to_csv(savepath, sep='\t', index=False, header=False) #, encoding='gbk')
            test.to_csv(savepath, sep='\t', index=False) #! header 还是得True
            
            savedata = []
            tt = ti
            

        l = [str(i+1), date, j[0], str(idx_num), '211', j[1]]
        savedata.append(l) 
    
    
def rfid_1folder(config):
    folder_path = config['folder_path'] 
    if not os.path.exists(folder_path):
        raise ValueError("RFID文件夹不存在")
    print(folder_path)
    
    date = folder_path[: folder_path.rfind('-')]
    date = date[date.rfind('/')+1 : date.rfind('-')]
    # date = date[: 4] + '.' + date[4: 6] + '.' + date[6: ]
    
    paths = os.listdir(folder_path)
    for p in paths:
        if 'COM_' not in p or '0000' in p: 
            continue
        idx = p[p.find('_')+1 : p.find('.')] #!! 必须得COMxxx.txt (命名格式)
        p = folder_path + '/' + p
        print(idx)
        idx_num = idx_map[idx]
        
        print(folder_path, p, date, idx_num)
        convert_file(folder_path, p, date, idx_num)
        # break
    

#!! remove dirty data & save to another file  : COM -> COM_   and print 
def preprocess(config):
    folder_path = config['folder_path'] 
    if not os.path.exists(folder_path):
        raise ValueError("RFID file not exists")
    
    print('===================================================')
    print('================== preprocess: ====================')
    print('===================================================')
    paths = os.listdir(folder_path)
    for p in paths:
        if 'COM' in p and '_' not in p:
            print(p)
            savepath = folder_path + '/' + p[: p.find('M')+1] + '_' + p[p.find('M')+1: ]
            print(savepath)
            f = open(folder_path + '/' + p, encoding='unicode_escape')
            data = f.readlines()
            
            savedata = []
            for i,j in enumerate(data):  #! 开始丑..
                if not len(j):  #! 空行
                    continue
                elif j[0] != '[':
                    continue
                elif '$' in j and '#' in j:
                    savedata.append(j) 
                else:
                    print('path %s,  line %d has a dirty data ' % (p, i)) 
                    continue
            
            with open(savepath, 'w') as f:
                for item in savedata:
                    f.write("%s" % item)
                    
            # test = pd.DataFrame(savedata)
            # test.to_csv(savepath, index=None, header=None)  #! 转pandas 输出有\n问题  拉跨..
    print('===================================================')
    print('================ preprocess done ==================')
    print('===================================================')
                

#!! combine with 60ms or whatever data & save to another file
def postprocess(config):
    folder_path = config['folder_path'] 
    save_folder = folder_path + '/combine/' 
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    
    def time2num(t): #! time str --> sec
        # print(t[: t.find(':')], t[t.find(':')+1: t.rfind(':')], t[t.rfind(':')+1: ])
        hour, minute, sec = int(t[: t.find(':')]), int(t[t.find(':')+1: t.rfind(':')]), float(t[t.rfind(':')+1: ])
        return hour * 60 * 60 + minute * 60 + sec
    
    print('===================================================')
    print('================== postprocess: ===================')
    print('===================================================')
    
    paths = os.listdir(folder_path)
    for p in paths:
        if '0000' not in p:
            continue 
        save_path = save_folder + '/' + p
        
        data = pd.read_csv(folder_path + '/' + p, sep='\t')
        print(data)
        
        save_data = pd.DataFrame(columns=data.keys())  #! save to a new DataFrame.
        print(save_data)
        
        t_start = data['time'][0]
        t_temp = t_start

        # t_start = time2num(data['time'][0])
        # t_temp = time2num(t_start)
        i_idx = 0
        save_data_idx = 0
        for i,j in enumerate(data['time']):
            # print(time2num(j))
            if time2num(j) - time2num(t_temp) <= config['msec']:
                t_temp = j 
                continue 
            else :
                save_data.loc[save_data_idx] = data.loc[i_idx]
                # save_data.loc[save_data_idx]['duration'] = (time2num(t_temp) - time2num(t_start)) * 1000
                save_data['duration'][save_data_idx] = (time2num(t_temp) - time2num(t_start)) * 1000
                
                t_start = j 
                t_temp = t_start 
                
                i_idx = i
                save_data_idx += 1
        print(save_data)
        save_data.to_csv(save_path, sep='\t', index=False, header=False)
        # break 
    
    print('===================================================')
    print('=============== preprocess done ===================')
    print('===================================================')


#!! merge same day-hour's 'combine folder' file  together   : undone now
def postprocess_merge_time(config):
    folder_path = config['folder_path'] + '/combine'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    savepath = config['folder_path'] + '/mergetime'
    paths = os.listdir(folder_path)
    used = [0] * len(paths) #! used : 1, not used : 0
    
    for i,j in enumerate(paths):
        if used[i] == 0:
            used[i] = 1
    
        
    

if __name__ == "__main__":
    
    idx_map = {'28' : 7, '29' : 1, '45' : 3, '30': 4, '31' : 5, '42': 6, '43': 7, '44': 9, '45': 10} #!! COM29-7 : 27 -> 7
    idx_map['30'] = 1
    idx_map['8'] = 8
    idx_map['9'] = 19
    idx_map['10'] = 11
    idx_map['11'] = 13
    idx_map['46'] = 46
    idx_map['47'] = 47
    idx_map['48'] = 48
    idx_map['49'] = 49
    
    
    config = {
        # "folder_path" : "./20210917-20210921-RFID",
        # "folder_path" : "/run/media/arch/A/Workspace_/rfid/20210917-20210921-RFID",
        # "folder_path" : "/run/media/arch/A/Workspace_/rfid/20211118-50211119-RFID",
        "folder_path" : "/run/media/arch/A/Workspace_/rfid/20210001-RFID", #! test
        
        'idx_map' : idx_map,
        'msec' : 60 * (1e-3)  #! 60ms
    }
    
    
    preprocess(config) #! 数据预处理, COM -> COM_.txt
    
    rfid_1folder(config)
    
    postprocess(config)
    
```

