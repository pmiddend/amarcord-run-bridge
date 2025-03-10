# JsonExperimentType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**attributi** | [**List[JsonAttributiIdAndRole]**](JsonAttributiIdAndRole.md) |  | 

## Example

```python
from openapi_client.models.json_experiment_type import JsonExperimentType

# TODO update the JSON string below
json = "{}"
# create an instance of JsonExperimentType from a JSON string
json_experiment_type_instance = JsonExperimentType.from_json(json)
# print the JSON string representation of the object
print(JsonExperimentType.to_json())

# convert the object into a dict
json_experiment_type_dict = json_experiment_type_instance.to_dict()
# create an instance of JsonExperimentType from a dict
json_experiment_type_from_dict = JsonExperimentType.from_dict(json_experiment_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


