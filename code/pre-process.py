import json
import os
import zipfile

import cv2 as cv
from tqdm import tqdm

from config import img_height, img_width


def ensure_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

#exract zip and bulid classes files by class and image prepocess
def extract(usage, package, image_path, json_path):
    filename = 'data/{}.zip'.format(package)
    print('Extracting {}...'.format(filename))
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall('data')

    if not os.path.exists('data/{}'.format(usage)):
        os.makedirs('data/{}'.format(usage))
    with open('data/{}/{}'.format(package, json_path)) as json_data:
        data = json.load(json_data) #this is json file
    num_samples = len(data)
    print("num_samples: " + str(num_samples))
    for i in tqdm(range(num_samples)):
        item = data[i]
        image_name = item['image_id']
        label_id = item['label_id']
        src_folder = 'data/{}/{}'.format(package, image_path)
        src_path = os.path.join(src_folder, image_name)
        dst_folder = 'data/{}'.format(usage)
        label = "%02d" % (int(label_id),)
        dst_path = os.path.join(dst_folder, label)

        #
        if not os.path.exists(dst_path):
            os.makedirs(dst_path)
        dst_path = os.path.join(dst_path, image_name)
        src_image = cv.imread(src_path)
        dst_image = cv.resize(src_image, (img_height, img_width), cv.INTER_CUBIC)
        cv.imwrite(dst_path, dst_image)