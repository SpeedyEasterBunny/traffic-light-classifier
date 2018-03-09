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

## Installation

```
pip install -r requirements.txt
```

Or create a virtual environment with Anaconda:

```
conda env create -f environment.yml
```

## Example Use

1. test tf_classifier

```
cd code
python tf_classifier_test.py
```

2. main

```
cd code
python main.py
```

## Test Log

    March 8th

    1. prepare_trafficlight
        conflict use for main and tl_classifier_test
    2. tlc.gc.predict()
        AttributeError: 'TLClassifier' object has no attribute 'gc'

