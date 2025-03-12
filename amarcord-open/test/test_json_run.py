# coding: utf-8

"""
    AMARCORD OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from amarcord_open.models.json_run import JsonRun

class TestJsonRun(unittest.TestCase):
    """JsonRun unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JsonRun:
        """Test JsonRun
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonRun`
        """
        model = JsonRun()
        if include_optional:
            return JsonRun(
                id = 56,
                external_id = 56,
                attributi = [
                    amarcord_open.models.json_attributo_value.JsonAttributoValue(
                        attributo_id = 56, 
                        attributo_value_str = '', 
                        attributo_value_int = 56, 
                        attributo_value_chemical = 56, 
                        attributo_value_datetime = 56, 
                        attributo_value_float = 1.337, 
                        attributo_value_bool = True, 
                        attributo_value_list_str = [
                            ''
                            ], 
                        attributo_value_list_float = [
                            1.337
                            ], 
                        attributo_value_list_bool = [
                            True
                            ], )
                    ],
                started = 56,
                stopped = 56,
                files = [
                    amarcord_open.models.json_run_file.JsonRunFile(
                        id = 56, 
                        glob = '', 
                        source = '', )
                    ],
                summary = amarcord_open.models.json_indexing_fom.JsonIndexingFom(
                    hit_rate = 1.337, 
                    indexing_rate = 1.337, 
                    indexed_frames = 56, 
                    detector_shift_x_mm = 1.337, 
                    detector_shift_y_mm = 1.337, ),
                experiment_type_id = 56
            )
        else:
            return JsonRun(
                id = 56,
                external_id = 56,
                attributi = [
                    amarcord_open.models.json_attributo_value.JsonAttributoValue(
                        attributo_id = 56, 
                        attributo_value_str = '', 
                        attributo_value_int = 56, 
                        attributo_value_chemical = 56, 
                        attributo_value_datetime = 56, 
                        attributo_value_float = 1.337, 
                        attributo_value_bool = True, 
                        attributo_value_list_str = [
                            ''
                            ], 
                        attributo_value_list_float = [
                            1.337
                            ], 
                        attributo_value_list_bool = [
                            True
                            ], )
                    ],
                started = 56,
                files = [
                    amarcord_open.models.json_run_file.JsonRunFile(
                        id = 56, 
                        glob = '', 
                        source = '', )
                    ],
                summary = amarcord_open.models.json_indexing_fom.JsonIndexingFom(
                    hit_rate = 1.337, 
                    indexing_rate = 1.337, 
                    indexed_frames = 56, 
                    detector_shift_x_mm = 1.337, 
                    detector_shift_y_mm = 1.337, ),
                experiment_type_id = 56,
        )
        """

    def testJsonRun(self):
        """Test JsonRun"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
