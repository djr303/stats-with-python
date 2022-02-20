import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Gender': ['f', 'f', 'm', 'f', 'm',
               'm', 'f', 'm', 'f', 'm', 'm'], 'TV': [3.4, 3.5, 2.6, 4.7, 4.1, 4.1, 5.1, 3.9, 3.7, 2.1, 4.3]})

grouped = data.groupby('Gender')
print(grouped.describe())
grouped.boxplot()
plt.show()

print(grouped.describe())

df_female = grouped.get_group('f')
print('df_female', df_female)

values_female = grouped.get_group('f').values
print('values_female', values_female)