# JsonDataSetWithFom


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_set** | [**JsonDataSet**](JsonDataSet.md) |  | 
**fom** | [**JsonIndexingFom**](JsonIndexingFom.md) |  | 

## Example

```python
from openapi_client.models.json_data_set_with_fom import JsonDataSetWithFom

# TODO update the JSON string below
json = "{}"
# create an instance of JsonDataSetWithFom from a JSON string
json_data_set_with_fom_instance = JsonDataSetWithFom.from_json(json)
# print the JSON string representation of the object
print(JsonDataSetWithFom.to_json())

# convert the object into a dict
json_data_set_with_fom_dict = json_data_set_with_fom_instance.to_dict()
# create an instance of JsonDataSetWithFom from a dict
json_data_set_with_fom_from_dict = JsonDataSetWithFom.from_dict(json_data_set_with_fom_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


