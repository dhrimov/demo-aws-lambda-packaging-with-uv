from pydantic_settings import BaseSettings


class LambdaEnvironment(BaseSettings):
    tier: str = "test"
