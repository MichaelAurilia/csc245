# Importing necessary libraries
from gettext import install

import numpy as np
import pandas as pd
import warnings

import pip

# Ignore all warnings
warnings.filterwarnings('ignore')

# Reading the CSV file into a DataFrame
df = pd.read_csv('movies.csv')
df.info()

# Printing the first few rows of the DataFrame
print(df.head())

# Calculating the percentage of missing values in each column
missing_percent = (df.isnull().sum() / len(df)) * 100

# Printing the number of null values in each column
print(missing_percent)

# Dropping unnecessary columns from the DataFrame
df = df.drop(['movie_id', 'link', 'cast_id', 'writer_id', 'review_id', 'director_id', 'user_id'], axis=1)
print(df.head())

# Removing commas and converting 'imbd_votes' column values to integers
df['imbd_votes'] = df['imbd_votes'].apply(lambda x: int(x.replace(",", "")))
print(df.head())
df.info()

# Printing the number of unique values in the 'certificate' column
print(df['certificate'].nunique())

# Printing the unique values in the 'certificate' column
print(df['certificate'].unique())

# Installing and importing the 'plotly' library

import plotly.express as px

# Creating an interactive scatter plot using plotly
fig = px.scatter(df, x='imbd_rating', y='certificate', color='certificate',
                 hover_name='title', title='IMDB Rating vs. Certificate')
fig.update_layout(
    xaxis_title='IMDB Rating',
    yaxis_title='Certificate',
    legend_title='Certificate'
)
fig.show()

# Performing one-hot encoding on the 'certificate' column
df = pd.get_dummies(df, columns=['certificate'])
df.info()

# Function to convert duration to minutes
def convert_duration(duration_str):
    if 'h ' in duration_str:
        hours, minutes = duration_str.split('h ')
        hours = int(hours)
        minutes = int(minutes[:-1])
    else:
        hours = 0
        minutes = int(duration_str[:-1])
    total_minutes = hours * 60 + minutes
    return total_minutes

# Applying the duration conversion function to the 'duration' column
df['duration'] = df['duration'].apply(convert_duration)
df.info()

# Creating an interactive scatter plot using plotly
fig = px.scatter(df, x='imbd_rating', y='genre', color='genre',
                 hover_name='title', title='IMDB Rating vs. Genre')
fig.update_layout(
    xaxis_title='IMDB Rating',
    yaxis_title='Genre',
    legend_title='Genre'
)
fig.show()

# Creating an interactive scatter plot using plotly
fig = px.scatter(df, x='imbd_rating', y='imbd_votes', color='genre',
                 hover_name='director_name', title='IMDb Rating vs. IMDb Votes for All genre')
fig.update_layout(
    xaxis_title='IMDb Rating',
    yaxis_title='IMDb Votes',
    legend_title='genre'
)
fig.show()

# Printing the number of unique values in the 'genre' column
print(df['genre'].nunique())

# Printing the unique values in the 'genre' column
print(df['genre'].unique())

# Importing MultiLabelBinarizer from sklearn.preprocessing
from sklearn.preprocessing import MultiLabelBinarizer

# Creating a MultiLabelBinarizer object
mlb = MultiLabelBinarizer()

# Applying MultiLabelBinarizer on the 'genre' column
genres = df['genre'].apply(lambda x: x.split(','))
genre_binary = mlb.fit_transform(genres)

# Creating a new dataframe with the binary variables
genre_df = pd.DataFrame(genre_binary, columns=mlb.classes_)

# Concatenating the genre_df with the original dataframe
df = pd.concat([df, genre_df], axis=1)
df.head()

# Dropping the 'genre' column from the DataFrame
df = df.drop('genre', axis=1)
df.info()

# Calculating the correlation matrix
corr_matrix = df.corr()
print(corr_matrix)

# Creating a heatmap of the correlation matrix using plotly
import plotly.express as px
fig = px.imshow(corr_matrix, color_continuous_scale='RdBu', zmin=-1, zmax=1)
fig.update_layout(
    xaxis=dict(title='Features'),
    yaxis=dict(title='Features'),
    title='Correlation Matrix Heatmap'
)
fig.show()

# Removing duplicated columns from the DataFrame
df = df.loc[:, ~df.columns.duplicated()]

# Calculating correlation of each column with the 'rank' column
rank_corr = df.corrwith(df['rank'])
print(rank_corr)

# Grouping the data by year and selecting the top 5 movies with the most imbd_votes
yearly_votes = df.groupby('year').apply(lambda x: x.nlargest(5, 'imbd_votes')).reset_index(drop=True)

# Creating an interactive scatter plot of the data using plotly
fig = px.scatter(yearly_votes, x='year', y='imbd_votes', hover_name='title',
                 hover_data={'imbd_rating': True, 'director_name': True},
                 labels={'year':'Year', 'imbd_votes':'Total IMBD Votes'},
                 title='Most Rated Movies by Year')
fig.show()

# Creating an interactive scatter plot of the data using plotly
fig = px.scatter(df, x='imbd_votes', y='imbd_rating', hover_name='title',
                 hover_data={'year': True, 'director_name': True},
                 labels={'imbd_votes':'Total IMBD Votes', 'imbd_rating': 'IMBD Rating'},
                 title='IMBD Votes vs. IMBD Rating')
fig.show()

# Creating an interactive scatter plot of the data using plotly
fig = px.scatter(df, x='imbd_rating', y='duration', hover_name='title',
                 hover_data={'year': True, 'imbd_votes': True},
                 labels={'imbd_rating':'IMBD Rating', 'duration':'Duration (minutes)'},
                 title='IMBD Rating vs. Movie Duration')
fig.show()

# Creating an interactive scatter plot of the data using plotly
fig = px.scatter(df, x='imbd_rating', y='director_name',
                 hover_name='title', title='IMDb Rating vs. Director Name')
fig.update_layout(
    xaxis_title='IMDb Rating',
    yaxis_title='Director Name',
    legend_title='Director Name'
)
fig.show()

# Finding the director with the highest average IMDb rating and sum of IMDb votes
director = df.groupby('director_name').agg({'imbd_rating': 'mean', 'imbd_votes': 'sum'}).sort_values(['imbd_rating', 'imbd_votes'], ascending=False).head(1).index[0]

# Creating an interactive scatter plot of the data using plotly
fig = px.scatter(df, x='imbd_rating', y='imbd_votes',
                 hover_name='title', title=f'IMDb Rating vs. IMDb Votes for all Director')
fig.update_layout(
    xaxis_title='IMDb Rating',
    yaxis_title='IMDb Votes',
    legend_title='Title'
)
fig.show()

# Creating an interactive scatter plot of the data using plotly
fig = px.scatter(df, x='imbd_rating', y='imbd_votes', color='director_name',
                 hover_name='director_name', title='IMDb Rating vs. IMDb Votes for All Directors')
fig.update_layout(
    xaxis_title='IMDb Rating',
    yaxis_title='IMDb Votes',
    legend_title='Director'
)
fig.show()

# Creating an interactive scatter plot of the data using plotly
fig = px.scatter(df, x='imbd_rating', y='imbd_votes', color='writer_name',
                 hover_name='director_name', title='IMDb Rating vs. IMDb Votes for All Writers')
fig.update_layout(
    xaxis_title='IMDb Rating',
    yaxis_title='IMDb Votes',
    legend_title='writer_name'
)
fig.show()

