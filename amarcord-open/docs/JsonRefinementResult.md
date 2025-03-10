# JsonRefinementResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**merge_result_id** | **int** |  | 
**pdb_file_id** | **int** |  | 
**mtz_file_id** | **int** |  | 
**r_free** | **float** |  | 
**r_work** | **float** |  | 
**rms_bond_angle** | **float** |  | 
**rms_bond_length** | **float** |  | 

## Example

```python
from openapi_client.models.json_refinement_result import JsonRefinementResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonRefinementResult from a JSON string
json_refinement_result_instance = JsonRefinementResult.from_json(json)
# print the JSON string representation of the object
print(JsonRefinementResult.to_json())

# convert the object into a dict
json_refinement_result_dict = json_refinement_result_instance.to_dict()
# create an instance of JsonRefinementResult from a dict
json_refinement_result_from_dict = JsonRefinementResult.from_dict(json_refinement_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


