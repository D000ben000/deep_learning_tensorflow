#!/usr/bin/env python
# -*- coding:UTF-8 -*-

"""
    Use CNN cloud dtection
"""


# Step 1: Prepare data for model
from PIL import Image
from numpy.ma import array
import os
import random

train_data_path = "data/train_data/"
class_tags = {"more_cloud": 1, "less_cloud": 0}


def get_train_data():
    data = []
    for class_tag in class_tags:
        data_file_path = train_data_path + class_tag
        data_file_list = os.listdir(data_file_path)
        for data_file in range(1, 5):
            # read picture to im_temp
            im_temp = Image.open(data_file_path + "/" + str(data_file) + ".jpg")
            # ori
            x = array(im_temp)
            data.append([x, class_tags[class_tag]])
            # Left-Right flip
            x = array(im_temp.transpose(Image.FLIP_LEFT_RIGHT))
            data.append([x, class_tags[class_tag]])
            # Top-Bottom flip
            x = array(im_temp.transpose(Image.FLIP_TOP_BOTTOM))
            data.append([x, class_tags[class_tag]])
            # roate 90
            x = array(im_temp.transpose(Image.ROTATE_90))
            data.append([x, class_tags[class_tag]])
            # rotate 180
            x = array(im_temp.transpose(Image.ROTATE_180))
            data.append([x, class_tags[class_tag]])
            # rotate 270
            x = array(im_temp.transpose(Image.ROTATE_270))
            data.append([x, class_tags[class_tag]])

        random.shuffle(data)
    return data

data = get_train_data()
train_data_size = len(data) * 3 / 5
train_data = data[:train_data_size]
test_data = data[train_data_size+1:]

train_data_x = []
train_data_y = []
for line_train_data in train_data:
    train_data_x.append(line_train_data[0])
    train_data_y.append(line_train_data[1])
test_data_x = []
test_data_y = []
for line_test_data in test_data:
    test_data_x.append(line_test_data[0])
    test_data_y.append(line_test_data[1])

# Step 2:
