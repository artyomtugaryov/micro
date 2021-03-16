from typing import Type


class BaseConfig:
    CONFIG_NAME = 'base'
    USE_MOCK_EQUIVALENCY = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = 'development'
    DEBUG = True


def get_config(environment: str = 'development') -> Type[BaseConfig]:
    return {
        DevelopmentConfig.CONFIG_NAME: DevelopmentConfig,
    }[environment]
