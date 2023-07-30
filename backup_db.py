import sqlite3
import shutil
import os


def backup_db(db_name, backup_path):
    try:
        # Check if backup path exists, create if it doesn't
        if not os.path.exists(backup_path):
            os.makedirs(backup_path)

        # Create a backup
        shutil.copy2(db_name, backup_path)
        print('Database backup was successful.')

    except Exception as e:
        print(f'An error occurred during backup: {str(e)}')


def restore_db(backup_path, restore_path):
    try:
        # Check if restore path exists
        if not os.path.exists(restore_path):
            print('Restore path does not exist.')
            return

        # Restore the database
        shutil.copy2(backup_path, restore_path)
        print('Database restore was successful.')

    except Exception as e:
        print(f'An error occurred during restore: {str(e)}')