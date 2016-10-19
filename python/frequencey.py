import csv
import sys
import re
import operator
from prettytable import PrettyTable

marks = (";",",","-","\.","\/")
trimwords = ("with","and","the","by","of","or","at","it","you","but","for","on","a","to","be","is","are","")

re.compile("|".join(marks))
fullset = set()
fulllist = []
result=[]

with open(sys.argv[1]) as csvfile:
	answers = csv.reader(csvfile, delimiter=',')
	for row in answers:
		w=re.compile("|".join(marks)).sub("",row[2].lower()).split(' ')
		fulllist.extend(w)
		fullset = set(fullset) | set(w)

fullset = set(fullset) - set(trimwords)


for word in list(set(fullset)):
	answer=[word, fulllist.count(word)]
	result.append(answer)

results=sorted(result,key=operator.itemgetter(1,0))

print("========================= Word Frequency Report =============================")

t=PrettyTable(["Key Word", "Frequency"])
t.padding_width=1
for row in reversed(results):
	t.add_row(row)

print(t)


		