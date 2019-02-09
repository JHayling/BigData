import unicodedata
# u2a converts Unicode to ASCII
def u2a(u): return str(unicodedata.normalize('NFKD',u).encode('ascii','ignore'))

# strip removes any non-alpha characters
def strip(s): return ''.join(filter(str.isalpha, s))

import findspark
findspark.init()

import pyspark
sc = pyspark.SparkContext.getOrCreate()
books = sc.textFile("file:///home/big/wordcount/*.txt")

split = books.flatMap(lambda line: line.split())
asc = split.map(u2a)
stripped = asc.map(strip)
notempty = stripped.filter(lambda w: len(w)>0)

#now map the words to lower case

#next convert the words into (k,v) pairs, where the key is the word, and the value is the.count so far

#next reduce by key, adding up the counts as you go

#make sure your final variable is called wordcount, so this next line will print it out

for k,v in sort.collect():
    print k,v
