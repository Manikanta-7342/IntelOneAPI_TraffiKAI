from Audio_Emergency.model_audio import *
from Opencv_Emergency.model_image import *
import time,sys

tick=time.time()

def emergency(e,s,w,n):
    east_path = e
    south_path = s
    west_path = w
    north_path = n

    li1=emergency_audio(east_path,south_path,west_path,north_path,'Audio_Emergency/')
    li2=emergency_image(east_path,south_path,west_path,north_path)
    li=[]

    for i in range(0,3):
        i=int(i)
        t=li1[i]*0.8+li2[i]*0.1
        li.append(1) if t>0.5 else li.append(0)


    with open('Resources/text_files/emer.txt', 'w') as file:
        file.write(str(li))

    print('\n\n', 'Time taken: ', time.time() - tick)
