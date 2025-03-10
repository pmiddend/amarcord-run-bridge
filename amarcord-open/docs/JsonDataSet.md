# JsonDataSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**experiment_type_id** | **int** |  | 
**beamtime_id** | **int** |  | 
**attributi** | [**List[JsonAttributoValue]**](JsonAttributoValue.md) |  | 

## Example

```python
from openapi_client.models.json_data_set import JsonDataSet

# TODO update the JSON string below
json = "{}"
# create an instance of JsonDataSet from a JSON string
json_data_set_instance = JsonDataSet.from_json(json)
# print the JSON string representation of the object
print(JsonDataSet.to_json())

# convert the object into a dict
json_data_set_dict = json_data_set_instance.to_dict()
# create an instance of JsonDataSet from a dict
json_data_set_from_dict = JsonDataSet.from_dict(json_data_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


