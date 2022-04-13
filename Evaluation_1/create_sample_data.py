import csv
from data_maker.data_generator import DataMaker
import os

with open(os.path.join('.','data_maker','first_names.csv'), 'r') as fn:
    first_names = [i['Name '].upper() for i in csv.DictReader(fn, delimiter='\t')]

with open(os.path.join('.','data_maker','last_names.csv'), 'r') as fn:
    last_names = [i['SURNAME'] for i in csv.DictReader(fn, delimiter='\t')]

if __name__=='__main__':
    dm = DataMaker(first_names, last_names,750,30)
    dm.dump()