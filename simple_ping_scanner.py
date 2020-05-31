import socket
import platform
import subprocess

# Breandan Heiliger
# CYB333 Security Automation

# Simple Ping Scanner
# 1. Get host ip address
# 2. Use built in ping program to ping all ipv4 addresses on network
# 3. Display results

class PingScanner():
    def __init__(self):
        # Initalize variables
        self.ping_count = 1
        self.alive_hosts = []
        self.option = '-n' if platform.system().lower()=='windows' else '-c'
        self.proceed = False

        print("Welcome to SimplePingScanner!")

        # Get and display host ipv4 address
        self.host_ip = self.get_host_ip()
        print("The host IPv4 address is: " + self.host_ip)
        print()

        if self.proceed:
            # Begin scan
            print("Begging scan.")
            self.ping_scan(self.alive_hosts)

            print("Here is the list of alive hosts:")
            print(self.alive_hosts)
        else:
            print("Scan stopped.")

    def get_host_ip(self):
        try:
            host_name = socket.gethostname()
            host_ip = socket.gethostbyname(host_name)
            self.proceed = True
            return host_ip
        except:
            print("Unable to get host name.")

    def ping_scan(self, alive_hosts):

        begin_ip = ".".join(str(self.host_ip).split('.')[0:3])

        for i in range(20):
            ip = begin_ip + "." + str(i)

            # If ping comes back true, then add to alive hosts.
            if self.ping(ip) == 0:
                alive_hosts.append(ip)
                print ("\n" + ip + " Is ALIVE!")
                

    def ping(self, host):

        command = ['ping', str(self.option), str(self.ping_count), str(host)]

        return subprocess.call(command)


def main():

    PingScanner()

        
if __name__ == '__main__':
    main()
