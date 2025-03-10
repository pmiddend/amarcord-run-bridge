# JsonReadExperimentTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**experiment_types** | [**List[JsonExperimentType]**](JsonExperimentType.md) |  | 
**attributi** | [**List[JsonAttributo]**](JsonAttributo.md) |  | 
**experiment_type_id_to_run** | [**List[JsonExperimentTypeAndRuns]**](JsonExperimentTypeAndRuns.md) |  | 
**current_experiment_type_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.json_read_experiment_types import JsonReadExperimentTypes

# TODO update the JSON string below
json = "{}"
# create an instance of JsonReadExperimentTypes from a JSON string
json_read_experiment_types_instance = JsonReadExperimentTypes.from_json(json)
# print the JSON string representation of the object
print(JsonReadExperimentTypes.to_json())

# convert the object into a dict
json_read_experiment_types_dict = json_read_experiment_types_instance.to_dict()
# create an instance of JsonReadExperimentTypes from a dict
json_read_experiment_types_from_dict = JsonReadExperimentTypes.from_dict(json_read_experiment_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


