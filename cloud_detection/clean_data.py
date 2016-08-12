from PIL import Image


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
    read_img = read_picture()
    if read_img is None:
        print "read_img is None!"

    else:
        picture_size = read_img.size


def main():
    apart_picture_into_size()


if __name__ == '__main__':
    main()

