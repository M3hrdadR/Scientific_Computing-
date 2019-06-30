import cv2
import numpy


def Print_Matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print()


def Dft(matrix):
    mtx = numpy.fft.fft2(matrix)
    mx = numpy.max(numpy.max(numpy.abs(mtx)))
    value = 0.0000000000000000001
    for i in range(len(mtx)):
        for j in range(len(mtx[0])):
            if abs(mtx[i][j]) < value * mx:
                mtx[i][j] = 0
    return numpy.real(numpy.fft.ifft2(mtx))


def Show_Image(arg):
    if type(arg) == str:
        matrix = cv2.imread(arg, 0)
    else:
        matrix = arg
    cv2.imshow('image', matrix)
    cv2.waitKey(0)
    return matrix


def Read_Image(path):
    img = cv2.imread(path)
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img2


matrix = Read_Image('aa.jpg')
Show_Image('aa.jpg')
dft_matrix = Dft(matrix)
Show_Image(dft_matrix)
