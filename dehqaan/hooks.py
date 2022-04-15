from . import __version__ as app_version

app_name = "dehqaan"
app_title = "Dehqaan"
app_publisher = "Dehaqan"
app_description = "Dehqaan"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "erpnextaddon@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/dehqaan/css/dehqaan.css"
# app_include_js = "/assets/dehqaan/js/dehqaan.js"

# include js, css files in header of web template
# web_include_css = "/assets/dehqaan/css/dehqaan.css"
# web_include_js = "/assets/dehqaan/js/dehqaan.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "dehqaan/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "dehqaan.install.before_install"
# after_install = "dehqaan.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "dehqaan.uninstall.before_uninstall"
# after_uninstall = "dehqaan.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "dehqaan.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
 	"GL Entry": {
 		"validate": "dehqaan.dehqaan.gl_entry.update_payment_entry",
# 		"on_cancel": "method",
# 		"on_trash": "method"
	}
}


doctypes_list = ["Purchase Order", "Request for Quotation","Supplier Quotation","Material Request","Purchase Receipt","Project","Sales Order","Purchase Invoice"]

fixtures = [
    {"doctype": "Client Script", "filters": [
        [
            "dt", "in", doctypes_list
        ]
    ]},
    {"doctype": "Property Setter", "filters": [
        [
            "doc_type", "in", doctypes_list
        ]
    ]},
    {"doctype": "Custom Field", "filters": [
        [
            "dt", "in", doctypes_list
        ]
    ]},
    {"doctype": "Workflow", "filters": [
        [
            "document_type", "in", doctypes_list
        ]
    ]},
    {"doctype": "Notification", "filters": [
        [
            "document_type", "in", doctypes_list
        ]
    ]},
    {"doctype": "Email Account", "filters": [
        [
            "email_id", "in", ['orders@northcorpgroup.com']
        ]
    ]},
    {"doctype": "Print Format", "filters": [
        [
            "doc_type", "in", doctypes_list
        ]
    ]}


]


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"dehqaan.tasks.all"
# 	],
# 	"daily": [
# 		"dehqaan.tasks.daily"
# 	],
# 	"hourly": [
# 		"dehqaan.tasks.hourly"
# 	],
# 	"weekly": [
# 		"dehqaan.tasks.weekly"
# 	]
# 	"monthly": [
# 		"dehqaan.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "dehqaan.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "dehqaan.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "dehqaan.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"dehqaan.auth.validate"
# ]

