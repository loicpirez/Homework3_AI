import csv
from Parsing import *

def pars():
    c = {}
    first_b = {}
    second_b = {}
    third_b = {}
    ss = {}
    of = {}

    with open("./data/dataset.csv", "rt") as file:
        reader = csv.reader(file, delimiter=';', quotechar='|')
        for r in reader:
            #print(r)
            if r[2] == "C":
                c[r[0]] = (float(r[1]), float(r[3]))
            elif r[2] == "1B":
                first_b[r[0]] = (float(r[1]), float(r[3]))
            elif r[2] == "2B":
                second_b[r[0]] = (float(r[1]), float(r[3]))
            elif r[2] == "3B":
                third_b[r[0]] = (float(r[1]), float(r[3]))
            elif r[2] == "SS":
                ss[r[0]] = (float(r[1]), float(r[3]))
            elif r[2] == "OF":
                of[r[0]] = (float(r[1]), float(r[3]))
    return c, first_b, second_b, third_b, ss, of

def getIAResult():
    res = pars()
    return myAlgo(res[0], res[1], res[2], res[3], res[4], res[5], 100)
