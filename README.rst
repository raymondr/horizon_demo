====================================
Horizon Customization Demo Dashboard
====================================

This Django project demonstrates how the `Horizon`_ app can be used to
construct customized dashboards (for OpenStack or anything else).

The ``horizon`` module is pulled down from GitHub during setup
(see setup instructions below) and added to the virtual environment.

.. _Horizon: http://github.com/openstack/horizon

Setup Instructions
==================

The following should get you started::

    $ git clone https://github.com/gabrielhurley/demo_dashboard.git
    $ cd demo_dashboard
    $ python tools/install_venv.py
    $ cp local/local_settings.py.example local/local_settings.py

Edit the ``local_settings.py`` file as needed.

When you're ready to run the development server::

    $ ./run_tests.sh --runserver
