# jpk-fa-parser

JPK FA parser - a simple Python script to parse JPK_FA XML file and convert loaded data to CSV, JSON or DB.

What is JPK (in Polish) https://poradnikprzedsiebiorcy.pl/-jpk-fa-struktura-wszystko-co-warto-wiedziec

JPK structure (in Polish) https://www.gov.pl/web/kas/struktury-jpk

## Installation

```bash
.venv\Scripts\python -m pip install -r requirements.txt
```

## Setup

### Add .env file in the root directory

```bash
DB_HOST=localhost
DB_DATABASE=jpk_fa_db
DB_USER=db_user
DB_PASSWORD=db_password
#DB_PORT=5432
```

There is an example `input.xml` file with some basic (partial!) data.

Use your real exported JPK file XML file. You can do that using `Subiekt123` (https://subiekt123.pl/) or other accounting software.

In Subiekt 123 go to `Księgowość` -> `+` icon on top right -> select `Faktury VAT (JPK_FA)` and dates range -> Select version `JPK_VAT (v3)` -> `Zapisz` -> Export XML file 

## Testing

```bash
.venv\Scripts\python -m unittest
```

## Linting

```bash
.venv\Scripts\python -m pylint **/*.py
```

## Usage

### Export to CSV

```bash
.venv\Scripts\python main.py input.xml csv
```
or
```bash
start.bat csv
```

### Export to JSON

```bash
.venv\Scripts\python main.py input.xml json
```
or
```bash
start.bat json
```

### Export to DB

```bash
.venv\Scripts\python main.py input.xml db
```
or
```bash
start.bat db
```

### Clear output directories

```bash
start.bat clear
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
