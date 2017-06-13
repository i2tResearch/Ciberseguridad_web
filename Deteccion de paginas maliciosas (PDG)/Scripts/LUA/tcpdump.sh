#!/bin/bash 
#start a process in the background (it happens to be a TCP HTTP sniffer on the loopback interface, for my apache server): 
tcpdump -U -i lo -w dump.pcap 'port 80' &
sleep 5 
#.....other commands that send packets to tcpdump.....
#now interrupt the process. get its PID:
pid=$(ps -e | pgrep tcpdump)
echo $pid 
#interrupt it:
sleep 5
kill -2 $pid