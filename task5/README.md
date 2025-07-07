# Task 5 - Deployment of Nginx using Ansible

## Description
This Ansible playbook automates:
- System package updates
- Nginx installation
- Custom index.html deployment
- Nginx service management

## Files
- `playbook.yml` - Main playbook
- `inventory.ini` - Inventory file with target host
- `index.html` - Custom webpage

## Usage
```bash
ansible-playbook -i inventory.ini playbook.yml -k -K --ssh-extra-args='-o StrictHostKeyChecking=no'