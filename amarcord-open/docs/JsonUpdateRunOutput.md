# JsonUpdateRunOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **bool** |  | 
**files** | [**List[JsonRunFile]**](JsonRunFile.md) |  | 

## Example

```python
from openapi_client.models.json_update_run_output import JsonUpdateRunOutput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonUpdateRunOutput from a JSON string
json_update_run_output_instance = JsonUpdateRunOutput.from_json(json)
# print the JSON string representation of the object
print(JsonUpdateRunOutput.to_json())

# convert the object into a dict
json_update_run_output_dict = json_update_run_output_instance.to_dict()
# create an instance of JsonUpdateRunOutput from a dict
json_update_run_output_from_dict = JsonUpdateRunOutput.from_dict(json_update_run_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


