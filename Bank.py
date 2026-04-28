from Account import Account
from Branch import Branch
from Customer import Customer
from Payroll import Payroll
from Staff import Staff


class Bank:
    def __init__(self):
        self.accounts = []
        self.customers = []
        self.branches = []
        self.payroll = None

    def setup_branch(self, branch: Branch):
        self.branches.append(branch)

    def close_branch(self, branch: Branch, transfer_branch: Branch):
        branch.transfer_all_staff_to(transfer_branch)
        self.branches.remove(branch)

    def transfer_staff_member(self, from_branch: Branch, to_branch: Branch, staff: Staff):
        from_branch.transfer_staff_member(to_branch, staff)

    def setup_new_account(self, account: Account, customer: Customer):
        account.set_customer(customer)
        self.accounts.append(account)

        if customer not in self.customers:
            self.customers.append(customer)

    def obtain_balance(self, account: Account):
        return account.get_balance()

    def close_account(self, account: Account):
        account.close()
        self.accounts.remove(account)

    def change_payroll_date(self, payroll: Payroll, date: str, staff_category: str):
        self.payroll = payroll
        self.payroll.get_staff_category_pay_schedule(staff_category).set_pay_date(date)