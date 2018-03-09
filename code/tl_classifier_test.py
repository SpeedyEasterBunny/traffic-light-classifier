# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 08:16:48 2018

@author: Danilo Canivel
This need to be runned at the cli just when you want to generate a new trained model
"""
from tl_classifier import TLClassifier
#from sklearn.metrics import accuracy_score

clf = TLClassifier(for_real=True)

test_red_batch = ['../data/google/red1.png',
                  '../data/google/red2.png']

test_green_batch = ['../data/google/green1.jpg',
                    '../data/google/green2.png',
                    '../data/google/green3.png']

#test_red_batch = ['../data/test_images/img_10.jpg',
#                  '../data/test_images/img_17.jpg',
#                  '../data/test_images/img_18.jpg']
#
#test_green_batch = ['../data/test_images/img_9.jpg',
#                    '../data/test_images/img_12.jpg',
#                    '../data/test_images/img_13.jpg',
#                    '../data/test_images/img_14.jpg',
#                    '../data/test_images/img_15.jpg',
#                    '../data/test_images/img_16.jpg']

test_yellow_single = '../data/google/yellow1.png'

test_red_yellow_batch = ['../data/google/red1.png',
                         '../data/google/yellow2.png',
                         '../data/google/red2.png']


def tlc_test_batch(test_images):
    state = clf.get_classification_batch_argmax(image_list=test_images, save_tl=False)
    if state == 0:
        print('RED', state)
    elif state == 1:
        print('YELLOW', state)
    elif state == 2:
        print('GREEN', state)
    else:
        print('UNKNOWN', state)


def tlc_test_single(test_image):
    state = clf.get_classification(image=test_image)
    if state == 0:
        print('RED', state)
    elif state == 1:
        print('YELLOW', state)
    else:
        print('GREEN', state)


def main():
    # test
    print('Test 01: Testing RED')
    tlc_test_batch(test_red_batch)

    # test
    print('Test 02: Testing Green')
    tlc_test_batch(test_green_batch)

    # test
    print('Test 03: Testing Yellow Single')
    #tlc_test_single(test_yellow_single)

    # test
    print('Test 04: Testing RED & Yellow Mixed')
    print('Should return RED ...')
    tlc_test_batch(test_red_yellow_batch)


if __name__ == "__main__":
    main()
