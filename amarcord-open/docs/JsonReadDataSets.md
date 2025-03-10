# JsonReadDataSets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_sets** | [**List[JsonDataSet]**](JsonDataSet.md) |  | 
**chemicals** | [**List[JsonChemical]**](JsonChemical.md) |  | 
**attributi** | [**List[JsonAttributo]**](JsonAttributo.md) |  | 
**experiment_types** | [**List[JsonExperimentType]**](JsonExperimentType.md) |  | 

## Example

```python
from openapi_client.models.json_read_data_sets import JsonReadDataSets

# TODO update the JSON string below
json = "{}"
# create an instance of JsonReadDataSets from a JSON string
json_read_data_sets_instance = JsonReadDataSets.from_json(json)
# print the JSON string representation of the object
print(JsonReadDataSets.to_json())

# convert the object into a dict
json_read_data_sets_dict = json_read_data_sets_instance.to_dict()
# create an instance of JsonReadDataSets from a dict
json_read_data_sets_from_dict = JsonReadDataSets.from_dict(json_read_data_sets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


