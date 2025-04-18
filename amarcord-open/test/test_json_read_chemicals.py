# coding: utf-8

"""
    AMARCORD OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from amarcord_open.models.json_read_chemicals import JsonReadChemicals

class TestJsonReadChemicals(unittest.TestCase):
    """JsonReadChemicals unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JsonReadChemicals:
        """Test JsonReadChemicals
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonReadChemicals`
        """
        model = JsonReadChemicals()
        if include_optional:
            return JsonReadChemicals(
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
                attributi = [
                    amarcord_open.models.json_attributo.JsonAttributo(
                        id = 56, 
                        name = '', 
                        description = '', 
                        group = '', 
                        associated_table = 'run', 
                        attributo_type_integer = amarcord_open.models.json_schema_integer.JSONSchemaInteger(
                            type = 'integer', 
                            format = 'date-time', ), 
                        attributo_type_number = amarcord_open.models.json_schema_number.JSONSchemaNumber(
                            type = 'number', 
                            minimum = 1.337, 
                            maximum = 1.337, 
                            exclusive_minimum = 1.337, 
                            exclusive_maximum = 1.337, 
                            suffix = '', 
                            format = 'standard-unit', 
                            tolerance = 1.337, 
                            tolerance_is_absolute = True, ), 
                        attributo_type_string = amarcord_open.models.json_schema_string.JSONSchemaString(
                            type = 'string', 
                            enum = [
                                ''
                                ], ), 
                        attributo_type_array = amarcord_open.models.json_schema_array.JSONSchemaArray(
                            type = 'array', 
                            item_type = 'string', 
                            min_items = 56, 
                            max_items = 56, ), 
                        attributo_type_boolean = amarcord_open.models.json_schema_boolean.JSONSchemaBoolean(
                            type = 'boolean', ), )
                    ]
            )
        else:
            return JsonReadChemicals(
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
                attributi = [
                    amarcord_open.models.json_attributo.JsonAttributo(
                        id = 56, 
                        name = '', 
                        description = '', 
                        group = '', 
                        associated_table = 'run', 
                        attributo_type_integer = amarcord_open.models.json_schema_integer.JSONSchemaInteger(
                            type = 'integer', 
                            format = 'date-time', ), 
                        attributo_type_number = amarcord_open.models.json_schema_number.JSONSchemaNumber(
                            type = 'number', 
                            minimum = 1.337, 
                            maximum = 1.337, 
                            exclusive_minimum = 1.337, 
                            exclusive_maximum = 1.337, 
                            suffix = '', 
                            format = 'standard-unit', 
                            tolerance = 1.337, 
                            tolerance_is_absolute = True, ), 
                        attributo_type_string = amarcord_open.models.json_schema_string.JSONSchemaString(
                            type = 'string', 
                            enum = [
                                ''
                                ], ), 
                        attributo_type_array = amarcord_open.models.json_schema_array.JSONSchemaArray(
                            type = 'array', 
                            item_type = 'string', 
                            min_items = 56, 
                            max_items = 56, ), 
                        attributo_type_boolean = amarcord_open.models.json_schema_boolean.JSONSchemaBoolean(
                            type = 'boolean', ), )
                    ],
        )
        """

    def testJsonReadChemicals(self):
        """Test JsonReadChemicals"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
