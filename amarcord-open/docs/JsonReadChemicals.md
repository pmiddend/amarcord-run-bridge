# JsonReadChemicals


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chemicals** | [**List[JsonChemical]**](JsonChemical.md) |  | 
**attributi** | [**List[JsonAttributo]**](JsonAttributo.md) |  | 

## Example

```python
from openapi_client.models.json_read_chemicals import JsonReadChemicals

# TODO update the JSON string below
json = "{}"
# create an instance of JsonReadChemicals from a JSON string
json_read_chemicals_instance = JsonReadChemicals.from_json(json)
# print the JSON string representation of the object
print(JsonReadChemicals.to_json())

# convert the object into a dict
json_read_chemicals_dict = json_read_chemicals_instance.to_dict()
# create an instance of JsonReadChemicals from a dict
json_read_chemicals_from_dict = JsonReadChemicals.from_dict(json_read_chemicals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


