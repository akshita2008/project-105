import os
import cv2

path = './images'


images = []


for file in os.listdir(path):
    name, extension = os.path.splitext(file)

    
    if extension in ['.jpg', '.jpeg', '.png']:
        file_name =path+"/"+file
     
        images.append(file_name)
        print(file_name)
count = len(images)
print(count)

frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width, height)

out = cv2.VideoWriter('Project.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 1, size)

for i in range(0,count):
    print(images[i])
    img = cv2.imread(images[i])

   
    out.write(img)

out.release()
print("Done")
