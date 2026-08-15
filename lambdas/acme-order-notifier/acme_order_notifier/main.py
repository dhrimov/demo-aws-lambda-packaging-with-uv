import logging

from acme_order_notifier.environment import LambdaEnvironment

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

environment: LambdaEnvironment = LambdaEnvironment()


def handler(event, context):
    logger.info(f"Hello ACME order notifier lambda on {environment.tier}!")
