"""
Docker stats python reader
"""
import sys
import os
from subprocess import call
from datetime import datetime
import string
import re
import requests

__version__ = "0.1.0"


tabulation_splitter = re.compile(r'\s{2,}')
FILENAME = 'docker_stats.csv' if len(sys.argv) < 2 else sys.argv[1]
URL =''

if os.path.exists(FILENAME):
    os.remove(FILENAME)

def start_parser():
    while True:
        started = False
        for line in sys.stdin:
            line = tabulation_splitter.sub('\t', line.strip())
            
            
            if line[0] in string.printable:
                values = line.split('\t')
                timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
                values.append(timestamp)
                splitted_values = []
                
                for val in values:
                    if '/' in val:
                        val1, val2 = val.split('/')
                        splitted_values.extend([val1, val2])
                        
                    else:
                        splitted_values.append(val)
                
                values = splitted_values
                
                print('\t'.join(values))
                with open('docker_stats.csv', 'a') as f:
                    f.write(','.join(values) + '\n')
                    
                # To send data anywhere you could use this example
                # columns = dict(zip(headers, values))
                # requests.post(URL, data=columns)
                
            elif not started:
                started = True
                
                header_line = line[7:]
                headers = header_line.split('\t') + ['timestamp']
                new_headers = []
                
                for val in headers:
                    if '/' in val:
                        val_pair = val.split('/')
                        main_val = val.split(' ')[0]
                        
                        val1, val2 = val_pair[0], main_val + ' ' + val_pair[1]
                        new_headers.extend([val1, val2])
                        
                    else:
                        new_headers.append(val)
                        
                    headers = new_headers
                        
                        
                print('\t'.join([f'{val :20}' for val in headers]))
                
                with open('docker_stats.csv', 'a') as f:
                    f.write(','.join(headers) + '\n')
            
            else:
                call('clear' if os.name == 'posix' else 'cls')
                print('\t'.join(headers))
                    
def main():
    print("Executing package version %s." % __version__)
    print("List of argument strings: %s" % sys.argv[1:])
    start_parser()


if __name__ == '__main__':
    main()
                    