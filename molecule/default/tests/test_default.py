import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_executables_folder(host):
    tomcat = host.file('/opt/tomcat')
    assert tomcat.exists
    assert tomcat.is_symlink


def test_service(host):
    tomcat = host.service('tomcat')
    assert tomcat.is_running


def test_curl_output(host):
    assert host.check_output('curl localhost:8080').find(u'Tomcat') > -1
