# JsonIndexingStatistic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **int** |  | 
**frames** | **int** |  | 
**hits** | **int** |  | 
**indexed** | **int** |  | 
**crystals** | **int** |  | 

## Example

```python
from openapi_client.models.json_indexing_statistic import JsonIndexingStatistic

# TODO update the JSON string below
json = "{}"
# create an instance of JsonIndexingStatistic from a JSON string
json_indexing_statistic_instance = JsonIndexingStatistic.from_json(json)
# print the JSON string representation of the object
print(JsonIndexingStatistic.to_json())

# convert the object into a dict
json_indexing_statistic_dict = json_indexing_statistic_instance.to_dict()
# create an instance of JsonIndexingStatistic from a dict
json_indexing_statistic_from_dict = JsonIndexingStatistic.from_dict(json_indexing_statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


