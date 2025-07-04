# Warehouse Sale Stock Access Control

This repository provides two Odoo 18 modules to manage warehouse restrictions.

## Modules

### sale_stock_restrict
Restricts confirming sale orders when products are not available.

- Toggle the behaviour with the `sale_stock_restrict.product_restriction` setting.
- Use `sale_stock_restrict.check_stock` to decide whether on-hand or forecast quantities are evaluated.

### user_access_restrict
Adds warehouse-based access control. Users can be assigned access to specific warehouses with custom roles (manager or user) that determine permitted operations.

## Installation
Follow the standard Odoo installation guide: <https://www.odoo.com/documentation/18.0/setup/install.html>.
After installing Odoo, add these modules to your addons path and install them from the Apps menu.

## Running Tests
Tests rely on an existing Odoo 18.0 installation. You can either install Odoo locally from source or use a Docker container such as `odoo:18.0`.

Install the Python requirements with:

```bash
pip install -r requirements.txt
```

Once Odoo is available and dependencies are installed, run:

```bash
pytest
```

The tests ensure both modules load correctly and validate core functionality.
