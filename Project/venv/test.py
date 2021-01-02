"""
import pandas as pd
import matplotlib.ticker as ticker
import matplotlib.cm as cm
import matplotlib as mpl
from matplotlib.gridspec import GridSpec
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")

print(df.head())

from collections import Counter
print(Counter(df['type']))

print(Counter(df['rating']))

print(title_type)


plt.figure(1, figsize=(20,10))
the_grid = GridSpec(2, 2)

cmap = plt.get_cmap('Spectral')
colors = [cmap(i) for i in np.linspace(0, 1, 8)]

plt.subplot(the_grid[0, 1], aspect=1, title='Types of Netflix Titles')
type_show_ids = plt.pie(type_counts, labels=type_labels, autopct='%1.1f%%', shadow=True, colors=colors)
plt.show()

title_rating = df.groupby('rating').agg('count')
rating_labels = title_rating.show_id.sort_values().index
rating_counts = title_rating.show_id.sort_values()

plt.figure(1, figsize=(40,20))
the_grid = GridSpec(2, 2)
cmap = plt.get_cmap('Spectral')
colors = [cmap(i) for i in np.linspace(0, 1, 8)]
plt.subplot(the_grid[0, 1], aspect=1, title='Ratings of Netflix Titles')
type_show_ids = plt.pie(rating_counts, labels=rating_labels, autopct='%1.1f%%', shadow=True, colors=colors)
plt.show()

def group_lower_ranking_values(column):
    rating_counts = df.groupby(column).agg('count')
    pct_value = rating_counts[lambda x: x.columns[0]].quantile(.75)
    values_below_pct_value = rating_counts[lambda x: x.columns[0]].loc[lambda s: s < pct_value].index.values
    def fix_values(row):
        if row[column] in values_below_pct_value:
            row[column] = 'Other'
        return row
    rating_grouped = df.apply(fix_values, axis=1).groupby(column).agg('count')
    return rating_grouped


def group_lower_ranking_values(column):
    ...
    pct_value = rating_counts[lambda x: x.columns[0]].quantile(.99)
    ...
    return rating_grouped
country_grouped = group_lower_ranking_values('country')
country_labels = country_grouped.show_id.sort_values().index
country_counts = country_grouped.show_id.sort_values()
plt.subplot(the_grid[0, 1], aspect=1, title='Country of Netflix Titles')
type_show_ids = plt.pie(country_counts, labels=country_labels, autopct='%1.1f%%', shadow=True, colors=colors)
plt.show()
"""