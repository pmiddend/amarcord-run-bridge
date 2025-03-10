# openapi_client.EventsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_event_api_events_post**](EventsApi.md#create_event_api_events_post) | **POST** /api/events | Create Event
[**create_live_stream_snapshot_api_live_stream_snapshot_beamtime_id_get**](EventsApi.md#create_live_stream_snapshot_api_live_stream_snapshot_beamtime_id_get) | **GET** /api/live-stream/snapshot/{beamtimeId} | Create Live Stream Snapshot
[**delete_event_api_events_delete**](EventsApi.md#delete_event_api_events_delete) | **DELETE** /api/events | Delete Event
[**read_events_api_events_beamtime_id_get**](EventsApi.md#read_events_api_events_beamtime_id_get) | **GET** /api/events/{beamtimeId} | Read Events


# **create_event_api_events_post**
> JsonEventTopLevelOutput create_event_api_events_post(json_event_top_level_input)

Create Event

### Example


```python
import openapi_client
from openapi_client.models.json_event_top_level_input import JsonEventTopLevelInput
from openapi_client.models.json_event_top_level_output import JsonEventTopLevelOutput
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
    api_instance = openapi_client.EventsApi(api_client)
    json_event_top_level_input = openapi_client.JsonEventTopLevelInput() # JsonEventTopLevelInput | 

    try:
        # Create Event
        api_response = await api_instance.create_event_api_events_post(json_event_top_level_input)
        print("The response of EventsApi->create_event_api_events_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->create_event_api_events_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_event_top_level_input** | [**JsonEventTopLevelInput**](JsonEventTopLevelInput.md)|  | 

### Return type

[**JsonEventTopLevelOutput**](JsonEventTopLevelOutput.md)

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

# **create_live_stream_snapshot_api_live_stream_snapshot_beamtime_id_get**
> JsonCreateLiveStreamSnapshotOutput create_live_stream_snapshot_api_live_stream_snapshot_beamtime_id_get(beamtime_id)

Create Live Stream Snapshot

### Example


```python
import openapi_client
from openapi_client.models.json_create_live_stream_snapshot_output import JsonCreateLiveStreamSnapshotOutput
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
    api_instance = openapi_client.EventsApi(api_client)
    beamtime_id = 56 # int | 

    try:
        # Create Live Stream Snapshot
        api_response = await api_instance.create_live_stream_snapshot_api_live_stream_snapshot_beamtime_id_get(beamtime_id)
        print("The response of EventsApi->create_live_stream_snapshot_api_live_stream_snapshot_beamtime_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->create_live_stream_snapshot_api_live_stream_snapshot_beamtime_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beamtime_id** | **int**|  | 

### Return type

[**JsonCreateLiveStreamSnapshotOutput**](JsonCreateLiveStreamSnapshotOutput.md)

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

# **delete_event_api_events_delete**
> JsonDeleteEventOutput delete_event_api_events_delete(json_delete_event_input)

Delete Event

### Example


```python
import openapi_client
from openapi_client.models.json_delete_event_input import JsonDeleteEventInput
from openapi_client.models.json_delete_event_output import JsonDeleteEventOutput
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
    api_instance = openapi_client.EventsApi(api_client)
    json_delete_event_input = openapi_client.JsonDeleteEventInput() # JsonDeleteEventInput | 

    try:
        # Delete Event
        api_response = await api_instance.delete_event_api_events_delete(json_delete_event_input)
        print("The response of EventsApi->delete_event_api_events_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->delete_event_api_events_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_delete_event_input** | [**JsonDeleteEventInput**](JsonDeleteEventInput.md)|  | 

### Return type

[**JsonDeleteEventOutput**](JsonDeleteEventOutput.md)

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

# **read_events_api_events_beamtime_id_get**
> JsonReadEvents read_events_api_events_beamtime_id_get(beamtime_id)

Read Events

### Example


```python
import openapi_client
from openapi_client.models.json_read_events import JsonReadEvents
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
    api_instance = openapi_client.EventsApi(api_client)
    beamtime_id = 56 # int | 

    try:
        # Read Events
        api_response = await api_instance.read_events_api_events_beamtime_id_get(beamtime_id)
        print("The response of EventsApi->read_events_api_events_beamtime_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->read_events_api_events_beamtime_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beamtime_id** | **int**|  | 

### Return type

[**JsonReadEvents**](JsonReadEvents.md)

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

