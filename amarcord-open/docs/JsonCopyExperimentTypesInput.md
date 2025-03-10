# JsonCopyExperimentTypesInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_beamtime** | **int** |  | 
**to_beamtime** | **int** |  | 

## Example

```python
from openapi_client.models.json_copy_experiment_types_input import JsonCopyExperimentTypesInput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonCopyExperimentTypesInput from a JSON string
json_copy_experiment_types_input_instance = JsonCopyExperimentTypesInput.from_json(json)
# print the JSON string representation of the object
print(JsonCopyExperimentTypesInput.to_json())

# convert the object into a dict
json_copy_experiment_types_input_dict = json_copy_experiment_types_input_instance.to_dict()
# create an instance of JsonCopyExperimentTypesInput from a dict
json_copy_experiment_types_input_from_dict = JsonCopyExperimentTypesInput.from_dict(json_copy_experiment_types_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


