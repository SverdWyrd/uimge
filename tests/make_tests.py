#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from helpers import TEST_DIR, FIXTURES, uimge

################################
# Генератор тестов. использует exec
################################
HEAD = \
'''#!/usr/bin/python
# -*- coding: utf-8 -*-

from helpers import BaseHostCase
'''
def make_test():
    class_template = \
'''
class Test{0}(BaseHostCase):
    fixtures = {1}
'''
    methods_template = \
'''
    def test_{0}(self):
        """
        Test{2}.test_{0} http://{1}
        """
        for f in self.fixtures:
            self._run_host('{0}', f)
'''

    for_eval = []
    for_eval.append(HEAD)
    for classname, fixtures in (
                ('HostsUpload', FIXTURES),
                ):
        for_eval.append(class_template.format(classname, fixtures))
        for host, host_obj in uimge.Hosts.hosts_dict.iteritems():
            for_eval.append(methods_template.format(host, host_obj.host, classname))

    for classname, fixtures in (
                ('DevHostsUpload', FIXTURES),
                ):
        for_eval.append(class_template.format(classname, fixtures))
        for host, host_obj in uimge.Hosts.dev_hosts_dict.iteritems():
            if host != 'ex_example':
                for_eval.append(methods_template.format(host, host_obj.host, classname))

    s = ''.join(for_eval)
    return s

def save_test(string, filename):
    filepath = os.path.join(TEST_DIR, filename)
    with open(filepath, 'wb') as f:
        f.write(string)



if __name__ == "__main__":
    s = make_test()
    save_test(s, 'test_hosts.py')

__test__ = False
