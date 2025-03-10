import asyncio
from dataclasses import dataclass
import datetime
from enum import Enum
import json
from pathlib import Path
from statistics import mean
from typing import TypeAlias

from pydantic import BaseModel
import structlog
import openapi_client
from run_bridge.logging_util import setup_structlog

setup_structlog()
logger = structlog.stdlib.get_logger(__name__)

class Config(BaseModel):
    attributi: list[AttributoDescription]
