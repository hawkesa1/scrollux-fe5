import azure.functions as func
import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler

# Set up Application Insights Logging
logger = logging.getLogger(__name__)
handler = AzureLogHandler(connection_string="InstrumentationKey=ae5bd5d0-ce93-48cf-be23-234ac7bb1b0e;IngestionEndpoint=https://westeurope-5.in.applicationinsights.azure.com/;LiveEndpoint=https://westeurope.livediagnostics.monitor.azure.com/;ApplicationId=2a6265c8-c5c1-4f61-b8bf-8c2204eaab61")
logger.addHandler(handler)
logger.setLevel(logging.INFO)

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logger.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        response_message = f"Hello, {name}. This HTTP triggered function executed successfully."
        logger.info(f"Responding with message: {response_message}")  # Log the response message
        return func.HttpResponse(response_message)
    else:
        response_message = "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response."
        logger.info(f"Responding with default message: {response_message}")  # Log the response message
        return func.HttpResponse(response_message, status_code=200)
