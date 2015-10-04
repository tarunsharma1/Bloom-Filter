import csv
import mmh3
from bitarray import bitarray


#size =  9585059;
size =   5000000;
#size= 50;
bit_array = bitarray(size)
bit_array.setall(0)

def mapf(url): 
	b1 = mmh3.hash(url, 41) % size
	bit_array[b1]=1

	b2 = mmh3.hash(url, 42) % size
	bit_array[b2]=1

	b3 = mmh3.hash(url, 43) % size
	bit_array[b3]=1

	b4 = mmh3.hash(url, 44) % size
	bit_array[b4]=1

	b5 = mmh3.hash(url, 45) % size
	bit_array[b5]=1

	b6 = mmh3.hash(url, 46) % size
	bit_array[b6]=1

	b7 = mmh3.hash(url, 47) % size
	bit_array[b7]=1
	

#r = csv.reader(open("C:\\Users\\tarun_000\\Desktop\\top1m.csv"));
r = csv.reader(open("top1m.csv"));
for row in r:
	url=row[1]
	mapf(url);
#print line[1]


f=open("bloom_filter.txt","wb")
f.write(bit_array)
f.close()
#pickle.dump(bit_array, open("bit_array.npy", "wb" ));
print "done";


####################################### working code below #############


# url="amazon.in"


# def check(url):
# 	b1 = mmh3.hash(url, 41) % size
# 	b2 = mmh3.hash(url, 42) % size
# 	b3 = mmh3.hash(url, 43) % size
# 	b4 = mmh3.hash(url, 44) % size
# 	b5 = mmh3.hash(url, 45) % size
# 	b6 = mmh3.hash(url, 46) % size
# 	b7 = mmh3.hash(url, 47) % size
# 	if bit_array[b1]==True and bit_array[b2]==True and bit_array[b3]==True and bit_array[b4]==True and bit_array[b5]==True and bit_array[b6]==True and bit_array[b7]==True:
# 		print "maybe malicious...making disc access now to be safe";
# 	else:
# 	    print "definitely not malicious...can proceed without disc lookup";	

	


# check(url);
