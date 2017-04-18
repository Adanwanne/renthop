import json
import pandas as pd


''' Generating csv of training set '''
train = []
with open('train.json', 'r') as t:
	t1 = json.load(t)

k = t1.keys()
# ids = t1[k[0]].keys()
for key in k:
	train.append([v for v in t1[key].values()])

traine = []
for i in range(15):
	traine.append([])

for idx, i in enumerate(train):
	for entry in i:
		if type(entry) == unicode:
			traine[idx].append(''.join(entry).splitlines())
		else:
			traine[idx].append(entry)

combo = zip(traine[0], traine[1], traine[2], traine[3], traine[4], traine[5], traine[6], traine[7], traine[8], traine[9], traine[10], traine[11], traine[12], traine[13], traine[14])

# col = ['key'] + k
train_df = pd.DataFrame.from_records(combo, columns=k)
# train_df.to_csv('renthop_tr.csv', index=False, encoding='utf-8')


''' Generating csv of test set '''
test = []
with open('test.json', 'r') as t:
	t2 = json.load(t)

k2 = t2.keys()
# # ids2 = t2[k2[0]].keys()
for key in k2:
	test.append([v for v in t2[key].values()])

teste = []
for i in range(14):
	teste.append([])

for idx, i in enumerate(test):
	for entry in i:
		if type(entry) == unicode:
			teste[idx].append(''.join(entry).splitlines())
		else:
			teste[idx].append(entry)

combo2 = zip(teste[0], teste[1], teste[2], teste[3], teste[4], teste[5], teste[6], teste[7], teste[8], teste[9], teste[10], teste[11], teste[12], teste[13])

# # col = ['key'] + k2
test_df = pd.DataFrame.from_records(combo2, columns=k2)
test_df.to_csv('renthop_te.csv', index=False, encoding='utf-8')

