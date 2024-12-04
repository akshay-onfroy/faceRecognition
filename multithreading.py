from deepface import DeepFace
import threading
import os
lists = os.listdir("imgs/")
source ="imgs/5.jpg"
img_list=[]
thread_list=[]
def verification(img2):
    global source
    for image in img2:
        para ="/Users/akshay/Documents/Work/faceClustering/imgs/" + image
        response = DeepFace.verify(img1_path = source, img2_path = para , enforce_detection=False )
        if response["verified"]:
            img_list.append(image)
filtered_list = [file for file in lists if not file.endswith('.pkl')]
chunk_size = 3
split_list = [filtered_list[i:i + chunk_size] for i in range(0, len(filtered_list), chunk_size)]
for i in split_list:
    run_thread = threading.Thread(target= verification,args=(i,))
    thread_list.append(run_thread)
    run_thread.start()
for i in thread_list:
    i.join()
'''
for i in split_list:
    verification(i) #14 seconds
print(img_list)'''