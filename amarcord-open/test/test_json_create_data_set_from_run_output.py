# coding: utf-8

"""
    AMARCORD OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.json_create_data_set_from_run_output import JsonCreateDataSetFromRunOutput

class TestJsonCreateDataSetFromRunOutput(unittest.TestCase):
    """JsonCreateDataSetFromRunOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JsonCreateDataSetFromRunOutput:
        """Test JsonCreateDataSetFromRunOutput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonCreateDataSetFromRunOutput`
        """
        model = JsonCreateDataSetFromRunOutput()
        if include_optional:
            return JsonCreateDataSetFromRunOutput(
                data_set_id = 56
            )
        else:
            return JsonCreateDataSetFromRunOutput(
                data_set_id = 56,
        )
        """

    def testJsonCreateDataSetFromRunOutput(self):
        """Test JsonCreateDataSetFromRunOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
