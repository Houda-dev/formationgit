import pandas as pd

def addition(a,b):
    return a+b

def nettoyer(nom):
    return nom.strip().upper()

def supprimer_doublons(data):
    return list(set(data))
def diviser(a,b):
    if b==0:
        raise ValueError("Division par Zéro")
    return a/b

def nettoyer_dataframe(df):
    df=df.drop_duplicates()
    df["name"]=df["name"].str.strip().str.upper()
    return df
