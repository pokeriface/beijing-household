import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame

def year(yyyyMM: str):
    if (len(yyyyMM) != 7):
        print('error %s' % yyyyMM)
    return yyyyMM[0:4]

candidates = pd.read_csv('data/2020/candidates.txt', sep="\t", names = ['id', 'name', 'birth', 'company', 'score'])
candidates['year'] = candidates['birth'].map(year)
print(candidates[candidates['year'] >= '1985'])
