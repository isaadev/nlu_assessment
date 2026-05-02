CREATE TABLE IF NOT EXISTS violations(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	address TEXT,
	violation_date TEXT,
	violation_status TEXT,
	violation_description TEXT,
	violation_inspector_comments TEXT,
	violation_code TEXT
);

-- idx to allow fast lookups and joins w/ scofflaw
CREATE INDEX IF NOT EXISTS idx_violations_address ON violations(address);

-- idx to filter by date for scofflaw violation endpoint
CREATE INDEX IF NOT EXISTS idx_violations_date ON violations (violation_date);

CREATE TABLE IF NOT EXISTS scofflaws(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	address text
);

CREATE INDEX IF NOT EXISTS idx_scofflaws_address ON scofflaws (address);


CREATE TABLE IF NOT EXISTS comments(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	address TEXT,
	author TEXT,
	datetime TEXT,
	comment TEXT
);

CREATE INDEX IF NOT EXISTS idx_comments_address ON comments(address);



