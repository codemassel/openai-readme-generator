import logging

# Logging-Konfiguration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("readme_generator.log", encoding="utf-8")
    ]
)

logger = logging.getLogger(__name__)
