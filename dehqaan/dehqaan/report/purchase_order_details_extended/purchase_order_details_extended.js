// Copyright (c) 2023, Dehaqan and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Purchase Order Details Extended"] = {
	"filters": [
		{
                        "fieldname":"company",
                        "label": __("Company"),
                        "fieldtype": "Link",
                        "options": "Company",
                        "default": frappe.defaults.get_user_default("Company")
                },
		{
			"fieldname":"from_date",
			"label": __("From Range"),
			"fieldtype": "Date",
			"reqd": 1
		},
		{
                        "fieldname":"to_date",
                        "label": __("To Range"),
                        "fieldtype": "Date",
                        "reqd": 1
                },
		{	
			"fieldname":"workflow_state",
			"label": __("Workflow State"),
			"fieldtype": "Link",
			"options": "Workflow State"
		},
		{
		        "fieldname":"supplier",
                        "label": __("Supplier"),
                        "fieldtype": "Link",
                        "options": "Supplier"
                },
		{
                        "fieldname":"project",
                        "label": __("Project"),
                        "fieldtype": "Link",
                        "options": "Project"
                },
		{
                        "fieldname":"department",
                        "label": __("Department"),
                        "fieldtype": "Link",
                        "options": "Cost Center"
                }

	],
	"tree": true,
	"parent_field": "parent_department",
	"name_field": "department",
	"initial_depth": 2

}

