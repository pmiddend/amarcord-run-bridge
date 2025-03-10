# openapi_client.ScheduleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_beamtime_schedule_api_schedule_beamtime_id_get**](ScheduleApi.md#get_beamtime_schedule_api_schedule_beamtime_id_get) | **GET** /api/schedule/{beamtimeId} | Get Beamtime Schedule
[**update_beamtime_schedule_api_schedule_post**](ScheduleApi.md#update_beamtime_schedule_api_schedule_post) | **POST** /api/schedule | Update Beamtime Schedule


# **get_beamtime_schedule_api_schedule_beamtime_id_get**
> JsonBeamtimeSchedule get_beamtime_schedule_api_schedule_beamtime_id_get(beamtime_id)

Get Beamtime Schedule

### Example


```python
import openapi_client
from openapi_client.models.json_beamtime_schedule import JsonBeamtimeSchedule
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
    api_instance = openapi_client.ScheduleApi(api_client)
    beamtime_id = 56 # int | 

    try:
        # Get Beamtime Schedule
        api_response = await api_instance.get_beamtime_schedule_api_schedule_beamtime_id_get(beamtime_id)
        print("The response of ScheduleApi->get_beamtime_schedule_api_schedule_beamtime_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleApi->get_beamtime_schedule_api_schedule_beamtime_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beamtime_id** | **int**|  | 

### Return type

[**JsonBeamtimeSchedule**](JsonBeamtimeSchedule.md)

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

# **update_beamtime_schedule_api_schedule_post**
> JsonBeamtimeScheduleOutput update_beamtime_schedule_api_schedule_post(json_update_beamtime_schedule_input)

Update Beamtime Schedule

### Example


```python
import openapi_client
from openapi_client.models.json_beamtime_schedule_output import JsonBeamtimeScheduleOutput
from openapi_client.models.json_update_beamtime_schedule_input import JsonUpdateBeamtimeScheduleInput
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
    api_instance = openapi_client.ScheduleApi(api_client)
    json_update_beamtime_schedule_input = openapi_client.JsonUpdateBeamtimeScheduleInput() # JsonUpdateBeamtimeScheduleInput | 

    try:
        # Update Beamtime Schedule
        api_response = await api_instance.update_beamtime_schedule_api_schedule_post(json_update_beamtime_schedule_input)
        print("The response of ScheduleApi->update_beamtime_schedule_api_schedule_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduleApi->update_beamtime_schedule_api_schedule_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_update_beamtime_schedule_input** | [**JsonUpdateBeamtimeScheduleInput**](JsonUpdateBeamtimeScheduleInput.md)|  | 

### Return type

[**JsonBeamtimeScheduleOutput**](JsonBeamtimeScheduleOutput.md)

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

