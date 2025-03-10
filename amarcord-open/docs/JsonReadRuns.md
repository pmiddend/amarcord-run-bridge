# JsonReadRuns


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_dates** | **List[str]** |  | 
**runs** | [**List[JsonRun]**](JsonRun.md) |  | 
**attributi** | [**List[JsonAttributo]**](JsonAttributo.md) |  | 
**experiment_types** | [**List[JsonExperimentType]**](JsonExperimentType.md) |  | 
**events** | [**List[JsonEvent]**](JsonEvent.md) |  | 
**chemicals** | [**List[JsonChemical]**](JsonChemical.md) |  | 

## Example

```python
from openapi_client.models.json_read_runs import JsonReadRuns

# TODO update the JSON string below
json = "{}"
# create an instance of JsonReadRuns from a JSON string
json_read_runs_instance = JsonReadRuns.from_json(json)
# print the JSON string representation of the object
print(JsonReadRuns.to_json())

# convert the object into a dict
json_read_runs_dict = json_read_runs_instance.to_dict()
# create an instance of JsonReadRuns from a dict
json_read_runs_from_dict = JsonReadRuns.from_dict(json_read_runs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


