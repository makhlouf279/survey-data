import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from IPython.display import display


df_sur =pd.read_csv("https://cocl.us/datascience_survey_data",index_col=0)
pd.options.display.max_columns = None 
display(df_sur)
print(df_sur.shape)

#create this bar chart
#Sort the dataframe in descending order of Very interested.
df_sur.sort_values(by='Very interested', ascending=False, axis=0, inplace=True)
print(df_sur)

# Bar chart
colors_list = ['#5cb85c','#5bc0de','#d9534f']
df_sur = df_sur.div(df_sur.sum(1), axis=0)
ax = df_sur.plot(kind='bar',figsize=(20,8),width = 0.8,color = colors_list,edgecolor=None)
plt.legend(labels=df_sur.columns,fontsize= 14)
plt.title("Percentage of Respondents' Interest in Data Science Areas",fontsize= 16)
plt.xticks(fontsize= 14)
#remove the left, top, and right borders.
for spine in plt.gca().spines.values():
    spine.set_visible(False)
plt.yticks([])

# Add this loop to add the annotations
for p in ax.patches:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy() 
    ax.annotate(f'{height:.0%}', (x + width/2, y + height*1.02), ha='center')
