.. image:: https://img.shields.io/badge/license-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

User Access Restrict
====================
* Restricts stock, sale and purchase records by the user’s allowed warehouses.

Access Types
------------
* **Custom Manager** – full create, read, update and delete rights inside the selected warehouses.
* **Custom User** – read and write access only for the selected warehouses.

Warehouse Assignment
--------------------
* On each user form choose the access type and add the warehouses that the user can access.
* Leaving the access type empty gives the user unrestricted access.

Required Groups
---------------
* ``Custom Manager`` (``user_access_restrict.group_user_access_custom_manager``)
* ``Custom User`` (``user_access_restrict.group_user_access_custom_user``)

Record Rules
------------
* Stock pickings, locations, moves, quants and sale & purchase orders are filtered by the user’s allowed warehouses. Managers can create and delete, while users can only read and update.

Installation
============
- www.odoo.com/documentation/17.0/setup/install.html
- Install our custom addon

License
-------
Affero General Public License v3.0 (AGPL v3)
(https://www.gnu.org/licenses/agpl-3.0-standalone.html)

Company
-------
* Cybrosys Techno Solutions <https://cybrosys.com/>

Credits
-------
* Developer: Cybrosys Techno Solutions
Contact: odoo@cybrosys.com

Contacts
--------
* Mail Contact : odoo@cybrosys.com
* Website : https://cybrosys.com

Bug Tracker
-----------
Bugs are tracked on GitHub Issues. In case of trouble, please check there if your issue has already been reported.

Maintainer
==========
.. image:: https://cybrosys.com/images/logo.png
   :target: https://cybrosys.com

This module is maintained by Cybrosys Technologies.

For support and more information, please visit https://www.cybrosys.com
