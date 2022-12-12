from celery import Celery
from src.config.app_config import Config

celery = Celery(__name__, broker_url=Config.BROKER_URL, resukt_backend=Config.RESULT_BACKEND)

__all__ = ['celery_app']