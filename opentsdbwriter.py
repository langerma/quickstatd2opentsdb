#!/bin/env python
import pprint
import json

perffile  = open('all.active', 'r').readlines()

def metric(perfarray, prefix, zone):
    if perfarray[1] == "disk":
        tag_disk  = str(perfarray[2])
        metric = prefix + "diskio_" + str(perfarray[3])
        value = float(perfarray[4])
        timestamp = int(perfarray[5].rstrip())
        tags_dict = {'host':tag_host, 'disk':tag_disk}
    elif perfarray[1] == "diskspace":
        tag_path  = str(perfarray[2]).replace('_','/')
        metric = prefix + "disk_" + str(perfarray[3])
        value = float(perfarray[4])
        timestamp = int(perfarray[5].rstrip())
        tags_dict = {'host':tag_host, 'path':tag_path}
    elif perfarray[1] == "network" and perfarray[2] != "tcp":
        tag_interface = str(perfarray[2])
        metric = prefix + "net_" + str(perfarray[3])
        value = float(perfarray[4])
        timestamp = int(perfarray[5].rstrip())
        tags_dict = {'host':tag_host, 'interface':tag_interface}
    elif perfarray[1] == "network" and perfarray[2] == "tcp":
        metric = prefix + "net_" + str(perfarray[3])
        value = float(perfarray[4])
        timestamp = int(perfarray[5].rstrip())
        tags_dict = {'host':tag_host}
    elif perfarray[1] == "cpu":
        tag_cpu = str(perfarray[2]).replace('cpu-','')
        metric = prefix + "cpu_" + str(perfarray[3]).replace('cpu-','')
        value = float(perfarray[4])
        timestamp = int(perfarray[5].rstrip())
        tags_dict = {'host':tag_host, 'cpu':tag_cpu}
    elif perfarray[1] == "ioadapters":
        tag_ioadapter = str(perfarray[2])
        metric = prefix + "ioadapters_" + str(perfarray[3])
        value = float(perfarray[4])
        timestamp = int(perfarray[5].rstrip())
        tags_dict = {'host':tag_host, 'ioadapter':tag_ioadapter}
    #elif perfarray[1] == "memory"
    elif perfarray[1] == "paging":#r perfarray[1] == "processes" or perfarray[1] == "paging":
        metric = prefix + (str(perfarray[1]) + '_').replace('memory_','') + str(perfarray[2]).replace('-','_')
        value = float(perfarray[3])
        timestamp = int(perfarray[4].rstrip())
        tags_dict = {'host':tag_host}
    elif perfarray[1] == "zfs":
        tag_zpool = str(perfarray[2])
        metric = prefix + "zfs_" + str(perfarray[3])
        value = float(perfarray[4])
        timestamp = int(perfarray[5].rstrip())
        tags_dict = {'host':tag_host,'zpool':tag_zpool}
    elif perfarray[1] == "loadavg":
        metric = prefix + "system_load" + str(perfarray[2]).replace('_min','')
        value = float(perfarray[3])
        timestamp = int(perfarray[4].rstrip())
        tags_dict = {'host':tag_host}
    elif perfarray[1] == "vmstat":
        metric = prefix + "vmstat_" + str(perfarray[2]) + "_" + str(perfarray[3])
        value = float(perfarray[4])
        timestamp = int(perfarray[5].rstrip())
        tags_dict = {'host':tag_host}
    elif perfarray[1] == "users":
        tag_users = str(perfarray[2])
        metric = prefix + "user_" + str(perfarray[3])
        value = float(perfarray[4])
        timestamp = int(perfarray[5].rstrip())
        tags_dict = {'host':tag_host, 'user':tag_users}
    else:
        print perfarray


for perfline in perffile:
    perfarray = perfline.split(' ')
    perfarray = perfarray[0].split('.') + perfarray[1:]
    perfarray = perfarray[2:]
    metric(perfarray,'solaris.')
