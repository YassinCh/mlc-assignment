from fastapi import APIRouter, FastAPI
from starlette.middleware.cors import CORSMiddleware

from assessment.api.fastapi.lifespan import lifespan
from assessment.dataset.routes import router as dataset_router
from assessment.dataset_feature.routes import router as dataset_feature_router
from assessment.dataset_product.routes import router as dataset_product_router
from assessment.dataset_value.routes import router as dataset_value_router
from assessment.dataset_parser.routes import router as dataset_parser_routers


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
