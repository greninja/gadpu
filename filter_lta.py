import re
import os
import glob
data_dir = '/LTA/data/cycle20/'
#data_dir = '/LTA/data/test/'
VALID_LIST = 'parser/filter_healthy/healthy2_file.txt'
valid_observations = open(VALID_LIST, 'r').read().split('\n')[0:-1]
all_observations = os.listdir(data_dir)

def INVALID_OBS():
    invalid_obs = []
    for DIR_NAME in all_observations:
        current_obslog = glob.glob(data_dir+DIR_NAME+'/'+'*.obslog')
        if current_obslog == []:
            continue
        
        #Extract substring that contains obslog relative path
        relative_path = re.findall(r'[/][\d]+[.]obslog', current_obslog[0])[0][1:] 
        #Invalid file (not fitting given constraints i.e. < 900 MHz and IF BW != 6,16,32)
        if relative_path not in valid_observations:
 	    invalid_obs.append(data_dir+DIR_NAME)   
    
	#Valid obslog file with no LTA file in the DIR        
        if relative_path in valid_observations:
            if glob.glob(data_dir+DIR_NAME+'/'+'*.lta') == []:
                #print data_dir+DIR_NAME
		invalid_obs.append(data_dir+DIR_NAME)
    return invalid_obs

def VALID_OBS():
    valid_obs = []
    for DIR_NAME in all_observations:
            current_obslog = glob.glob(data_dir+DIR_NAME+'/'+'*.obslog')
	    if current_obslog == []:
            	continue
            #Extract substring that contains obslog relative path
            relative_path = re.findall(r'[/][\d]+[.]obslog', current_obslog[0])[0][1:] 
                                    
            if relative_path in valid_observations:
                if glob.glob(data_dir+DIR_NAME+'/'+'*.lta') != []:
                    valid_obs.append(data_dir+DIR_NAME)
    return valid_obs


print VALID_OBS()
print  '--------------------------------------------------------------------------------------------------'
print INVALID_OBS()
