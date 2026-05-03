# Take-home


## Tables
3 tables needed
- **violations**: `id`, `address`, `violation_date`, `violation_code`, `violation_status`, `violation_description`, `violation_inspector_comments`
- **scofflaws**: `id`, `address`
- **comments**: `id`, `address`, `author`, `datetime`, `comment



# SQL
---
```sql
	CREATE TABLE violations(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	ADDRESS TEXT,
	VIOLATION_DATE TEXT,
	VIOLATION_DESCRIPTION text,
	VIOLATION_STATUS TEXT,
	COMMENTS TEXT,
	VIOLATION_CODE TEXT
	);

CREATE INDEX idx_violations_address ON violations (address);
```

```sql
CREATE TABLE scofflaws(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	ADDRESS TEXT
);
```


```SQL
CREATE TABLE COMMENTS(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	ADDRESS TEXT,
	AUTHOR TEXT,
	DATETIME TEXT,
	COMMENT TEXT
	);
```
