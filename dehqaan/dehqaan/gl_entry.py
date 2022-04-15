import frappe
from frappe import _
from frappe.utils import getdate, formatdate, flt

def update_payment_entry(self, method):
    if self.voucher_type == 'Payment Entry':
            account_type=frappe.db.get_value("Account",self.account,'account_type')
            if account_type == 'Receivable' or account_type == 'Payable':
                if self.against_voucher_type == 'Purchase Invoice' or self.against_voucher_type == 'Purchase Order':
                    project=frappe.db.get_value(self.against_voucher_type,self.against_voucher,'project')
                    cost_center=frappe.db.get_value(self.against_voucher_type,self.against_voucher,'cost_center')
                    self.cost_center = cost_center
                    self.project = project


