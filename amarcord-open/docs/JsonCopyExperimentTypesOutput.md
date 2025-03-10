# JsonCopyExperimentTypesOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_beamtime_experiment_type_ids** | **List[int]** |  | 

## Example

```python
from openapi_client.models.json_copy_experiment_types_output import JsonCopyExperimentTypesOutput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonCopyExperimentTypesOutput from a JSON string
json_copy_experiment_types_output_instance = JsonCopyExperimentTypesOutput.from_json(json)
# print the JSON string representation of the object
print(JsonCopyExperimentTypesOutput.to_json())

# convert the object into a dict
json_copy_experiment_types_output_dict = json_copy_experiment_types_output_instance.to_dict()
# create an instance of JsonCopyExperimentTypesOutput from a dict
json_copy_experiment_types_output_from_dict = JsonCopyExperimentTypesOutput.from_dict(json_copy_experiment_types_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


