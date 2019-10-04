import nmap
import sys
import matplotlib.pyplot as plt

scann = nmap.PortScanner()

scanner = scann.scan(sys.argv[1],'80',arguments='-O')

try:
    host_state = "The host is :" + scanner['scan'][sys.argv[1]]['status']['state']
    os_state = "percentage of system using OS %s is %s %%" %(scanner['scan'][sys.argv[1]]['osmatch'][0]['name'],scanner['scan'][sys.argv[1]]['osmatch'][0]['accuracy'])


    print(host_state);
    print(os_state);

    print("\n")
    print("Do you want to see graphical representation (Y/n) \n")
    choice = input('?>')

    if choice == 'Y' or choice == 'y':
        os_name = scanner['scan'][sys.argv[1]]['osmatch'][0]['name']
        os_percent = scanner['scan'][sys.argv[1]]['osmatch'][0]['accuracy']
        x = ['0',os_percent]
        y = ['0',os_name]
        plt.bar(x,y)
        plt.show()
    else:
        print("OK.")
except IndexError:
    print("Scan was not Successfull")
