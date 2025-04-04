# coding: utf-8

"""
    AMARCORD OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from amarcord_open.api.attributi_api import AttributiApi


class TestAttributiApi(unittest.IsolatedAsyncioTestCase):
    """AttributiApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = AttributiApi()

    async def asyncTearDown(self) -> None:
        await self.api.api_client.close()

    async def test_create_attributi_from_schema_api_attributi_schema_post(self) -> None:
        """Test case for create_attributi_from_schema_api_attributi_schema_post

        Create Attributi From Schema
        """
        pass

    async def test_create_attributo_api_attributi_post(self) -> None:
        """Test case for create_attributo_api_attributi_post

        Create Attributo
        """
        pass

    async def test_delete_attributo_api_attributi_delete(self) -> None:
        """Test case for delete_attributo_api_attributi_delete

        Delete Attributo
        """
        pass

    async def test_read_attributi_api_attributi_beamtime_id_get(self) -> None:
        """Test case for read_attributi_api_attributi_beamtime_id_get

        Read Attributi
        """
        pass

    async def test_update_attributo_api_attributi_patch(self) -> None:
        """Test case for update_attributo_api_attributi_patch

        Update Attributo
        """
        pass


if __name__ == '__main__':
    unittest.main()
