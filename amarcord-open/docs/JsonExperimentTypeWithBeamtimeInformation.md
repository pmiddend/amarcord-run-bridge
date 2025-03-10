# JsonExperimentTypeWithBeamtimeInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**experiment_type** | [**JsonExperimentType**](JsonExperimentType.md) |  | 
**beamtime** | [**JsonBeamtime**](JsonBeamtime.md) |  | 

## Example

```python
from openapi_client.models.json_experiment_type_with_beamtime_information import JsonExperimentTypeWithBeamtimeInformation

# TODO update the JSON string below
json = "{}"
# create an instance of JsonExperimentTypeWithBeamtimeInformation from a JSON string
json_experiment_type_with_beamtime_information_instance = JsonExperimentTypeWithBeamtimeInformation.from_json(json)
# print the JSON string representation of the object
print(JsonExperimentTypeWithBeamtimeInformation.to_json())

# convert the object into a dict
json_experiment_type_with_beamtime_information_dict = json_experiment_type_with_beamtime_information_instance.to_dict()
# create an instance of JsonExperimentTypeWithBeamtimeInformation from a dict
json_experiment_type_with_beamtime_information_from_dict = JsonExperimentTypeWithBeamtimeInformation.from_dict(json_experiment_type_with_beamtime_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


