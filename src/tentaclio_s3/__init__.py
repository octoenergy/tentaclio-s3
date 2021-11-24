"""This package implements the tentaclio s3 client """
from tentaclio import *  # noqa

from .clients.s3_client import ClientClassName


# Add DB registry
DB_REGISTRY.register("s3", ClientClassName)  # type: ignore
