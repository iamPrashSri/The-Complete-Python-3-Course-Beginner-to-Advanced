import pandas as pd
import matplotlib.pyplot as plt

#  Creating an object of this type is very tedious and can be done easily using Pandas Library
# data = [
#     {
#         'name': 'Nick',
#         'jan_ir': 124,
#         'feb_ir': 100,
#         'mar_ir': 165
#     },
#     {
#         'name': 'Panda',
#         'jan_ir': 112,
#         'feb_ir': 143,
#         'mar_ir': 3
#     }]

raw_data = {'names': ['Nick', 'Panda', 'S', 'Ari', 'Valos'],
            'jan_ir': [143, 122, 101, 106, 365],
            'feb_ir': [122, 132, 144, 98, 62],
            'mar_ir': [65, 88, 12, 32, 65]}

dataFrwk = pd.DataFrame(raw_data, columns=['names', 'jan_ir', 'feb_ir', 'mar_ir'])

dataFrwk['total_ir'] = dataFrwk['jan_ir'] + dataFrwk['feb_ir'] + dataFrwk['mar_ir']

color = [(1, 0.4, 0.4), (1, .6, 1), (.5, .3, 1), (.3, 1, .5), (.7, .7, .2)]

print(dataFrwk)
plt.pie(dataFrwk['total_ir'],
        labels=dataFrwk['names'],
        colors=color,
        autopct='%1.1f%%')
plt.show()
