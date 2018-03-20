import psutil
import os
import json


def get_stats():
    cpu_times = psutil.cpu_times()
    virtual_memory = psutil.virtual_memory()
    swap_memory = psutil.swap_memory()
    disk_usage = psutil.disk_usage('/')
    network_io_counters = psutil.net_io_counters(pernic=True)

    data = {"hostname": os.uname()[1], "stats": {"cpu": {
        "nice": cpu_times.nice,
        "user": cpu_times.user,
        "system": cpu_times.system,
        "idle": cpu_times.idle,
        "iowait": cpu_times.iowait,
        "irq": cpu_times.irq,
        "softirq": cpu_times.softirq,
        "steal": cpu_times.steal,
        "guest": cpu_times.guest,
        "guest_nice": cpu_times.guest_nice
    },
        "virtual_memory": {
            "total": virtual_memory.total,
            "available": virtual_memory.available,
            "percent": virtual_memory.percent,
            "used": virtual_memory.used,
            "free": virtual_memory.free,
            "active": virtual_memory.active,
            "inactive": virtual_memory.inactive,
            "buffers": virtual_memory.buffers,
            "cached": virtual_memory.cached,
            "shared": virtual_memory.shared
        },
        "swap_memory": {
            "total": swap_memory.total,
            "used": swap_memory.used,
            "free": swap_memory.free,
            "percent": swap_memory.percent,
            "sin": swap_memory.sin,
            "sout": swap_memory.sout
        },
        "disk": {
            "total": disk_usage.total,
            "used": disk_usage.used,
            "free": disk_usage.free,
            "percent": disk_usage.percent,
        },
        "network": {}
    }}

    for key in network_io_counters:
        data["stats"]["network"][key] = {}
        data["stats"]["network"][key]["bytes_sent"] = network_io_counters[key].bytes_sent
        data["stats"]["network"][key]["packets_sent"] = network_io_counters[key].packets_sent
        data["stats"]["network"][key]["packets_recv"] = network_io_counters[key].packets_recv
        data["stats"]["network"][key]["errin"] = network_io_counters[key].errin
        data["stats"]["network"][key]["errout"] = network_io_counters[key].errout
        data["stats"]["network"][key]["dropin"] = network_io_counters[key].dropin
        data["stats"]["network"][key]["dropout"] = network_io_counters[key].dropout

    return data


def main():
    data = json.dumps({"data": get_stats()}).encode('utf-8')
    print(data)


if __name__ == "__main__":
    main()
