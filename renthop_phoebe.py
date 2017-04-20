import json
import pandas as pd
import re

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


train_copy = train_df.copy()

# Process description & create bigrams
description = []

for index, row in train_copy['description'].iteritems():
    local = []
    if len(row) != 0:
        for val in row:
            val = re.sub(r'\<[^\>]*\>', '', val)
            #print "step1", val
            val = re.sub(r'<a  website_redacted ', '', val)
            #print "step2", val
            val = re.sub(r'[^a-zA-Z0-9\s\'\-]', '', val) # [] meaning or
            #print "step3", val
            val = val.lower()
            #print "step4", val
            local.append(val)
        
        local = ' '.join(local)
        #print "local", local 
        description.append(local.decode('ascii','ignore').encode('ascii'))
        #print "description", description
    else:
        description.append('')

train_copy['description'] = description


# Process feature
feature = []
for index, row in train_copy['features'].iteritems():
    local = []
    if len(row) != 0:
        #print index
        for val in row:
            val = re.sub(r'[^a-zA-Z0-9\s\'\-]', '', val) # [] meaning "or"
            val = val.lower()
            local.append(val)
        
        local = ' '.join(local)
        #print "local", local 
        feature.append(local.decode('ascii','ignore').encode('ascii'))
        #print "feature", feature
    else:
        feature.append('')

train_copy['features'] = feature


# Process Photos
photo_count = []
photo_binary = []
for index, row in train_copy['photos'].iteritems():
    count = len(row)
    #print "count", count 
    photo_count.append(count)
    if count > 0: 
        binary = "Yes"
    else:
        binary = "No"
    print binary
    photo_binary.append(binary)

train_copy['photo_count'] = photo_count
train_copy['photo_binary'] = photo_binary

# Process the date:
date_list = []
for index, row in train_copy['created'].iteritems():
    date = ''.join(row)
    date_list.append(date)
train_copy['created'] = date_list
train_copy['created'] = pd.to_datetime(train_copy['created'])
train_copy['month'] = train_copy['created'].dt.month

# Display Address 
address = []
for index, row in train_copy['display_address'].iteritems():
    local = []
    if len(row) != 0:
        #print index
        for val in row:
            val = re.sub(r'[^a-zA-Z0-9\s\'\-]', '', val) # [] meaning "or"
            val = val.lower()
            local.append(val)
        
        local = ' '.join(local)
        #print "local", local 
        address.append(local.decode('ascii','ignore').encode('ascii'))
        #print "feature", feature
    else:
        address.append('')

train_copy['new_display_address'] = address

manager = []
for index, row in train_copy['manager_id'].iteritems():
    local = []
    if len(row) != 0:
        #print index
        for val in row:
            val = re.sub(r'[^a-zA-Z0-9\s\'\-]', '', val) # [] meaning "or"
            val = val.lower()
            local.append(val)
        
        local = ' '.join(local)
        #print "local", local 
        manager.append(local.decode('ascii','ignore').encode('ascii'))
        #print "feature", feature
    else:
        manager.append('')

train_copy['new_manager_id'] = manager

# building_id
building = []
for index, row in train_copy['building_id'].iteritems():
    local = []
    if len(row) != 0:
        #print index
        for val in row:
            val = re.sub(r'[^a-zA-Z0-9\s\'\-]', '', val) # [] meaning "or"
            val = val.lower()
            local.append(val)
        
        local = ' '.join(local)
        #print "local", local 
        building.append(local.decode('ascii','ignore').encode('ascii'))
        #print "feature", feature
    else:
        building.append('')

train_copy['new_building_id'] = building

# interest_level
interest = []
for index, row in train_copy['building_id'].iteritems():
    local = []
    if len(row) != 0:
        #print index
        for val in row:
            local.append(val)
        
        local = ' '.join(local)
        #print "local", local 
        interest.append(local.decode('ascii','ignore').encode('ascii'))
        #print "feature", feature
    else:
        interest.append('')

train_copy['new_interest_level'] = interest


# def process_list (string):
#     temp = []
#     for index, row in train_copy[string].iteritems():
#         #print "original", row
#         manager_id = ' '.join(row)
#         #print manager_id
#         temp.append(manager_id.decode('ascii','ignore').encode('ascii'))
#     train_copy[string] = temp

# process_list('manager_id')
# process_list('building_id')
# process_list('interest_level')

# Change building_id to Integer-Levels
labels, levels = pd.factorize(train_copy['new_building_id'])
#print labels
train_copy['building_id'] = labels

# Change building_id to Integer-Levels
labels2, levels2 = pd.factorize(train_copy['new_manager_id'])
#print labels
train_copy['manager_id'] = labels2

train_copy.to_csv('renthop_tr.csv', index=False)



