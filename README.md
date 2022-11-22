# Pharmacy CRM


Pharmacy CRM enables the distribution of products from the warehouse to the pharmacies, the control of the stocks in the pharmacies, and the management of the pharmacies.

## Installation
First of all we need to create virtual environment.
```bash
python -m venv venv
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install inside of requirements.

```bash

- Activate the virtual environment
your_file_path/venv/Scripts/Activate.ps1

After setup and activate virtual environment. We need to install requirements.txt
pip install -r requirements.txt
```

## Usage

```python
- Create migrate files and make all migrations
python manage.py makemigrations
python manage.py migrate

- Create superuser
python manage.py createsuperuser

- After create user run the server on localhost
python manage.py runserver

```



## License

[MIT](https://choosealicense.com/licenses/mit/)