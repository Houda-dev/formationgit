from calcul import addition
from calcul import nettoyer
from calcul import supprimer_doublons
from calcul import diviser
from calcul import nettoyer_dataframe 
import pytest
import pandas as pd

def test_addition():
    assert addition(2,3)==5
def test_nettoyer():
    assert nettoyer(" houda ")=="HOUDA"

def test_supprimer_doublons():
    data=[1,2,2,3,3]
    resultat=supprimer_doublons(data)
    assert len(resultat)==3

def test_division_zero():
    with pytest.raises(ValueError):
        diviser(10,0)


def test_nettoyer_dataframe():

    df = pd.DataFrame({
        "name": [" Houda ", "Ali", "Ali"]
    })

    resultat = nettoyer_dataframe(df)

    assert len(resultat) == 2
    assert resultat.iloc[0]["name"] == "HOUDA"