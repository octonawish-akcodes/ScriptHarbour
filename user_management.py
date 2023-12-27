import subprocess
import logging

def create_user(username, password):
    try:
        subprocess.run(['useradd', username, '-p', password], check=True)
        logging.info(f'User created successfully: {username}')
    except subprocess.CalledProcessError as e:
        logging.error(f'Error creating user {username}: {e}')

def modify_user(username, new_password):
    try:
        subprocess.run(['passwd', username, new_password], check=True)
        logging.info(f'Password modified successfully for user: {username}')
    except subprocess.CalledProcessError as e:
        logging.error(f'Error modifying password for user {username}: {e}')

def delete_user(username):
    try:
        subprocess.run(['userdel', '-r', username], check=True)
        logging.info(f'User deleted successfully: {username}')
    except subprocess.CalledProcessError as e:
        logging.error(f'Error deleting user {username}: {e}')

# Set up logging
logging.basicConfig(filename='user_management.log', level=logging.INFO)

# Usage Examples
create_user('Alex', 'password123')
modify_user('Alex', 'new_password456')
delete_user('Alex')
