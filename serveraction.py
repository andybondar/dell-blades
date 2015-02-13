#!/usr/bin/python

####
# Script concieved to manage Dell R620/630 rack servers,
# but it could be easily adapted for any other similar cases.

# To do:
# 1. Implemet reading IPs and maybe creds from yaml config file
# 2. Implement 'pexpect' module
# find example here -
# http://linux.byexamples.com/archives/346/python-how-to-access-ssh-with-pexpect/
#
#####

# Global vars

mask='192.168.220.'
#command = 'racadm serveraction '

# Functions

def convert_actions(c):
    return {
'stop': 'powerdown',
'start': 'powerup',
'reset': 'hardreset',
'status': 'powerstatus',
    }.get(c, 'none')



def single_node(a,n):
    print "Single node.\n"
    from subprocess import call
    url = 'root@' + mask + n
    cmd = call(["ssh", url, "racadm", "serveraction", a])
    return

def all_nodes(a):
    print "All nodes.\n"
    from subprocess import call
    for i in range(6):
url = 'root@' + mask + `i+1`
cmd = call(["ssh", url, "racadm", "serveraction", a])
    return


################################


import sys

action = convert_actions(sys.argv[1])

if sys.argv[2] == 'all':
all_nodes(action)
else:
single_node(action,sys.argv[2])
