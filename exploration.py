from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('healthcare-dataset-stroke-data.csv')
fig, axs = plt.subplots(3, 4, figsize=[10, 8])
for ax in axs.flat:
    ax.tick_params(axis='both', which='major', labelsize=6)
    ax.tick_params(axis='both', which='minor', labelsize=6)

axs[0, 0].hist(df.stroke, color = 'teal')
axs[0, 0].set_title('histogram infarktů', fontsize = 9)
axs[0, 0].set_xlabel('infarkt ano/ne', fontsize = 6)
axs[0, 0].set_ylabel('počet lidí', fontsize = 6)

axs[0, 1].hist(df.smoking_status, color = 'teal')
axs[0, 1].set_title('histogram kouření',fontsize = 9)
axs[0, 1].tick_params(axis='x', rotation=-15, labelsize=6)
axs[0, 1].set_ylabel('počet lidí', fontsize = 6)

axs[0, 2].hist(df.age, color = 'teal', bins = 30)
axs[0, 2].set_title('histogram věku', fontsize = 9)
axs[0, 2].set_xlabel('věkové rozpětí', fontsize = 6)
axs[0, 2].set_ylabel('počet lidí', fontsize = 6)

axs[0, 3].hist(df.bmi, color = 'teal', bins = 20)
axs[0, 3].set_title('histogram BMI', fontsize = 9)
axs[0, 3].set_xlabel('BMI', fontsize = 6)
axs[0, 3].set_ylabel('počet lidí', fontsize = 6)

c1 = Counter(zip(df.age,df.stroke))
s1 = [3*c1[(x1,y1)] for x1,y1 in zip(df.age,df.stroke)]
axs[1, 0].scatter(df.age, df.stroke, alpha = 0.1, color = 'teal', s=s1)
axs[1, 0].set_title('scatterplot věků a infarktů', fontsize = 9)
axs[1, 0].set_xlabel('věk', fontsize = 6)
axs[1, 0].set_ylabel('infarkt ano/ne', fontsize = 6)

c2 = Counter(zip(df.smoking_status, df.stroke))
s2 = [c2[(x1,y1)] for x1,y1 in zip(df.smoking_status, df.stroke)]
axs[1, 1].scatter(df.smoking_status, df.stroke, alpha = 0.1, color = 'teal', s=s2)
axs[1, 1].set_title('scatterplot kouření a infarktů', fontsize = 9)
axs[1, 1].tick_params(axis='x', rotation=-15, labelsize=6)
axs[1, 1].set_ylabel('infarkt ano/ne', fontsize = 6)

c3 = Counter(zip(df.bmi,df.stroke))
s3 = [5*c3[(x1,y1)] for x1,y1 in zip(df.bmi,df.stroke)]
axs[1, 2].scatter(df.bmi,df.stroke, alpha = 0.1, color = 'teal', s=s3)
axs[1, 2].set_title('scatterplot BMI a infarktů', fontsize = 9)
axs[1, 2].set_xlabel('BMI', fontsize = 6)
axs[1, 2].set_ylabel('infarkt ano/ne', fontsize = 6)

c4 = Counter(zip(df.hypertension,df.stroke))
s4 = [c4[(x1,y1)] for x1,y1 in zip(df.hypertension,df.stroke)]
axs[1, 3].scatter(df.hypertension,df.stroke, alpha = 0.1, color = 'teal', s=s4)
axs[1, 3].set_title('scatterplot hypertenze a infarktů', fontsize = 9)
axs[1, 3].set_xlabel('hypertenze ano/ne', fontsize = 6)
axs[1, 3].set_ylabel('infarkt ano/ne', fontsize = 6)

axs[2, 0].hist(df.avg_glucose_level, color = 'teal', bins = 30)
axs[2, 0].set_title('histogram hladiny glukózy', fontsize = 9)
axs[2, 0].set_xlabel('hladina glukózy', fontsize = 6)
axs[2, 0].set_ylabel('počet lidí', fontsize = 6)

c5 = Counter(zip(df.avg_glucose_level,df.stroke))
s5 = [15*c5[(x1,y1)] for x1,y1 in zip(df.avg_glucose_level,df.stroke)]
axs[2, 1].scatter(df.avg_glucose_level,df.stroke, alpha = 0.05, color = 'teal', s=s5)
axs[2, 1].set_title('scatterplot hladiny glukózy\n a infarktů', fontsize = 9)
axs[2, 1].set_xlabel('hladina glukózy', fontsize = 6)
axs[2, 1].set_ylabel('infarkt ano/ne', fontsize = 6)

axs[2, 2].hist(df.heart_disease, color = 'teal')
axs[2, 2].set_title('histogram srdečních\n onemocnění', fontsize = 9)
axs[2, 2].set_xlabel('srdeční onemocnění ano/ne', fontsize = 6)
axs[2, 2].set_ylabel('počet lidí', fontsize = 6)

c6 = Counter(zip(df.heart_disease,df.stroke))
s6 = [c6[(x1,y1)] for x1,y1 in zip(df.heart_disease,df.stroke)]
axs[2, 3].scatter(df.heart_disease,df.stroke, alpha = 0.05, color = 'teal', s=s6)
axs[2, 3].set_title('scatterplot srdečních onemocnění\n a infarktů', fontsize = 9)
axs[2, 3].set_xlabel('srdeční onemocnění ano/ne', fontsize = 6)
axs[2, 3].set_ylabel('infarkt ano/ne', fontsize = 6)

plt.subplots_adjust(hspace=0.75, wspace=0.5)
plt.show()