# coding: utf-8

"""
    AMARCORD OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from amarcord_open.models.json_create_attributo_input import JsonCreateAttributoInput

class TestJsonCreateAttributoInput(unittest.TestCase):
    """JsonCreateAttributoInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JsonCreateAttributoInput:
        """Test JsonCreateAttributoInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonCreateAttributoInput`
        """
        model = JsonCreateAttributoInput()
        if include_optional:
            return JsonCreateAttributoInput(
                beamtime_id = 56,
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
                    type = 'boolean', )
            )
        else:
            return JsonCreateAttributoInput(
                beamtime_id = 56,
                name = '',
                description = '',
                group = '',
                associated_table = 'run',
        )
        """

    def testJsonCreateAttributoInput(self):
        """Test JsonCreateAttributoInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
