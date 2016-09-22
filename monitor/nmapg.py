#!/usr/bin/python
# -*- coding: utf-8 -*-
#example web 
import sys
import nmap
scan_row = []
input_data = raw_input('Please input hosts and port:')
scan_row = input_data.split(" ")
if len(scan_row) != 2:
	print "Input errors,example\"192.168.1.0/24 80,443,22\""
	sys.exit(0)
hosts = scan_row[0]
port = scan_row[1]
print hosts
print port
try:
	nm = nmap.PortScanner() #创建端口扫描对象      
	print "1"
except nmap.PortScannerError:
	print('Nmap not found',sys.exc_info()[0])
	sys.exit(0)
except Exception,e:
	print("Unexpected error:",str(e))
	sys.exit(0)
try:
	print "2"
	nm.scan(hosts,port)   
except Exception,e:
	print "Scan error:" + str(e)
print nm.all_hosts()
for host in nm.all_hosts():
	print('----------------------------------------------')
	print('Host:%s (%s)'%(host,nm[host].hostname())) #输出主机及主机名
	print('State: %s'%nm[host].state())           #输出主机状态
	for proto in nm[host].all_protocols():           #少秒协议
		print('-----------')
		print ('Protocol: %s'%proto)
		Iport = nm[host][proto].keys()
		Iport.sort()
		for port in Iport:
			print ('port:%s\tsate:%s'%(port,nm[host][proto][port]['state']))
