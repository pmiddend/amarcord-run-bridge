# coding: utf-8

"""
    AMARCORD OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from amarcord_open.api.default_api import DefaultApi


class TestDefaultApi(unittest.IsolatedAsyncioTestCase):
    """DefaultApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = DefaultApi()

    async def asyncTearDown(self) -> None:
        await self.api.api_client.close()

    async def test_check_standard_unit_api_unit_post(self) -> None:
        """Test case for check_standard_unit_api_unit_post

        Check Standard Unit
        """
        pass

    async def test_update_live_stream_api_live_stream_beamtime_id_post(self) -> None:
        """Test case for update_live_stream_api_live_stream_beamtime_id_post

        Update Live Stream
        """
        pass


if __name__ == '__main__':
    unittest.main()
