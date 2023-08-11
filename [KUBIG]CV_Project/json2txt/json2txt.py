import json
import os

directory = '[KUBIG]CV_Project/json2txt/annotations'

print(os.getcwd())

for filename in os.listdir(directory):
    
    with open(os.path.join(directory, filename), 'r', encoding='UTF8') as f:
        data = json.load(f)

        annotations = data['ANNOTATION_INFO']
        txt_path = os.path.join('[KUBIG]CV_Project/json2txt/labels',filename.replace('.json','.txt'))

        with open(txt_path, 'w') as f:
            for ann in annotations:
                print(ann)
                class_id = 0
                img_width = data['IMAGE_INFO']['IMAGE_WIDTH']
                img_height = data['IMAGE_INFO']['IMAGE_HEIGHT']

                #points가 의미하는 게 뭐지?
                x_center = (ann['POINTS'][0][0] + ann['POINTS'][0][1]) / 2.0 / img_width
                y_center = (ann['POINTS'][0][2] + ann['POINTS'][0][3]) / 2.0 / img_height
                width = (ann['POINTS'][0][1] - ann['POINTS'][0][0]) / img_width
                height = (ann['POINTS'][0][3] - ann['POINTS'][0][2]) / img_height

                f.write(f"{class_id} {x_center} {y_center} {width} {height}\n")