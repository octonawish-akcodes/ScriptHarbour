import psutil
import logging

def check_system_health():
    try:
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent

        if cpu_usage > 90 or memory_usage > 90 or disk_usage > 90:
            generate_alert('Critical system health!')
            logging.warning('Critical system health detected.')
        else:
            logging.info('System health is normal.')
    except Exception as e:
        logging.error(f'Error checking system health: {e}')

def generate_alert(message):
    print(f'ALERT: {message}')

# Set up logging
logging.basicConfig(filename='monitoring_health.log', level=logging.INFO)

# Usage Example
check_system_health()
