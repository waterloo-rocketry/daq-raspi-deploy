# DAQ Raspi Deploy
An Ansible playbook used to deploy predictably and repetedly to a Raspberry Pi that acts as the main 
[Omnibus](https://github.com/waterloorocketry/omnibus) server during system tests and launch operations.

Based on [ansible-pi](https://github.com/Calychas/ansible-pi).

Tasks:
- Cron for updates
- SWAP expansion
- Install Git
- Install docker
- (WIP) Install Omnibus components
