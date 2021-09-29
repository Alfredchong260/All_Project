import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print('Invalid amount of arguments.')
    print('Syntax: python3 scanner.py <ip>')
    sys.exit()

# Add a pretty banner
print('-' * 50)
print('Scanning target ' + target)
print(f'Time started {str(datetime.now())}')
print('-' * 50)

try:
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except:
    pass
