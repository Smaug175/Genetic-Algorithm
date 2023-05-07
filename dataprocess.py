#5/5
"""
    删除没有标注的图像，和多标注的图像，只留单标注图像
"""
#读取全部的文件
import os
import shutil

folder_path='labels'
C_path='C'
YOLO_path='YOLO'

C=['C0','C1','C2','C3','C4','C5']

if not os.path.exists(C_path):
    os.makedirs(C_path)
if not os.path.exists(YOLO_path):
    os.makedirs(YOLO_path)
    os.makedirs(os.path.join(YOLO_path,'labels'))
    os.makedirs(os.path.join(YOLO_path, 'imgs'))

for c in C:
    if not os.path.exists(os.path.join(C_path,c)):
        os.makedirs(os.path.join(C_path,c))

#first delete ''
cls=[]
for file_name in os.listdir(folder_path):
    file_path=os.path.join(folder_path,file_name)
    img_path = 'imgs\\' + file_name[:-4] + '.jpg'
    draw_path = 'draw\\' + file_name[:-4] + '.jpg'
    with open(file_path,'r') as file:
        content=file.read()
    #删除没有标注的图像
    if content=='':#如果内容是空，则返回文件名
        #print('file name:',file_name[:-4])
        #同时删除txt文件和img文件
        #print(file_path,img_path)
        os.remove(file_path)
        os.remove(img_path)
        os.remove(draw_path)
        print(file_name,' is delete.')
    #print('content:',content)

    result=content.split('\n')

    num=[]
    for s in result:
        if s!='':
            num.append(int(s[0]))
    cls.append(num[0])

    #删除重复标注的图像
    if len(num)>1:
        x=num[0]
        for i in num:
            if x!=i:
                # print(file_path,img_path)
                os.remove(file_path)
                os.remove(img_path)
                os.remove(draw_path)
                print(file_name, ' is delete.')
                break

    if len(num)==1:
        # print(file_path,img_path)
        os.remove(file_path)
        os.remove(img_path)
        os.remove(draw_path)
        print(file_name, ' is delete.')


cls=[]
for file_name in os.listdir(folder_path):
    file_path=os.path.join(folder_path,file_name)
    img_path = 'imgs\\' + file_name[:-4] + '.jpg'
    draw_path = 'draw\\' + file_name[:-4] + '.jpg'
    with open(file_path,'r') as file:
        content=file.read()

    result=content.split('\n')

    num=[]
    for s in result:
        if s!='':
            num.append(int(s[0]))
    cls.append(num[0])

    copy_path = os.path.join(os.path.join(C_path, C[num[0]]), file_name[:-4] + '.jpg')
    # print(copy_path)
    shutil.copy(img_path, copy_path)

    yolo_img=os.path.join('YOLO\\imgs',file_name[:-4] + '.jpg')
    yolo_label=os.path.join('YOLO\\labels',file_name)
    shutil.copy(img_path,yolo_img)
    shutil.copy(file_path,yolo_label)

clses=[0,0,0,0,0,0]
for i in cls:
    clses[i]+=1
print(clses)#获得每一类的总数


