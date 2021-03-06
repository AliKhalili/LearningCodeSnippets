import time

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

from data.database import SessionLocal


class SetDbMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        response = Response("Internal Server Error", status_code=500)
        try:
            request.state.db = SessionLocal()
            response = await call_next(request)
        finally:
            request.state.db.close()
        return response


class MetricsMiddleware(BaseHTTPMiddleware):
    @staticmethod
    def get_path_template(request: Request) -> str:
        if hasattr(request, "path"):
            return ",".join(request.path.split("/")[1:4])
        return ".".join(request.url.path.split("/")[1:4])

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        path_template = MetricsMiddleware.get_path_template(request)

        # exclude non api requests e.g. static content
        if "api" not in path_template:
            return await call_next(request)

        method = request.method
        tags = {"method": method, "endpoint": path_template}

        try:
            start = time.perf_counter()
            response = await call_next(request)
            elapsed_time = time.perf_counter() - start
        except Exception as e:
            raise e from None
        else:
            tags.update({"status_code": response.status_code})
            response.headers["X-Process-Time"] = str(elapsed_time)

        return response
