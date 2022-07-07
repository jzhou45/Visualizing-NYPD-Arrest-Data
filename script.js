function getData(){
  ajaxGetRequest("/line", plotLineGraph);
  ajaxGetRequest("/pie", plotPieGraph);
}

// Line graph: Plot.ly automatically interprets the values associated with the 'arrest_date' key as dates; showing the number of arrests made on each date in your dataset.
function plotLineGraph(jsonString){
  var content = JSON.parse(jsonString);
  var data2 = {};
  var x = Object.keys(content);
  var y = Object.values(content);
  data2['x'] = x;
  data2['y'] = y;
  data2['type'] = 'scatter';
  var data = [];
  data.push(data2);
  var layout = {title:'Arrests in NYC By Date', xaxis: {title: 'Date'}, yaxis: {title: '# of Arrests'}};
  Plotly.newPlot('lineGraph', data, layout);
}

// pie chart showing the number of arrests which were made in each of the 5 boroughs.
function plotPieGraph(jsonString){
  var content = JSON.parse(jsonString);
  var data2 = {};
  var labels = Object.keys(content);
  var values = Object.values(content);
  labels.sort()
  var allLabels = ['Bronx', 'Brooklyn', 'Manhatten', 'Queens', 'Staten Island'];
  var hash = {};
  for (i in labels){
    hash[labels[i]] = allLabels[i];
  }
  data2['labels'] = Object.values(hash);
  data2['values'] = values;
  data2['type'] = 'pie';
  var data = [];
  data.push(data2);
  var layout = {title: 'Arrests Broken Out By Borough'};
  Plotly.newPlot('pieGraph', data, layout);
}

// bar chart showing the number of arrests broken out by the age of the person being arrested. Unlike the first two graphs, this graph's data will be limited to a specific borough and so will not be generated when the page starts up, but is instead generated whenever the user clicks a button. You will need to send the string that the user entered from the client to the server and only display results from that borough:

function txtbox(){
  let ele = document.getElementById("boroText");
  let vlue = ele["value"];
  let ele2 = document.getElementById('boroInner');
  ele2['innerHTML'] = "You've entered " + vlue + ".";
  ele["value"] = "";
  let jsonString = JSON.stringify(vlue);
  ajaxPostRequest("/bar", jsonString, plotBarGraph)
}

function plotBarGraph(jsonString){
  var content = JSON.parse(jsonString);
  var data2 = {};
  var x = Object.keys(content);
  var y = Object.values(content);
  data2['x'] = x;
  data2['y'] = y;
  data2['type'] = 'bar';
  var data = [];
  data.push(data2);
  var ele = document.getElementById("boroInner");
  var ele2 = ele['innerHTML'];
  var boro = '';
  if (ele2 == 'Q'){
    boro += "Queens";
  }
  else if (ele2 == 'B'){
    boro += 'Bronx';
  }
  else if (ele2 == 'K'){
    boro += 'Brooklyn'
  }
  else if (ele2 == 'M'){
    boro += 'Manhattan'
  }
  else if (ele2 == 'S'){
    boro += 'Staten Island'
  }
  var titl = 'Age of People Arrested in ' + boro;
  layout = {title: titl, xaxis: {title: 'Age Range'}, yaxis: {title: '# of Arrests'}};
  Plotly.newPlot('barGraph', data, layout);
}