# coding: utf-8

"""
    AMARCORD OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from amarcord_open.models.json_read_all_chemicals import JsonReadAllChemicals

class TestJsonReadAllChemicals(unittest.TestCase):
    """JsonReadAllChemicals unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JsonReadAllChemicals:
        """Test JsonReadAllChemicals
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonReadAllChemicals`
        """
        model = JsonReadAllChemicals()
        if include_optional:
            return JsonReadAllChemicals(
                chemicals = [
                    amarcord_open.models.json_chemical.JsonChemical(
                        id = 56, 
                        beamtime_id = 56, 
                        name = '', 
                        responsible_person = '', 
                        chemical_type = 'crystal', 
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
                        files = [
                            amarcord_open.models.json_file_output.JsonFileOutput(
                                id = 56, 
                                description = '', 
                                type_ = '', 
                                original_path = '', 
                                file_name = '', 
                                size_in_bytes = 56, )
                            ], )
                    ],
                beamtimes = [
                    amarcord_open.models.json_beamtime.JsonBeamtime(
                        id = 56, 
                        external_id = '', 
                        proposal = '', 
                        beamline = '', 
                        title = '', 
                        comment = '', 
                        start = 56, 
                        end = 56, 
                        chemical_names = [
                            ''
                            ], 
                        analysis_output_path = '', )
                    ],
                attributi_names = [
                    amarcord_open.models.json_attributo_with_name.JsonAttributoWithName(
                        id = 56, 
                        name = '', )
                    ]
            )
        else:
            return JsonReadAllChemicals(
                chemicals = [
                    amarcord_open.models.json_chemical.JsonChemical(
                        id = 56, 
                        beamtime_id = 56, 
                        name = '', 
                        responsible_person = '', 
                        chemical_type = 'crystal', 
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
                        files = [
                            amarcord_open.models.json_file_output.JsonFileOutput(
                                id = 56, 
                                description = '', 
                                type_ = '', 
                                original_path = '', 
                                file_name = '', 
                                size_in_bytes = 56, )
                            ], )
                    ],
                beamtimes = [
                    amarcord_open.models.json_beamtime.JsonBeamtime(
                        id = 56, 
                        external_id = '', 
                        proposal = '', 
                        beamline = '', 
                        title = '', 
                        comment = '', 
                        start = 56, 
                        end = 56, 
                        chemical_names = [
                            ''
                            ], 
                        analysis_output_path = '', )
                    ],
                attributi_names = [
                    amarcord_open.models.json_attributo_with_name.JsonAttributoWithName(
                        id = 56, 
                        name = '', )
                    ],
        )
        """

    def testJsonReadAllChemicals(self):
        """Test JsonReadAllChemicals"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
