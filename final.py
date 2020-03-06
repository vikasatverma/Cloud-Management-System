import uuid
import random
import sys
with open('config.xml', 'r') as file:
    config = file.read()

sequence = 1

vmId = sequence+1
vmName = "VM"+str(vmId)
UUID = (uuid.uuid4())

mac = [ 0x00, 0x16, 0x3e,
random.randint(0x00, 0x7f),
random.randint(0x00, 0xff),
random.randint(0x00, 0xff) ]

mac_addr=':'.join(map(lambda x: "%02x" % x, mac))
source_path="/home/vikas/Documents/cs695/assignment2/ubuntu-3gb.qcow2"
cpu_count = 4

print vmId,vmName,UUID,mac_addr, source_path

config.replace("REPLACE_BY_CPU_COUNT",str(cpu_count))