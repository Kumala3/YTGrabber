"""Import all routers and add them to routers_list."""
from .admin import admin_router
from .user import user_router
from .video import video_router

routers_list = [
    admin_router,
    video_router,
    user_router,
]

__all__ = [
    "routers_list",
]
