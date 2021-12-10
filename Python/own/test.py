import subprocess
import threading
import socket
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:",
                            ['help', 'listem', 'execute', 'target', 'port', 'command', 'upload'])
    print(opts)
except getopt.GetoptError as err:
    print(err)

