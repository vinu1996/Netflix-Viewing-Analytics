import pandas as pd
import numpy as np
import os
import ast

df1=pd.read_csv('NetflixViewingHistory.csv')
df1.head(5)
df1.shape
df1[df1.duplicated()==1]
df1=df1.drop_duplicates()
df1.shape

df1.isnull().any()
df1= df1.dropna()

# Function to check if a title is present
def is_movie_present(title, dataframe):
    return title in dataframe['Title'].values

# Function to get rows with the specific title
def get_movie_info(title, dataframe):
    return dataframe[dataframe['Title'] == title]

# Check if 'Movie A' is present
movie_title = 'Money Heist'
is_present = is_movie_present(movie_title, df1)
print(f"Is '{movie_title}' present? {is_present}")

# Get information for 'Movie A'
if is_present:
    movie_info = get_movie_info(movie_title, df1)
    print(f"Information for '{movie_title}':\n{movie_info}")
else:
    print(f"'{movie_title}' not found in the dataset.")

# Function to transform the title
df1['Title'].info()
def transform_title(Title):
    parts = Title.split(':')
    if len(parts) >= 2:
        return ': '.join(parts[:2])
    return Title

df1['Title'] = df1['Title'].apply(transform_title)
df1['Title']

# Use regular expression to remove "Season" and everything after it
df1['Title'] = df1['Title'].str.replace(r':\s*(Season|Part).*$', '', regex=True)
df1['Title']
df1.shape

df1.tail(10)

df2=pd.read_csv('titles.csv')
df2.head()
df2.shape
new_cols_dict ={
    'Title':'title'
    }
df1 = df1.rename(columns=new_cols_dict)
combined1=pd.merge(df1,df2,how="inner",on="title")
combined1.shape
combined1.isnull
combined1[combined1.duplicated()==1]
combined1=combined1.drop_duplicates()
combined1.tail(10)
combined1['production_countries']
combined1.shape
combined1.tail(10)
combined1.production_countries.value_counts()
combined1.describe()
combined1.info()

# Function to convert string representation of list to string
def convert_country(value):
    try:
        # Use ast.literal_eval to safely evaluate the string as a Python literal
        country_list = ast.literal_eval(value)
        if isinstance(country_list, list) and len(country_list) > 0:
            return country_list[0]
        else:
            return value  # Return original value if not a valid list of length 1
    except (SyntaxError, ValueError):
        return value  # Return original value if evaluation fails

# Apply the transformation to the Country column
combined1['production_countries'] = combined1['production_countries'].apply(convert_country)






# Create a boolean mask for duplicated titles
duplicate_mask = combined1.duplicated(subset=['title'])
combined1

# Filter out rows with duplicated titles
combined2 = combined1.drop_duplicates(subset=['title'],keep='last')
combined2

combined2[combined2['title'].duplicated()==1]
combined2.tail(10)

def convert_genre(valuee):
    try:
        # Use ast.literal_eval to safely evaluate the string as a Python literal
        genre_list = ast.literal_eval(valuee)
        if isinstance(genre_list, list) and len(genre_list) > 0:
            return genre_list[0]
        else:
            return valuee  # Return original value if not a valid list of length 1
    except (SyntaxError, ValueError):
        return valuee  # Return original value if evaluation fails

# Apply the transformation to the Country column
combined2['genres'] = combined2['genres'].apply(convert_genre)

combined2.to_excel('Nerflix_final_2.xlsx')

