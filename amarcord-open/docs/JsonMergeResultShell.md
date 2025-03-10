# JsonMergeResultShell


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**one_over_d_centre** | **float** |  | 
**nref** | **int** |  | 
**d_over_a** | **float** |  | 
**min_res** | **float** |  | 
**max_res** | **float** |  | 
**cc** | **float** |  | 
**ccstar** | **float** |  | 
**r_split** | **float** |  | 
**reflections_possible** | **int** |  | 
**completeness** | **float** |  | 
**measurements** | **int** |  | 
**redundancy** | **float** |  | 
**snr** | **float** |  | 
**mean_i** | **float** |  | 

## Example

```python
from openapi_client.models.json_merge_result_shell import JsonMergeResultShell

# TODO update the JSON string below
json = "{}"
# create an instance of JsonMergeResultShell from a JSON string
json_merge_result_shell_instance = JsonMergeResultShell.from_json(json)
# print the JSON string representation of the object
print(JsonMergeResultShell.to_json())

# convert the object into a dict
json_merge_result_shell_dict = json_merge_result_shell_instance.to_dict()
# create an instance of JsonMergeResultShell from a dict
json_merge_result_shell_from_dict = JsonMergeResultShell.from_dict(json_merge_result_shell_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


