import pandas as pd
import os
os.chdir('c:/users/nicolas/documents/data/ieee-fraud-detection')

files = [elem for item in os.listdir() for elem in item.split() if elem.endswith('csv')]

train_identity = pd.read_csv(files[-2], index_col='TransactionID')
train_transaction = pd.read_csv(files[-1], index_col='TransactionID')

train = pd.concat([train_identity, train_transaction], axis=1, sort=False)

train.to_csv('merged-train.csv')

test_identity = pd.read_csv(files[1], index_col='TransactionID')
test_transaction = pd.read_csv(files[2], index_col='TransactionID')

test = pd.concat([test_identity, test_transaction], axis=1, sort=False)

test.to_csv('merged-test.csv')