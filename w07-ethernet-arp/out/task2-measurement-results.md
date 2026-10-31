# Task 2 measurement results

## ARP BEFORE

```text

Interface: 192.168.30.1 --- 0x7
  Internet Address      Physical Address      Type
  192.168.30.255        ff-ff-ff-ff-ff-ff     static    
  224.0.0.22            01-00-5e-00-00-16     static    
  224.0.0.251           01-00-5e-00-00-fb     static    
  224.0.0.252           01-00-5e-00-00-fc     static    

Interface: 192.168.219.178 --- 0xd
  Internet Address      Physical Address      Type
  192.168.219.1         80-ca-4b-1c-3a-2d     dynamic   
  192.168.219.189       4c-5f-70-05-a4-1f     dynamic   
  192.168.219.255       ff-ff-ff-ff-ff-ff     static    
  224.0.0.22            01-00-5e-00-00-16     static    
  224.0.0.251           01-00-5e-00-00-fb     static    
  224.0.0.252           01-00-5e-00-00-fc     static    
  239.255.255.250       01-00-5e-7f-ff-fa     static    
  255.255.255.255       ff-ff-ff-ff-ff-ff     static    

Interface: 192.168.15.1 --- 0x14
  Internet Address      Physical Address      Type
  224.0.0.22            01-00-5e-00-00-16     static    
  224.0.0.251           01-00-5e-00-00-fb     static    
  224.0.0.252           01-00-5e-00-00-fc     static    

```

## ARP IMMEDIATELY AFTER CLEAR

```text

Interface: 192.168.30.1 --- 0x7
  Internet Address      Physical Address      Type
  224.0.0.22            01-00-5e-00-00-16     static    

Interface: 192.168.219.178 --- 0xd
  Internet Address      Physical Address      Type
  192.168.219.1         80-ca-4b-1c-3a-2d     dynamic   
  224.0.0.22            01-00-5e-00-00-16     static    
  239.255.255.250       01-00-5e-7f-ff-fa     static    

Interface: 192.168.15.1 --- 0x14
  Internet Address      Physical Address      Type
  224.0.0.22            01-00-5e-00-00-16     static    

```

## GATEWAY PING

```text

Pinging 192.168.219.1 with 32 bytes of data:
Reply from 192.168.219.1: bytes=32 time=6ms TTL=64
Reply from 192.168.219.1: bytes=32 time=4ms TTL=64
Reply from 192.168.219.1: bytes=32 time=4ms TTL=64

Ping statistics for 192.168.219.1:
    Packets: Sent = 3, Received = 3, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 4ms, Maximum = 6ms, Average = 4ms

```

## WEB ACCESS

```text
HTTP status: 200
Remote IP: 163.152.6.10

```

## ARP AFTER

```text

Interface: 192.168.30.1 --- 0x7
  Internet Address      Physical Address      Type
  224.0.0.22            01-00-5e-00-00-16     static    

Interface: 192.168.219.178 --- 0xd
  Internet Address      Physical Address      Type
  192.168.219.1         80-ca-4b-1c-3a-2d     dynamic   
  224.0.0.22            01-00-5e-00-00-16     static    
  239.255.255.250       01-00-5e-7f-ff-fa     static    

Interface: 192.168.15.1 --- 0x14
  Internet Address      Physical Address      Type
  224.0.0.22            01-00-5e-00-00-16     static    

```

## WI-FI DYNAMIC ENTRY COUNTS

```text
before=2, after=1
```

## MY ARP REQUEST/REPLY (seconds,srcMAC,dstMAC,opcode,srcIP,dstIP)

```text
1.051444900,8c:17:59:ac:3b:cc,ff:ff:ff:ff:ff:ff,1,192.168.219.178,192.168.219.1
1.054668700,80:ca:4b:1c:3a:2d,8c:17:59:ac:3b:cc,2,192.168.219.1,192.168.219.178
34.736453400,80:ca:4b:1c:3a:2d,8c:17:59:ac:3b:cc,1,192.168.219.1,192.168.219.178
34.736488200,8c:17:59:ac:3b:cc,80:ca:4b:1c:3a:2d,2,192.168.219.178,192.168.219.1
```

## ARP COUNT

```text
139 ARP packets in the configured 60-second capture.
Example estimate for 1000 machines: 139 x 1000 = 139000 packets/min.
This is a rough arithmetic estimate; shared broadcasts and traffic differences prevent linear prediction.
```
