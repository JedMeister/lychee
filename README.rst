Lychee - Self-hosted photo-management done right
================================================

`Lychee`_ is a free web-based photo-management tool. Upload, manage
and share photos like from a native application. Lychee comes with 
everything you need and all your photos are stored securely.

Lychee includes all the standard features in `TurnKey Core`_, and on
top of that:

- Lychee configuration:

   - Install (from upstream source) to /var/www/lychee

     **Security note**: Updates to Lychee may require supervision so
     they **ARE NOT** configured to install automatically. See below for
     updating Lychee.

- SSL support out of the box.
- `Adminer`_ administration frontend for MySQL (listening on port
  12322 - uses SSL).
- Postfix MTA (bound to localhost) to allow sending of email (e.g.,
  password recovery).
- Webmin modules for configuring Apache2, PHP, MySQL and Postfix.

Supervised Manual Lychee Update
-------------------------------

Update Lychee from the command line::

    cd /var/www/lychee
    git pull

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH, MySQL, Adminer: username **root**
-  Lychee: username **admin**

.. _Lychee: http://lychee.electerious.com/
.. _TurnKey Core: https://www.turnkeylinux.org/core

