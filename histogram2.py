import pandas as pd
from matplotlib import pyplot as plt


data = pd.read_csv('~/Downloads/git/CoreySchafer/Python/Matplotlib/06-Histograms/data.csv')
ids = data['Responder_id']
ages = data['Age']
#print(data.head(5))
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, bins=bins, edgecolor='black', log=True)
median_age = 29
color = '#fc4f30'
plt.axvline(median_age, color=color, label='Age Median', linewidth=2)

plt.style.use('fivethirtyeight')
plt.legend()
plt.title('Age of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')
plt.tight_layout()

plt.show()
