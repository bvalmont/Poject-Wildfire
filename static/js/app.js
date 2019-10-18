// Plot the default route once the page loads
let defaultURL = "/total_years";
d3.json(defaultURL).then(function(line) {
  console.log(line.y)
  //var data = [data];
  
  let xvalues = line.x;
  let yvalues = line.y;
  //let markersize = line.y;
  //let markercolors = line.x;
  //let textvalues = bub.otu_labels;

  let trace = {
        type: 'scatter',
        x: xvalues,
        y: yvalues,
        mode: 'lines',
        name: 'USA',
        line: {
          color: 'red',
          width: 5
        }
      
      };

  let data = [trace];
  let layout = {autoscaleYAxis: true,
  title: "Count of United States Wildfires (1996-2015)",
xaxis: {
  title: 'Wildfire Years'
},
yaxis:{
  title: 'Total Wildfires'
} };


  Plotly.plot("scatter", data, layout);
});

// Update the plot with new data
function updatePlotly(newdata) {
  Plotly.restyle("scatter", "x", [newdata.x]);
  Plotly.restyle("scatter", "y", [newdata.y]);
}

// Get new data whenever the dropdown selection changes
function getData(route) {
  console.log(route);
  d3.json(`/${route}`).then(function(data) {
    console.log("newdata", data);
    updatePlotly(data);
  });
}




