# SNORT-IDS - Intrusion Detection System

This repository contains the configuration and setup files to install and configure Snort, a popular open-source Intrusion Detection System (IDS). This repository provides an automated installation script, basic configuration, and a sample ruleset to get you started with Snort.

## Features
- Automated Snort installation via script (`install.sh`)
- Basic Snort configuration (`snort.conf`)
- Custom rule set (`local.rules`)
- Supports traffic logging and real-time packet analysis

## Prerequisites
- Ubuntu/Debian Linux environment
- Root access to install packages and configure system
- Basic understanding of networking and IDS concepts

## Installation

Follow these steps to set up Snort IDS:

1. Clone this repository:
    ```bash
    git clone https://Harshita3942/Snort-IDS.git
    cd Snort-IDS
    ```

2. Run the installation script:
    ```bash
    chmod +x scripts/install.sh
    sudo ./scripts/install.sh
    ```

3. The script will install Snort, configure the system, and download necessary rule sets.

4. After installation, check Snort version to verify installation:
    ```bash
    snort -V
    ```

5. Start Snort:
    ```bash
    sudo snort -c /etc/snort/snort.conf -i eth0
    ```

   Replace `eth0` with your network interface.

## Customizing Rules
- Modify the `local.rules` file to add your own rules.
- Add new rules to the `snort.conf` file by including the new `.rules` files.

## Logging and Monitoring
Snort will log alerts to `/etc/snort/snort.alert` by default. You can modify this behavior in the `snort.conf` file.

## Troubleshooting
- Ensure that your network interface is correctly specified in the command line (e.g., `eth0`).
- Check Snort logs for any error messages.

## License
MIT License
