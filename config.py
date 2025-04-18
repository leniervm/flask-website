# config.py
import os
class Config:
# Common settings for all environments
    SECRET_KEY = os.getenv("SECRET_KEY")
    # ... other settings

class DevelopmentConfig(Config):
    DEBUG = True
    # ... development-specific settings (e.g., a development database)

class ProductionConfig(Config):
    DEBUG = False
    # ... production-specific settings (e.g., a production database)
