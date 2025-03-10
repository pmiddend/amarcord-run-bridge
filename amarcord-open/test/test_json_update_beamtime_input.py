# coding: utf-8

"""
    AMARCORD OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.json_update_beamtime_input import JsonUpdateBeamtimeInput

class TestJsonUpdateBeamtimeInput(unittest.TestCase):
    """JsonUpdateBeamtimeInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JsonUpdateBeamtimeInput:
        """Test JsonUpdateBeamtimeInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonUpdateBeamtimeInput`
        """
        model = JsonUpdateBeamtimeInput()
        if include_optional:
            return JsonUpdateBeamtimeInput(
                id = 56,
                external_id = '',
                beamline = '',
                proposal = '',
                title = '',
                comment = '',
                start = 56,
                end = 56,
                analysis_output_path = ''
            )
        else:
            return JsonUpdateBeamtimeInput(
                id = 56,
                external_id = '',
                beamline = '',
                proposal = '',
                title = '',
                comment = '',
                start = 56,
                end = 56,
                analysis_output_path = '',
        )
        """

    def testJsonUpdateBeamtimeInput(self):
        """Test JsonUpdateBeamtimeInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
