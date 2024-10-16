# Importing Modules
import subprocess


def ping(host:str):
    """Pings a host and checks if it's reachable.

    Args:
        host: The hostname or IP address to ping.

    Raises:
        CalledProcessError: If the ping command fails.
    """
    try:
        # Use the ping command with a count of 4 and a timeout of 2 seconds
        subprocess.run(['ping', '-n', '4', '-w', '2', host], check=True)  
        print(f"{host} is reachable")
    except subprocess.CalledProcessError:
        return str("offline")
    else:
        return str("online")