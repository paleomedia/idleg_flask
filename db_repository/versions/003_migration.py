from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
post = Table('post', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('body', VARCHAR(length=140)),
    Column('timestamp', DATETIME),
    Column('user_id', INTEGER),
)

user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('nickname', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
    Column('party', VARCHAR(length=12)),
    Column('website', VARCHAR(length=64)),
    Column('district_cong', INTEGER),
    Column('district_leg', INTEGER),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=100)),
    Column('pwdhash', String),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['post'].drop()
    pre_meta.tables['user'].columns['district_cong'].drop()
    pre_meta.tables['user'].columns['district_leg'].drop()
    pre_meta.tables['user'].columns['email'].drop()
    pre_meta.tables['user'].columns['nickname'].drop()
    pre_meta.tables['user'].columns['party'].drop()
    pre_meta.tables['user'].columns['website'].drop()
    post_meta.tables['user'].columns['pwdhash'].create()
    post_meta.tables['user'].columns['username'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['post'].create()
    pre_meta.tables['user'].columns['district_cong'].create()
    pre_meta.tables['user'].columns['district_leg'].create()
    pre_meta.tables['user'].columns['email'].create()
    pre_meta.tables['user'].columns['nickname'].create()
    pre_meta.tables['user'].columns['party'].create()
    pre_meta.tables['user'].columns['website'].create()
    post_meta.tables['user'].columns['pwdhash'].drop()
    post_meta.tables['user'].columns['username'].drop()
