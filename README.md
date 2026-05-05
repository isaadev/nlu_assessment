# NLU Back-End Assessment

This project is a simple back-end API built with Flask for working with two City of Chicago datasets:

- Building Violations
- Building Code Scofflaw List

The application ingests the CSV files, stores the data locally, and provides API endpoints for querying property information by address. It joins violation and scofflaw data by address so a user can view related building information in one place. The API also supports creating comments associated with a property address.

## Dependencies

- Python 3.10+
- Flask
- SQLite

## Project Structure

```text
├── app.py
├── datasets
    ├── Building_Code_Scofflaw_List_20250807.csv
    └── Building_Violations_20250815.csv
├── docs.md
├── notes.md
├── README.md
├── requirements.txt
├── scripts
    ├── script.py
    └── tables.sql


```

## Instructions
Run:
```bash
pip install -r requirements.txt
```

Then:
1. Place the two CSV files in the `datasets/` folder (if not already):
   - `Building_Code_Scofflaw_List_20250807.csv`
   - `Building_Violations_20250815.csv`

2. Run the ingestion script
```bash
python3.10 scripts/script.py
```

3. Start the server
```bash
python3.10 app.py
```
