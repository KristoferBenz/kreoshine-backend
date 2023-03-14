"""
API implementation of /services endpoint
"""
import json
import logging

from aiohttp.web_response import Response
from aiohttp.web_routedef import Request
from aiohttp.web_urldispatcher import View

from service.api import const

logger = logging.getLogger('app')


class ServicesEndpoint(View):
    """
    View of a 'services' service
    """

    async def get(self) -> Response:
        return await self._process_get(self.request)

    # todo: make decorator for errors
    async def _process_get(self, request: Request) -> Response:

        response_dict = {
            const.STATUS_CODE: 200,
            const.FAILED_FLAG: False,
            const.BODY: {}  # todo: fill body and select status code if needed
        }
        return Response(body=json.dumps(response_dict), content_type="application/json")
