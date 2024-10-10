from flask import Flask
#from opencensus.ext.azure.log_exporter import AzureLogHandler
import logging

app = Flask(__name__)

# Set up logging with Application Insights
#app.logger.addHandler(AzureLogHandler(connection_string='InstrumentationKey=4510a283-e981-4f78-99a1-fea2285db610;IngestionEndpoint=https://westus2-2.in.applicationinsights.azure.com/;LiveEndpoint=https://westus2.livediagnostics.monitor.azure.com/;ApplicationId=266fbb8a-3fa0-41c5-9c71-3d6c16b8bb8c'))

@app.route('/')
def hello():
    app.logger.info("Hello World endpoint was accessed")
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
