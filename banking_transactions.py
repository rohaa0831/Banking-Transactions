import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

accounts = pd.read_csv('/Users/rohananjutgi/Desktop/new_folder/banking-transactions-dataset/versions/1/accounts.csv')
cards = pd.read_csv('/Users/rohananjutgi/Desktop/new_folder/banking-transactions-dataset/versions/1/cards.csv')
loan = pd.read_csv('/Users/rohananjutgi/Desktop/new_folder/banking-transactions-dataset/versions/1/loans.csv')
loan_payment = pd.read_csv('/Users/rohananjutgi/Desktop/new_folder/banking-transactions-dataset/versions/1/loan_payments.csv')
employees = pd.read_csv('/Users/rohananjutgi/Desktop/new_folder/banking-transactions-dataset/versions/1/employees.csv')

accounts = accounts[accounts['status'] != 'Closed']

#def millions(x, pos):
    #"""The two arguments are the value and tick position."""
    #return f'${x*1e-6:1.1f}M'

loan['start_date'] = pd.to_datetime(loan['start_date'])
loan['year'] = loan[loan['start_date'].dt.year <2023 ]['start_date'].dt.year#strftime("%Y-%m")
df3 = loan.groupby('year')['loan_amount'].agg('sum')

df4 = employees.groupby('role')['salary']

fig, axs = plt.subplots(2,1, figsize = (15,10))
#axs[0].yaxis.set_major_formatter('^\d{1,3},\d{3},\d{3}$')
axs[0].set_title('Total Loan Amounts Given by Year')

sns.lineplot(data = loan, x = 'year', y= 'loan_amount', hue = 'loan_type', ax = axs[0], errorbar = None)
sns.move_legend(axs[0], "upper left", bbox_to_anchor=(.97, 1))

sns.boxplot(data = employees, x = 'role', y = 'salary', ax = axs[1])

axs[0].set_ylabel('Loan Amount')
axs[0].set_xlabel('Year')
axs[1].tick_params(axis='x', labelrotation=45)
for label in axs[1].get_xticklabels():
    label.set_horizontalalignment('right')
axs[1].set_title('Numerical distribution of Salaries')

plt.show()