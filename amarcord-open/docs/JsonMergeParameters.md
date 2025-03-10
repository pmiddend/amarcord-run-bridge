# JsonMergeParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**point_group** | **str** |  | 
**space_group** | **str** |  | [optional] 
**cell_description** | **str** |  | 
**negative_handling** | [**MergeNegativeHandling**](MergeNegativeHandling.md) |  | [optional] 
**merge_model** | [**MergeModel**](MergeModel.md) |  | 
**scale_intensities** | [**ScaleIntensities**](ScaleIntensities.md) |  | 
**post_refinement** | **bool** |  | 
**iterations** | **int** |  | 
**polarisation** | [**JsonPolarisation**](JsonPolarisation.md) |  | [optional] 
**start_after** | **int** |  | [optional] 
**stop_after** | **int** |  | [optional] 
**rel_b** | **float** |  | 
**no_pr** | **bool** |  | 
**force_bandwidth** | **float** |  | [optional] 
**force_radius** | **float** |  | [optional] 
**force_lambda** | **float** |  | [optional] 
**no_delta_cc_half** | **bool** |  | 
**max_adu** | **float** |  | [optional] 
**min_measurements** | **int** |  | 
**logs** | **bool** |  | 
**min_res** | **float** |  | [optional] 
**push_res** | **float** |  | [optional] 
**w** | **str** |  | [optional] 
**ambigator_command_line** | **str** |  | 

## Example

```python
from openapi_client.models.json_merge_parameters import JsonMergeParameters

# TODO update the JSON string below
json = "{}"
# create an instance of JsonMergeParameters from a JSON string
json_merge_parameters_instance = JsonMergeParameters.from_json(json)
# print the JSON string representation of the object
print(JsonMergeParameters.to_json())

# convert the object into a dict
json_merge_parameters_dict = json_merge_parameters_instance.to_dict()
# create an instance of JsonMergeParameters from a dict
json_merge_parameters_from_dict = JsonMergeParameters.from_dict(json_merge_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


