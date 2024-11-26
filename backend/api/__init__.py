from flask import Flask, jsonify
from flask_cors import CORS
from config.config import config_by_name
import random
import time

def create_app(config_name='dev'):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    CORS(app)

    @app.route('/api/health-check')
    def health_check():
        return {'status': 'healthy'}

    @app.route('/api/insights/<layer>')
    def get_insights(layer):
        # Simulate some processing time
        time.sleep(1)
        
        insights = {
            "Wards 2021": [
                "Analyzing ward demographics and land use patterns...",
                "Ward has a mixed-use development profile with 60% residential and 40% commercial zoning",
                "Recent trends show increased applications for rezoning from residential to commercial",
                "Population density suggests need for additional public amenities"
            ],
            "Building Control Zones": [
                "Examining building control regulations and compliance...",
                "Area falls under high-density development zone with height restrictions of 5 stories",
                "Recent amendments to building codes affect setback requirements",
                "Notable increase in applications for height restriction departures"
            ]
        }
        
        return jsonify(insights.get(layer, [
            "Analyzing selected layer...",
            "Generating insights based on spatial patterns...",
            "Examining historical trends and current state...",
            "Providing recommendations based on analysis..."
        ]))

    return app