#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data)
# print len(enron_data["SKILLING JEFFREY K"])
#
countS = 10
countP = 10
for p in enron_data:
    if enron_data[p]["poi"] == 1:
        countP += 1
        print p, enron_data[p]["total_payments"]
    if enron_data[p]["total_payments"] == "NaN":
        countS += 1
print countS * 1.0 / countP, countP, countS

# # for f in enron_data["PRENTICE JAMES"]:
# #     print f
# #     print enron_data["PRENTICE JAMES"][f]
#
#
# print enron_data["SKILLING JEFFREY K"]["total_payments"]
# print enron_data["FASTOW ANDREW S"]["total_payments"]
# print enron_data["LAY KENNETH L"]["total_payments"]

# feature_list = []
# for f in enron_data["PRENTICE JAMES"]:
#     feature_list.append(f)
#
# from tools.feature_format import featureFormat
#
# featureFormat(enron_data, feature_list)
