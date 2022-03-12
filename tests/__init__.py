from flarum_migrations import fm_create_engine
from flarum_migrations.migrations.flarum import ALL_FLARUM_MODELS


ENGINE = fm_create_engine(ALL_FLARUM_MODELS, 'sqlite:///tests/test.db')
