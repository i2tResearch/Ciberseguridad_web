import requests as requests
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin
import json

from backend.Services.ReportServices import ReportService
from backend.Services.ScanServices import ScanServices

app = Flask(__name__,
            static_folder="../../dist",
            template_folder="../../dist")
cors = CORS(app, resources={r"/*": {"origins": "*"}})

scanService = ScanServices()
reportService = ReportService()

@app.route('/api/mining/<int:task_id>', methods=['GET'])
def startScanController(task_id):
    if task_id == 0:
        scanService.setIsRunning(True)
        scanService.run()
    else:
        scanService.setIsRunning(False)
    return jsonify()


@app.route('/api/notification/', methods=['POST'])
def configureEmailController():
    email = request.json.get('email')
    scanService.configureEmail(email)
    return jsonify()


@app.route('/api/database/<int:task_id>', methods=['GET'])
def getDataReportChartController(task_id):
    if task_id == 0:
        list = reportService.getDataReportChart()
    else:
        list = reportService.getPredictionsHistory()
    return jsonify(list)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")



