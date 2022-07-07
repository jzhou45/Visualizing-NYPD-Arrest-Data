import csv
import json
import urllib.request

# Your unique_values function should use the accumulator pattern to return a new list containing exactly 1 copy of the value associated with k in lst's dictionaries.

# For example, the function call:
# unique_values('arrest_boro', data) would be expected to evaluate to a list. The list should have the same entries as the following one, but the entries do not need to appear in this order:
# [ 'Q', 'M', 'K', 'B' ]

def unique_values(k, lst): # k is a string; lst is a list of dictionaries.
  hash = {}
  for char in values(k, lst):
    if char not in hash:
      hash[char] = 0
    else:
      hash[char] += 1
  return list(hash.keys())

def values(k, lst):
  list = []
  for hash in lst:
    for ele in hash:
      if ele == k:
        list.append(hash.get(ele))
  return list

# Each dictionary in lst which includes k:v as a key-value pairing should be added to the accumulator. 
  
# For example, the function call:
# filter_list('arrest_boro','B', data) would be expected to evaluate to the following list:
# [ {'arrest_date': '2021-09-22T00:00:00.000', 'pd_cd': '109', 'pd_desc': 'ASSAULT 2,1,UNCLASSIFIED', 'ky_cd': '106.0', 'arrest_boro': 'B', 'age_group': '25-44', 'ofns_desc': 'FELONY ASSAULT'} ]

def filter_list(k, v, lst): # k is a string; v is a string; lst is a list of dictionaries.
  list = []
  for hash in lst:
    for key in hash:
      if key == k and hash[key] == v:
        list.append(hash)
  return list

# The entries in keys will be the accumulator's keys. The accumulator's values will be the entries in values. Once complete, the accumulator will need to associate keys' entry at index 0 with values' entry at index 0, keys' entry at index 1 with values' entry at index 1, and so on. You SHOULD keys and values have an equal length.
  
# For example, the function call:
# dict_gen(['arrest_date','arrest_boro'], [ '2022-01-01' , 'B' ]) would be expected to evaluate to:
# {'arrest_date' : '2022-01-01', 'arrest_boro' : 'B'}

def dict_gen(keys, values): # keys is a list of strings; values is also a list of strings.
  hash = {}
  for i in range(len(keys)):
    for j in range(len(values)):
      hash[keys[i]] = values[i]
  return hash

# Your get_values function should use the accumulator pattern to return a new list. The list should contain the values in dic that are associated with the strings in keys. The order of the values in your accumulator must mirror the order of the keys in keys so the accumulator's entry at index 0 will be the value associated with the key at keys index 0, the accumulator's entry at index 1 will be the value associated with the key at keys index 1, and so on. You SHOULD assume that every entry in keys is a key in dic.

# For example, the function call:
# get_values(['arrest_boro', 'pd_cd'], data[0]) would be expected to evaluate to the following list:
#[ 'Q' , '268' ]

def get_values(keys, ele): # keys is a list of strings; dic is a dictionary;
  arr = []
  for i in keys:
    for j in ele:
      if i == j:
        arr.append(ele[i])
  return arr

# Sample Data For Testing
# data = [ {'arrest_date': '2020-07-17T00:00:00.000', 'pd_cd': '268', 'pd_desc': 'CRIMINAL MIS 2 & 3', 'ky_cd': '121.0', 'arrest_boro': 'Q', 'age_group': '18-24', 'ofns_desc': 'CRIMINAL MISCHIEF & RELATED OF'},
# {'arrest_date': '2021-08-31T00:00:00.000', 'pd_cd': '779', 'pd_desc': 'PUBLIC ADMINISTRATION,UNCLASSI', 'ky_cd': '126.0', 'arrest_boro': 'Q', 'age_group': '45-64', 'ofns_desc': 'MISCELLANEOUS PENAL LAW'},
# {'arrest_date': '2021-07-15T00:00:00.000', 'pd_cd': '739', 'pd_desc': 'FRAUD,UNCLASSIFIED-FELONY', 'ky_cd': '112.0', 'arrest_boro': 'Q', 'age_group': '25-44', 'ofns_desc': 'THEFT-FRAUD'},
# {'arrest_date': '2021-08-03T00:00:00.000', 'pd_cd': '511', 'pd_desc': 'CONTROLLED SUBSTANCE, POSSESSI', 'ky_cd': '235.0', 'arrest_boro': 'M', 'age_group': '25-44', 'ofns_desc': 'DANGEROUS DRUGS'},
# {'arrest_date': '2021-08-28T00:00:00.000', 'pd_cd': '101', 'pd_desc': 'ASSAULT 3', 'ky_cd': '344.0', 'arrest_boro': 'K', 'age_group': '25-44', 'ofns_desc': 'ASSAULT 3 & RELATED OFFENSES'},
# {'arrest_date': '2021-09-20T00:00:00.000', 'pd_cd': '101', 'pd_desc': 'ASSAULT 3', 'ky_cd': '344.0', 'arrest_boro': 'M', 'age_group': '25-44', 'ofns_desc': 'ASSAULT 3 & RELATED OFFENSES'},
# {'arrest_date': '2021-08-18T00:00:00.000', 'pd_cd': '101', 'pd_desc': 'ASSAULT 3', 'ky_cd': '344.0', 'arrest_boro': 'K', 'age_group': '25-44', 'ofns_desc': 'ASSAULT 3 & RELATED OFFENSES'},
# {'arrest_date': '2021-09-22T00:00:00.000', 'pd_cd': '109', 'pd_desc': 'ASSAULT 2,1,UNCLASSIFIED', 'ky_cd': '106.0', 'arrest_boro': 'B', 'age_group': '25-44', 'ofns_desc': 'FELONY ASSAULT'},
# {'arrest_date': '2021-07-15T00:00:00.000', 'pd_cd': '109', 'pd_desc': 'ASSAULT 2,1,UNCLASSIFIED', 'ky_cd': '106.0', 'arrest_boro': 'K', 'age_group': '45-64', 'ofns_desc': 'FELONY ASSAULT'},
# {'arrest_date': '2021-08-11T00:00:00.000', 'pd_cd': '515', 'pd_desc': 'CONTROLLED SUBSTANCE,SALE 3', 'ky_cd': '117.0', 'arrest_boro': 'K', 'age_group': '45-64', 'ofns_desc': 'DANGEROUS DRUGS'} ]

# Your function will need to open f_in and read in the first row of the file. (The first row of the file contains the column headers).  Your function must return a list containing the values in that header row.

# For example, if the first line of a file named "bogus.csv" contained: arrest_date,arrest_boro
# then the function call: 
# header_reader("bogus.csv")
# would be expected to evaluate to:
# ['arrest_date','arrest_boro']
 
def header_reader(f_in): #f_in is a string.

  with open(f_in) as f:
    reader = csv.reader(f)
    header = next(reader)
    return header

# Each non-header row in f_in should be added to the accumulator. You SHOULD assume that f_in contains a header row.

# For example, suppose the lines of a file named "fake_example.csv" were:
# arrest_date,arrest_boro
# 2022-01-01,B
# then the function call:
#data_reader("fake_example.csv")
# would be expected to evaluate to:
# [ [ '2022-01-01' , 'B' ] ]

def data_reader(f_in): #f_in is a string.
  lst = []
  with open(f_in) as f:
    reader=csv.reader(f)
    next(reader)
    for line in reader:
      lst.append(line)
  return lst

# Your function will need to open f_out so that any existing contents will be erased. The contents of lst should be written to f_out as a row in a CSV file. Your function does not need to return anything.

# For example, calling:
# header_writer(['arrest_date','ky_cd'], "fic.csv") would result in the file named "fic.csv" containing a single line of text reading:
# arrest_date,ky_cd


def header_writer(lst, f_out): # lst is a list of strings; f_out is a string.
  with open(f_out, "w") as f:
    writer = csv.writer(f)
    writer.writerow(lst)

# Your function will need to open f_out so that its existing contents are preserved. Your function will need to write each entry in lst as a row in a CSV file at the end of f_out. The order of the added rows in  f_out must match the order the entries appear in lst. Your function does not need to return anything.

# For example, calling:
# data_writer([ [ '2022-01-01' , 'B' ] ], "fake.csv") would result in the following line being added at the end of "fake.csv":
# 2022-01-01,B

def data_writer(lst, f_out): # lst is a list of lists; f_out is a string.
  with open(f_out, "a") as f:
    writer = csv.writer(f)
    for i in lst:
      writer.writerow(i)

# Your clean_list function should use the accumulator pattern to return a new list. Each dictionary in lst which has k as a key should be added to the accumulator list. You SHOULD NOT assume that all dictionaries in lst will have k as a key.

# For example, the function call:
# clean_list('keep', [{'a':'b'}, {'c':'d'}, {'keep':'t','a':'d'}]) would be expected to evaluate to:
# [ {'keep':'t','a':'d'} ]

def clean_list(k, lst): # k is a string; lst is a list of dictionaries.
  ret_val = []
  for i in lst:
    for j in i:
      if k in j:
        ret_val.append(i)
  return ret_val

#Your function will need to read in this file and return a list of dictionaries. There will need to be 1 dictionary per non-header row in the file. For each dictionary, its keys will be the strings read in the header row and the values will be the data read in from a data row. The data rows will parallel the header row: the dictionary should map the value of the initial column in the header row to the value at the initial column in that data row, and so on. You SHOULD assume that all rows in f_in have an equal number of columns. 

# For example, suppose the file madeUp.csv contains:
#       arrest_date,arrest_boro
#       2022-01-20,B
#       2022-01-11,M
# then the function call: cache_reader('madeUp.csv') would be expected to evaluate to:
# 	[{'arrest_date': '2022-01-20', 'arrest_boro': 'B'},
#    {'arrest_date': '2022-01-11', 'arrest_boro': 'M'}] 

def cache_reader(f_in): # f_in is a string.  ret_val = []
  ret_val = []
  with open(f_in) as f:
    reader = csv.reader(f)
    header = next(reader)
    for line in reader:
      hash = {}
      for i in range(len(header)):
        for j in range(i, len(line)):
          if i == j:
            hash[header[i]] = line[j]
      ret_val.append(hash)
  return ret_val

# Your function should be certain f_out is opened such that all its contents are erased. When your function has finished f_out will need to be a proper, valid CSV file. You SHOULD assume that lst has at least 1 dictionary and SHOULD assume that all the dictionaries in lst have the same keys. lst's dictionaries' keys will need to be written out as the initial row in the CSV file named in f_out. After the row containing the keys, f_out will need to have rows containing the values in lst's dictionaries. The order of the rows of values in f_out should be the same as the order of the dictionaries in lst. Within a row, each value must be written in the same column as its key was written in the initial row.

# For example, if
# lst = [{'arrest_date': '2022-01-20', 'arrest_boro': 'B'},
#        {'arrest_date': '2022-01-11', 'arrest_boro': 'M'}] 
# Then the call 
# 	cache_writer(lst, 'data.csv')
# would result in the file named data.csv having the following lines:
# arrest_date,arrest_boro
# 	2022-01-20,B
# 	2022-01-11,M

def cache_writer(lst, f_out): # lst is a list of dictionaries; f_out is a string.
  with open(f_out, "w") as f:
    writer = csv.writer(f)
    writer.writerow(lst[0].keys())
    for i in lst:
      writer.writerow(i.values())

# url will contain a URL at which a JSON string is stored. Your function will need to return the JSON string at url as usable Python data.

# For example, suppose there were a JSON string stored at "https://bit.ly/3zP8DE5" and that this faked URL had the JSON string:
# 	{"arrest_date" : "2022-01-01", "arrest_boro" : "B" }
# then the function call:
# 	retrieve_json("https://bit.ly/3zP8DE5")
# would be expected to evaluate to:
# { 'arrest_date' : '2022-01-01', 'arrest_boro' : 'B' }

def retrieve_json(url): # url is a string.
  response = urllib.request.urlopen(url)
  content_string = response.read().decode()
  content = json.loads(content_string)
  return content