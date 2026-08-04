import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

accounts = pd.read_csv('/Users/rohananjutgi/Desktop/new_folder/banking-transactions-dataset/versions/1/accounts.csv')
cards = pd.read_csv('/Users/rohananjutgi/Desktop/new_folder/banking-transactions-dataset/versions/1/cards.csv')
loan = pd.read_csv('/Users/rohananjutgi/Desktop/new_folder/banking-transactions-dataset/versions/1/loans.csv')
loan_payment = pd.read_csv('/Users/rohananjutgi/Desktop/new_folder/banking-transactions-dataset/versions/1/loan_payments.csv')
employees = pd.read_csv('/Users/rohananjutgi/Desktop/new_folder/banking-transactions-dataset/versions/1/employees.csv')
support_tickets = pd.read_csv('/Users/rohananjutgi/Desktop/new_folder/banking-transactions-dataset/versions/1/support_tickets.csv')
branches = pd.read_csv('/Users/rohananjutgi/Desktop/new_folder/banking-transactions-dataset/versions/1/branches.csv')

accounts = accounts[accounts['status'] != 'Closed']


loan['start_date'] = pd.to_datetime(loan['start_date'])
loan['year'] = loan[loan['start_date'].dt.year <2023 ]['start_date'].dt.year#strftime("%Y-%m")
df3 = loan.groupby('year')['loan_amount'].agg('sum')

df4 = employees.groupby('role')['salary']

fig, axs = plt.subplots(1,2, figsize = (13,8))
fig2, axs2 = plt.subplots(1,2, figsize = (13,8))
#axs[0,0].yaxis.set_major_formatter('^\d{1,3},\d{3},\d{3}$')
axs[0].set_title('Total Loan Amounts Given by Year')

#lineplot and boxplot
sns.lineplot(data = loan, x = 'year', y= 'loan_amount', hue = 'loan_type', ax = axs[0], errorbar = None)
sns.move_legend(axs[0], "upper right", fontsize = 'small', bbox_to_anchor=(.3, 1))
sns.boxplot(data = employees, x = 'role', y = 'salary', ax = axs[1])

#aetting ax labels
axs[0].set_ylabel('Loan Amount')
axs[0].set_xlabel('Year')
axs[1].tick_params(axis='x', labelrotation=45, labelsize = 'x-small')
for label in axs[1].get_xticklabels():
    label.set_horizontalalignment('right')
axs[1].set_title('Numerical distribution of Salaries')

#Heatmap analyzing the number of tickets intiated
accounts_support = pd.merge(accounts, support_tickets, on = 'customer_id')
accounts_support['Group_Count'] = accounts_support.groupby('customer_id')['ticket_id'].transform('count')
account_support_distinct = accounts_support.drop_duplicates(subset = ['customer_id'], keep = 'first')

df4 = account_support_distinct[['Group_Count']].value_counts().to_frame()

sns.heatmap(data = df4, ax = axs2[0])
axs[1].set_title('Distribution of Tickets Initiated')

#  Top 10 in most loans being offered? 
loan_branches = pd.merge(loan, branches, on = 'branch_id')
loan_branches = loan_branches.groupby('branch_name').size().reset_index()

loan_branches.columns = loan_branches.columns.str.strip()
loan_branches = loan_branches.rename(columns ={np.nan:"Count"})
loan_branches = loan_branches.sort_values(by = 'Count', ascending=False).head(10)
sns.barplot(data =loan_branches, x = 'branch_name', y = 'Count')

axs2[1].tick_params(axis='x', labelrotation=45, labelsize = 'x-small')
for label in axs2[0].get_xticklabels():
    label.set_horizontalalignment('right')
axs2[0].set_title('Numerical distribution of Salaries')

axs2[1].set_title('Top 10 Branches in Loans Offered')
plt.show()