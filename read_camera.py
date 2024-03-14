#import character_recognition
import colour_recognition
import qr_read
import take_picutre
import dice_seperation
import sys
import enum
import cv2 as cv

class recognition_type(enum.Enum):
    QR = 1
    COLOUR = 2
    TESSERACT = 3
    COLOUR_HSV = 4

class camera_reader():

    def __init__(self):
        self.camera = take_picutre.cam()

    def read_camera(self, type_of_recognition:recognition_type):
        img = self.camera.take_picture()
        #cv.imwrite("img.jpg",img)
        #cv.waitKey(0)
        outputs = ()
        if(type_of_recognition == recognition_type.QR):
            grey_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

            outputs = qr_read.read_qr(grey_img)


        else:
            seperate_imgs = dice_seperation.seperate_image(img)
            for individual_img in seperate_imgs:
                match(type_of_recognition):
                    case recognition_type.COLOUR:
                        outputs = outputs + (colour_recognition.result_from_colour(individual_img),)
                    case recognition_type.COLOUR_HSV:
                        outputs = outputs + (colour_recognition.result_from_colour_hsv(individual_img),)
                    case recognition_type.TESSERACT:
                        grey_img = cv.cvtColor(individual_img,cv.COLOR_BGR2GRAY)
                    # character_recognition.read_image(grey_img)
        return outputs

if __name__ == "__main__":
    cr = camera_reader()
    print(cr.read_camera(recognition_type.COLOUR_HSV))
