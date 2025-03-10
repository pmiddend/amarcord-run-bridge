# coding: utf-8

"""
    AMARCORD OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.json_indexing_statistic import JsonIndexingStatistic

class TestJsonIndexingStatistic(unittest.TestCase):
    """JsonIndexingStatistic unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JsonIndexingStatistic:
        """Test JsonIndexingStatistic
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonIndexingStatistic`
        """
        model = JsonIndexingStatistic()
        if include_optional:
            return JsonIndexingStatistic(
                time = 56,
                frames = 56,
                hits = 56,
                indexed = 56,
                crystals = 56
            )
        else:
            return JsonIndexingStatistic(
                time = 56,
                frames = 56,
                hits = 56,
                indexed = 56,
                crystals = 56,
        )
        """

    def testJsonIndexingStatistic(self):
        """Test JsonIndexingStatistic"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
