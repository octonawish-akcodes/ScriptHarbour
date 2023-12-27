import subprocess
import logging

def install_package(package_name):
    try:
        subprocess.run(['apt-get', 'install', '-y', package_name], check=True)
        logging.info(f'Package installed successfully: {package_name}')
    except subprocess.CalledProcessError as e:
        logging.error(f'Error installing package {package_name}: {e}')

def update_system():
    try:
        subprocess.run(['apt-get', 'update'], check=True)
        subprocess.run(['apt-get', 'upgrade', '-y'], check=True)
        logging.info('System updated successfully')
    except subprocess.CalledProcessError as e:
        logging.error(f'Error updating system: {e}')

# Set up logging
logging.basicConfig(filename='software_management.log', level=logging.INFO)

# Usage Examples
install_package('nginx')
update_system()
