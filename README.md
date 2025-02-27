# Expense Settlement Algorithm

## Description
This project implements a **heuristic algorithm** for settling expenses within a group of users. Based on a list of transactions indicating who paid whom and how much, the algorithm calculates the net balances of all users and determines a set of transactions to minimize outstanding debts.

The problem of finding the truly **optimal** way to settle debts is **NP-complete**, as it is related to the **Subset Sum Problem**. Therefore, this algorithm provides a **sub-optimal heuristic solution** that efficiently balances debts while keeping the number of transactions reasonably low.

Inspired by the **Splitwise** mobile app.

## Installation
Requires Python 3 and the `sortedcontainers` package.

Install dependencies using:
```sh
pip install sortedcontainers
