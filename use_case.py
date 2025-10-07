import logging

from app_entities.pepas import PepaApp

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    PepaApp().run()