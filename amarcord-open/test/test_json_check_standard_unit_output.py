# coding: utf-8

"""
    AMARCORD OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.json_check_standard_unit_output import JsonCheckStandardUnitOutput

class TestJsonCheckStandardUnitOutput(unittest.TestCase):
    """JsonCheckStandardUnitOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JsonCheckStandardUnitOutput:
        """Test JsonCheckStandardUnitOutput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonCheckStandardUnitOutput`
        """
        model = JsonCheckStandardUnitOutput()
        if include_optional:
            return JsonCheckStandardUnitOutput(
                input = '',
                error = '',
                normalized = ''
            )
        else:
            return JsonCheckStandardUnitOutput(
                input = '',
        )
        """

    def testJsonCheckStandardUnitOutput(self):
        """Test JsonCheckStandardUnitOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
