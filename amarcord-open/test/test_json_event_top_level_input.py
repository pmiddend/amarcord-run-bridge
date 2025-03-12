# coding: utf-8

"""
    AMARCORD OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from amarcord_open.models.json_event_top_level_input import JsonEventTopLevelInput

class TestJsonEventTopLevelInput(unittest.TestCase):
    """JsonEventTopLevelInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JsonEventTopLevelInput:
        """Test JsonEventTopLevelInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonEventTopLevelInput`
        """
        model = JsonEventTopLevelInput()
        if include_optional:
            return JsonEventTopLevelInput(
                beamtime_id = 56,
                event = amarcord_open.models.json_event_input.JsonEventInput(
                    source = '', 
                    text = '', 
                    level = '', 
                    file_ids = [
                        56
                        ], ),
                with_live_stream = True
            )
        else:
            return JsonEventTopLevelInput(
                beamtime_id = 56,
                event = amarcord_open.models.json_event_input.JsonEventInput(
                    source = '', 
                    text = '', 
                    level = '', 
                    file_ids = [
                        56
                        ], ),
                with_live_stream = True,
        )
        """

    def testJsonEventTopLevelInput(self):
        """Test JsonEventTopLevelInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
