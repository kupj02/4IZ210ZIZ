import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv('healthcare-dataset-stroke-data.csv')
fig, axs = plt.subplots(2, 3)
axs[0, 0].hist(df.stroke)
axs[0, 0].set_title('histogram infarktů')
axs[0, 1].hist(df.smoking_status)
axs[0, 1].set_title('histogram kouření')
axs[0, 2].hist(df.age)
axs[0, 2].set_title('histogram věků')
axs[1, 0].scatter(df.age,df.stroke)
axs[1, 0].set_title('scatterplot věků a infarktů')
axs[1, 1].scatter(df.smoking_status,df.stroke)
axs[1, 1].set_title('scatterplot kouření a infarktů')
axs[1, 2].scatter(df.bmi,df.stroke)
axs[1, 2].set_title('scatterplot BMI a infarktů')
plt.show()