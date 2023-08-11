import json
import os

os.chdir('[KUBIG]CV_Project/json2txt')

directory = 'annotations'

class_num=0

for foldername in os.listdir(directory):
    
    for filename in os.listdir(os.path.join(directory,foldername)):
        with open(os.path.join(directory, foldername, filename), 'r', encoding='UTF8') as f:
            data = json.load(f)

            annotations = data['ANNOTATION_INFO']
            txt_path = os.path.join('labels',filename.replace('.json','.txt'))

            # 저장할 때도 class 별로 폴더 달리 해서 저장하는 게 나은가?
            # 아니면 일괄적으로 모아놓는 게 나은가?
            with open(txt_path, 'w') as f:
                for ann in annotations:
                    class_id = class_num
                    img_width = data['IMAGE_INFO']['IMAGE_WIDTH']
                    img_height = data['IMAGE_INFO']['IMAGE_HEIGHT']

                    # points에 있는 좌표 4개가 각각 뭐지?
                    # points가 4개가 아니라 2개로 이루어진 애들도 있는데 뭐지
                    x_center = abs(ann['POINTS'][0][0] + ann['POINTS'][0][2]) / 2.0 / img_width
                    y_center = abs(ann['POINTS'][0][1] + ann['POINTS'][0][3]) / 2.0 / img_height
                    width = abs(ann['POINTS'][0][2] - ann['POINTS'][0][0]) / img_width
                    height = abs(ann['POINTS'][0][3] - ann['POINTS'][0][1]) / img_height

                    f.write(f"{class_id} {x_center} {y_center} {width} {height}\n")
    class_num+=1