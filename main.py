from FileActionLibrary import FileActionLibrary

library = FileActionLibrary()

# Convert file
# converted_file = library.perform_action('convert', 'pokemon_data.csv')
# print(f'Converted file')

# Read file
data = library.perform_action('read', 'pokemon_data.parquet')

# print(data.head(10))
# print(data.tail(10))

# RETURN JUST NAME, TYPE 1
# print(data[["Name", "Type 1"]].head())

# FROM ID, TO ID
# print(data.iloc[1:4].head())

# FROM ID, TO ID
# print(data.iloc[2, 1])

# ITTERATE ROWS
# for index, row in data.iterrows():
#     print(index, row.Name)

# SEARCH BY
# print(data.loc[data['Type 1'] == 'Fire'])

# CONTAINS
# print(data.loc[data['Name'].str.contains('Mega')])

# DOES NOT CONTAIN
# print(data.loc[~data['Name'].str.contains('Mega')])

# print(data.describe())

# print(data.sort_values('Name', ascending=False))

# print(data.sort_values(['Type 1', 'HP'], ascending=[True, False]))

# FILTER BY
# print(data.loc[(data['Type 1'] == 'Fire') & (data['Type 2'] == 'Dragon')])

# GROUP MULTIPLE
# print(data.groupby(['Type 1', 'Type 2']).count())