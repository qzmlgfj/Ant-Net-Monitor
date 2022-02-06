CREATE TABLE status (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  time_stamp TIMESTAMP NOT NULL DEFAULT (datetime('now','localtime')),
  cpu_percent REAL,
  mem_availiable REAL,
  disk_usage REAL
);

DELETE FROM status;