#!.env/bin/python

####
# Script concieved to manage Dell R620/630 rack servers,
# but it could be easily adapted for any other similar cases.

# To do:
# 1. Implemet reading IPs and maybe creds from yaml config file
# 2. Implement 'pexpect' module (Done)
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
 ip = mask + n
 ssh_cmd(ip,'root','root',a)
 return

def all_nodes(a):
 print "All nodes.\n"
 for i in range(5):
  ip = mask + `i+1`
  ssh_cmd(ip,'root','root',a)
 return

###
def ssh_cmd(ip,usr,pw,command):
 print "Blade ",ip,",",command,"\n" 
 cmd = 'ssh ' + usr + '@' + ip + ' racadm serveraction ' + command
 import pexpect
 ssh_newkey = 'Are you sure you want to continue connecting'
 # my ssh command line
 p=pexpect.spawn(cmd)
 i=p.expect([ssh_newkey,'password:',pexpect.EOF])
 if i==0:
  print "I say yes"
  p.sendline('yes')
  i=p.expect([ssh_newkey,'password:',pexpect.EOF])
 if i==1:
  print "I give password",
  p.sendline(pw)
  p.expect(pexpect.EOF)
 elif i==2:
  print "I either got key or connection timeout"
  pass
 print p.before # print out the result
 return

################################

import sys

action = convert_actions(sys.argv[1])

if sys.argv[2] == 'all':
 all_nodes(action)
else:
 single_node(action,sys.argv[2])
