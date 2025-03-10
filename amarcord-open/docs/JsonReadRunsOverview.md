# JsonReadRunsOverview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**live_stream** | [**JsonLiveStream**](JsonLiveStream.md) |  | [optional] 
**attributi** | [**List[JsonAttributo]**](JsonAttributo.md) |  | 
**latest_indexing_result** | [**JsonRunAnalysisIndexingResult**](JsonRunAnalysisIndexingResult.md) |  | [optional] 
**latest_run** | [**JsonRun**](JsonRun.md) |  | [optional] 
**foms_for_this_data_set** | [**JsonDataSetWithFom**](JsonDataSetWithFom.md) |  | [optional] 
**experiment_types** | [**List[JsonExperimentType]**](JsonExperimentType.md) |  | 
**events** | [**List[JsonEvent]**](JsonEvent.md) |  | 
**chemicals** | [**List[JsonChemical]**](JsonChemical.md) |  | 
**user_config** | [**JsonUserConfig**](JsonUserConfig.md) |  | 
**current_beamtime_user** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.json_read_runs_overview import JsonReadRunsOverview

# TODO update the JSON string below
json = "{}"
# create an instance of JsonReadRunsOverview from a JSON string
json_read_runs_overview_instance = JsonReadRunsOverview.from_json(json)
# print the JSON string representation of the object
print(JsonReadRunsOverview.to_json())

# convert the object into a dict
json_read_runs_overview_dict = json_read_runs_overview_instance.to_dict()
# create an instance of JsonReadRunsOverview from a dict
json_read_runs_overview_from_dict = JsonReadRunsOverview.from_dict(json_read_runs_overview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


