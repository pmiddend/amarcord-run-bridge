# coding: utf-8

"""
    AMARCORD OpenAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.5.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from amarcord_open.models.json_data_set_with_indexing_results import JsonDataSetWithIndexingResults

class TestJsonDataSetWithIndexingResults(unittest.TestCase):
    """JsonDataSetWithIndexingResults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JsonDataSetWithIndexingResults:
        """Test JsonDataSetWithIndexingResults
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonDataSetWithIndexingResults`
        """
        model = JsonDataSetWithIndexingResults()
        if include_optional:
            return JsonDataSetWithIndexingResults(
                data_set = amarcord_open.models.json_data_set.JsonDataSet(
                    id = 56, 
                    experiment_type_id = 56, 
                    beamtime_id = 56, 
                    attributi = [
                        amarcord_open.models.json_attributo_value.JsonAttributoValue(
                            attributo_id = 56, 
                            attributo_value_str = '', 
                            attributo_value_int = 56, 
                            attributo_value_chemical = 56, 
                            attributo_value_datetime = 56, 
                            attributo_value_float = 1.337, 
                            attributo_value_bool = True, 
                            attributo_value_list_str = [
                                ''
                                ], 
                            attributo_value_list_float = [
                                1.337
                                ], 
                            attributo_value_list_bool = [
                                True
                                ], )
                        ], ),
                internal_run_ids = [
                    56
                    ],
                runs = [
                    amarcord_open.models.json_run_range.JsonRunRange(
                        run_from = 56, 
                        run_to = 56, )
                    ],
                point_group = '',
                space_group = '',
                cell_description = '',
                indexing_results = [
                    amarcord_open.models.json_indexing_parameters_with_results.JsonIndexingParametersWithResults(
                        parameters = amarcord_open.models.json_indexing_parameters.JsonIndexingParameters(
                            id = 56, 
                            cell_description = '', 
                            is_online = True, 
                            command_line = '', 
                            geometry_file = '', ), 
                        indexing_results = [
                            amarcord_open.models.json_indexing_result.JsonIndexingResult(
                                id = 56, 
                                created = 56, 
                                started = 56, 
                                stopped = 56, 
                                parameters = amarcord_open.models.json_indexing_parameters.JsonIndexingParameters(
                                    id = 56, 
                                    cell_description = '', 
                                    is_online = True, 
                                    command_line = '', 
                                    geometry_file = '', ), 
                                program_version = '', 
                                run_internal_id = 56, 
                                run_external_id = 56, 
                                frames = 56, 
                                hits = 56, 
                                indexed_frames = 56, 
                                indexed_crystals = 56, 
                                status = 'queued', 
                                detector_shift_x_mm = 1.337, 
                                detector_shift_y_mm = 1.337, 
                                geometry_file = '', 
                                geometry_hash = '', 
                                generated_geometry_file = '', 
                                unit_cell_histograms_file_id = 56, 
                                has_error = True, )
                            ], 
                        merge_results = [
                            amarcord_open.models.json_merge_result.JsonMergeResult(
                                id = 56, 
                                created = 56, 
                                runs = [
                                    ''
                                    ], 
                                indexing_result_ids = [
                                    56
                                    ], 
                                state_queued = amarcord_open.models.json_merge_result_state_queued.JsonMergeResultStateQueued(
                                    queued = True, ), 
                                state_error = amarcord_open.models.json_merge_result_state_error.JsonMergeResultStateError(
                                    started = 56, 
                                    stopped = 56, 
                                    error = '', 
                                    latest_log = '', ), 
                                state_running = amarcord_open.models.json_merge_result_state_running.JsonMergeResultStateRunning(
                                    started = 56, 
                                    job_id = 56, 
                                    latest_log = '', ), 
                                state_done = amarcord_open.models.json_merge_result_state_done.JsonMergeResultStateDone(
                                    started = 56, 
                                    stopped = 56, 
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
                                            ], ), ), 
                                parameters = amarcord_open.models.json_merge_parameters.JsonMergeParameters(
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
                                refinement_results = [
                                    amarcord_open.models.json_refinement_result.JsonRefinementResult(
                                        id = 56, 
                                        merge_result_id = 56, 
                                        pdb_file_id = 56, 
                                        mtz_file_id = 56, 
                                        r_free = 1.337, 
                                        r_work = 1.337, 
                                        rms_bond_angle = 1.337, 
                                        rms_bond_length = 1.337, )
                                    ], )
                            ], )
                    ]
            )
        else:
            return JsonDataSetWithIndexingResults(
                data_set = amarcord_open.models.json_data_set.JsonDataSet(
                    id = 56, 
                    experiment_type_id = 56, 
                    beamtime_id = 56, 
                    attributi = [
                        amarcord_open.models.json_attributo_value.JsonAttributoValue(
                            attributo_id = 56, 
                            attributo_value_str = '', 
                            attributo_value_int = 56, 
                            attributo_value_chemical = 56, 
                            attributo_value_datetime = 56, 
                            attributo_value_float = 1.337, 
                            attributo_value_bool = True, 
                            attributo_value_list_str = [
                                ''
                                ], 
                            attributo_value_list_float = [
                                1.337
                                ], 
                            attributo_value_list_bool = [
                                True
                                ], )
                        ], ),
                internal_run_ids = [
                    56
                    ],
                runs = [
                    amarcord_open.models.json_run_range.JsonRunRange(
                        run_from = 56, 
                        run_to = 56, )
                    ],
                point_group = '',
                space_group = '',
                cell_description = '',
                indexing_results = [
                    amarcord_open.models.json_indexing_parameters_with_results.JsonIndexingParametersWithResults(
                        parameters = amarcord_open.models.json_indexing_parameters.JsonIndexingParameters(
                            id = 56, 
                            cell_description = '', 
                            is_online = True, 
                            command_line = '', 
                            geometry_file = '', ), 
                        indexing_results = [
                            amarcord_open.models.json_indexing_result.JsonIndexingResult(
                                id = 56, 
                                created = 56, 
                                started = 56, 
                                stopped = 56, 
                                parameters = amarcord_open.models.json_indexing_parameters.JsonIndexingParameters(
                                    id = 56, 
                                    cell_description = '', 
                                    is_online = True, 
                                    command_line = '', 
                                    geometry_file = '', ), 
                                program_version = '', 
                                run_internal_id = 56, 
                                run_external_id = 56, 
                                frames = 56, 
                                hits = 56, 
                                indexed_frames = 56, 
                                indexed_crystals = 56, 
                                status = 'queued', 
                                detector_shift_x_mm = 1.337, 
                                detector_shift_y_mm = 1.337, 
                                geometry_file = '', 
                                geometry_hash = '', 
                                generated_geometry_file = '', 
                                unit_cell_histograms_file_id = 56, 
                                has_error = True, )
                            ], 
                        merge_results = [
                            amarcord_open.models.json_merge_result.JsonMergeResult(
                                id = 56, 
                                created = 56, 
                                runs = [
                                    ''
                                    ], 
                                indexing_result_ids = [
                                    56
                                    ], 
                                state_queued = amarcord_open.models.json_merge_result_state_queued.JsonMergeResultStateQueued(
                                    queued = True, ), 
                                state_error = amarcord_open.models.json_merge_result_state_error.JsonMergeResultStateError(
                                    started = 56, 
                                    stopped = 56, 
                                    error = '', 
                                    latest_log = '', ), 
                                state_running = amarcord_open.models.json_merge_result_state_running.JsonMergeResultStateRunning(
                                    started = 56, 
                                    job_id = 56, 
                                    latest_log = '', ), 
                                state_done = amarcord_open.models.json_merge_result_state_done.JsonMergeResultStateDone(
                                    started = 56, 
                                    stopped = 56, 
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
                                            ], ), ), 
                                parameters = amarcord_open.models.json_merge_parameters.JsonMergeParameters(
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
                                refinement_results = [
                                    amarcord_open.models.json_refinement_result.JsonRefinementResult(
                                        id = 56, 
                                        merge_result_id = 56, 
                                        pdb_file_id = 56, 
                                        mtz_file_id = 56, 
                                        r_free = 1.337, 
                                        r_work = 1.337, 
                                        rms_bond_angle = 1.337, 
                                        rms_bond_length = 1.337, )
                                    ], )
                            ], )
                    ],
        )
        """

    def testJsonDataSetWithIndexingResults(self):
        """Test JsonDataSetWithIndexingResults"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
