import os

ENV = os.environ.get("ENV", "dev")

if ENV == "dev":
    from .settings_dev import *

    if os.path.exists("./settings/settings_local.py"):
        from .settings_local import *
elif ENV == "qa":
    from .settings_qa import *
elif ENV == "prod":
    from .settings_prod import *
else:
    raise NotImplementedError()
