# JsonUpdateBeamtimeInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**external_id** | **str** |  | 
**beamline** | **str** |  | 
**proposal** | **str** |  | 
**title** | **str** |  | 
**comment** | **str** |  | 
**start** | **int** |  | 
**end** | **int** |  | 
**analysis_output_path** | **str** |  | 

## Example

```python
from openapi_client.models.json_update_beamtime_input import JsonUpdateBeamtimeInput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonUpdateBeamtimeInput from a JSON string
json_update_beamtime_input_instance = JsonUpdateBeamtimeInput.from_json(json)
# print the JSON string representation of the object
print(JsonUpdateBeamtimeInput.to_json())

# convert the object into a dict
json_update_beamtime_input_dict = json_update_beamtime_input_instance.to_dict()
# create an instance of JsonUpdateBeamtimeInput from a dict
json_update_beamtime_input_from_dict = JsonUpdateBeamtimeInput.from_dict(json_update_beamtime_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


