# coding: utf-8
import math


class TaxInfo:
    def __init__(
            self,
            tax_by_percent: int,
            gt_min_income: int,
            max_income: int,
            deduction: int
    ):
        self.tax_by_percent = tax_by_percent
        self.gt_min_income = gt_min_income
        self.max_income = max_income
        self.deduction = deduction


class TaxIncomeManager:

    tax_income_list = []

    def __init__(self):
        self.tax_income_list = [
            TaxInfo(5, 0, 1950000, 0),
            TaxInfo(10, 1950000, 3300000, 97500),
            TaxInfo(20, 3300000, 6950000, 427500),
            TaxInfo(23, 6950000, 9000000, 636000),
            TaxInfo(33, 9000000, 17800000, 1536000),
            TaxInfo(40, 17800000, 40000000, 2796000),
            TaxInfo(45, 40000000, math.inf, 4796000)
        ]

    def get_tax(self, income: int) -> int:
        range = self.get_range(income)
        return income * range.tax_by_percent * 0.01 - range.deduction

    def get_range(self, income: int) -> TaxInfo:
        for tax_income in self.tax_income_list:
            gt_min_income = tax_income.gt_min_income
            max_income = tax_income.max_income

            if income > gt_min_income and income <= max_income:
                return tax_income
