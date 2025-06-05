import re
import pandas as pd
from datetime import datetime

def load_and_parse_log(filename):
    log_pattern = re.compile(
        r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<datetime>[^\]]+)\] "(?P<method>\w+) (?P<url>[^ ]+) [^"]+" (?P<status>\d+) "(?P<user_agent>[^"]*)"'
    )
    data = []
    with open(filename, 'r') as file:
        for line in file:
            match = log_pattern.match(line)
            if match:
                d = match.groupdict()
                d['datetime'] = datetime.strptime(d['datetime'], "%d/%b/%Y:%H:%M:%S %z")
                d['status'] = int(d['status'])
                data.append(d)
    return pd.DataFrame(data)
