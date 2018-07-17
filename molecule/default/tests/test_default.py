import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_mercurial_is_installed(host):
    mercurial = host.package('mercurial')

    assert mercurial.is_installed
