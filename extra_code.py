#From CoinQuery python notebook

#while loop to expand out all of the columns 
i = 0
concat_df = pd.DataFrame()
while i <= 10:
    i+=1
    tags = df['tags'].apply(pd.Series)
    exploded_df = tags[i].apply(pd.Series)
concat_df.append(exploded_df)


i = 0
number_of_columns = []
while i < len(tags.columns):
    number_of_columns.append(i)
    i+= 1


#while loop to expand out all of the columns 
i = 0
concat_df = pd.DataFrame()
number_of_columns = []
tags = df['tags'].apply(pd.Series)
while i < len(tags.columns):
    number_of_columns.append(i)
    i+=1






#while loop to expand out all of the columns 
i = 0
concat_df = pd.DataFrame()
number_of_columns = []
tags = df['tags'].apply(pd.Series)
while i < len(tags.columns):
    number_of_columns.append(i)
    i+=1
#returns a lot of columns, will need to rename as well
concat_df = pd.DataFrame()
for column in number_of_columns:
    exploded_df = tags[column].apply(pd.Series)
    cols = exploded_df.columns
    cols_new = ["{}_{}_{}".format(x,column,"Expanded") for x in cols]
    mapping = {key1: key2 for key1, key2 in zip(cols, cols_new)}
    exploded_df = exploded_df.rename(columns=mapping)
    concat_df = pd.concat([exploded_df, concat_df], axis=1)            