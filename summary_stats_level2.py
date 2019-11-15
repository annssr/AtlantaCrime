import csv
import pandas as pd
import time
startTime = time.time()

# Read the data
df = pd.read_csv("data/COBRA-2019.csv")
keep_col = ['Occur Date', 'Occur Time', 'UCR Literal', 'Neighborhood', 'Longitude', 'Latitude']

new_f = df[keep_col]
new_f.rename(columns = {'Occur Date':'OccurDate','Occur Time':'OccurTime'},inplace = True)

new_f = new_f.drop(columns = ['OccurTime'])

# new_f[['Neighborhood']] = new_f[['Neighborhood']].fillna(value='Null')

# def occurence_time(row):
# 	if row['OccurTime'] < 800:
# 		return "Morning"
# 	elif row['OccurTime'] < 1600:
# 		return "Day"
# 	else:
# 		return "Evening"

# def print_month(row):
#     cur_date = row['OccurDate']
#     year, month, day = (int(x) for x in cur_date.split('-'))    
#     month = int(month)
#     return month

# def day_of_week(row):
#     cur_date = row['OccurDate']
#     year, month, day = (int(x) for x in cur_date.split('-'))    
#     dt = datetime.date(year, month, day)
#     return(dt.weekday())

def year(row):
    cur_date = row['OccurDate']
    month, day, year = (int(x) for x in cur_date.split('/'))    
    year = int(year)
    return year

new_f['Year'] = new_f.apply(lambda row: year(row), axis=1)
# new_f['Day of Week'] = new_f.apply(lambda row: day_of_week (row), axis=1)
# new_f['Month'] = new_f.apply(lambda row: print_month (row), axis=1)
# new_f['Shift Occurence'] = new_f.apply (lambda row: occurence_time (row),axis=1)
new_f = new_f[ (new_f['Longitude'] >= -84.5) & (new_f['Longitude'] <= -84.2)]
new_f = new_f[ (new_f['Latitude'] >= 33.61) & (new_f['Latitude'] <= 33.92)]
new_f = new_f.drop(columns = ['Longitude','Latitude'])

new_f = new_f[ (new_f['Year'] == 19)]# & (new_f['Year'] <= 18)]


new_f = new_f.dropna(axis=0, subset=['Neighborhood','Neighborhood'])
#new_f.sort_values(by='OccurDate',inplace=True)
#print(new_f['OccurDate'])

d_list = new_f.OccurDate.unique()
n_list = new_f.Neighborhood.unique()
#print(d_list)

# shifts = ('Morning', 'Day', 'Evening')
# days = (0,1,2,3,4,5,6)
# months = (1,2,3,4,5,6,7,8,9,10,11,12)

#category = dict((day, shift) for item in day)
#stuff = dict((months, category) for month in months)
#data_dict = dict((key, stuff) for key in n_list)
def count_occurrences(local,date):
	cat1 = len(new_f[(new_f['Neighborhood']==local) & (new_f['OccurDate']==date) & (new_f['UCR Literal'].isin(['HOMICIDE','MANSLAUGHTER']))])
	cat2 = len(new_f[(new_f['Neighborhood']==local) & (new_f['OccurDate']==date) & (new_f['UCR Literal'].isin(['AGG ASSAULT','ROBBERY-PEDESTRIAN','ROBBERY-COMMERCIAL','ROBBERY-RESIDENCE']))])
	cat3 = len(new_f[(new_f['Neighborhood']==local) & (new_f['OccurDate']==date) & (new_f['UCR Literal'].isin(['BURGLARY-RESIDENCE','BURGLARY-NONRES','AUTO THEFT']))])
	cat4 = len(new_f[(new_f['Neighborhood']==local) & (new_f['OccurDate']==date) & (new_f['UCR Literal'].isin(['LARCENY-FROM VEHICLE','LARCENY-NON VEHICLE']))])
	count = (cat1, cat2, cat3, cat4)
	return count

our_dict = {}
#print(len(n_list))
counter = 0
for local in n_list:
	counter+=1
	print('Neighborhood #',counter,': ',local)
	#print(our_dict)
	our_dict[local] = {}
	for date in d_list:
		our_dict[local][date] = count_occurrences(local,date)
		#print(date)

# for local in n_list:
# 	our_dict[local] = {}

# 	for month in months:
# 		our_dict[local][month] = {}
# 		for day in days:
# 			our_dict[local][month][day] = {}
# 			for shift in shifts:
# 				our_dict[local][month][day][shift] = count_occurrences(local, month, day, shift)
# 				print(our_dict[local][month][day][shift])

# new_f.to_csv("cobra-summary.csv", index=False)

endTime = time.time()
duration = endTime-startTime
print(our_dict)
print('# Seconds: ',duration)
print('# Minutes: ',duration/60)
# csv_file = "stats.csv"
# try:
#     with open(csv_file, 'w') as csvfile:
#         writer = csv.DictWriter(csvfile)
#         writer.writeheader()
#         for data in our_dict:
#             writer.writerow(data)
#     print(datetime.datetime.now() - startTime)
# except IOError:
#     print("I/O error") 