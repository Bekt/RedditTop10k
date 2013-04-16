import datetime

r = open('created.data')
w = open('seconds.data', 'w')

for line in r:
	line = line.strip()
	if len(line) > 0:
		date = datetime.datetime.utcfromtimestamp(int(float(line)))
		sec = date.hour * 60 * 60 + date.minute * 60 + date.second
		w.write(str(sec) + '\n')

r.close()
w.close()

