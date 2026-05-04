import csv
import sqlite3
from datetime import datetime, date

cn = sqlite3.connect('test.db')
ddl = open('scripts/tables.sql').read()
cn.executescript(ddl)
cursor = cn.cursor()

with open('datasets/Building_Code_Scofflaw_List_20250807.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute(
            """
            INSERT INTO scofflaws (address)
            VALUES (?)
            """,
            (row["ADDRESS"].strip().upper(),)
        )
    cn.commit()
    
with open('datasets/Building_Violations_20250815.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        d = datetime.strptime(row["VIOLATION DATE"], "%m/%d/%Y").date()

        if d < date(2024,1,1):
            continue
        else:
            cursor.execute(
             """
                INSERT INTO violations(
                
                     address,
                    violation_date,
                    violation_status,
                     violation_description,
                     violation_inspector_comments,
                    violation_code
                )
                VALUES(?,?,?,?,?,?)
                """,
                (
                    row["ADDRESS"].strip().upper(),
                    d.isoformat(),
                    row["VIOLATION STATUS"],
                    row["VIOLATION DESCRIPTION"],
                    row["VIOLATION INSPECTOR COMMENTS"],
                    row["VIOLATION CODE"],
                )
            )
cn.commit()

