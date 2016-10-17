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
            box = ((i-1)*size, (j-1)*size, i*size, j*size)
            temp = read_img.crop(box)
            save_name = save_path + str(im_save_name)
            temp.save(save_name, 'JPEG')
            im_save_name += 1


def main():
    apart_picture_into_size()

if __name__ == '__main__':
    main()

