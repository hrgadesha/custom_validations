from __future__ import unicode_literals
import frappe
from frappe import msgprint,throw, _
from frappe.model.document import Document

@frappe.whitelist()
def validateSerialNo(self):
	si = frappe.get_doc('Sales Invoice', self)
	for d in si.items:
		serial_no = frappe.db.get_list('Serial No', {'warehouse': d.warehouse,'item_code': d.item_code,'status':"Active"}, ['name'],as_list=True)
		if d.serial_no:
			for serial in d.serial_no.split('\n'):
				if serial not in serial_no:
					msgprint(_("In Row {0} : Item {1}, Serial Number {2} not part of warehouse {3}.").format(d.idx,d.item_code,serial,d.warehouse))

		if si.tax_category:
			if not d.item_tax_template:
				msgprint(_("Item Tax Template Missing In Row {0}.").format(d.idx))

