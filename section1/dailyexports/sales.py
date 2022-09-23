import pandas as pd

def getSales():
    df = pd.concat([pd.read_csv('dataset1.csv', dtype=str),pd.read_csv('dataset2.csv', dtype=str)])

    # Split the name field into first_name, and last_name
    df[['first_name','last_name']] = df['name'].str.extract(r'([A-Z][a-z]+)+ ([A-Z][a-z]+)+')

    # Remove any zeros prepended to the price field
    df.loc[df['price'].str.contains(r'^0'),'price'] = df[df['price'].str.contains(r'^0')]['price'].str[1:]

    # Delete any rows which do not have a name
    df = df[~df['name'].isna()]

    # Create a new field named above_100, which is true if the price is strictly greater than 100
    df['above_100'] = df['price'].astype(float)
    df.loc[df['above_100'] > 100, 'above_100'] = True
    df.loc[df['above_100'] != True, 'above_100'] = False

    df = df[['name', 'first_name', 'last_name', 'price', 'above_100']]
    df.to_csv('processed_dataset.csv', index=False)