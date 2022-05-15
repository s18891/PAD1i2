import pandas as pd
import string

if __name__ == '__main__':
    df = pd.read_csv('PAD_03_PD.csv', sep=';')

    print(df)

    print(df.head())

    print(df.columns)

    print(df[["Country"]])


    zad1 = df[['Country']].groupby(['Country']).nunique()
    zad1[['Count']] = df[['ID']].groupby(df['Country']).nunique()
    print(zad1[['Count']])

    zad2 = df
    zad2["owned_goods"] = df["owns_car"] + df["owns_TV"] + df["owns_house"] + df["owns_Phone"]

    print(zad2[['owned_goods']])

    zad3 = zad2.groupby(['gender']).mean().round(2)

    print(zad3[["owned_goods"]])


    zad4 = zad2[['Country']].groupby(['Country']).nunique()
    zad4[['avg_goods']]= zad2.groupby(['Country'])[["owned_goods"]].mean().round(2)



    print(zad4)