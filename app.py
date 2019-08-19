import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station



app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def Welcome():
    return(
        "/api/v1.0/precipitation"
            "Convert the query results to a Dictionary using date as the key and prcp as the value."
            "Return the JSON representation of your dictionary."
        
        "/api/v1.0/stations"
            "Return a JSON list of stations from the dataset."
       
        "/api/v1.0/tobs"
            "Query for the dates and temperature observations from a year from the last data point."
            "Return a JSON list of Temperature Observations (tobs) for the previous year."
        
        "/api/v1.0/<start> and /api/v1.0/<start>/<end>"
            "The date should be under form YYYY-mm-dd"
            "Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range."
            "When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date."
            "When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive."
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    session.close()
    return( )

@app.route("/api/v1.0/stations")
def stations():
    return()


@app.route("/api/v1.0/tobs")
def tobs():
    return()

@app.route("/api/v1.0/<start>")
def start():
    return()

@app.route("/api/v1.0/<start>/<end>")
def start_end():
    return()
