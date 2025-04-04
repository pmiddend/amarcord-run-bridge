# coding: utf-8

"""
    AMARCORD OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from amarcord_open.models.json_refinement_result_internal import JsonRefinementResultInternal

class TestJsonRefinementResultInternal(unittest.TestCase):
    """JsonRefinementResultInternal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JsonRefinementResultInternal:
        """Test JsonRefinementResultInternal
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonRefinementResultInternal`
        """
        model = JsonRefinementResultInternal()
        if include_optional:
            return JsonRefinementResultInternal(
                id = 56,
                pdb_file_id = 56,
                mtz_file_id = 56,
                r_free = 1.337,
                r_work = 1.337,
                rms_bond_angle = 1.337,
                rms_bond_length = 1.337
            )
        else:
            return JsonRefinementResultInternal(
                pdb_file_id = 56,
                mtz_file_id = 56,
                r_free = 1.337,
                r_work = 1.337,
                rms_bond_angle = 1.337,
                rms_bond_length = 1.337,
        )
        """

    def testJsonRefinementResultInternal(self):
        """Test JsonRefinementResultInternal"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
