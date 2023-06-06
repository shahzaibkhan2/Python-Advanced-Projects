# Import third party module called psutil
import psutil

# Function to get cpu usage
def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

# Function to get memory usage
def get_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    return memory_usage

# Function to get disk usage
def get_disk_usage():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    return disk_usage

# Function to get temperature
def get_temperature():
    temperature = psutil.sensors_temperatures()
    cpu_temperature = temperature['coretemp'][0].current if 'coretemp' in temperature else None
    return cpu_temperature

# Function to get pc health
def get_pc_health():
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    disk_usage = get_disk_usage()
    cpu_temperature = get_temperature()

    health = {
        'CPU Usage': cpu_usage,
        'Memory Usage': memory_usage,
        'Disk Usage': disk_usage,
        'CPU Temperature': cpu_temperature
    }
    return health

# Get PC Health test
pc_health = get_pc_health()
for metric, value in pc_health.items():
    print(f'{metric}: {value}')
