# Traffic Light Classifier

A sub project of CarND-Capstone.

Traffic Light Classifier using gcForest + Traffic Light Detector using Tensorflow Object Detection Api

## Dependencies

Required packages:
 - Numpy
 - Scikit-Learn
 - joblib
 - OpenCV2+
 - gcForest(https://github.com/kingfengji/gcForest) * included into the project as a project lib(not necessary to install it)
 - Tensorflow-gpu/ Tensorflow models
 - Coco faster_rcnn_resnet101_coco_11_06_2017 model

## Example Use


## Test Log

    March 8th

    1. prepare_trafficlight
        conflict use for main and tl_classifier_test
    2. tlc.gc.predict()
        AttributeError: 'TLClassifier' object has no attribute 'gc'

