import os

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/diabetes/diabetes.data',
                 sep=' ',
                 header=None)
df.columns = ['AGE', 'SEX', 'BMI', 'BP', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'Y']
fig, axes = plt.subplots(2, 1, figsize=(8,8))

axes.scatter(df['AGE'], df['SEX'], s=10, label='DIABETES_CLASS', color='green', marker='^')
axes.set_title('AGE vs GENDER')
axes.set_xlabel('AGE')
axes.set_ylabel('SEX')
axes.legend()