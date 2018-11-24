import logging

FORMAT='%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)
logger=logging.getLogger('')
s1=logger.warning('My message')
FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
d = {'clientip': '192.168.43.52', 'user': 'fbloggs'}
logger = logging.getLogger('tcpserver')
s2=logger.warning('Protocol problem: %s', 'connection reset', extra=d)
my_file = open('/home/quynh/mynewfile.txt','w')
my_file.write(str('Protocol problem: %s', 'connection reset', extra=d))
my_file.write(str(s2))
my_file.close()
