# coding: utf-8

"""
    AMARCORD OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from amarcord_open.models.json_import_finished_indexing_job_input import JsonImportFinishedIndexingJobInput

class TestJsonImportFinishedIndexingJobInput(unittest.TestCase):
    """JsonImportFinishedIndexingJobInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JsonImportFinishedIndexingJobInput:
        """Test JsonImportFinishedIndexingJobInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonImportFinishedIndexingJobInput`
        """
        model = JsonImportFinishedIndexingJobInput()
        if include_optional:
            return JsonImportFinishedIndexingJobInput(
                is_online = True,
                cell_description = '',
                command_line = '',
                source = '',
                run_internal_id = 56,
                stream_file = '',
                program_version = '',
                frames = 56,
                hits = 56,
                indexed_frames = 56,
                detector_shift_x_mm = 1.337,
                detector_shift_y_mm = 1.337,
                geometry_file = '',
                geometry_hash = '',
                generated_geometry_file = '',
                job_log = ''
            )
        else:
            return JsonImportFinishedIndexingJobInput(
                is_online = True,
                cell_description = '',
                command_line = '',
                source = '',
                run_internal_id = 56,
                stream_file = '',
                program_version = '',
                frames = 56,
                hits = 56,
                indexed_frames = 56,
                geometry_file = '',
                geometry_hash = '',
                job_log = '',
        )
        """

    def testJsonImportFinishedIndexingJobInput(self):
        """Test JsonImportFinishedIndexingJobInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
