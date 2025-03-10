# JsonBeamtime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**external_id** | **str** |  | 
**proposal** | **str** |  | 
**beamline** | **str** |  | 
**title** | **str** |  | 
**comment** | **str** |  | 
**start** | **int** |  | 
**end** | **int** |  | 
**chemical_names** | **List[str]** |  | 
**analysis_output_path** | **str** |  | 

## Example

```python
from openapi_client.models.json_beamtime import JsonBeamtime

# TODO update the JSON string below
json = "{}"
# create an instance of JsonBeamtime from a JSON string
json_beamtime_instance = JsonBeamtime.from_json(json)
# print the JSON string representation of the object
print(JsonBeamtime.to_json())

# convert the object into a dict
json_beamtime_dict = json_beamtime_instance.to_dict()
# create an instance of JsonBeamtime from a dict
json_beamtime_from_dict = JsonBeamtime.from_dict(json_beamtime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


