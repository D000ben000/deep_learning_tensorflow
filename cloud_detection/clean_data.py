from PIL import Image


class clean_data():
    def read_picture(self):
        try:
            im = Image.open('data/test.jpg')
            gray_img = im.conver("L")
        except:
            print "read picture failure!"

        return gray_img

    def apart_picture_into_size(self, data, size = 25):
        pass


def main():
    pass

if __name__ == '__main__':
    main()

