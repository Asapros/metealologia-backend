import secrets
from datetime import datetime
from hashlib import md5, sha256
from sys import argv

import uvicorn

from metealologia_backend.config import settings


def start():
    reload = settings.environment == "development"
    uvicorn.run(
        "metealologia_backend:app",
        host=settings.host,
        port=settings.port,
        reload=reload,
        log_config=settings.logging_config,
        reload_dirs=["metealologia_backend"] if reload else [],
        reload_includes=["dev_stations.yaml", "dev_logging.yaml", ".env.development"] if reload else []
    )


def generate_api_key():
    date = datetime.now().strftime("%y%m%d")
    payload_1 = secrets.token_hex(13)
    checksum_1 = md5(payload_1.encode("ascii")).hexdigest()[:3]
    payload_2 = secrets.token_hex(13)
    checksum_2 = md5(payload_2.encode("ascii")).hexdigest()[:3]
    key = date + "-" + payload_1 + "X" + checksum_1 + "-" + payload_2 + "X" + checksum_2 + "H"
    return key


def hash_api_key():
    key = argv[1] if len(argv) > 1 else generate_api_key()

    print("Key:", key)
    print("Hash:", sha256(key.encode("ascii")).hexdigest())

if __name__ == "__main__":
    start()
