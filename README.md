# ScriptHarbour
ScriptHarbour is a comprehensive suite of scripts designed to automate common system administration tasks, ensuring efficiency and reliability in managing systems across various platforms.

## Features

- **User Management:**
  - Create, modify, or delete user accounts.
  - Set permissions and user roles.
  - Reset passwords.

- **Backup and Restore:**
  - Automated backups of specific directories or entire systems.
  - Restoration of backups when needed.

- **Software Installation and Updates:**
  - Install, update, and manage software packages.
  - Ensure systems are up-to-date with the latest patches.

- **Monitoring and Health Checks:**
  - System health monitoring (CPU, memory, disk usage).
  - Alert generation for critical thresholds.

- **Log Analysis and Management:**
  - Log rotation and management.
  - Parsing logs for specific events or errors.

## Usage

### User Management

```bash
python3 user_management.py create_user Alex password123
python3 user_management.py modify_user Alex new_password456
python3 user_management.py delete_user Alex
```

### Backup and Restore

```bash
python3 backup_restore.py backup /path/to/source /path/to/backups
python3 backup_restore.py restore /path/to/backups/backup_20230101120000 /path/to/restore
```

### Software Installation and Updates

```bash
python3 software_management.py install_package nginx
python3 software_management.py update_system
```

### Monitoring and Health Checks

```bash
python3 monitoring_health.py
```

### Log Analysis and Management

```bash
python3 log_management.py /path/to/application.log ERROR
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/octonawish-akcodes/ScriptHarbour.git
   ```

2. Navigate to the project directory:

   ```bash
   cd ScriptHarbour
   ```

3. Run scripts as described in the usage section.

## Configuration

- Adjust script configurations and settings directly in the scripts or through configuration files if needed.

## Logging and Error Handling

- Each script includes logging functionality to track script activities and errors. Log files are created for each script in the project directory.

## Contributing

Contributions are welcome! If you have ideas for new features, improvements, or bug fixes, please open an issue or submit a pull request.
