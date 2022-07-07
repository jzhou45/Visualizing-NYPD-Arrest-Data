import bottle
import json
import data
import os.path
import csv

def csv_to_dict(file_name):
  with open(file_name) as f:
    reader = csv.reader(f)
    header = next(reader)
    arr = []
    for line in reader:
      arr.append(data.dict_gen(header,line))
    return arr

# A route annotation for "/" must serve up the HTML file as a static file.
@bottle.route('/')
def index():
  html_file = bottle.static_file("index.html", root=".")
  return html_file

# A route annotation to serve up the ajax.js file as a static file. (This is the JavaScript file that contains the ajaxGetRequest and ajaxPostRequest function definitions.)
@bottle.route('/ajax.js')
def ajax_file():
  ajax_js_file = bottle.static_file("ajax.js", root=".")
  return ajax_js_file  

#A route annotation to serve up the JavaScript code file you wrote as a static file
@bottle.route('/script.js')
def chat_file():
  script_js_file = bottle.static_file("script.js", root=".")
  return script_js_file


# test_data = [ {'arrest_date': '2020-07-17', 'pd_cd': '268', 'pd_desc': 'CRIMINAL MIS 2 & 3', 'ky_cd': '121.0', 'arrest_boro': 'Q', 'age_group': '18-24', 'ofns_desc': 'CRIMINAL MISCHIEF & RELATED OF'},
# {'arrest_date': '2021-08-31', 'pd_cd': '779', 'pd_desc': 'PUBLIC ADMINISTRATION,UNCLASSI', 'ky_cd': '126.0', 'arrest_boro': 'Q', 'age_group': '45-64', 'ofns_desc': 'MISCELLANEOUS PENAL LAW'},
# {'arrest_date': '2021-07-15', 'pd_cd': '739', 'pd_desc': 'FRAUD,UNCLASSIFIED-FELONY', 'ky_cd': '112.0', 'arrest_boro': 'Q', 'age_group': '25-44', 'ofns_desc': 'THEFT-FRAUD'},
# {'arrest_date': '2021-08-03', 'pd_cd': '511', 'pd_desc': 'CONTROLLED SUBSTANCE, POSSESSI', 'ky_cd': '235.0', 'arrest_boro': 'M', 'age_group': '25-44', 'ofns_desc': 'DANGEROUS DRUGS'},
# {'arrest_date': '2021-08-28', 'pd_cd': '101', 'pd_desc': 'ASSAULT 3', 'ky_cd': '344.0', 'arrest_boro': 'K', 'age_group': '25-44', 'ofns_desc': 'ASSAULT 3 & RELATED OFFENSES'},
# {'arrest_date': '2021-09-20', 'pd_cd': '101', 'pd_desc': 'ASSAULT 3', 'ky_cd': '344.0', 'arrest_boro': 'M', 'age_group': '25-44', 'ofns_desc': 'ASSAULT 3 & RELATED OFFENSES'},
# {'arrest_date': '2021-08-18', 'pd_cd': '101', 'pd_desc': 'ASSAULT 3', 'ky_cd': '344.0', 'arrest_boro': 'K', 'age_group': '25-44', 'ofns_desc': 'ASSAULT 3 & RELATED OFFENSES'},
# {'arrest_date': '2021-09-22', 'pd_cd': '109', 'pd_desc': 'ASSAULT 2,1,UNCLASSIFIED', 'ky_cd': '106.0', 'arrest_boro': 'B', 'age_group': '25-44', 'ofns_desc': 'FELONY ASSAULT'},
# {'arrest_date': '2021-07-15', 'pd_cd': '109', 'pd_desc': 'ASSAULT 2,1,UNCLASSIFIED', 'ky_cd': '106.0', 'arrest_boro': 'K', 'age_group': '45-64', 'ofns_desc': 'FELONY ASSAULT'},
# {'arrest_date': '2021-08-11', 'pd_cd': '515', 'pd_desc': 'CONTROLLED SUBSTANCE,SALE 3', 'ky_cd': '117.0', 'arrest_boro': 'K', 'age_group': '45-64', 'ofns_desc': 'DANGEROUS DRUGS'} ]

# A get annotation to serve up the line graph data as a JSON string
@bottle.get('/line')
def get_line():
  cache = csv_to_dict("cache.csv")
  x = data.unique_values("arrest_date",cache)
  x.sort()
  arr = []
  for i in x:
    arr.append((len(data.filter_list('arrest_date', i, cache))))
  hash = data.dict_gen(x, arr)
  arr2 = []
  for j in hash:
    arr3 = []
    arr3.append(j)
    arr3.append(hash[j])
    arr2.append(arr3)
  ele = json.dumps(hash)
  return ele
  
# A get annotation to serve up the pie chart data as a JSON string

@bottle.get('/pie')
def get_pie():
  cache = csv_to_dict("cache.csv")
  x = data.unique_values("arrest_boro",cache)
  x.sort()
  arr = []
  for i in x:
    arr.append((len(data.filter_list('arrest_boro', i, cache))))
  hash = data.dict_gen(x, arr)
  arr2 = []
  for j in hash:
    arr3 = []
    arr3.append(j)
    arr3.append(hash[j])
    arr2.append(arr3)
  ele = json.dumps(hash)
  return ele
  
# A post annotation to serve up the bar chart data a JSON string
@bottle.post('/bar')
def post_bar():
  cache = csv_to_dict("cache.csv")
  content = bottle.request.body.read().decode() # gets data from post request
  content = json.loads(content)
  age = data.unique_values('age_group', cache)
  age.sort()
  arr = []
  arrest_in_boro = data.filter_list('arrest_boro', content, cache)
  for i in age:
    arr.append(len(data.filter_list('age_group', i, arrest_in_boro)))
  hash = data.dict_gen(age, arr)
  arr2 = []
  for j in hash:
    arr3 = []
    arr3.append(i)
    arr3.append(hash[i])
    arr2.append(arr3)
  ele = json.dumps(hash)
  return ele
  
def load_data( ):
  csv_file = 'cache.csv'
  if not os.path.isfile(csv_file):
    url = 'https://data.cityofnewyork.us/resource/uip8-fykc.json?$limit=50000&$select=arrest_date,pd_desc,ofns_desc,arrest_boro,arrest_precinct,law_cat_cd,age_group,perp_sex,perp_race'
    info = data.retrieve_json(url)
    needed_keys = ['arrest_date','age_group','arrest_boro','pd_desc','law_cat_cd']
    for k in needed_keys :
      info = data.clean_list(k, info)
    data.cache_writer(info, csv_file)

load_data()

bottle.run(host='0.0.0.0', port=8080)