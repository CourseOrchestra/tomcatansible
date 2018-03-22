import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_executable_file(host):
    tomcat = host.file('/opt/tomcat/bin')
    assert tomcat.exists
