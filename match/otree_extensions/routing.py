from channels.routing import route_class
from .consumers import WPTracker

channel_routing = [
    route_class(WPTracker, path=WPTracker.url_pattern),
]
