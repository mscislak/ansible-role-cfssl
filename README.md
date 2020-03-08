# ansible-role-cfssl
[![Build Status](https://travis-ci.org/mscislak/ansible-role-cfssl.svg?branch=master)](https://travis-ci.org/mscislak/ansible-role-cfssl)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

This role installs CFSSL (Cloudflare's PKI and TLS toolkit) which includes the following binaries:
- cfssl
- cfssljson
- cfssl-bundle
- cfssl-certinfo
- cfssl-newkey
- cfssl-scan
- mkbundle
- multirootca

## Requirements

None.

## Role Variables

Please see [defaults/main.yml](defaults/main.yml).

## Dependencies

Does not depend on any other roles.

## Example Playbook

```
- hosts: all
  roles:
    - mscislak.cfssl
```

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/mscislak/ansible-role-cfssl/tags). 

# Author

Maros Scislak

## License

This project is licensed under the BSD 3-Clause License - see the [LICENSE](LICENSE) file for details.