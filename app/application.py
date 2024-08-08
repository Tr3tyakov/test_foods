from contextlib import asynccontextmanager
from logging.config import dictConfig

from fastapi import FastAPI

from app.config import settings
from app.controllers import foods
from app.core.context import ApplicationContext
from app.core.database import Database


class Application:
    def __init__(self):
        self.app = FastAPI(lifespan=self.lifespan)
        self.database = Database(settings.POSTGRES)

    @asynccontextmanager
    async def lifespan(self, _):
        self.database._connect()
        yield
        await self.database._close()

    def _init_logger(self) -> None:
        """Инициализация логгера"""
        dictConfig(settings.LOGGING)

    def _init_context(self) -> ApplicationContext:
        """Инициализация контекста сервиса"""
        return ApplicationContext(database=self.database)

    def _add_routers(self) -> None:
        """Добавление роутеров"""
        routers = [foods.router]
        for router in routers:
            self.app.include_router(router)

    def init_app(self) -> FastAPI:
        self._add_routers()
        self._init_logger()
        self.app.extra["context"] = self._init_context()
        return self.app


app = Application().init_app()
