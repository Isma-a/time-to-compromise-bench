import os
import requests
import hashlib

github_data_url = 'https://raw.githubusercontent.com/Isma-a/hashcat-gpu-benchmarks/refs/heads/main/data/hashcat_gpu_benchmarks.csv'
data_path = 'resources/data/hashcat_gpu_benchmarks.csv'

def get_local_file_hash(file_path:str)->str|None:
    """Calculates the fingerprint of a local file."""
    if not os.path.exists(file_path):
        return None

    with open(file_path, 'rb') as f:
        content = f.read().replace(b'\r\n', b'\n').strip() # Clean local file
        return hashlib.sha256(content).hexdigest() # Read the file and generate his hash


def update_from_github(raw_github_url:str, local_path:str)->bool:
    """
    Checks network connection, downloads the remote file, and replaces
    the local one only if it has been modified.
    """
    print(f"Checking for updates for {local_path}")

    # Network check
    try:
        response = requests.get(raw_github_url, timeout=5) # timeout=5 prevents the app from freezing if slow network
        response.raise_for_status()  # Verify that the page exists
    except requests.RequestException:
        print("-> No network or remote file unreachable.")
        return False

    # Hash the remote content
    remote_content = response.content # Clean remote file
    clean_remote_content = remote_content.replace(b'\r\n', b'\n').strip()
    remote_hash = hashlib.sha256(clean_remote_content).hexdigest()

    local_hash = get_local_file_hash(local_path) # Get the hash of the current local file

    if local_hash == remote_hash: # Comparison
        print("-> The file is already up to date.")
        return False
    else:
        print("-> New version detected! Updating...")

        # Ensure the destination folder exists
        os.makedirs(os.path.dirname(local_path), exist_ok=True)

        # Overwrite old file with the new one
        with open(local_path, 'wb') as f:
            f.write(remote_content)

        print("-> File successfully updated!")
        return True