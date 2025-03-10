# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_standard_unit_api_unit_post**](DefaultApi.md#check_standard_unit_api_unit_post) | **POST** /api/unit | Check Standard Unit
[**update_live_stream_api_live_stream_beamtime_id_post**](DefaultApi.md#update_live_stream_api_live_stream_beamtime_id_post) | **POST** /api/live-stream/{beamtimeId} | Update Live Stream


# **check_standard_unit_api_unit_post**
> JsonCheckStandardUnitOutput check_standard_unit_api_unit_post(json_check_standard_unit_input)

Check Standard Unit

### Example


```python
import openapi_client
from openapi_client.models.json_check_standard_unit_input import JsonCheckStandardUnitInput
from openapi_client.models.json_check_standard_unit_output import JsonCheckStandardUnitOutput
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    json_check_standard_unit_input = openapi_client.JsonCheckStandardUnitInput() # JsonCheckStandardUnitInput | 

    try:
        # Check Standard Unit
        api_response = await api_instance.check_standard_unit_api_unit_post(json_check_standard_unit_input)
        print("The response of DefaultApi->check_standard_unit_api_unit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->check_standard_unit_api_unit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_check_standard_unit_input** | [**JsonCheckStandardUnitInput**](JsonCheckStandardUnitInput.md)|  | 

### Return type

[**JsonCheckStandardUnitOutput**](JsonCheckStandardUnitOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_live_stream_api_live_stream_beamtime_id_post**
> JsonUpdateLiveStream update_live_stream_api_live_stream_beamtime_id_post(beamtime_id, file)

Update Live Stream

### Example


```python
import openapi_client
from openapi_client.models.json_update_live_stream import JsonUpdateLiveStream
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    beamtime_id = 56 # int | 
    file = None # bytearray | 

    try:
        # Update Live Stream
        api_response = await api_instance.update_live_stream_api_live_stream_beamtime_id_post(beamtime_id, file)
        print("The response of DefaultApi->update_live_stream_api_live_stream_beamtime_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_live_stream_api_live_stream_beamtime_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beamtime_id** | **int**|  | 
 **file** | **bytearray**|  | 

### Return type

[**JsonUpdateLiveStream**](JsonUpdateLiveStream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

