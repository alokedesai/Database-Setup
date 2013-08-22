from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
reply = Table('reply', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('reply', Text),
    Column('user_id', Integer),
    Column('conversation_id', Integer),
)

conversation = Table('conversation', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('user1_id', Integer),
    Column('user2_id', Integer),
)

conversation = Table('conversation', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('user_id', Integer),
    Column('user2_id', Integer),
    Column('extra_data', String(length=50)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['reply'].drop()
    pre_meta.tables['conversation'].columns['user1_id'].drop()
    post_meta.tables['conversation'].columns['extra_data'].create()
    post_meta.tables['conversation'].columns['user_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['reply'].create()
    pre_meta.tables['conversation'].columns['user1_id'].create()
    post_meta.tables['conversation'].columns['extra_data'].drop()
    post_meta.tables['conversation'].columns['user_id'].drop()
