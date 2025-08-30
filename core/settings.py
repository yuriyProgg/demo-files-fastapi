from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_URL = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"

MEDIA_URL = "/api/media/"
MEDIA_ROOT = BASE_DIR / "media" / "files"
