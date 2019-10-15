console.log("justfires");
let myMap = L.map("map", {
  center: [39.8283, -98.5795],
  zoom: 6
});


L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='https://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, Imagery © <a href='https://www.mapbox.com/'>Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.outdoors",
  accessToken: "pk.eyJ1IjoidmFsbW9udDM3NSIsImEiOiJjazE4OXZnMHowOHdmM25vOXI1NzJva3lvIn0.kqjs4SZox6IYe5d4c6N-uw"
}).addTo(myMap);
console.log("It");

let url_heat = "/heatmap";

d3.json(url_heat, function(data) {

  console.log(data);
  console.log(data.x);
  console.log(data.x.length);

  let heatArray = [];
  

  for (var i = 0; i < data.x.length; i++) {
    
    let x = data.x[i];
    let y = data.y[i];
    
      
      heatArray.push([x,y]);
    }
  
  console.log(heatArray);

  let heat = L.heatLayer(heatArray, {
    radius: 20,
    blur: 35
  }).addTo(myMap);
  //console.log(data);
  //console.log(heatArray);
});

(L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'));
L.terminator().addTo(myMap)



console.log("is working");