import os
import subprocess
import urllib.request

# Helper function to run bash commands
def run_command(command):
    try:
        subprocess.check_call(command, shell=True)
        print(f"Command '{command}' executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        exit(1)

# Function to install dependencies
def install_dependencies():
    print("Installing dependencies...")
    run_command("sudo apt-get update -y")
    run_command("sudo apt-get install -y build-essential libpcap-dev libpcre3-dev libdumbnet-dev zlib1g-dev liblzma-dev")

# Function to install Snort
def install_snort():
    print("Downloading and installing Snort...")
    run_command("wget https://www.snort.org/downloads/snort/snort-2.9.17.tar.gz")
    run_command("tar -xzvf snort-2.9.17.tar.gz")
    os.chdir("snort-2.9.17")
    run_command("./configure --enable-sourcefire")
    run_command("make")
    run_command("sudo make install")

# Function to configure Snort directories
def configure_directories():
    print("Setting up Snort directories...")
    run_command("sudo mkdir -p /etc/snort")
    run_command("sudo mkdir -p /etc/snort/rules")
    run_command("sudo mkdir -p /etc/snort/preproc_rules")
    run_command("sudo mkdir -p /etc/snort/so_rules")

# Function to download Snort community rules
def download_community_rules():
    print("Downloading Snort community rules...")
    run_command("wget https://snort.org/downloads/community/snort-2.9.17-community-rules.tar.gz")
    run_command("tar -xzvf snort-2.9.17-community-rules.tar.gz -C /etc/snort/rules")

# Function to create snort.conf file
def create_snort_config():
    print("Creating Snort configuration file (snort.conf)...")
    snort_conf = """
# Snort Configuration File (snort.conf)

# Set the network variable
ipvar HOME_NET any

# Enable rule sets
include $RULE_PATH/local.rules
include $RULE_PATH/community.rules

# Define output plugin
output alert_fast: snort.alert

# Log traffic in pcap format
output log_tcpdump: snort.log

# Set preprocessor settings
preprocessor frag3_global: max_frags 65536, timeout 60
preprocessor stream5_global: max_tcp 8192, max_udp 8192, max_icmp 8192

# Define rule paths
var RULE_PATH /etc/snort/rules
"""
    
    with open("/etc/snort/snort.conf", "w") as f:
        f.write(snort_conf)

# Function to create local.rules file
def create_local_rules():
    print("Creating custom Snort rules (local.rules)...")
    local_rules = """
# Custom Snort Rules (local.rules)

alert ip any any -> $HOME_NET any (msg:"Traffic from untrusted IP"; sid:1000001;)
alert tcp $HOME_NET any -> any 80 (msg:"HTTP Access"; sid:1000002;)
"""
    
    with open("/etc/snort/rules/local.rules", "w") as f:
        f.write(local_rules)

# Function to set up Snort user
def create_snort_user():
    print("Creating Snort user...")
    run_command("sudo useradd snort")
    run_command("sudo usermod -aG snort snort")
    run_command("sudo chown snort:snort /etc/snort -R")

# Function to verify Snort installation
def verify_snort():
    print("Verifying Snort installation...")
    run_command("snort -V")

# Function to run Snort
def run_snort():
    print("Running Snort...")
    run_command("sudo snort -c /etc/snort/snort.conf -i eth0")  # Replace eth0 with your network interface

# Main function
def main():
    install_dependencies()
    install_snort()
    configure_directories()
    download_community_rules()
    create_snort_config()
    create_local_rules()
    create_snort_user()
    verify_snort()
    run_snort()

if __name__ == "__main__":
    main()
