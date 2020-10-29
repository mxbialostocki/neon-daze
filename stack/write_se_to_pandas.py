import pandas as pd
from pandas import json_normalize, to_datetime
# load the local json file to a pandas dataframe
data_path = "./data/items.json"
json_data = pd.read_json(data_path, orient='records')
items = json_data["items"]
df = pd.DataFrame(json_normalize(items))

# print the head to check data
# print(df.head(1))
# print(df.shape)

# iterate over DataFrame to print question_id and title to terminal
for index, row in df.iterrows():
  print('question_id:', row.question_id)
  print('question::', row.title, end='\n\n')

def return_view_count(df):
  highest_views = 0
  # iterate over DataFrame to check for view_count 
  for index, row in df.iterrows():
    # print(row.view_count)
    if row.view_count > highest_views:
      highest_views = row.view_count
    # print('highest view count:', highest_views)
  return highest_views

highest_view_count = return_view_count(df)
most_viewed_question = df.loc[df.view_count == highest_view_count]
biggest_day = to_datetime(most_viewed_question.creation_date, unit='s')
print('MOST VIEWED QUESTION: \n', most_viewed_question.title, end='\n\n')
print('... WHICH WAS CREATED ON: \n', biggest_day, end='\n\n')
