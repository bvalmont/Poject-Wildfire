let defaultURL3 = "/fire_cause";
d3.json(defaultURL3).then(function(pie) {
  console.log(pie)
  //var data = [data];
  
  let xvalues3 = pie.x;
  let yvalues3= pie.y;
  

  let trace3 = {
    values: pie.y,
    labels: pie.x,
    type: 'pie'
    
  };

  let data = [trace3];
  let layout = {autoscaleYAxis: true,
  title: "Top 10 Causes of Wildfires (1992-2015)",
 };


  Plotly.plot("pie", data, layout);
});









