#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]
#########################################################
### your code goes here ###

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

clf = SVC(C=10000, kernel="rbf")

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t1, 3), "s"

accuracy = accuracy_score(labels_test, pred)
print "accuracy:", accuracy

print "element 10:", pred[10]
print "element 26:", pred[26]
print "element 50:", pred[50]

print "# Chris:", sum(pred)

#########################################################

# output
'''
    no. of Chris training emails: 7936
    no. of Sara training emails: 7884
    C= 10
    training time: 0.121 s
    prediction time: 1.214 s
    accuracy: 0.616040955631
    C= 100
    training time: 0.117 s
    prediction time: 1.211 s
    accuracy: 0.616040955631
    C= 1000
    training time: 0.114 s
    prediction time: 1.173 s
    accuracy: 0.821387940842
    C= 10000
    training time: 0.112 s
    prediction time: 0.965 s
    accuracy: 0.892491467577

    element 10: 1
    element 26: 0
    element 50: 1

    # Chris: 877
'''
