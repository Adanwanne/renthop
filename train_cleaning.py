import pandas as pd

train = pd.DataFrame.from_csv('/Users/adaezeajoku/Desktop/STATS415/Project/train.csv')

t1 = train.ix[:,['interest_level','features']]
print t1.dtypes

# def var_dict_maker(df):
# 	dikt = {'high': {}, 'medium': {}, 'low': {}}
# 	for i in df.iterrows():
# 		varz = i[1][1].split(',')
# 		for var in varz:
# 			if var not in dikt[i[1][0]]:
# 				dikt[i[1][0]][var] = 0
# 			dikt[i[1][0]][var] += 1 
# 	return dikt

# features_dict = var_dict_maker(t1)

# print features_dict['high']