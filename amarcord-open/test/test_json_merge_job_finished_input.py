# coding: utf-8

"""
    AMARCORD OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from amarcord_open.models.json_merge_job_finished_input import JsonMergeJobFinishedInput

class TestJsonMergeJobFinishedInput(unittest.TestCase):
    """JsonMergeJobFinishedInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JsonMergeJobFinishedInput:
        """Test JsonMergeJobFinishedInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonMergeJobFinishedInput`
        """
        model = JsonMergeJobFinishedInput()
        if include_optional:
            return JsonMergeJobFinishedInput(
                latest_log = '',
                error = '',
                result = amarcord_open.models.json_merge_result_internal.JsonMergeResultInternal(
                    mtz_file_id = 56, 
                    fom = amarcord_open.models.json_merge_result_fom.JsonMergeResultFom(
                        snr = 1.337, 
                        wilson = 1.337, 
                        ln_k = 1.337, 
                        discarded_reflections = 56, 
                        one_over_d_from = 1.337, 
                        one_over_d_to = 1.337, 
                        redundancy = 1.337, 
                        completeness = 1.337, 
                        measurements_total = 56, 
                        reflections_total = 56, 
                        reflections_possible = 56, 
                        r_split = 1.337, 
                        r1i = 1.337, 
                        r2 = 1.337, 
                        cc = 1.337, 
                        ccstar = 1.337, 
                        ccano = 1.337, 
                        crdano = 1.337, 
                        rano = 1.337, 
                        rano_over_r_split = 1.337, 
                        d1sig = 1.337, 
                        d2sig = 1.337, 
                        outer_shell = amarcord_open.models.json_merge_result_outer_shell.JsonMergeResultOuterShell(
                            resolution = 1.337, 
                            ccstar = 1.337, 
                            r_split = 1.337, 
                            cc = 1.337, 
                            unique_reflections = 56, 
                            completeness = 1.337, 
                            redundancy = 1.337, 
                            snr = 1.337, 
                            min_res = 1.337, 
                            max_res = 1.337, ), ), 
                    ambigator_fg_graph_file_id = 56, 
                    detailed_foms = [
                        amarcord_open.models.json_merge_result_shell.JsonMergeResultShell(
                            one_over_d_centre = 1.337, 
                            nref = 56, 
                            d_over_a = 1.337, 
                            min_res = 1.337, 
                            max_res = 1.337, 
                            cc = 1.337, 
                            ccstar = 1.337, 
                            r_split = 1.337, 
                            reflections_possible = 56, 
                            completeness = 1.337, 
                            measurements = 56, 
                            redundancy = 1.337, 
                            snr = 1.337, 
                            mean_i = 1.337, )
                        ], 
                    refinement_results = [
                        amarcord_open.models.json_refinement_result_internal.JsonRefinementResultInternal(
                            id = 56, 
                            pdb_file_id = 56, 
                            mtz_file_id = 56, 
                            r_free = 1.337, 
                            r_work = 1.337, 
                            rms_bond_angle = 1.337, 
                            rms_bond_length = 1.337, )
                        ], )
            )
        else:
            return JsonMergeJobFinishedInput(
        )
        """

    def testJsonMergeJobFinishedInput(self):
        """Test JsonMergeJobFinishedInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
