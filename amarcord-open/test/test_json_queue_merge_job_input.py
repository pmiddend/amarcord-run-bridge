# coding: utf-8

"""
    AMARCORD OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from amarcord_open.models.json_queue_merge_job_input import JsonQueueMergeJobInput

class TestJsonQueueMergeJobInput(unittest.TestCase):
    """JsonQueueMergeJobInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JsonQueueMergeJobInput:
        """Test JsonQueueMergeJobInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonQueueMergeJobInput`
        """
        model = JsonQueueMergeJobInput()
        if include_optional:
            return JsonQueueMergeJobInput(
                strict_mode = True,
                indexing_parameters_id = 56,
                data_set_id = 56,
                merge_parameters = amarcord_open.models.json_merge_parameters.JsonMergeParameters(
                    point_group = '', 
                    space_group = '', 
                    cell_description = '', 
                    negative_handling = 'ignore', 
                    merge_model = 'unity', 
                    scale_intensities = 'off', 
                    post_refinement = True, 
                    iterations = 56, 
                    polarisation = amarcord_open.models.json_polarisation.JsonPolarisation(
                        angle = 56, 
                        percent = 56, ), 
                    start_after = 56, 
                    stop_after = 56, 
                    rel_b = 1.337, 
                    no_pr = True, 
                    force_bandwidth = 1.337, 
                    force_radius = 1.337, 
                    force_lambda = 1.337, 
                    no_delta_cc_half = True, 
                    max_adu = 1.337, 
                    min_measurements = 56, 
                    logs = True, 
                    min_res = 1.337, 
                    push_res = 1.337, 
                    w = '', 
                    ambigator_command_line = '', )
            )
        else:
            return JsonQueueMergeJobInput(
                strict_mode = True,
                indexing_parameters_id = 56,
                data_set_id = 56,
                merge_parameters = amarcord_open.models.json_merge_parameters.JsonMergeParameters(
                    point_group = '', 
                    space_group = '', 
                    cell_description = '', 
                    negative_handling = 'ignore', 
                    merge_model = 'unity', 
                    scale_intensities = 'off', 
                    post_refinement = True, 
                    iterations = 56, 
                    polarisation = amarcord_open.models.json_polarisation.JsonPolarisation(
                        angle = 56, 
                        percent = 56, ), 
                    start_after = 56, 
                    stop_after = 56, 
                    rel_b = 1.337, 
                    no_pr = True, 
                    force_bandwidth = 1.337, 
                    force_radius = 1.337, 
                    force_lambda = 1.337, 
                    no_delta_cc_half = True, 
                    max_adu = 1.337, 
                    min_measurements = 56, 
                    logs = True, 
                    min_res = 1.337, 
                    push_res = 1.337, 
                    w = '', 
                    ambigator_command_line = '', ),
        )
        """

    def testJsonQueueMergeJobInput(self):
        """Test JsonQueueMergeJobInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
