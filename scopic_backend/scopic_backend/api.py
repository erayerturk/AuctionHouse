import os

from ninja import NinjaAPI


from backend.api import router as backend_router


secret = os.environ.get("SECRET_KEY")

api = NinjaAPI()

api.add_router('be/', backend_router, tags=["backend"])
