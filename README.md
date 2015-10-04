# Bloom-Filter

This is an implementation of a bloom filter in Python. The bloom filter here is an example of a bloom filter that would be used in a browser
to check for malicious URLs. 

For more details on how bloom filters work - http://stackoverflow.com/questions/4282375/what-is-the-advantage-to-using-bloom-filters/30247022#30247022

##Data 
I have downloaded a csv file of 1million URLs from 'Alexa top 1 million sites'. I have CUT out the first 800 URLs from this file and
COPIED the next 200 URLs into another csv file called top2m.csv .This file which now contains 1000 entries is my test case and is 
what I assume a user to come enter at a browser. The original 1 million file now has 1,000,000 - 800 = 999,200 URLs.
This file is called top1m.csv and is the final list of malicious URLs (which in a real case would be stored in an offline server).

Thus we have 999,200 malicious URLs and 1000 URLs which a user comes along and enters into his browser, and we need to check if the
URL entered is malicious using a bloom filter. We know for a fact that out of the 1000 URLs he enters, 800 are actually non malicious
and 200 are malicious. We can use this fact to calculate the percentage of false positives. 

The csv files can be downloaded from here - 
https://drive.google.com/folderview?id=0B9Wfot2H0E9IemZDdklldjdBazQ&usp=sharing

##Hash Function 
For hashing, murmurhash3 in python was used. MurmurHash is a non-cryptographic hashing function which generates a 128bit hash value. Using an engineered hash function like Murmur will maximize the quality of the distribution, and minimize the number of collisions. A different seed value (value which specifies how many times the hash function should randomize and mix the data)
can be used. In the code given, 7 hash functions are used by changing the seed value from 41-47. A bit array of size 5000000 is used here.

##Code description
The first file is bloom_filter.py where a bit array of size 5000000 is created, 999200 URLs are read one by one, and each of the URLs is
passed through 7 hashing functions. The corresponding bits are set to 1 in the bit array. This bit array (which is the bloom filter)
is then stored to a file called bloom_filter.txt .Since we are writting bits, the file can only be understood using a bitreader.
This file which is our bloom filter is only 611 KB.

After creating the bloom filter, we check for malicious URLs in the 1000 URLs that the user enters. This is done in the file 
called test.py .Here the bit file is loaded, and each of the 1000 URLs are passed through the same hashing functions to check if the
corresponding bits are set or not. Whenever all 1s are found then the URL might be malicious and a server access has to be made.
The number of disk accesses are counted and printed. 

In this example, with a bit array size of 5,000,000 and with 7 hashing functions, the number of disk accesses required is 306.
Compare this to a typical hash table where every i.e. 1000 URLs would have to make a server access. We know for a fact that
the number of malicious URLs in this file is 200/1000. Thus only 106 false positives have occured.
