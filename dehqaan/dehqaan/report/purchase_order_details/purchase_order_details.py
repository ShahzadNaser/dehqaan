# Copyright (c) 2013, Dehaqan and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import flt
from frappe import _


def execute(filters=None):
    columns, data = [], []
    departments  = get_all_departments(filters)
    columns = get_columns()
    order_details = get_data(filters)

    totals = frappe._dict({})
    totals.update({
                "indent": 0.0, "name":'Grand Total', "parent_department":'',
                        "department": '', "workflow_state": '', "project": '',
                        "project_name":'', "supplier_name": '', "grand_total":0.0,
                        "outstanding": 0.0,'transaction_date':'','paid':0.0,
                        "advance_paid":0.0,"invoiced":0.0
                })
    
    blank_totals = frappe._dict({})
    blank_totals.update({
                "indent": 0.0, "name":'', "parent_department":'',
                        "department": '', "workflow_state": '', "project": '',
                        "project_name":'', "supplier_name": '', "grand_total":'',
                        "outstanding": 0.0,'transaction_date':'','paid':0.0,
                        "advance_paid":0.0,"invoiced":0.0

                })

    
    for department in departments:
        data.append({
			"indent": 0.0, "is_parent": True,
			"parent_department": "",
			"department":department.department,
		})

        department_totals = frappe._dict({})
        department_totals.update({
                "indent": 0.0, "name":'Total', "parent_department":'',
                        "department": '', "workflow_state": '', "project": '',
                        "project_name":'', "supplier_name": '', "grand_total":0.0,
                        "outstanding": 0.0,'transaction_date':'','paid':0.0,
                        "advance_paid":0.0,"invoiced":0.0
                })

        for ss in order_details:
            
            if department.department == ss.cost_center:
                temp = frappe._dict({})
                temp.update({
			"indent": 1.0, "name": ss.name, "parent_department": ss.cost_center,
			"department": '', "workflow_state": ss.workflow_state, "project": ss.project,
			"project_name": ss.project_name, "supplier_name": ss.supplier_name, "grand_total": ss.grand_total,
                        "outstanding": 0,'transaction_date':ss.transaction_date,'paid':0.0,'advance_paid':ss.advance_paid,
                        "invoiced":0.0
                })

                payment_details = frappe.db.sql("""select distinct pi.name,pi.grand_total,pi.outstanding_amount as outstanding
                                            from `tabPurchase Invoice Item` pii
                                            inner join `tabPurchase Invoice` pi
                                            on pii.parent=pi.name
                                            where pi.docstatus = 1
                                            and purchase_order = '%s'
                                            """%ss.name,as_dict=1)
                grand_total = 0
                outstanding_amount = 0
                if payment_details:
                    for payment in payment_details:
                        grand_total = grand_total = grand_total + payment.grand_total 
                        outstanding_amount = outstanding_amount + payment.outstanding

                temp.advance_paid = ss.advance_paid
                temp.invoiced = grand_total
            
                total_paid = grand_total - outstanding_amount

                if total_paid <= temp.advance_paid:
                    total_paid = temp.advance_paid

                temp.paid = total_paid

                data.append(temp)
                totals.invoiced += grand_total
                totals.paid += total_paid
                totals.advance_paid += temp.advance_paid 
                totals.grand_total += ss.grand_total

                department_totals.paid += total_paid
                department_totals.advance_paid += temp.advance_paid
                department_totals.invoiced += temp.invoiced
                department_totals.grand_total += ss.grand_total

        #data.append(blank_totals)
        data.append(department_totals)
    
    data.append(totals)
    return columns, data

def get_columns():
    columns = [{
			"fieldname": "department",
			"label": "Department",
			"width": 250,
			"fieldtype": "Link",
                        "options": "Cost Center"
		},{
			"fieldname": "name",
			"label": "Purchase Order",
			"width": 150,
			"fieldtype": "Link",
			"options": "Purchase Order"
		},
                {
                        "fieldname": "transaction_date",
                        "label": "Date",
                        "width": 100,
                        "fieldtype": "Date"
                },
                {
                        "fieldname":"workflow_state",
			"label": "Workflow State",
			"width": 150,
			"fieldtype": "Data"
		},
                {
                        "fieldname":"project",
                        "label": "Project",
                        "width": 150,
                        "fieldtype": "Link",
                        "options": "Project"
                },
                {
                        "fieldname":"project_name",
                        "label": "Project Name",
                        "width": 150,
                        "fieldtype": "Data"
                },
                {
                        "fieldname":"supplier_name",
                        "label": "Supplier Name",
                        "width": 150,
                        "fieldtype": "Data"
                },
                {
                        "fieldname":"grand_total",
                        "label": "Grand Total",
                        "width": 110,
                        "fieldtype": "Currency"
                        
                },
                {
                        "fieldname":"advance_paid",
                        "label": "Advance Paid",
                        "width": 120,
                        "fieldtype": "Currency",
                        "hidden":1
                },
                {
                        "fieldname":"invoiced",
                        "label": "Invoiced Amount",
                        "width": 140,
                        "fieldtype": "Currency"
                },
                {
                        "fieldname":"paid",
                        "label": "Total Paid Amount",
                        "width": 140,
                        "fieldtype": "Currency"
                }

	]
    return columns

def get_all_departments(filters):
    departments = frappe.db.sql("""select distinct name as department from `tabCost Center` where company = '%s' and is_group = 0""" %filters.company, as_dict=1)
    return departments

def get_data(filters):
    cond = " and company = '%s' and transaction_date between '%s' and '%s'"%(filters.company,filters.from_date,filters.to_date)

    if filters.workflow_state:
        cond += " and workflow_state = '%s'"%filters.workflow_state

    if filters.supplier:
        cond += " and supplier = '%s'"%filters.supplier

    if filters.project:
        cond += " and project = '%s'"%filters.project

    if filters.department:
        cond += " and cost_center = '%s'"%filters.department



    return frappe.db.sql("""select name,advance_paid,transaction_date,cost_center,project_name,supplier_name,workflow_state,project,supplier,grand_total,0 as outstanding from `tabPurchase Order` where docstatus=1 %s """%cond,as_dict=1)
