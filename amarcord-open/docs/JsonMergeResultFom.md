# JsonMergeResultFom


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snr** | **float** |  | 
**wilson** | **float** |  | [optional] 
**ln_k** | **float** |  | [optional] 
**discarded_reflections** | **int** |  | 
**one_over_d_from** | **float** |  | 
**one_over_d_to** | **float** |  | 
**redundancy** | **float** |  | 
**completeness** | **float** |  | 
**measurements_total** | **int** |  | 
**reflections_total** | **int** |  | 
**reflections_possible** | **int** |  | 
**r_split** | **float** |  | 
**r1i** | **float** |  | 
**r2** | **float** |  | 
**cc** | **float** |  | 
**ccstar** | **float** |  | 
**ccano** | **float** |  | [optional] 
**crdano** | **float** |  | [optional] 
**rano** | **float** |  | [optional] 
**rano_over_r_split** | **float** |  | [optional] 
**d1sig** | **float** |  | 
**d2sig** | **float** |  | 
**outer_shell** | [**JsonMergeResultOuterShell**](JsonMergeResultOuterShell.md) |  | 

## Example

```python
from openapi_client.models.json_merge_result_fom import JsonMergeResultFom

# TODO update the JSON string below
json = "{}"
# create an instance of JsonMergeResultFom from a JSON string
json_merge_result_fom_instance = JsonMergeResultFom.from_json(json)
# print the JSON string representation of the object
print(JsonMergeResultFom.to_json())

# convert the object into a dict
json_merge_result_fom_dict = json_merge_result_fom_instance.to_dict()
# create an instance of JsonMergeResultFom from a dict
json_merge_result_fom_from_dict = JsonMergeResultFom.from_dict(json_merge_result_fom_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


