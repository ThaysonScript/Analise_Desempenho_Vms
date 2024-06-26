TIPO_VIRTUALIZADOR = '_kvm/logs'

CAMINHO_ABSOLUTO = f'./data_logs/logs{TIPO_VIRTUALIZADOR}'

logs_gerais = {
    'machine_monitoring_cpu': f'{CAMINHO_ABSOLUTO}/machine_monitoring-cpu.csv',
    'machine_monitoring_zombies': f'{CAMINHO_ABSOLUTO}/machine_monitoring-zombies.csv',
    'machine_monitoring_mem': f'{CAMINHO_ABSOLUTO}/machine_monitoring-mem.csv',
    'machine_monitoring_disk': f'{CAMINHO_ABSOLUTO}/machine_monitoring-disk.csv',
    'machineHost_server_status': f'{CAMINHO_ABSOLUTO}/machineHost_server_status.csv',
    
    'response_times': f'{CAMINHO_ABSOLUTO}/response_times.csv',
    'reset_times': f'{CAMINHO_ABSOLUTO}/reset_times.csv'
}

logs_vbox = {
    'vbox_monitoring_VBoxHeadless': f'{CAMINHO_ABSOLUTO}/vbox_monitoring-VBoxHeadless.csv',
    'vbox_monitoring_VBoxSVC': f'{CAMINHO_ABSOLUTO}/vbox_monitoring-VBoxSVC.csv',
    'vbox_monitoring_VBoxXPCOMIPCD': f'{CAMINHO_ABSOLUTO}/vbox_monitoring-VBoxXPCOMIPCD.csv'
}

logs_kvm = {
    'kvm_Headless_monitoring': f'{CAMINHO_ABSOLUTO}/kvm_Headless_monitoring.csv',
    'kvm_libvirtd_service_monitoring': f'{CAMINHO_ABSOLUTO}/kvm_libvirtd_service_monitoring.csv'
}

logs_xen = {
    
}

logs_lxc = {
    
}

logs_fragmentacao = {
    'fragmentation': f'{CAMINHO_ABSOLUTO}/fragmentation.csv'
}