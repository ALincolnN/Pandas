import pandas as pd


df = pd.read_csv('pokemon_data.csv')

#df_txt = pd.read_csv('pokemon_data.txt', delimiter='\t')

#df_xlsx = pd.read_excel('pokemon_data.xlsx')
#Prints the DataFrame accessing the .csv document
    #print(df)
#printing columns in the dataframe
    #print(df.columns)
#printing data from a specified column in the dataframe
    #print(df['Name'])
#Printing more than one column data in the dataframe
print(df.loc[0])
