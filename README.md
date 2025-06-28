# Warehouse Sale Stock Access Control

This repository provides two Odoo 18 modules to manage warehouse restrictions.

## Modules

### sale_stock_restrict
Restricts confirming sale orders when products are not available. The check can be based on on-hand or forecasted quantities.

### user_access_restrict
Adds warehouse-based access control. Users can be assigned access to specific warehouses with custom roles (manager or user) that determine permitted operations.

## Installation
Follow the standard Odoo installation guide: <https://www.odoo.com/documentation/18.0/setup/install.html>.
After installing Odoo, add these modules to your addons path and install them from the Apps menu.

## Running Tests
Tests require a working Odoo environment. Once Odoo and the modules' dependencies are installed, run:

```bash
pytest
```

The tests ensure both modules load correctly and validate core functionality.
