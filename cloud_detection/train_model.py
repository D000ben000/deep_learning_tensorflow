#!/usr/bin/env python
# -*- coding:UTF-8 -*-

"""
    To get the train_data: train_x and train_y
"""


from PIL import Image
import os


train_data_path = "data/train_data/"
class_tags = {"more_cloud": 1, "less_cloud": 0}


def get_train_data():
    data = []
    for class_tag in class_tags:
        data_file_path = train_data_path + class_tag
        data_file_list = os.listdir(data_file_path)
        for data_file in data_file_list:
            # read picture to im_temp
            im_temp = Image.open(data_file_path + "/" + data_file)
            r_im, c_im = im_temp.size
            x = []
            for h in range(0, r_im):
                for w in range(0, c_im):
                    pixel = im_temp.getpixel((h, w))
                    x.append(pixel)

            data.append([x, class_tags[class_tag]])
    return data


def rename_train_file():
    file_path = "F:/git_repositories/deep_learning_tensorflow/cloud_detection/data/train_data/less_cloud"
    file_list = os.listdir(file_path)
    new_file_name = 1
    for train_file in file_list:
        if train_file is not []:
            file_name = file_path + "/" + train_file
            file_name_new = file_path + "/" + str(new_file_name) + ".jpg"
            os.rename(file_name, file_name_new)
            # print train_file, "----->", str(new_file_name) + ".jpg"
            new_file_name += 1


def main():
    train_data = get_train_data()


if __name__ == '__main__':
    main()
