import logging
import sys
from pathlib import Path

def get_logger(name: str):
    log_dir = Path("src/utils/logs")
    log_dir.mkdir(exist_ok=True)
    
    logger = logging.getLogger(name)
    
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        " [%(levelname)s] - %(name)s | %(asctime)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # 3. Stream Handler (Terminal output)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(logging.INFO)  # Info and above to console

    # 4. File Handler (Persistent logs)
    file_handler = logging.FileHandler(log_dir / "app.log")
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)  # Debug and above to file

    # Add handlers to the logger
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    return logger