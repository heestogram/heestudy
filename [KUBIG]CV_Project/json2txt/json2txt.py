import json
import os

directory = 'annotations'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    data = json.load(f)

    for entry in data:

        annotations = entry['ANNOTATION_INFO']

        txt_path = os.path.join('labels',filename.replace('.json','.txt'))

        with open(txt_path, 'w') as f
            for ann in annotations:
                class_id = 0
                img_width = entry['IMAGE_INFO']['IMAGE_WIDTH']
                img_height = entry['IMAGE_INFO']['IMAGE_HEIGHT']

                #points가 의미하는 게 뭐지?
                x_center = (ann['POINSTS'][0][0] + ann['POINSTS'][0][1]) / 2.0 / img_width
                y_center = (ann['POINSTS'][0][2] + ann['POINSTS'][0][3]) / 2.0 / img_height
                width = (ann['POINSTS'][0][1] - ann['POINSTS'][0][0]) / img_width
                height = (ann['POINSTS'][0][3] - ann['POINSTS'][0][2]) / img_height

                f.write(f"{class_id} {x_center} {y_center} {width} {height}\n")