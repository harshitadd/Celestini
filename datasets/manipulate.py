import openpyxl as ox
import numpy as np
import csv 
import pandas as pd


wbr = ox.load_workbook('ito11th_June.xlsx')
sheetr = wbr['Sheet1']
csv_file=open('ITO_11thJune.csv','w')
csv_writer=csv.writer(csv_file)
#for the sake of printing after 12 noon the dial goes back to 00:00 - 00:15 
time=int(input('What time interval would you want ?'))
if(time == 15):
	csv_writer.writerow(['0:00 - 00:15','00:15 - 00:30','00:30 - 00:45','00:45 - 01:00','1:00 - 01:15','01:15 - 01:30','01:30 - 01:45','01:45 - 02:00','02:00 - 02:15','02:15 - 02:30','02:30 - 02:45','02:45 - 03:00','03:00 - 03:15','03:15 - 03:30','03:30 - 03:45','03:45 - 04:00','04:00 - 04:15','04:15 - 04:30','04:30 - 04:45','04:45 - 05:00','05:00 - 05:15','05:15 - 05:30','05:30 - 05:45','05:45 - 06:00','06:00 - 06:15','06:15 - 06:30','06:30 - 06:45','06:45 - 07:00','07:00 - 07:15','07:15 - 07:30','07:30 - 07:45','07:45 - 08:00','08:00 - 08:15','08:15 - 08:30','08:30 - 08:45','08:45 - 09:00','09:00 - 09:15','09:15 - 09:30','09:30 - 09:45','09:45 - 10:00','10:00 - 10:15','10:15 - 10:30','10:30 - 10:45','10:45 - 11:00','11:00 - 11:15','11:15 - 11:30','11:30 - 11:45','11:45 - 12:00','0:00 - 00:15','00:15 - 00:30','00:30 - 00:45','00:45 - 01:00','1:00 - 01:15','01:15 - 01:30','01:30 - 01:45','01:45 - 02:00','02:00 - 02:15','02:15 - 02:30','02:30 - 02:45','02:45 - 03:00','03:00 - 03:15','03:15 - 03:30','03:30 - 03:45','03:45 - 04:00','04:00 - 04:15','04:15 - 04:30','04:30 - 04:45','04:45 - 05:00','05:00 - 05:15','05:15 - 05:30','05:30 - 05:45','05:45 - 06:00','06:00 - 06:15','06:15 - 06:30','06:30 - 06:45','06:45 - 07:00','07:00 - 07:15','07:15 - 07:30','07:30 - 07:45','07:45 - 08:00','08:00 - 08:15','08:15 - 08:30','08:30 - 08:45','08:45 - 09:00','09:00 - 09:15','09:15 - 09:30','09:30 - 09:45','09:45 - 10:00','10:00 - 10:15','10:15 - 10:30','10:30 - 10:45','10:45 - 11:00','11:00 - 11:15','11:15 - 11:30','11:30 - 11:45','11:45 - 12:00'])
elif(time == 30):
	csv_writer.writerow(['0:00 - 0:30','0:30 - 1:00','1:00 - 1:30','1:30 - 2:00','2:00 - 2:30','2:30 - 3:00','3:00 - 3:30','3:30 - 4:00','4:00 - 4:30','4:30 - 4:30','4:30 - 5:00','5:00 - 5:30','5:30 - 6:00','6:00 - 6:30','6:30 - 7:00','7:00 - 7:30','7:30 - 8:00','8:00 - 8:30','8:30 - 9:00','9:00 - 9:30','9:30 - 10:00','10:00 - 10:30','10:30 - 11:00','11:00 - 11:30','11:30 - 12:00','0:00 - 0:30','0:30 - 1:00','1:00 - 1:30','1:30 - 2:00','2:00 - 2:30','2:30 - 3:00','3:00 - 3:30','3:30 - 4:00','4:00 - 4:30','4:30 - 4:30','4:30 - 5:00','5:00 - 5:30','5:30 - 6:00','6:00 - 6:30','6:30 - 7:00','7:00 - 7:30','7:30 - 8:00','8:00 - 8:30','8:30 - 9:00','9:00 - 9:30','9:30 - 10:00','10:00 - 10:30','10:30 - 11:00','11:00 - 11:30','11:30 - 12:00'])	
temp=[]
k=1
j=18
i=1
while(j<14611):
    while(k%97!=0):
        r=sheetr['D'+str(j)]
        temp.append(r.value)
        j+=1
        k+=1
    csv_writer.writerow(temp)
    k=1
    temp=[]
 

#csv_writer.writerows(map(lambda x:x,temp))

# print(temp)  
# csv_writer.writerows(map(lambda x:[x],temp))

# np.resize(temp, (-1, 24))
# # print(np.shape(temp))
