from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('healthcare-dataset-stroke-data.csv')
fig, axs = plt.subplots(3, 4)
axs[0, 0].hist(df.stroke)
axs[0, 0].set_title('histogram infarktů')
axs[0, 1].hist(df.smoking_status)
axs[0, 1].set_title('histogram kouření')
axs[0, 2].hist(df.age)
axs[0, 2].set_title('histogram věků')
axs[0, 3].hist(df.bmi)
axs[0, 3].set_title('histogram BMI')
c1 = Counter(zip(df.age,df.stroke))
s1 = [5*c1[(x1,y1)] for x1,y1 in zip(df.age,df.stroke)]
axs[1, 0].scatter(df.age, df.stroke, s=s1)
axs[1, 0].set_title('scatterplot věků a infarktů')
c2 = Counter(zip(df.smoking_status,df.stroke))
s2 = [5*c2[(x1,y1)] for x1,y1 in zip(df.smoking_status, df.stroke)]
axs[1, 1].scatter(df.smoking_status,df.stroke, s=s2)
axs[1, 1].set_title('scatterplot kouření a infarktů')
c3 = Counter(zip(df.bmi,df.stroke))
s3 = [5*c3[(x1,y1)] for x1,y1 in zip(df.bmi,df.stroke)]
axs[1, 2].scatter(df.bmi,df.stroke, s=s3,)
axs[1, 2].set_title('scatterplot BMI a infarktů')
c4 = Counter(zip(df.hypertension,df.stroke))
s4 = [5*c4[(x1,y1)] for x1,y1 in zip(df.hypertension,df.stroke)]
axs[1, 3].scatter(df.hypertension,df.stroke, s=s4)
axs[1, 3].set_title('scatterplot hypertenze a infarktů')
axs[2, 0].hist(df.avg_glucose_level)
axs[2, 0].set_title('histogram hladiny glukózy')
c5 = Counter(zip(df.avg_glucose_level,df.stroke))
s5 = [5*c5[(x1,y1)] for x1,y1 in zip(df.avg_glucose_level,df.stroke)]
axs[2, 1].scatter(df.avg_glucose_level,df.stroke, s=s5)
axs[2, 1].set_title('scatterplot hladiny glukózy a infarktů')
axs[2, 2].hist(df.heart_disease)
axs[2, 2].set_title('histogram srdečních onemocnění')
c6 = Counter(zip(df.heart_disease,df.stroke))
s6 = [5*c6[(x1,y1)] for x1,y1 in zip(df.heart_disease,df.stroke)]
axs[2, 3].scatter(df.heart_disease,df.stroke, s=s6)
axs[2, 3].set_title('scatterplot hladiny glukózy a infarktů')

plt.show()