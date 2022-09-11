import pandas as pd

import re


df = pd.read_csv('pokemon_data.csv')

    #Loading a .txt file to the DataFrame
#df_txt = pd.read_csv('pokemon_data.txt', delimiter='\t')

    #Loading an excel .xlsx file to the DataFrame
#df_xlsx = pd.read_excel('pokemon_data.xlsx')

    #Prints the DataFrame accessing the .csv document
#print(df)

    #printing headers in the dataframe
#print(df.columns)

    #Read data from a specified column in the dataframe
#print(df['Name'])

    #Printing the first row in the dataframe
#print(df.loc[0])

    #Reading multiple columns
#print(df[['Name','Speed','Generation','Type 1']])

    #Read each row
#print(df.iloc[1:4])

    #Read from a specific location.
#print(df.iloc[1,4])

    #Reads the rows by reiterrating through them in the loop
"""
for index,row in df.iterrows():
    print(index,row)
"""
    #Prints out the row that meets a certain criteria passed through the .loc method.
#print(df.loc[df['Name'] == 'Venusaur'])

    #Gives a tabular report on the diferrent metrics of statistical analysis.
#print(df.describe())

    #Sorts the data in the dataframe using the criteria passed to the sort method.
#print(df.sort_values('Name', ascending=True))

    #Creating a new column in the DataFrame and assigning values to it
df['Total'] = df['HP']+ df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

    #Altering the data in a column
#df['Legendary'] = 'True'

    #Dropping a column
#df.drop(columns = ['Legendary']

    #Saves a modified instance of the Dataframe to a new CSV formatted document'modified.csv' while omitting the Index column as an option.
    #Use the to_xlsx() method in case you want the output fle to be formatted in an excel xlsx format.
    #To save into a .txt file format, use the to_csv() method but now pass in the parameter sep(for separator)='\t'.
#df.to_csv('Modified.csv', index=False)

    #Filtering the data with multiple sets of options
#print(df.loc[(df['Name'] == 'Venusaur') & df['Generation'] == 1])

    #After filtering out data, the index persists from the old dataframe. To change this, you can apply the method 'reset_index()'on the new dataframe with an additional argument 'drop = true' in order to remove the old index from the column.

    #Setting the maximum number of columns that can be displayed on the console.

pd.options.display.max_columns = 20

    #Printing out results by matching out a string in the filter pattern.

#print(df.loc[df['Name'].str.contains('Mega')])

    #Printing out results that don't match a string in the filter pattern.

#print(df.loc[~df['Name'].str.contains('Mega')])

    #Matching filters to a regex pattern
#print(df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)])

    #Changing the value of a column based on a filter pattern
#df.loc[df['Type 1'] == 'Fire','Legendary'] = 'True'

    #Modifying multiple columns after filtering out data using a given pattern.
#df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ('Test', 'Value')

    #Aggregating using the groupby function and mean method on a specified column
#print(df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False))

#print(df)








