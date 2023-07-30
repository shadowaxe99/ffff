# # Backup Database Utility

This utility provides a Python module for backing up and restoring SQLite databases.

## Features

- Backup a SQLite database to a specified location.
- Restore a SQLite database from a backup file.

## Installation

To use the Backup Database Utility, you need to have Python installed on your system. You can install it using the following command:

```shell
$ pip install backup-db-utility
```

## Usage

Here is an example of how to use the Backup Database Utility:

```python
from backup_db import backup_db, restore_db

# Create a backup
backup_db('mydatabase.db', 'backup/')

# Restore a database
restore_db('backup/mydatabase.db', 'restored/')
```

## Documentation

For detailed documentation and usage examples, please refer to the [Backup Database Utility Documentation](https://backup-db-utility-docs.com).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

This utility provides functions to backup and restore a SQLite database.

## Overview

The Backup Database Utility is a Python module that allows you to easily create backups of SQLite databases and restore them when needed. It provides two main functions: `backup_db` and `restore_db`.

## Features

- Create a backup of a specified SQLite database
- Restore a SQLite database from a backup file
- Handle errors such as file not found or permission issues

## Installation

To use the Backup Database Utility, follow these steps:

1. Install the required dependencies by running `pip install sqlite3`.
2. Import the `backup_db` and `restore_db` functions from `backup_db.py` in your Python script.
3. Use the functions to create backups and restore databases as needed.

## Usage

Here is an example of how to use the Backup Database Utility:

```python
from backup_db import backup_db, restore_db

# Create a backup
backup_db('mydatabase.db', 'backup/')

# Restore a database
restore_db('backup/mydatabase.db', 'restored/')
```


This utility provides functions to backup and restore a SQLite database.

This utility provides functions to backup and restore a SQLite database.

This utility provides functions to backup and restore a SQLite database.

## Functions

- `backup_db(db_name, backup_path)`: Creates a backup of the specified SQLite database.

### Parameters

- `db_name` (str): The name of the database to backup.
- `backup_path` (str): The path where the backup file will be saved.

#### Parameters

- `backup_path` (str): The path to the backup file.
- `restore_path` (str): The path where the restored database will be saved.

#### Returns

- None

#### Raises

- `FileNotFoundError`: If the specified backup file does not exist.
- `PermissionError`: If the user does not have permission to access the backup file or the restore path.

- `db_name` (str): The name of the database to backup.
- `backup_path` (str): The path where the backup file will be saved.

#### Returns

- None

#### Raises

- `FileNotFoundError`: If the specified database file does not exist.
- `PermissionError`: If the user does not have permission to access the database file or the backup path.

- `backup_path` (str): The path to the backup file.
- `restore_path` (str): The path where the restored database will be saved.

#### Returns

- None

#### Raises

- `FileNotFoundError`: If the specified backup file does not exist.
- `PermissionError`: If the user does not have permission to access the backup file or the restore path.

- `db_name` (str): The name of the database to backup.
- `backup_path` (str): The path where the backup file will be saved.

#### Returns

- None

#### Raises

- `FileNotFoundError`: If the specified database file does not exist.
- `PermissionError`: If the user does not have permission to access the database file or the backup path.

- `db_name` (str): The name of the database to backup.
- `backup_path` (str): The path where the backup will be saved.

#### Returns

- None

#### Raises

- `FileNotFoundError`: If the specified database file does not exist.
- `PermissionError`: If the user does not have permission to access the database file or the backup path.
- `restore_db(backup_path, restore_path)`: Restores a SQLite database from a backup file.

### Parameters

- `backup_path` (str): The path to the backup file.
- `restore_path` (str): The path where the restored database will be saved.

#### Parameters

- `backup_path` (str): The path to the backup file.
- `restore_path` (str): The path where the restored database will be saved.

#### Returns

- None

#### Raises

- `FileNotFoundError`: If the specified backup file does not exist.
- `PermissionError`: If the user does not have permission to access the backup file or the restore path.

## Usage

Import the `backup_db` and `restore_db` functions from `backup_db.py`:

```python
from backup_db import backup_db, restore_db
```

Call the `backup_db` function to create a backup of the SQLite database:

```python
backup_db('mydatabase.db', 'backup/')
```

Call the `restore_db` function to restore a SQLite database from a backup:

```python
restore_db('backup/mydatabase.db', 'restored/')
```

Import the `backup_db` and `restore_db` functions from `backup_db.py`:

```python
from backup_db import backup_db, restore_db
```

Call the `backup_db` function to create a backup of the database:

```python
backup_db('mydatabase.db', 'backup/')
```

Call the `restore_db` function to restore a database from a backup:

```python
restore_db('backup/mydatabase.db', 'restored/')
```

1. Import the `backup_db` and `restore_db` functions from `backup_db.py`.
2. Call the `backup_db` function to create a backup of the database.
3. Call the `restore_db` function to restore a database from a backup.

## Example

```python
from backup_db import backup_db, restore_db

# Create a backup
backup_db('mydatabase.db', 'backup/')

# Restore a database
restore_db('backup/mydatabase.db', 'restored/')
```
