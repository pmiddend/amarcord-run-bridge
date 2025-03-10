# JsonIndexingFom


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hit_rate** | **float** |  | 
**indexing_rate** | **float** |  | 
**indexed_frames** | **int** |  | 
**detector_shift_x_mm** | **float** |  | [optional] 
**detector_shift_y_mm** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.json_indexing_fom import JsonIndexingFom

# TODO update the JSON string below
json = "{}"
# create an instance of JsonIndexingFom from a JSON string
json_indexing_fom_instance = JsonIndexingFom.from_json(json)
# print the JSON string representation of the object
print(JsonIndexingFom.to_json())

# convert the object into a dict
json_indexing_fom_dict = json_indexing_fom_instance.to_dict()
# create an instance of JsonIndexingFom from a dict
json_indexing_fom_from_dict = JsonIndexingFom.from_dict(json_indexing_fom_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


