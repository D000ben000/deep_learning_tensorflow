from PIL import Image


save_path = "data/"


def read_picture():
    try:
        im = Image.open('data/test.jpg')
        gray_img = im.convert("L")
        return gray_img
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
    for i in range(10):
        for j in range(3):
            box = (i*size, j*size, (i + 1)*size, (j + 1)*size)
            # print box
            temp = read_img.crop(box)
            save_name = save_path + str(im_save_name) + ".jpg"
            temp.save(save_name, 'JPEG')
            im_save_name += 1


def main():
    apart_picture_into_size()

if __name__ == '__main__':
    main()

