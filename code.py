# --------------
import json
from collections import Counter
with open(path) as f:
    data = json.load(f)

#print(data) 
 
# Code starts here

#  Can you find how many deliveries were faced by batsman  `SC Ganguly`.
count_deliveries = 0
for deliv in data['innings'][0]['1st innings']['deliveries']:
    for delivery_num,delivery_info in deliv.items():
        if (delivery_info['batsman'] == 'SC Ganguly'):
            count_deliveries += 1
            
            
print("The number of deliveries faced by SC Ganguly is: ", count_deliveries)

#  Who was man of the match and how many runs did he scored ?
man_of_match = data['info']['player_of_match']

runs_scored = 0
for deliv in data['innings'][0]['1st innings']['deliveries']:
    for delivery_num,delivery_info in deliv.items():
        if(delivery_info['batsman'] == man_of_match[0]):
            runs_scored += delivery_info['runs']['batsman']            

print("The runs scored by Man of Match", runs_scored)


#print(data['info']['player_of_match'])

#  Which batsman played in the first inning?
batsman_list = []
for deliv in data['innings'][0]['1st innings']['deliveries']:
    for delivery_num,delivery_info in deliv.items():
        bats_name = delivery_info['batsman']
        if bats_name not in batsman_list:
            batsman_list.append(bats_name)
print("The batsman playing in the 1st innings are:",batsman_list)

# Which batsman had the most no. of sixes in first inning ?
most_sixes_batsman = []
for deliv in data['innings'][0]['1st innings']['deliveries']:
    for delivery_num,delivery_info in deliv.items():
        if(delivery_info['runs']['batsman'] == 6):
            most_sixes_batsman.append(delivery_info['batsman'])
            
batsman_sixes = Counter(most_sixes_batsman)
print(batsman_sixes)

# Find the names of all players that got bowled out in the second innings.
list_out = []
for deliv in data['innings'][1]['2nd innings']['deliveries']:
    for delivery_num,delivery_info in deliv.items():
        if 'wicket' in delivery_info and delivery_info['wicket']['kind'] == 'bowled':
            list_out.append(delivery_info['wicket']['player_out'])
print(list_out)

# How many more "extras" (wides, legbyes, etc) were bowled in the second innings as compared to the first inning?
#print(len(data['innings'][0]['1st innings']['deliveries']))
#print(len(data['innings'][1]['2nd innings']['deliveries']))
extra_2nd_inning = []
for deliv in data['innings'][1]['2nd innings']['deliveries']:
    for delivery_num,delivery_info in deliv.items():
        if 'extras' in delivery_info:
            extra_2nd_inning.append(delivery_info['extras'])
print(len(extra_2nd_inning))

extra_1st_inning = []
for deliv in data['innings'][0]['1st innings']['deliveries']:
    for delivery_num,delivery_info in deliv.items():
        if 'extras' in delivery_info:
            extra_1st_inning.append(delivery_info['extras'])
print(len(extra_1st_inning))

extras_count = len(extra_2nd_inning) - len(extra_1st_inning)
print("Number of extras more in 2nd innings is",extras_count)

# Code ends here


