# JsonMergeResultInternal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mtz_file_id** | **int** |  | 
**fom** | [**JsonMergeResultFom**](JsonMergeResultFom.md) |  | 
**ambigator_fg_graph_file_id** | **int** |  | [optional] 
**detailed_foms** | [**List[JsonMergeResultShell]**](JsonMergeResultShell.md) |  | 
**refinement_results** | [**List[JsonRefinementResultInternal]**](JsonRefinementResultInternal.md) |  | 

## Example

```python
from openapi_client.models.json_merge_result_internal import JsonMergeResultInternal

# TODO update the JSON string below
json = "{}"
# create an instance of JsonMergeResultInternal from a JSON string
json_merge_result_internal_instance = JsonMergeResultInternal.from_json(json)
# print the JSON string representation of the object
print(JsonMergeResultInternal.to_json())

# convert the object into a dict
json_merge_result_internal_dict = json_merge_result_internal_instance.to_dict()
# create an instance of JsonMergeResultInternal from a dict
json_merge_result_internal_from_dict = JsonMergeResultInternal.from_dict(json_merge_result_internal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


