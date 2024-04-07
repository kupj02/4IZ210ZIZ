import numpy as np
import pandas as pd

from modeling_tree import clf

df = pd.read_csv('healthcare-dataset-stroke-data.csv')

sample = []
sample.gender = 1
sample.age = 65
sample.hypertension = 0
sample[:] = np.nan
print(clf.predict(sample))
