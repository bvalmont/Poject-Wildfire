import pandas as pd



from flask import (
    Flask,
    render_template,
    jsonify)

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine

import numpy as np

app = Flask(__name__)

#Database Configuration


@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")

@app.route("/map")
def mappage():
    """Render heatmap."""
    return render_template("heatmap.html")

@app.route("/heatmap")
def heat_map_data():
    """Return lat and long for wildfires"""
    engine = create_engine("sqlite:///wildfire.sqlite")
    connection = engine.connect()


    # Query for total fires per year AL
    lat_long_fires = "select Lat, Long from wildfire"
    lat_long_fires2 = pd.read_sql(lat_long_fires, connection)

    # Format the data for Plotly
    us_heat = {
        "x": lat_long_fires2["Lat"].values.tolist(),
        "y": lat_long_fires2["Long"].values.tolist(),
        
    }
    connection.close()
    return jsonify(us_heat)


@app.route("/total_years")
def total_years_data():
    """Return total fires and years"""
    engine = create_engine("sqlite:///wildfire.sqlite")
    connection = engine.connect()

    # Query for total fires per year US
    total_years_fire = "select fire_year, count(st) from wildfire where fire_year >= 1996 group by fire_year order by fire_year LIMIT 20"
    United_States_total = pd.read_sql(total_years_fire, connection)

    # Format the data for Plotly
    US = {
        "x": United_States_total["fire_year"].values.tolist(),
        "y": United_States_total["count(st)"].values.tolist(),
        "type": "'scatter'"
    }
    connection.close()
    return jsonify(US)


@app.route("/ca_years")
def ca_years_data():
    """Return ca fires and years"""
    engine = create_engine("sqlite:///wildfire.sqlite")
    connection = engine.connect()

    # Query for total fires per year CA
    ca_years_fire = "select fire_year, count(st) from wildfire where fire_year >= 1996 and st = 'CA' group by fire_year order by fire_year LIMIT 20"
    california_total = pd.read_sql(ca_years_fire, connection)

    # Format the data for Plotly
    California = {
        "x": california_total["fire_year"].values.tolist(),
        "y": california_total["count(st)"].values.tolist(),
        "type": "scatter"
    }
    connection.close()
    return jsonify(California)

@app.route("/ga_years")
def ga_years_data():
    """Return ga fires and years"""
    engine = create_engine("sqlite:///wildfire.sqlite")
    connection = engine.connect()


    # Query for total fires per year GA
    ga_years_fire = "select fire_year, count(st) from wildfire where fire_year >= 1996 and st = 'GA' group by fire_year order by fire_year LIMIT 20"
    georgia_total = pd.read_sql(ga_years_fire, connection)

    # Format the data for Plotly
    Georgia = {
        "x": georgia_total["fire_year"].values.tolist(),
        "y": georgia_total["count(st)"].values.tolist(),
        "type": "scatter"
    }
    connection.close()
    return jsonify(Georgia)

@app.route("/tx_years")
def tx_years_data():
    """Return tx fires and years"""
    engine = create_engine("sqlite:///wildfire.sqlite")
    connection = engine.connect()


    # Query for total fires per year TX
    tx_years_fire = "select fire_year, count(st) from wildfire where fire_year >= 1996 and st = 'TX' group by fire_year order by fire_year LIMIT 20"
    texas_total = pd.read_sql(tx_years_fire, connection)

    # Format the data for Plotly
    Texas = {
        "x": texas_total["fire_year"].values.tolist(),
        "y": texas_total["count(st)"].values.tolist(),
        "type": "scatter"
    }
    connection.close()
    return jsonify(Texas)

@app.route("/nc_years")
def nc_years_data():
    """Return nc fires and years"""
    engine = create_engine("sqlite:///wildfire.sqlite")
    connection = engine.connect()


    # Query for total fires per year NY
    nc_years_fire = "select fire_year, count(st) from wildfire where fire_year >= 1996 and st = 'NC' group by fire_year order by fire_year LIMIT 20"
    north_carolina_total = pd.read_sql(nc_years_fire, connection)

    # Format the data for Plotly
    North_Carolina = {
        "x": north_carolina_total["fire_year"].values.tolist(),
        "y": north_carolina_total["count(st)"].values.tolist(),
        "type": "scatter"
    }
    connection.close()
    return jsonify(North_Carolina)

@app.route("/fl_years")
def fl_years_data():
    """Return fl fires and years"""
    engine = create_engine("sqlite:///wildfire.sqlite")
    connection = engine.connect()


    # Query for total fires per year FL
    fl_years_fire = "select fire_year, count(st) from wildfire where fire_year >= 1996 and st = 'FL' group by fire_year order by fire_year LIMIT 20"
    florida_total = pd.read_sql(fl_years_fire, connection)

    # Format the data for Plotly
    Florida = {
        "x": florida_total["fire_year"].values.tolist(),
        "y": florida_total["count(st)"].values.tolist(),
        "type": "scatter"
    }
    connection.close()
    return jsonify(Florida)

@app.route("/sc_years")
def sc_years_data():
    """Return sc fires and years"""
    engine = create_engine("sqlite:///wildfire.sqlite")
    connection = engine.connect()


    # Query for total fires per year SC
    sc_years_fire = "select fire_year, count(st) from wildfire where fire_year >= 1996 and st = 'SC' group by fire_year order by fire_year LIMIT 20"
    south_carolina_total = pd.read_sql(sc_years_fire, connection)

    # Format the data for Plotly
    South_Carolina = {
        "x": south_carolina_total["fire_year"].values.tolist(),
        "y": south_carolina_total["count(st)"].values.tolist(),
        "type": "scatter"
    }
    connection.close()
    return jsonify(South_Carolina)

@app.route("/ny_years")
def ny_years_data():
    """Return ny fires and years"""
    engine = create_engine("sqlite:///wildfire.sqlite")
    connection = engine.connect()


    # Query for total fires per year NY
    ny_years_fire = "select fire_year, count(st) from wildfire where fire_year >= 1996 and st = 'NY' group by fire_year order by fire_year LIMIT 20"
    new_york_total = pd.read_sql(ny_years_fire, connection)

    # Format the data for Plotly
    New_York = {
        "x": new_york_total["fire_year"].values.tolist(),
        "y": new_york_total["count(st)"].values.tolist(),
        "type": "scatter"
    }
    connection.close()
    return jsonify(New_York)

@app.route("/ms_years")
def ms_years_data():
    """Return ms fires and years"""
    engine = create_engine("sqlite:///wildfire.sqlite")
    connection = engine.connect()


    # Query for total fires per year MS
    ms_years_fire = "select fire_year, count(st) from wildfire where fire_year >= 1996 and st = 'MS' group by fire_year order by fire_year LIMIT 20"
    mississippi_total = pd.read_sql(ms_years_fire, connection)

    # Format the data for Plotly
    Mississippi = {
        "x": mississippi_total["fire_year"].values.tolist(),
        "y": mississippi_total["count(st)"].values.tolist(),
        "type": "scatter"
    }
    connection.close()
    return jsonify(Mississippi)

@app.route("/az_years")
def az_years_data():
    """Return az fires and years"""
    engine = create_engine("sqlite:///wildfire.sqlite")
    connection = engine.connect()


    # Query for total fires per year AZ
    az_years_fire = "select fire_year, count(st) from wildfire where fire_year >= 1996 and st = 'AZ' group by fire_year order by fire_year LIMIT 20"
    arizona_total = pd.read_sql(az_years_fire, connection)

    # Format the data for Plotly
    Arizona = {
        "x": arizona_total["fire_year"].values.tolist(),
        "y": arizona_total["count(st)"].values.tolist(),
        "type": "scatter"
    }
    connection.close()
    return jsonify(Arizona)

@app.route("/al_years")
def al_years_data():
    """Return al fires and years"""
    engine = create_engine("sqlite:///wildfire.sqlite")
    connection = engine.connect()


    # Query for total fires per year AL
    al_years_fire = "select fire_year, count(st) from wildfire where fire_year >= 1996 and st = 'AL' group by fire_year order by fire_year LIMIT 20"
    alabama_total = pd.read_sql(al_years_fire, connection)

    # Format the data for Plotly
    Alabama = {
        "x": alabama_total["fire_year"].values.tolist(),
        "y": alabama_total["count(st)"].values.tolist(),
        "type": "scatter"
    }
    connection.close()
    return jsonify(Alabama)

@app.route("/acreage")
def acreage_data():
    """Return acreage burned for top 10 States"""
    engine = create_engine("sqlite:///wildfire.sqlite")
    connection = engine.connect()


    # Query for total fires per year AL
    acreage = "select st, round(sum(fire_size_acre)) from wildfire group by st order by sum(fire_size_acre) DESC Limit 10"
    acreage_total = pd.read_sql(acreage, connection)

    # Format the data for Plotly
    all_years = {
        "x": acreage_total["ST"].values.tolist(),
        "y": acreage_total["round(sum(fire_size_acre))"].values.tolist(),
        "type": "bar"
    }
    connection.close()
    return jsonify(all_years)

@app.route("/acreage_2011")
def acreage_2011_data():
    """Return acreage burned for top 10 States in 2011"""
    engine = create_engine("sqlite:///wildfire.sqlite")
    connection = engine.connect()


    # Query for total fires per year AL
    acreage_2011 = "select st, round(sum(fire_size_acre)) from wildfire where fire_year = 2011 group by st order by sum(fire_size_acre) DESC Limit 10"
    acreage_total_2011 = pd.read_sql(acreage_2011, connection)

    # Format the data for Plotly
    year_2011 = {
        "x": acreage_total_2011["ST"].values.tolist(),
        "y": acreage_total_2011["round(sum(fire_size_acre))"].values.tolist(),
        "type": "bar"
    }
    connection.close()
    return jsonify(year_2011)

@app.route("/acreage_2012")
def acreage_2012_data():
    """Return acreage burned for top 10 States in 2012"""
    engine = create_engine("sqlite:///wildfire.sqlite")
    connection = engine.connect()


    # Query for total fires per year AL
    acreage_2012 = "select st, round(sum(fire_size_acre)) from wildfire where fire_year = 2012 group by st order by sum(fire_size_acre) DESC Limit 10"
    acreage_total_2012 = pd.read_sql(acreage_2012, connection)

    # Format the data for Plotly
    year_2012 = {
        "x": acreage_total_2012["ST"].values.tolist(),
        "y": acreage_total_2012["round(sum(fire_size_acre))"].values.tolist(),
        "type": "bar"
    }
    connection.close()
    return jsonify(year_2012)

@app.route("/acreage_2013")
def acreage_2013_data():
    """Return acreage burned for top 10 States in 2013"""
    engine = create_engine("sqlite:///wildfire.sqlite")
    connection = engine.connect()


    # Query for total fires per year AL
    acreage_2013 = "select st, round(sum(fire_size_acre)) from wildfire where fire_year = 2013 group by st order by sum(fire_size_acre) DESC Limit 10"
    acreage_total_2013 = pd.read_sql(acreage_2013, connection)

    # Format the data for Plotly
    year_2013 = {
        "x": acreage_total_2013["ST"].values.tolist(),
        "y": acreage_total_2013["round(sum(fire_size_acre))"].values.tolist(),
        "type": "bar"
    }
    connection.close()
    return jsonify(year_2013)

@app.route("/acreage_2014")
def acreage_2014_data():
    """Return acreage burned for top 10 States in 2014"""
    engine = create_engine("sqlite:///wildfire.sqlite")
    connection = engine.connect()


    # Query for total fires per year AL
    acreage_2014 = "select st, round(sum(fire_size_acre)) from wildfire where fire_year = 2014 group by st order by sum(fire_size_acre) DESC Limit 10"
    acreage_total_2014 = pd.read_sql(acreage_2014, connection)

    # Format the data for Plotly
    year_2014 = {
        "x": acreage_total_2014["ST"].values.tolist(),
        "y": acreage_total_2014["round(sum(fire_size_acre))"].values.tolist(),
        "type": "bar"
    }
    connection.close()
    return jsonify(year_2014)

@app.route("/acreage_2015")
def acreage_2015_data():
    """Return acreage burned for top 10 States in 2014"""
    engine = create_engine("sqlite:///wildfire.sqlite")
    connection = engine.connect()


    # Query for total fires per year AL
    acreage_2015 = "select st, round(sum(fire_size_acre)) from wildfire where fire_year = 2015 group by st order by sum(fire_size_acre) DESC Limit 10"
    acreage_total_2015 = pd.read_sql(acreage_2015, connection)

    # Format the data for Plotly
    year_2015 = {
        "x": acreage_total_2015["ST"].values.tolist(),
        "y": acreage_total_2015["round(sum(fire_size_acre))"].values.tolist(),
        "type": "bar"
    }
    connection.close()
    return jsonify(year_2015)

@app.route("/fire_cause")
def fire_cause_data():
    """Return top 10 causes of fire for dataset"""
    engine = create_engine("sqlite:///wildfire.sqlite")
    connection = engine.connect()


    # Query for causes of wildfires and its count
    causes = "select Fire_Cause, count(Fire_Cause) from wildfire group by Fire_Cause order by count(Fire_Cause) DESC LIMIT 10"
    causes_fire = pd.read_sql(causes, connection)

    # Format the data for Plotly
    fire_causes = {
        "x": causes_fire["Fire_Cause"].values.tolist(),
        "y": causes_fire["count(Fire_Cause)"].values.tolist(),
        "type": "pie"
    }
    connection.close()
    return jsonify(fire_causes)



if __name__ == '__main__':
    app.run(debug=True)

