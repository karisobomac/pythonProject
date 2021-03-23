# pythonProject

magaloop-data-dev-test
create a basic programm in python without ui which simulates a bank account. This bank account should be able to be

- initialized(give iban, maximum debt amount)
- transfer money toamount
- transfer money from
- return payment_allowed true false(check if a certain amount is available)
- transfer money to another bank account
- transfer money from another bank account
- log all transfers and checks to a txt file
- show current balance
make sure that every transaction also gets a label for what the transaction is used for(payed for aldi, payed for wallmart, cash payout, salary etc.pp.) and a timestamp.

create issues and pull requests to solve this task during your developement like you would do within a production environment.

after the programm works write a little script which initialize 2 bank accounts, do atleast 30 random transactions with those 2 in order to simulate spendings / income within a month, read the transaction logs and build visualisations of spending/incoming using one or more of the following libraries

pandas
seaborn
matplotlib
