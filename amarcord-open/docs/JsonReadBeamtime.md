# JsonReadBeamtime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beamtimes** | [**List[JsonBeamtime]**](JsonBeamtime.md) |  | 

## Example

```python
from openapi_client.models.json_read_beamtime import JsonReadBeamtime

# TODO update the JSON string below
json = "{}"
# create an instance of JsonReadBeamtime from a JSON string
json_read_beamtime_instance = JsonReadBeamtime.from_json(json)
# print the JSON string representation of the object
print(JsonReadBeamtime.to_json())

# convert the object into a dict
json_read_beamtime_dict = json_read_beamtime_instance.to_dict()
# create an instance of JsonReadBeamtime from a dict
json_read_beamtime_from_dict = JsonReadBeamtime.from_dict(json_read_beamtime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


