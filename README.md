# Kismet MetaGPS Quickstart

This Python script simplifies the process of setting up Kismet remote capture and integrating it with MetaGPS for location-tagged survey results. It assumes that you have the latest stable release of Kismet installed from 2023 or higher, with appropriate WiFi drivers and hardware capable of monitor mode or supported Kismet hardware with remote capture tools enabled.

## Prerequisites

- **Kismet Installation**: Ensure you have Kismet installed and configured. You can download the latest stable release from the [Kismet website](https://www.kismetwireless.net/downloads/). Nightly builds should also work.
  
- **API Key**: Create an API key on the Kismet server following the instructions on the [MetaGPS GitHub page](https://github.com/hobobandy/python-kismet-metagpsd).

- **MetaGPS Integration**: Clone the [python-kismet-metagpsd](https://github.com/hobobandy/python-kismet-metagpsd) repository and follow the instructions to set it up.

## Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/alphafox02/kismet_metagpsd_quickstart.git
    ```

2. Clone the `python-kismet-metagpsd` repository:

    ```bash
    git clone https://github.com/hobobandy/python-kismet-metagpsd.git
    ```

3. Copy the script into the `python-kismet-metagpsd` directory:

    ```bash
    cp kismet_metagpsd_quickstart.py python-kismet-metagpsd/
    ```

4. Navigate to the `python-kismet-metagpsd` directory:

    ```bash
    cd python-kismet-metagpsd
    ```

5. Ensure that the `metagpsd.py` script is in the same directory as the wrapper script.

6. Install the required dependencies for `python-kismet-metagpsd`:

    On DragonOS FocalX, the only requirements currently needed for the `python-kismet-metagpsd` repository are the following, installed via pip3:

    ```bash
    sudo pip3 install gpsdclient loguru
    ```

7. Run the script with appropriate arguments:

    ```bash
    python3 kismet_metagpsd_quickstart.py --kismet-cap-bin <path-to-kismet-cap-bin> --kismet-host <kismet-server-address> --kismet-apikey <kismet-api-key> --source-name <source-name> --metagps-name <metagps-name> --use-ssl
    ```

    Replace `<path-to-kismet-cap-bin>`, `<kismet-server-address>`, `<kismet-api-key>`, `<source-name>`, and `<metagps-name>` with your specific values.

    For example:

    ```bash
    python3 kismet_metagpsd_quickstart.py --kismet-cap-bin kismet_cap_linux_wifi --kismet-host 10.185.1.147:2501 --kismet-apikey 156AD3F90791C3960058E53BD7FF80CE --source-name wlp1s0 --metagps-name remote0
    ```

8. The script will start the Kismet remote capture tool and the MetaGPS script. It will continuously monitor and restart the MetaGPS script if necessary.

## Notes

- Ensure that your Kismet server is reachable via the internet or both sides are on a VPN.
- This script assumes appropriate WiFi drivers and hardware capable of monitor mode or other supported Kismet hardware.
- For more information and troubleshooting, refer to the documentation of Kismet and python-kismet-metagpsd.

