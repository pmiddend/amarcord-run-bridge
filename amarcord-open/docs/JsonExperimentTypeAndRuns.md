# JsonExperimentTypeAndRuns


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**runs** | **List[str]** |  | 
**number_of_runs** | **int** |  | 

## Example

```python
from openapi_client.models.json_experiment_type_and_runs import JsonExperimentTypeAndRuns

# TODO update the JSON string below
json = "{}"
# create an instance of JsonExperimentTypeAndRuns from a JSON string
json_experiment_type_and_runs_instance = JsonExperimentTypeAndRuns.from_json(json)
# print the JSON string representation of the object
print(JsonExperimentTypeAndRuns.to_json())

# convert the object into a dict
json_experiment_type_and_runs_dict = json_experiment_type_and_runs_instance.to_dict()
# create an instance of JsonExperimentTypeAndRuns from a dict
json_experiment_type_and_runs_from_dict = JsonExperimentTypeAndRuns.from_dict(json_experiment_type_and_runs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


