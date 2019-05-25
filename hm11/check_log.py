import subprocess
from collections import Counter
import re
import json


class LogAnalysis:
    def __init__(self, path_to_json, path, *args):
        self.path_to_json = path_to_json
        self.path = path
        self.files = args
        self.paths = {}
        self.dump = {}
        self.check_log()
        self.save_json()

    def find_path(self):
        for file in self.files:
            self.paths[file] = ''.join((self.path, file))

        if len(self.files) == 0:
            logs = subprocess.getoutput('ls {0}'.format(self.path))
            print(logs)
            for l in logs.split('\n'):
                self.paths[l] = ''.join((self.path, l))

    def create_struct(self):
        for f in self.files:
            self.dump[f] = {'total_request': 0, 'top_ip': [], 'long_requests': [],
                            'clent_error_requests': [], 'server_error_requests': []}

    def grep(self, param, pattern, path_to_log):
        return subprocess.getoutput('grep {0} {1} {2}'.format(param, pattern, path_to_log))

    def add_to_report(self, log_name, key, pattern, grep_out):
        ip_reg = '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\s'
        logs_str = ''
        location = re.search(pattern, grep_out).span()
        ip_str = re.findall(ip_reg, grep_out[:location[1]])
        main_str = re.findall('".*', grep_out[:location[1]])
        if len(ip_str) != 0 and len(main_str) != 0:
            logs_str += ''.join((ip_str[0], main_str[0]))
            self.dump[log_name][key].append(logs_str)

    def count_ip(self, log_name, path_to_log):
        regexx = '"[[:digit:]]{1,3}\.[[:digit:]]{1,3}\.[[:digit:]]{1,3}\.[[:digit:]]{1,3}\s-"'
        list_ip = self.grep('-oE', regexx, path_to_log).split('\n')
        items_ip = list(Counter(list_ip[:len(list_ip) - 1]).items())
        items_ip.sort(key=lambda i: i[1])
        for n in items_ip[::-1][:10]:
            ip = n[0][:len(n[0])-2]
            self.dump[log_name]['top_ip'].append(''.join(ip))

    def long_requests(self, log_name, path_to_log):
        time_reg = '"\s[[:digit:]]{1,5}\.[[:digit:]]{1,5}\s"'
        times = self.grep('-oE', time_reg, path_to_log).split('\n')
        times.sort()
        for t in times[::-1][:10]:
            str_log = self.grep('-wE', t, path_to_log)
            self.add_to_report(log_name, 'long_requests', t, str_log)

    def client_server_error(self, selection, log_name, path_to_log):
        error_reg = ''
        error_reg_py = ''
        key = ''
        if selection == "client":
            error_reg = '"\s[4]{1}[0-9]{2}\s"'
            error_reg_py = '\s[4]{1}[0-9]{2}\s'
            key = 'clent_error_requests'
        elif selection == "server":
            error_reg = '"\s[5]{1}[0-9]{2}\s"'
            error_reg_py = '\s[5]{1}[0-9]{2}\s'
            key = 'server_error_requests'

        times = self.grep('-E', error_reg, path_to_log).split('\n')
        times.sort()
        for str_log in times:
            error = re.findall(error_reg_py, str_log)
            self.add_to_report(log_name, key, error[0], str_log)

    def access_log(self, log_name):
        request = ['GET', 'POST']
        path_to_log = self.paths[log_name]
        self.count_ip(log_name, path_to_log)
        self.long_requests(log_name, path_to_log)
        self.client_server_error('client', log_name, path_to_log)
        self.client_server_error('server', log_name, path_to_log)
        for req_name in request:
            self.dump[log_name][req_name] = {'count': self.grep('-c', req_name, path_to_log)}
            self.dump[log_name]['total_request'] += int(self.dump[log_name][req_name]['count'])

    def check_log(self):
        self.find_path()
        self.create_struct()
        while len(self.paths) != 0:
            for log_name in self.dump:
                if log_name == 'access.log':
                    self.access_log(log_name)
                    self.paths.pop('access.log')
                elif log_name == 'error.log':
                    self.paths.pop('error.log')
                    print("Error.log not processed")
            self.paths.clear()
        print(self.dump)

    def save_json(self):
        with open('{0}response.json'.format(self.path_to_json), 'w', encoding='utf-8') as file:
            json.dump(self.dump, file, indent=2, ensure_ascii=False)


LogAnalysis('/home/kyklaed/PycharmProjects/otus-qa-course/hm11/log/',
            '/home/kyklaed/PycharmProjects/otus-qa-course/hm11/log/',
            'access.log',
            'error.log')



# a = LogAnalysis('/home/burdyuk/Downloads/hm11/log/', 'access.log')#, 'error.log')
# a.check_log()