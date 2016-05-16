#!/usr/bin/python
"""Set Lychee admin password

Option:
    --pass=     unless provided, will ask interactively

"""

import sys
import getopt
import bcrypt

from dialog_wrapper import Dialog
from mysqlconf import MySQL

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'email='])
    except getopt.GetoptError, e:
        usage(e)

    password = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val

    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "Lychee Password",
            "Enter new password for the Lychee 'admin' account.")

    salt = bcrypt.gensalt()
    hashpass = bcrypt.hashpw(password, salt)

    m = MySQL()
    m.execute('UPDATE lychee.lychee_settings SET `value`=\"%s\" WHERE `key`="password";' % hashpass)

if __name__ == "__main__":
    main()

