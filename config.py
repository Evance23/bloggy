import os


class Config:
    '''
    General configuration parent class
    '''


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = "postgresql://bqcywcgfpxfuvh:aaf3b37f07242734b8b5cad017ccf6b5c363235698c86ec91a098f54457cfba5@ec2-3-212-75-25.compute-1.amazonaws.com:5432/d1kkd9a7ih1l3j?sslmode=require"


class TestConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cocoh:kitkAt10@localhost/blogomatic_test'

 pass 
class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cocoh:kitkAt10@localhost/blogomatic'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig

}
