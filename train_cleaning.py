import pandas as pd

train = pd.DataFrame.from_csv('/Users/adaezeajoku/Desktop/STATS415/Project/train.csv')

t1 = train.ix[:,['interest_level','features']]

def var_dict_maker(df):
	dikt = {'high': {}, 'medium': {}, 'low': {}}
	for i in df.iterrows():
		try:
			varz = i[1][1].split(', ')
			for var in varz:
				if var not in dikt[i[1][0]]:
					dikt[i[1][0]][var] = 0
				dikt[i[1][0]][var] += 1 
		except:
			if 'NA' not in dikt[i[1][0]]:
				dikt[i[1][0]]['NA'] = 0
			dikt[i[1][0]]['NA'] += 1
	return dikt

features_dict = var_dict_maker(t1)
 
high_features = pd.DataFrame.from_records([(k,v) for (k,v) in features_dict['high'].items()], columns=['Feature', 'Frequency'])

medium_features = pd.DataFrame.from_records([(k,v) for (k,v) in features_dict['medium'].items()], columns=['Feature', 'Frequency'])

low_features = pd.DataFrame.from_records([(k,v) for (k,v) in features_dict['low'].items()], columns=['Feature', 'Frequency'])

high_features.to_csv('/Users/adaezeajoku/Desktop/STATS415/Project/high_features.csv', index=False)
medium_features.to_csv('/Users/adaezeajoku/Desktop/STATS415/Project/medium_features.csv', index=False)
low_features.to_csv('/Users/adaezeajoku/Desktop/STATS415/Project/low_features.csv', index=False)

