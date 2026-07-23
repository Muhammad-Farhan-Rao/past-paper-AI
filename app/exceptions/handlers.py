from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(FileNotFoundError)
    async def file_not_found_handler(
        request: Request,
        exc: FileNotFoundError
    ):
        return JSONResponse(
            status_code=404,
            content={
                "error": str(exc)
            }
        )

    @app.exception_handler(ValueError)
    async def value_error_handler(
        request: Request,
        exc: ValueError
    ):
        return JSONResponse(
            status_code=400,
            content={
                "error": str(exc)
            }
        )