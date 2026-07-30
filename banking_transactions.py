import pandas as pd
import numpy as np

accounts = pd.read_csv('/Users/rohananjutgi/Desktop/new_folder/banking-transactions-dataset/versions/1/accounts.csv')
cards = pd.read_csv('/Users/rohananjutgi/Desktop/new_folder/banking-transactions-dataset/versions/1/cards.csv')
loan = pd.read_csv('/Users/rohananjutgi/Desktop/new_folder/banking-transactions-dataset/versions/1/cards.csv')

accounts = accounts[accounts['status'] != 'Closed']
print(accounts)
