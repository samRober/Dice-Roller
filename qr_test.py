import cv2 as cv
import sys

img = cv.imread(sys.argv[1], cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
qcd = cv.wechat_qrcode_WeChatQRCode(
        "detect.prototxt", "detect.caffemodel", "sr.prototxt", "sr.caffemodel")
res,points = qcd.detectAndDecode(img)
print(res)
