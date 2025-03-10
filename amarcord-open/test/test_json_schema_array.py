# coding: utf-8

"""
    AMARCORD OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.json_schema_array import JSONSchemaArray

class TestJSONSchemaArray(unittest.TestCase):
    """JSONSchemaArray unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JSONSchemaArray:
        """Test JSONSchemaArray
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JSONSchemaArray`
        """
        model = JSONSchemaArray()
        if include_optional:
            return JSONSchemaArray(
                type = 'array',
                item_type = 'string',
                min_items = 56,
                max_items = 56
            )
        else:
            return JSONSchemaArray(
                type = 'array',
                item_type = 'string',
        )
        """

    def testJSONSchemaArray(self):
        """Test JSONSchemaArray"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
