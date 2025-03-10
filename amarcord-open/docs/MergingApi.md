# openapi_client.MergingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**merge_job_finished_api_merging_merge_result_id_finish_post**](MergingApi.md#merge_job_finished_api_merging_merge_result_id_finish_post) | **POST** /api/merging/{mergeResultId}/finish | Merge Job Finished
[**merge_job_started_api_merging_merge_result_id_start_post**](MergingApi.md#merge_job_started_api_merging_merge_result_id_start_post) | **POST** /api/merging/{mergeResultId}/start | Merge Job Started
[**queue_merge_job_api_merging_post**](MergingApi.md#queue_merge_job_api_merging_post) | **POST** /api/merging | Queue Merge Job
[**read_merge_jobs_api_merging_get**](MergingApi.md#read_merge_jobs_api_merging_get) | **GET** /api/merging | Read Merge Jobs


# **merge_job_finished_api_merging_merge_result_id_finish_post**
> JsonMergeJobFinishOutput merge_job_finished_api_merging_merge_result_id_finish_post(merge_result_id, json_merge_job_finished_input)

Merge Job Finished

### Example


```python
import openapi_client
from openapi_client.models.json_merge_job_finish_output import JsonMergeJobFinishOutput
from openapi_client.models.json_merge_job_finished_input import JsonMergeJobFinishedInput
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
    api_instance = openapi_client.MergingApi(api_client)
    merge_result_id = 56 # int | 
    json_merge_job_finished_input = openapi_client.JsonMergeJobFinishedInput() # JsonMergeJobFinishedInput | 

    try:
        # Merge Job Finished
        api_response = await api_instance.merge_job_finished_api_merging_merge_result_id_finish_post(merge_result_id, json_merge_job_finished_input)
        print("The response of MergingApi->merge_job_finished_api_merging_merge_result_id_finish_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MergingApi->merge_job_finished_api_merging_merge_result_id_finish_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merge_result_id** | **int**|  | 
 **json_merge_job_finished_input** | [**JsonMergeJobFinishedInput**](JsonMergeJobFinishedInput.md)|  | 

### Return type

[**JsonMergeJobFinishOutput**](JsonMergeJobFinishOutput.md)

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

# **merge_job_started_api_merging_merge_result_id_start_post**
> JsonMergeJobStartedOutput merge_job_started_api_merging_merge_result_id_start_post(merge_result_id, json_merge_job_started_input)

Merge Job Started

### Example


```python
import openapi_client
from openapi_client.models.json_merge_job_started_input import JsonMergeJobStartedInput
from openapi_client.models.json_merge_job_started_output import JsonMergeJobStartedOutput
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
    api_instance = openapi_client.MergingApi(api_client)
    merge_result_id = 56 # int | 
    json_merge_job_started_input = openapi_client.JsonMergeJobStartedInput() # JsonMergeJobStartedInput | 

    try:
        # Merge Job Started
        api_response = await api_instance.merge_job_started_api_merging_merge_result_id_start_post(merge_result_id, json_merge_job_started_input)
        print("The response of MergingApi->merge_job_started_api_merging_merge_result_id_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MergingApi->merge_job_started_api_merging_merge_result_id_start_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merge_result_id** | **int**|  | 
 **json_merge_job_started_input** | [**JsonMergeJobStartedInput**](JsonMergeJobStartedInput.md)|  | 

### Return type

[**JsonMergeJobStartedOutput**](JsonMergeJobStartedOutput.md)

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

# **queue_merge_job_api_merging_post**
> JsonQueueMergeJobOutput queue_merge_job_api_merging_post(json_queue_merge_job_input)

Queue Merge Job

### Example


```python
import openapi_client
from openapi_client.models.json_queue_merge_job_input import JsonQueueMergeJobInput
from openapi_client.models.json_queue_merge_job_output import JsonQueueMergeJobOutput
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
    api_instance = openapi_client.MergingApi(api_client)
    json_queue_merge_job_input = openapi_client.JsonQueueMergeJobInput() # JsonQueueMergeJobInput | 

    try:
        # Queue Merge Job
        api_response = await api_instance.queue_merge_job_api_merging_post(json_queue_merge_job_input)
        print("The response of MergingApi->queue_merge_job_api_merging_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MergingApi->queue_merge_job_api_merging_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_queue_merge_job_input** | [**JsonQueueMergeJobInput**](JsonQueueMergeJobInput.md)|  | 

### Return type

[**JsonQueueMergeJobOutput**](JsonQueueMergeJobOutput.md)

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

# **read_merge_jobs_api_merging_get**
> JsonReadMergeResultsOutput read_merge_jobs_api_merging_get(status=status)

Read Merge Jobs

### Example


```python
import openapi_client
from openapi_client.models.db_job_status import DBJobStatus
from openapi_client.models.json_read_merge_results_output import JsonReadMergeResultsOutput
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
    api_instance = openapi_client.MergingApi(api_client)
    status = openapi_client.DBJobStatus() # DBJobStatus |  (optional)

    try:
        # Read Merge Jobs
        api_response = await api_instance.read_merge_jobs_api_merging_get(status=status)
        print("The response of MergingApi->read_merge_jobs_api_merging_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MergingApi->read_merge_jobs_api_merging_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**DBJobStatus**](.md)|  | [optional] 

### Return type

[**JsonReadMergeResultsOutput**](JsonReadMergeResultsOutput.md)

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

