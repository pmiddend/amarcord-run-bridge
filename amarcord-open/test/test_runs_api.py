# coding: utf-8

"""
    AMARCORD OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from amarcord_open.api.runs_api import RunsApi


class TestRunsApi(unittest.IsolatedAsyncioTestCase):
    """RunsApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = RunsApi()

    async def asyncTearDown(self) -> None:
        await self.api.api_client.close()

    async def test_bulk_import_api_run_bulk_import_beamtime_id_post(self) -> None:
        """Test case for bulk_import_api_run_bulk_import_beamtime_id_post

        Bulk Import
        """
        pass

    async def test_bulk_import_info_api_run_bulk_import_beamtime_id_get(self) -> None:
        """Test case for bulk_import_info_api_run_bulk_import_beamtime_id_get

        Bulk Import Info
        """
        pass

    async def test_create_or_update_run_api_runs_run_external_id_post(self) -> None:
        """Test case for create_or_update_run_api_runs_run_external_id_post

        Create Or Update Run
        """
        pass

    async def test_delete_run_api_runs_beamtime_id_run_id_delete(self) -> None:
        """Test case for delete_run_api_runs_beamtime_id_run_id_delete

        Delete Run
        """
        pass

    async def test_read_runs_api_runs_beamtime_id_get(self) -> None:
        """Test case for read_runs_api_runs_beamtime_id_get

        Read Runs
        """
        pass

    async def test_read_runs_bulk_api_runs_bulk_post(self) -> None:
        """Test case for read_runs_bulk_api_runs_bulk_post

        Read Runs Bulk
        """
        pass

    async def test_read_runs_overview_api_runs_overview_beamtime_id_get(self) -> None:
        """Test case for read_runs_overview_api_runs_overview_beamtime_id_get

        Read Runs Overview
        """
        pass

    async def test_start_run_api_runs_run_external_id_start_beamtime_id_get(self) -> None:
        """Test case for start_run_api_runs_run_external_id_start_beamtime_id_get

        Start Run
        """
        pass

    async def test_stop_latest_run_api_runs_stop_latest_beamtime_id_get(self) -> None:
        """Test case for stop_latest_run_api_runs_stop_latest_beamtime_id_get

        Stop Latest Run
        """
        pass

    async def test_update_run_api_runs_patch(self) -> None:
        """Test case for update_run_api_runs_patch

        Update Run
        """
        pass

    async def test_update_runs_bulk_api_runs_bulk_patch(self) -> None:
        """Test case for update_runs_bulk_api_runs_bulk_patch

        Update Runs Bulk
        """
        pass


if __name__ == '__main__':
    unittest.main()
