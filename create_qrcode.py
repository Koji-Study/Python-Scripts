# ! -*- coding: utf-8 -*-
import qrcode

def create():
    qr = qrcode.QRCode(
        #version表示生成二维码的尺寸的大小，1-40，最小21*21，version加1，尺寸加4个单位，version为2,尺寸是25*25
        version=2,
        #容错系数
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        #二维码中每个格子的像素大小
        box_size=10,
        #边框格子的宽度，默认4
        border=1
    )
    qr.add_data("🧡I Love You~🧡")
    qr.make(fit=True)
    #保存为文件
    img = qr.make_image()
    img.save("QRcode.png")

if __name__ == '__main__':
    create()
