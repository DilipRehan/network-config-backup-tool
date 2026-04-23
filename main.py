from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoAuthenticationException, NetMikoTimeoutException
from devices import DEVICES
from datetime import datetime
import os

routers = DEVICES

success = []
failed = []

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
folder = f"backup_config/running_config_{timestamp}"
os.makedirs(folder)

print("=" * 45)
print("       NETWORK CONFIG BACKUP TOOL v2")
print("=" * 45)

for router in routers:
    try:
        connection = ConnectHandler(**router)
        connection.enable()

        output = connection.send_command("show running-config")
        filename = f"{folder}/{router['host']}_{timestamp}.txt"
        with open (filename,"w") as f:
            f.write(f"Device   : {router['host']}\n")
            f.write(f"Backup   : {timestamp}\n")
            f.write("=" * 45 + "\n")
            f.write(output)
            
        success.append(router['host'])
        print(f"  ✅ {router['host']} — backed up")
        connection.disconnect()


    except NetmikoAuthenticationException:
        failed.append(router['host'])
        print(f"{router['host']} - Wrong credentials!")

    except NetMikoTimeoutException:
        failed.append(router['host'])
        print(f"{router['host']}- Unreachable (timeout)")
        
    except Exception as e:
        failed.append(router['host'])
        print(f"{router['host']} - Failed: {e}")


print("=" * 45)
print(f"  Success : {len(success)}")
print(f"  Failed  : {len(failed)}")
print(f"  Folder  : {folder}")
print("=" * 45) 

