import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import Series
from pandas import DataFrame

candidates = pd.read_csv('./data/2020/candidates.txt', sep="\t", names = ['id', 'name', 'birth', 'company', 'score'])

print("count:") 
print(candidates.count())

print()

print("type:")
print(type(candidates.values))