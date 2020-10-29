import pandas as pd

# load the local json file to a pandas dataframe
data_path = "./data/items.json"
df = pd.read_json(data_path)

# print the head to check data
print(df.head())

df.shape

# loop over columns
# for column_name in df:
#   print(type(column_name))
#   print(column_name)
#   print('/////////////\n')

# for column_name, item in df.iteritems():
#   print(type(column_name))
#   print(column_name)
#   print('~~~~~~')

#   print(type(item))
#   print(item)
#   print('------')

# for index, row in df.iterrows():
#   print(type(index))
#   print(index)
#   print('~~~~~~')

#   print(type(row))
#   print(row[0])
#   print('------')

for item in df['items']:
  print(item['title'])
  print(item['view_count'])
  print(item['creation_date'])

# def return_highest_view_count(dataframe):
#   for item in dataframe:
#     for entry in items:

# more_than_five = df['items'].loc[(['view_count'] >= 5)]
# print(more_than_five)