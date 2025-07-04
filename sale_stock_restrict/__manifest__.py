# -*- coding: utf-8 -*-
{
    "name": "Sale Stock Restrict",
    "version": "18.0.1.0.0",
    "category": "Sales",
    "summary": "Restrict sale order confirmation based on available stock",
    "description": "Prevent confirming sale orders when stock is insufficient.",
    "author": "Cybrosys Techno solutions",
    "company": "Cybrosys Techno Solutions",
    "maintainer": "Cybrosys Techno Solutions",
    "website": "https://www.cybrosys.com",
    "depends": ["sale_management", "stock"],
    "data": [
        "security/ir.model.access.csv",
    ],
    "license": "AGPL-3",
    "installable": True,
    "auto_install": False,
    "application": False,
}
