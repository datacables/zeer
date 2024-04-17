from apis.browse import blueprint as browse_blueprint
from apis.search import blueprint as search_blueprint
from apis.webhook import blueprint as webhook_blueprint
from apis.index import blueprint as index_blueprint

blueprints = [
    (browse_blueprint, "/browse"),
    (search_blueprint, "/search"),
    (webhook_blueprint, "/webhook"),
    (index_blueprint, "/"),
]
