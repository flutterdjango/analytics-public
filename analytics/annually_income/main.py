# coding: utf-8

from analytics.annually_income.tax_income import TaxIncomeManager
from matplotlib import pyplot as plt


def main():
    manager = TaxIncomeManager()

    income_list = []
    net_income_list = []
    for income in range(10000, 15000000, 10000):
        tax = manager.get_tax(income)
        income_list.append(income // 10000)
        net_income_list.append((income - tax) // 10000)

    plt.plot(income_list, net_income_list)
    plt.show()


if __name__ == '__main__':
    main()
