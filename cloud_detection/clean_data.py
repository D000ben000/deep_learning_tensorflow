#!/usr/bin/env python
# -*- coding:UTF-8 -*-

"""
    From the data/gray.jpg get train data and put into data/train_data, more_cloud and less_cloud
    After that, we do delete the unqualified samples
"""

from PIL import Image


save_path = "data/"
train_data_path = "data/train_data/"
class_tags = {"more_cloud": 1, "less_cloud": 0}


def read_picture():
    try:
        im = Image.open('data/gray.jpg', 'r')
        return im
    except IOError, e:
        print "read picture failure!", "--", e
        return None


def save_train_data(tran_data, name):
    """
    :param tran_data:
    :param name:
    :return:
    """
    pass


def apart_picture_into_size(size=25):
    """
    Args:
        size:
            the size of picture cut
    Returns:
        save the picture
    """
    im_save_name = 1
    read_img = read_picture()
    if read_img is None:
        print "read_img is None!"
        return
    (r, c) = read_img.size
    r_num = int(r/size)
    c_num = int(c/size)
    for i in range(r_num):
        for j in range(c_num):
            box = (i*size, j*size, (i + 1)*size, (j + 1)*size)
            # print box
            temp = read_img.crop(box)
            save_name = train_data_path + "less_cloud/" + str(im_save_name) + ".jpg"
            temp.save(save_name, 'JPEG')
            im_save_name += 1


def main():
    # apart_picture_into_size()
    get_data = read_picture()
    get_data.show()


if __name__ == '__main__':
    main()

