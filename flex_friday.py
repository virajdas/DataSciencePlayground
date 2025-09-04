'''
The following code was written by Viraj Das as a means of which to read and process large datasets, specifically,
a Pokemon dataset that was found on Kaggle at this URL: https://www.kaggle.com/datasets/abcsds/pokemon.
'''

# DEPENDENCIES
import pandas as pd

# READ IN DATA
pokemon_data = pd.read_csv("Datasets/Pokemon.csv", header=0, sep=",")
clean_pokemon_data = pokemon_data.dropna(axis=0, inplace=False)

# PRINT CLEAN DATA INFO
print("Info after cleaning data and dropping rows with missing values:")
print(clean_pokemon_data.info())

# PRINT STATISTICAL DATA
print("\nDescriptive statistics of the cleaned dataset:")
print(clean_pokemon_data.describe())

# PRINT FIRST 10 ROWS OF CLEAN DATA
print("\nFirst 10 rows of the cleaned dataset:")
print(clean_pokemon_data.head(10))

# PRINT MAX VALUES OF CLEAN DATA
print("\nMaximum values in each column of the cleaned dataset:")
print(clean_pokemon_data.max())
