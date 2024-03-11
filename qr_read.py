import cv2 as cv
import sys

def read_qr(img):

        qcd = cv.wechat_qrcode_WeChatQRCode(
                "detect.prototxt", "detect.caffemodel", "sr.prototxt", "sr.caffemodel")
        res,points = qcd.detectAndDecode(img)
        return res

if __name__ == "__main__":
        img = cv.imread("qrcodes.png", cv.IMREAD_GRAYSCALE)
        output = read_qr(img)
        print(type(output))

