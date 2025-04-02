import requests
import time
import psutil
import GPUtil

# ----- ESP32 IP Address -----
num = input('последние 3 цифры - ')
esp32_ip = "192.168.0." + num
data_endpoint = f"http://{esp32_ip}/data"

def get_gpu_usage():
    try:
        gpus = GPUtil.getGPUs()
        if gpus:
            gpu_load = gpus[0].load * 100  # Get load percentage of the first GPU
            return int(gpu_load)
        else:
            return 0  # No GPU found
    except Exception as e:
        print(f"Error getting GPU usage: {e}")
        return 0

while True:
    cpu_usage = psutil.cpu_percent(interval=0.1)
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    gpu_usage = get_gpu_usage()  # Get GPU usage

    data = {
        "cpu": int(cpu_usage),
        "ram": int(ram_usage),
        "disk": int(disk_usage),
        "gpu": int(gpu_usage)  # Include GPU usage in data
    }

    try:
        response = requests.post(data_endpoint, data=data, timeout=5)
        response.raise_for_status()
        print(f"Data sent, response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending {e}")

    time.sleep(1)