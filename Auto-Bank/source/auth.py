# packages
import winreg


def get_machine_uuid():
    # Open the registry key
    registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\Cryptography')
    
    # Read the value
    try:
        uuid, _ = winreg.QueryValueEx(registry_key, 'MachineGuid')
        return str(uuid).upper()
    except EnvironmentError:
        raise Exception("Could not retrieve Machine UUID")
    finally:
        winreg.CloseKey(registry_key)

# Example usage

def authenticate():
    return True
