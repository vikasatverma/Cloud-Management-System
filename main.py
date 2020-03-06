# Example-12.py
from __future__ import print_function
import sys
import libvirt
from time import sleep



conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

dom = conn.lookupByName("Client")

if dom == None:
    print('Failed to define a domain from an XML definition.', file=sys.stderr)
    exit(1)
#
# if dom.create() < 0:
#     print('Can not boot guest domain.', file=sys.stderr)
#     exit(1)
while(1):
    cpu_stats1 = dom.getCPUStats(False)
    sleep(2)
    cpu_stats2 = dom.getCPUStats(False)
    # for (i, cpu) in enumerate(cpu_stats):
    print(int((cpu_stats2[1]['cpu_time']-cpu_stats1[1]['cpu_time'])/2000000000.*100))

# print('Guest '+dom.name()+' has booted', file=sys.stderr)

conn.close()
exit(0)