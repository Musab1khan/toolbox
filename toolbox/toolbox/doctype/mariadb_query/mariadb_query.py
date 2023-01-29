# Copyright (c) 2023, Gavin D'souza and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class MariaDBQuery(Document):
    def validate(self):
        self.set_tables_summary()

    def set_tables_summary(self):
        tables_id = {x.table for x in self.query_explain}
        tables = frappe.get_all(
            "MariaDB Table", filters={"name": ("in", tables_id)}, pluck="_table_name"
        )
        self.tables = frappe.as_json(tables)