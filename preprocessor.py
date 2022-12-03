import pandas as pd
import preprocessor



def preprocess(df, region_df):
    df = df[df['Season']=='Summer']                      # filtering for summer olympics
    df = df.merge(region_df, on = 'NOC', how='left')                     # merge with region_df
    df.drop_duplicates(inplace=True)                                             # dropping duplicates
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)                    # One hot encoding medals
    return df