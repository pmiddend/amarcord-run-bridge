# JsonReadBeamtimeGeometryDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detector_shifts** | [**List[JsonDetectorShift]**](JsonDetectorShift.md) |  | 

## Example

```python
from openapi_client.models.json_read_beamtime_geometry_details import JsonReadBeamtimeGeometryDetails

# TODO update the JSON string below
json = "{}"
# create an instance of JsonReadBeamtimeGeometryDetails from a JSON string
json_read_beamtime_geometry_details_instance = JsonReadBeamtimeGeometryDetails.from_json(json)
# print the JSON string representation of the object
print(JsonReadBeamtimeGeometryDetails.to_json())

# convert the object into a dict
json_read_beamtime_geometry_details_dict = json_read_beamtime_geometry_details_instance.to_dict()
# create an instance of JsonReadBeamtimeGeometryDetails from a dict
json_read_beamtime_geometry_details_from_dict = JsonReadBeamtimeGeometryDetails.from_dict(json_read_beamtime_geometry_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


