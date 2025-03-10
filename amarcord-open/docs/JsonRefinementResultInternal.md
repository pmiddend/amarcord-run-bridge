# JsonRefinementResultInternal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**pdb_file_id** | **int** |  | 
**mtz_file_id** | **int** |  | 
**r_free** | **float** |  | 
**r_work** | **float** |  | 
**rms_bond_angle** | **float** |  | 
**rms_bond_length** | **float** |  | 

## Example

```python
from openapi_client.models.json_refinement_result_internal import JsonRefinementResultInternal

# TODO update the JSON string below
json = "{}"
# create an instance of JsonRefinementResultInternal from a JSON string
json_refinement_result_internal_instance = JsonRefinementResultInternal.from_json(json)
# print the JSON string representation of the object
print(JsonRefinementResultInternal.to_json())

# convert the object into a dict
json_refinement_result_internal_dict = json_refinement_result_internal_instance.to_dict()
# create an instance of JsonRefinementResultInternal from a dict
json_refinement_result_internal_from_dict = JsonRefinementResultInternal.from_dict(json_refinement_result_internal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


