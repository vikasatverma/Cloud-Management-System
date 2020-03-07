# Example-12.py
from __future__ import print_function
import sys
import libvirt
from time import sleep

spawnVM=0

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

dom = conn.lookupByName("Server-1")

if dom == None:
    print('Failed to define a domain from an XML definition.', file=sys.stderr)
    exit(1)
#
# if dom.create() < 0:
#     print('Can not boot guest domain.', file=sys.stderr)
#     exit(1)

vote_to_spawn=0
VMSpawned=0

def statGenarator():
    global vote_to_spawn,spawnVM,VMSpawned
    while(1):
        cpu_stats1 = dom.getCPUStats(False)
        sleep(1)
        cpu_stats2 = dom.getCPUStats(False)

        cpu_usage = int((cpu_stats2[0]['cpu_time']-cpu_stats1[0]['cpu_time'])/1000000000.*100)
        # print(cpu_stats2,cpu_stats1)
        # for (i, cpu) in enumerate(cpu_stats):
        # print(int((cpu_stats2[0]['cpu_time']-cpu_stats1[0]['cpu_time'])/1000000000.*100))

        if(cpu_usage<50):
            vote_to_spawn=0
        else:
            vote_to_spawn=vote_to_spawn+1

        if(vote_to_spawn==10 and not VMSpawned):
            #Spawn new VM
            print("Spawn VM!")
            spawnVM()
            #     exit(1)
            VMSpawned=1
            vote_to_spawn=-20


        yield (cpu_usage)

dom2=0

def spawnVM():
    dom2 = conn.lookupByName("Server-2")

    if dom2 == None:
        print('Failed to look for the domain.', file=sys.stderr)
    if dom2.create() < 0:
        print('Can not boot guest domain.', file=sys.stderr)

