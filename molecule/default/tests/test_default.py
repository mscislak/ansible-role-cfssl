import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_cfssl_binaries(host):
    binaries = [
        "cfssl",
        "cfssljson",
        "cfssl-bundle",
        "cfssl-certinfo",
        "cfssl-newkey",
        "cfssl-scan",
        "mkbundle",
        "multirootca"
    ]

    for binary in binaries:
        binary_file = host.file('/usr/local/bin/' + binary)
        assert binary_file.exists
        assert binary_file.user == 'root'
        assert binary_file.group == 'root'
        assert binary_file.mode == 0o755
