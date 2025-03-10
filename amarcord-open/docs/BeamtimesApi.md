# openapi_client.BeamtimesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_beamtime_api_beamtimes_post**](BeamtimesApi.md#create_beamtime_api_beamtimes_post) | **POST** /api/beamtimes | Create Beamtime
[**read_beamtime_api_beamtimes_beamtime_id_get**](BeamtimesApi.md#read_beamtime_api_beamtimes_beamtime_id_get) | **GET** /api/beamtimes/{beamtimeId} | Read Beamtime
[**read_beamtimes_api_beamtimes_get**](BeamtimesApi.md#read_beamtimes_api_beamtimes_get) | **GET** /api/beamtimes | Read Beamtimes
[**update_beamtime_api_beamtimes_patch**](BeamtimesApi.md#update_beamtime_api_beamtimes_patch) | **PATCH** /api/beamtimes | Update Beamtime


# **create_beamtime_api_beamtimes_post**
> JsonBeamtimeOutput create_beamtime_api_beamtimes_post(json_update_beamtime_input)

Create Beamtime

### Example


```python
import openapi_client
from openapi_client.models.json_beamtime_output import JsonBeamtimeOutput
from openapi_client.models.json_update_beamtime_input import JsonUpdateBeamtimeInput
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
    api_instance = openapi_client.BeamtimesApi(api_client)
    json_update_beamtime_input = openapi_client.JsonUpdateBeamtimeInput() # JsonUpdateBeamtimeInput | 

    try:
        # Create Beamtime
        api_response = await api_instance.create_beamtime_api_beamtimes_post(json_update_beamtime_input)
        print("The response of BeamtimesApi->create_beamtime_api_beamtimes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BeamtimesApi->create_beamtime_api_beamtimes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_update_beamtime_input** | [**JsonUpdateBeamtimeInput**](JsonUpdateBeamtimeInput.md)|  | 

### Return type

[**JsonBeamtimeOutput**](JsonBeamtimeOutput.md)

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

# **read_beamtime_api_beamtimes_beamtime_id_get**
> JsonBeamtime read_beamtime_api_beamtimes_beamtime_id_get(beamtime_id)

Read Beamtime

### Example


```python
import openapi_client
from openapi_client.models.json_beamtime import JsonBeamtime
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
    api_instance = openapi_client.BeamtimesApi(api_client)
    beamtime_id = 56 # int | 

    try:
        # Read Beamtime
        api_response = await api_instance.read_beamtime_api_beamtimes_beamtime_id_get(beamtime_id)
        print("The response of BeamtimesApi->read_beamtime_api_beamtimes_beamtime_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BeamtimesApi->read_beamtime_api_beamtimes_beamtime_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beamtime_id** | **int**|  | 

### Return type

[**JsonBeamtime**](JsonBeamtime.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_beamtimes_api_beamtimes_get**
> JsonReadBeamtime read_beamtimes_api_beamtimes_get()

Read Beamtimes

### Example


```python
import openapi_client
from openapi_client.models.json_read_beamtime import JsonReadBeamtime
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
    api_instance = openapi_client.BeamtimesApi(api_client)

    try:
        # Read Beamtimes
        api_response = await api_instance.read_beamtimes_api_beamtimes_get()
        print("The response of BeamtimesApi->read_beamtimes_api_beamtimes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BeamtimesApi->read_beamtimes_api_beamtimes_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**JsonReadBeamtime**](JsonReadBeamtime.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_beamtime_api_beamtimes_patch**
> JsonBeamtimeOutput update_beamtime_api_beamtimes_patch(json_update_beamtime_input)

Update Beamtime

### Example


```python
import openapi_client
from openapi_client.models.json_beamtime_output import JsonBeamtimeOutput
from openapi_client.models.json_update_beamtime_input import JsonUpdateBeamtimeInput
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
    api_instance = openapi_client.BeamtimesApi(api_client)
    json_update_beamtime_input = openapi_client.JsonUpdateBeamtimeInput() # JsonUpdateBeamtimeInput | 

    try:
        # Update Beamtime
        api_response = await api_instance.update_beamtime_api_beamtimes_patch(json_update_beamtime_input)
        print("The response of BeamtimesApi->update_beamtime_api_beamtimes_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BeamtimesApi->update_beamtime_api_beamtimes_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_update_beamtime_input** | [**JsonUpdateBeamtimeInput**](JsonUpdateBeamtimeInput.md)|  | 

### Return type

[**JsonBeamtimeOutput**](JsonBeamtimeOutput.md)

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

