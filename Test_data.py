import pandas as pd
import pytest
from datatest import validate
import re

data = pd.read_csv("input_file/test.csv")


def test_uniquness():
    IDFromDataset = data['ID']
    try:
        assert IDFromDataset.is_unique == True
    except Exception as ex:
        IDFromDataset.to_csv('output_test/ID_Value_Uniquness_fall.csv')


def test_isnull():
    try:
        IDFromDataset = data['ID']
        GetNullStatus = pd.notna(IDFromDataset)
        frames = [GetNullStatus,data]
        result = pd.concat(frames)
        # CheckThereIsNull = data[GetNullablity.any() == True]
        assert GetNullStatus.all() == True
    except Exception as ex:
        result.to_csv('output_test/ID_Value_null.csv')


def test_characterlength():
    try:
        e = data['Name'].str.len()
        # g = e.all() == 4
        assert e.all() == 4
    except Exception as ex:
        e.to_csv('output_test/characterlength_Invalid.csv')


def test_name_not_numaric():
    try:
        d = data['Name']
        patternCharacter = '^[a-zA-Z]+$'
        matchPattern = data[d.str.match(patternCharacter) == False]
        assert matchPattern['Name'].count() == 0
    except Exception as ex:
        matchPattern.to_csv('output_test/Name_Is_Invalid.csv')


def test_validemail():
    try:
        pattern_validemail = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        validmail = data[data['Email'].str.match(pattern_validemail) == False]
        assert data['Email'].str.match(pattern_validemail) == True
    except Exception as ex:
        validmail.to_csv('output_test/Email_is_invalid.csv')


def test_Age():
    e = data['Age'] <= 75
    f = data[e == False]
    try:
        assert e == True
    except Exception as ex:
        f.to_csv('output_test/Age_Is_Invalid.csv')

def test_gender():
    try:
        a = data['Gender']
        b = a.str.contains('M|F', regex=True)
        # c = data[b.all() == False]
        assert b.all() == True
    except Exception as ex:
        a.to_csv('output_test/gender_is_Invalid.csv')

