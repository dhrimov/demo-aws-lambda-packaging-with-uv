import logging

from acme_order_processor.environment import LambdaEnvironment

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

environment: LambdaEnvironment = LambdaEnvironment()


def handler(event, context):
    logger.info(f"Hello ACME order processor lambda on {environment.tier}!")
