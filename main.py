import nmap
import sys


scann = nmap.PortScanner()

scanner = scann.scan(sys.argv[1],'80',arguments='-O')

try:
    host_state = "The host is :" + scanner['scan'][sys.argv[1]]['status']['state']
    os_state = "percentage of system using OS %s is %s %%" %(scanner['scan'][sys.argv[1]]['osmatch'][0]['name'],scanner['scan'][sys.argv[1]]['osmatch'][0]['accuracy'])
    print(host_state)
    print(os_state)

except IndexError:
    print("Scan was not Successfull")
