Dev-environment installation
============================

Windows
-------

Linux
-----

MacOS X
-------

You need to install following applications:

* Python 3.8 - use `homebrew <https://brew.sh/>`_, it is a better way of installing / managing apps!
* git - you can install from `Github Desktop <https://desktop.github.com/>`_, which has an option to install command line tools.
* Qt Designer - you may find it on `fman <https://build-system.fman.io/qt-designer-download>`_.
* PyCharm - edition community (even if pro has django support...) from `Jet Brains <https://www.jetbrains.com/fr-fr/pycharm/download/#section=mac>`_.

Setting your dev-env
--------------------

Whatever the platform you are running on, best way to manage python developpement applications is by
using virtual environments. Below steps explain how to setup this environment for this apps, by using
PyCharm and Git.

* Start a new empty project in PyCharm.
* From VCS menu in Pycharm, click on *Get from Version Control*, then :

 * Repository URL = https://github.com/navugo/BaWaSter.git
 * Directory = ./src

* Install requirements, from PyCharm Terminal, execute :

 * cd src
 * pip install -r requirements.txt

Ready to code!