# Import the dependencies.
import numpy as np

import sqlalchemy
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    # 1. List all the available routes
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():

    session = Session(engine)
    results = session.query(measurement.prcp,
                            measurement.date).filter(measurement.date>='2016-08-23').order_by(measurement.date).all()

    session.close()
    
    precipitation = []
    for x in results:
        data = {}
        data["Date"] = x.date
        data["Precipitation"] = x.prcp
        precipitation.append(prcpData)

    return jsonify(data)


@app.route("/api/v1.0/station")
def stations():
    
    st_list = session.query(station.name).all()

    session.close()

    all_station = list(np.ravel(st_list))
    
    return jsonify(all_stations)


@app.route("/api/v1.0/tobs")
def tobs():
    year_ago_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    temp_data = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= year_ago_date).all()
    session.close()

    temp_info = []
    for date,tobs in temp_data:
        tobs_dic = {}
        tobs_dic["date"] = date
        tobs_dic["tobs"] = tobs
        temp_info.append(tobs_dic)
    return jsonify(temp_info)

@app.route("/api/v1.0/start")
def start():
    return
@app.route("/api/v1.0/<start>/<end>")
def start_end():
    return

if __name__ == '__main__':
      app.run(debug=True) 
