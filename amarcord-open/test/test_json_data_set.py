# coding: utf-8

"""
    AMARCORD OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from amarcord_open.models.json_data_set import JsonDataSet

class TestJsonDataSet(unittest.TestCase):
    """JsonDataSet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JsonDataSet:
        """Test JsonDataSet
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonDataSet`
        """
        model = JsonDataSet()
        if include_optional:
            return JsonDataSet(
                id = 56,
                experiment_type_id = 56,
                beamtime_id = 56,
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
                    ]
            )
        else:
            return JsonDataSet(
                id = 56,
                experiment_type_id = 56,
                beamtime_id = 56,
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
        )
        """

    def testJsonDataSet(self):
        """Test JsonDataSet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
