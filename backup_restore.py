import shutil
import os
import datetime
import logging

def backup(source, destination):
    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        backup_folder = os.path.join(destination, f'backup_{timestamp}')
        shutil.copytree(source, backup_folder)
        logging.info(f'Backup created successfully: {backup_folder}')
    except Exception as e:
        logging.error(f'Error creating backup: {e}')

def restore(source, destination):
    try:
        shutil.rmtree(destination)
        shutil.copytree(source, destination)
        logging.info(f'Restore completed successfully from: {source}')
    except Exception as e:
        logging.error(f'Error restoring backup: {e}')

# Set up logging
logging.basicConfig(filename='backup_restore.log', level=logging.INFO)

# Usage Examples
backup('/path/to/source', '/path/to/backups')
restore('/path/to/backups/backup_20230101120000', '/path/to/restore')
