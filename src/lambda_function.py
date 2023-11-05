import functions
from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext


logger = Logger(service="lambda_handler")


@logger.inject_lambda_context(log_event=True, clear_state=True)
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return functions.ok({})
