# test-task-odoo


## Overview

The **Persons** module is designed for managing person records within Odoo. This module provides a simple interface to add, view, and manage person information, including their names, birthdays, gender, and associated company.

## Features

- Add new person records through a user-friendly web form.
- View a list of existing persons with details such as full name, age, and gender.
- Display persons associated with a specific company.

## Installation

Python3 must be already installed.

### 1. Clone the Odoo Repository:
First, you need to clone the Odoo repository. You can do this by running the following command in your terminal:

```bash
git clone https://github.com/odoo/odoo.git --branch 16.0 --single-branch
cd odoo/addons
```
### 2.Install Dependencies:
```shell
pip install -r requirements.txt
```

## Usage

1. Install the modul 
2. Navigate to the **Persons** section from the main menu.
3. Click on the **Add New Person** link to open the form for adding a new person.
4. Fill out the form with the person's details and submit it.

## Configuration

- Ensure you have the `website` module installed, as this module depends on it.
- Adjust access permissions in `security/ir.model.access.csv` if necessary to control who can view or modify person records.

## Development

For developers looking to contribute or modify the module:

- The main code resides in the `models` and `controllers` directories.
- Use standard Odoo development practices for extending or customizing the functionality.
