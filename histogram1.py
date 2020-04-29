# https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Matplotlib/06-Histograms

import pandas as pd
from matplotlib import pyplot as plt

ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, bins=bins, edgecolor='black')
plt.style.use('fivethirtyeight')
plt.title('Age of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')
plt.tight_layout()

plt.show()
