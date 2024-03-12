monitoring_files = {
    'CPU': 'machine_monitoring-cpu.csv',
    'Disk': 'machine_monitoring-disk.csv',
    'Zumbis': 'machine_monitoring-zombies.csv',
    'Memory': 'machine_monitoring-mem.csv',
    'Process - VBoxHeadless': 'monitoring-VBoxHeadless.csv',
    'Process - VBoxSVC': 'monitoring-VBoxSVC.csv',
    'Process - VBoxXPCOMIPCD': 'monitoring-VBoxXPCOMIPCD.csv',
    'Server response time': 'response_times.csv'
}

ylabels = {
    'CPU': "(percentage)",
    'Disk': "Disk usage (GB)",
    'Zumbis': "Zumbis processes(qtt)",
    'Memory': "(MB)",
    'Process - VBoxHeadless': {
        'cpu': 'CPU usage (percentage)',
        "vmrss": "Physical memory usage(MB)",
        "vsz": "Virtual memory usage (MB)",
        "swap": "Swap used(MB)",
        'mem': 'Memory usage (percentage)',
        "thread": "Number of threads(qtt)"
    },
    'Process - VBoxSVC': {
        'cpu': 'CPU usage (percentage)',
        "vmrss": "Physical memory usage(MB)",
        "vsz": "Virtual memory usage (MB)",
        "swap": "Swap used(MB)",
        'mem': 'Memory usage (percentage)'
    },
    'Process - VBoxXPCOMIPCD': {
        'cpu': 'CPU usage (percentage)',
        "vmrss": "Physical memory usage(MB)",
        "vsz": "Virtual memory usage (MB)",
        "swap": "Swap used(MB)",
        'mem': 'Memory usage (percentage)'
    },
    'Server response time': "Response time(s)"
}
