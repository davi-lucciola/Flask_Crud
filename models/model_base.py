from sqlalchemy.orm import declarative_base
from conf.config_engine import __engine


Base = declarative_base(bind=__engine)