Releasing a New Version
=======================

```bash
make check test
emacs attd.py setup.py
emacs NEWS.md
sudo make install clean
make test-installed
tools/release
make push clean
sudo pip3 uninstall attd
sudo pip3 install attd
make test-installed
```
