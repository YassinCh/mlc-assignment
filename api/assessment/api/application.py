from fastapi import APIRouter, FastAPI
from starlette.middleware.cors import CORSMiddleware

from .lifespan import lifespan
from .routes.dataset import router as dataset_router
from .routes.dataset_feature import router as dataset_feature_router
from .routes.dataset_parser import router as dataset_parser_routers
from .routes.dataset_product import router as dataset_product_router
from .routes.dataset_value import router as dataset_value_router


def create_application() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    api = APIRouter(prefix="/api")
    api.include_router(dataset_router)
    api.include_router(dataset_feature_router)
    api.include_router(dataset_product_router)
    api.include_router(dataset_value_router)
    api.include_router(dataset_parser_routers)

    app.include_router(api)

    return app
