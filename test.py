import csv
import mmh3
from bitarray import bitarray
import struct
#size=50;
size =  5000000;
disk_accesses=0;


ba=bitarray(size);
ba.setall(0)
f=open("bloom_filter.txt","rb")
f.readinto(ba)



def check(url):
	global disk_accesses
 	b1 = mmh3.hash(url, 41) % size
 	b2 = mmh3.hash(url, 42) % size
 	b3 = mmh3.hash(url, 43) % size
 	b4 = mmh3.hash(url, 44) % size
 	b5 = mmh3.hash(url, 45) % size
 	b6 = mmh3.hash(url, 46) % size
 	b7 = mmh3.hash(url, 47) % size
 	if ba[b1]==True and ba[b2]==True and ba[b3]==True and ba[b4]==True and ba[b5]==True and ba[b6]==True and ba[b7]==True:
 		print "maybe malicious...making disc access now to be safe...this might take some time";
 		disk_accesses=disk_accesses+1;
 	else:
 	    print "definitely not malicious...can proceed without disc lookup...no time wasted because of bloom filter";	

	


r = csv.reader(open("top2m.csv"));

for row in r:
	url=row[1]
	#print url
	check(url);
	

print disk_accesses;

