import argparse
import subprocess
import time
import signal
import os
import psutil

kismet_process = None  # Global variable to store the process object

# Function to start the kismet_cap tool
def start_kismet_cap(kismet_cap_bin, host_uri, apikey, source_name, metagps_name):
    global kismet_process
    command = [
        kismet_cap_bin,
        "--connect", host_uri,
        "--apikey", apikey,
        "--source", f"{source_name}:name={metagps_name},metagps={metagps_name}"
    ]
    kismet_process = subprocess.Popen(command)

# Function to properly terminate the kismet_cap tool
def stop_kismet_cap():
    global kismet_process
    if kismet_process:
        kismet_process.terminate()

# Function to start the MetaGPSD script
def start_metagps(host_uri, metagps_name, apikey, use_ssl):
    print("Starting MetaGPSD script...")
    command = ["python3", "metagpsd.py"]
    command.extend(["--connect", host_uri])
    command.extend(["--metagps", metagps_name])
    command.extend(["--apikey", apikey])
    if use_ssl:
        command.append("--ssl")
    subprocess.Popen(command)

# Function to check if the MetaGPSD script is running
def is_metagps_running():
    for process in psutil.process_iter(['cmdline']):
        if process.info['cmdline'] and 'python3' in process.info['cmdline'] and 'metagpsd.py' in process.info['cmdline']:
            return True
    return False

# Function to continuously monitor and restart the MetaGPSD script if necessary
def monitor_metagps(host_uri, metagps_name, apikey, use_ssl):
    while True:
        if not is_metagps_running():
            print("MetaGPSD script is not running. Restarting...")
            start_metagps(host_uri, metagps_name, apikey, use_ssl)
            
            # Wait for a brief period to allow the script to attempt connection
            time.sleep(10)
            
            # Check if the script is still running after the restart
            if is_metagps_running():
                print("MetaGPSD script restarted successfully.")
            else:
                print("Failed to restart MetaGPSD script.")
        else:
            print("MetaGPSD script is running.")
        time.sleep(10)  # Check every 10 seconds

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--kismet-cap-bin", required=True, help="Kismet capture tool binary")
    parser.add_argument("--kismet-host", required=True, help="Host address for both Kismet and MetaGPS")
    parser.add_argument("--kismet-apikey", required=True, help="API key for both Kismet and MetaGPS")
    parser.add_argument("--source-name", required=True, help="Source name for kismet_cap tool")
    parser.add_argument("--metagps-name", required=True, help="MetaGPS name")
    parser.add_argument("--use-ssl", action="store_true", help="Use SSL for MetaGPS connection")
    args = parser.parse_args()

    # Start kismet_cap tool
    start_kismet_cap(args.kismet_cap_bin, args.kismet_host, args.kismet_apikey, args.source_name, args.metagps_name)

    # Start MetaGPSD script
    start_metagps(args.kismet_host, args.metagps_name, args.kismet_apikey, args.use_ssl)

    # Monitor and restart MetaGPSD script if necessary
    monitor_metagps(args.kismet_host, args.metagps_name, args.kismet_apikey, args.use_ssl)

    # Cleanly terminate kismet_cap tool before exiting
    stop_kismet_cap()

if __name__ == "__main__":
    main()
