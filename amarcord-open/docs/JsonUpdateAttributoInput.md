# JsonUpdateAttributoInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributo** | [**JsonAttributo**](JsonAttributo.md) |  | 
**conversion_flags** | [**JsonUpdateAttributoConversionFlags**](JsonUpdateAttributoConversionFlags.md) |  | 

## Example

```python
from openapi_client.models.json_update_attributo_input import JsonUpdateAttributoInput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonUpdateAttributoInput from a JSON string
json_update_attributo_input_instance = JsonUpdateAttributoInput.from_json(json)
# print the JSON string representation of the object
print(JsonUpdateAttributoInput.to_json())

# convert the object into a dict
json_update_attributo_input_dict = json_update_attributo_input_instance.to_dict()
# create an instance of JsonUpdateAttributoInput from a dict
json_update_attributo_input_from_dict = JsonUpdateAttributoInput.from_dict(json_update_attributo_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


