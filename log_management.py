import logging
from logging.handlers import RotatingFileHandler

def setup_logging(log_file):
    try:
        logging.basicConfig(
            handlers=[RotatingFileHandler(log_file, maxBytes=100000, backupCount=5)],
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        logging.info(f'Logging initialized. Log file: {log_file}')
    except Exception as e:
        print(f'Error setting up logging: {e}')

def parse_logs(log_file, keyword):
    try:
        with open(log_file, 'r') as file:
            for line in file:
                if keyword in line:
                    print(line.strip())
                    logging.info(f'Matched log entry: {line.strip()}')
    except Exception as e:
        logging.error(f'Error parsing logs: {e}')

# Set up logging
setup_logging('log_management.log')

# Usage Example
parse_logs('/path/to/application.log', 'ERROR')
