from odmantic import AIOEngine

from app.config import settings

if settings.MODE == 'TEST':
    engine = AIOEngine(database=f'{settings.MONGODB_DATABASE_TESTS}')
else:

    engine = AIOEngine(database= f'{settings.MONGODB_DATABASE}')