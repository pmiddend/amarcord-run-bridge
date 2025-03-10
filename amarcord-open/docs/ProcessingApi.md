# openapi_client.ProcessingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**indexing_job_finish_successfully_api_indexing_indexing_result_id_success_post**](ProcessingApi.md#indexing_job_finish_successfully_api_indexing_indexing_result_id_success_post) | **POST** /api/indexing/{indexingResultId}/success | Indexing Job Finish Successfully
[**indexing_job_finish_with_error_api_indexing_indexing_result_id_finish_with_error_post**](ProcessingApi.md#indexing_job_finish_with_error_api_indexing_indexing_result_id_finish_with_error_post) | **POST** /api/indexing/{indexingResultId}/finish-with-error | Indexing Job Finish With Error
[**indexing_job_get_errorlog_api_indexing_indexing_result_id_errorlog_get**](ProcessingApi.md#indexing_job_get_errorlog_api_indexing_indexing_result_id_errorlog_get) | **GET** /api/indexing/{indexingResultId}/errorlog | Indexing Job Get Errorlog
[**indexing_job_get_log_api_indexing_indexing_result_id_log_get**](ProcessingApi.md#indexing_job_get_log_api_indexing_indexing_result_id_log_get) | **GET** /api/indexing/{indexingResultId}/log | Indexing Job Get Log
[**indexing_job_queue_for_data_set_api_indexing_post**](ProcessingApi.md#indexing_job_queue_for_data_set_api_indexing_post) | **POST** /api/indexing | Indexing Job Queue For Data Set
[**indexing_job_still_running_api_indexing_indexing_result_id_still_running_post**](ProcessingApi.md#indexing_job_still_running_api_indexing_indexing_result_id_still_running_post) | **POST** /api/indexing/{indexingResultId}/still-running | Indexing Job Still Running
[**merge_job_get_log_api_merging_merge_result_id_log_get**](ProcessingApi.md#merge_job_get_log_api_merging_merge_result_id_log_get) | **GET** /api/merging/{mergeResultId}/log | Merge Job Get Log
[**read_indexing_jobs_api_indexing_get**](ProcessingApi.md#read_indexing_jobs_api_indexing_get) | **GET** /api/indexing | Read Indexing Jobs
[**read_indexing_parameters_api_indexing_parameters_data_set_id_get**](ProcessingApi.md#read_indexing_parameters_api_indexing_parameters_data_set_id_get) | **GET** /api/indexing-parameters/{dataSetId} | Read Indexing Parameters


# **indexing_job_finish_successfully_api_indexing_indexing_result_id_success_post**
> JsonIndexingJobUpdateOutput indexing_job_finish_successfully_api_indexing_indexing_result_id_success_post(indexing_result_id, json_indexing_result_finish_successfully)

Indexing Job Finish Successfully

### Example


```python
import openapi_client
from openapi_client.models.json_indexing_job_update_output import JsonIndexingJobUpdateOutput
from openapi_client.models.json_indexing_result_finish_successfully import JsonIndexingResultFinishSuccessfully
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
    api_instance = openapi_client.ProcessingApi(api_client)
    indexing_result_id = 56 # int | 
    json_indexing_result_finish_successfully = openapi_client.JsonIndexingResultFinishSuccessfully() # JsonIndexingResultFinishSuccessfully | 

    try:
        # Indexing Job Finish Successfully
        api_response = await api_instance.indexing_job_finish_successfully_api_indexing_indexing_result_id_success_post(indexing_result_id, json_indexing_result_finish_successfully)
        print("The response of ProcessingApi->indexing_job_finish_successfully_api_indexing_indexing_result_id_success_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessingApi->indexing_job_finish_successfully_api_indexing_indexing_result_id_success_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexing_result_id** | **int**|  | 
 **json_indexing_result_finish_successfully** | [**JsonIndexingResultFinishSuccessfully**](JsonIndexingResultFinishSuccessfully.md)|  | 

### Return type

[**JsonIndexingJobUpdateOutput**](JsonIndexingJobUpdateOutput.md)

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

# **indexing_job_finish_with_error_api_indexing_indexing_result_id_finish_with_error_post**
> JsonIndexingJobUpdateOutput indexing_job_finish_with_error_api_indexing_indexing_result_id_finish_with_error_post(indexing_result_id, json_indexing_result_finish_with_error)

Indexing Job Finish With Error

### Example


```python
import openapi_client
from openapi_client.models.json_indexing_job_update_output import JsonIndexingJobUpdateOutput
from openapi_client.models.json_indexing_result_finish_with_error import JsonIndexingResultFinishWithError
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
    api_instance = openapi_client.ProcessingApi(api_client)
    indexing_result_id = 56 # int | 
    json_indexing_result_finish_with_error = openapi_client.JsonIndexingResultFinishWithError() # JsonIndexingResultFinishWithError | 

    try:
        # Indexing Job Finish With Error
        api_response = await api_instance.indexing_job_finish_with_error_api_indexing_indexing_result_id_finish_with_error_post(indexing_result_id, json_indexing_result_finish_with_error)
        print("The response of ProcessingApi->indexing_job_finish_with_error_api_indexing_indexing_result_id_finish_with_error_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessingApi->indexing_job_finish_with_error_api_indexing_indexing_result_id_finish_with_error_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexing_result_id** | **int**|  | 
 **json_indexing_result_finish_with_error** | [**JsonIndexingResultFinishWithError**](JsonIndexingResultFinishWithError.md)|  | 

### Return type

[**JsonIndexingJobUpdateOutput**](JsonIndexingJobUpdateOutput.md)

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

# **indexing_job_get_errorlog_api_indexing_indexing_result_id_errorlog_get**
> str indexing_job_get_errorlog_api_indexing_indexing_result_id_errorlog_get(indexing_result_id)

Indexing Job Get Errorlog

### Example


```python
import openapi_client
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
    api_instance = openapi_client.ProcessingApi(api_client)
    indexing_result_id = 56 # int | 

    try:
        # Indexing Job Get Errorlog
        api_response = await api_instance.indexing_job_get_errorlog_api_indexing_indexing_result_id_errorlog_get(indexing_result_id)
        print("The response of ProcessingApi->indexing_job_get_errorlog_api_indexing_indexing_result_id_errorlog_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessingApi->indexing_job_get_errorlog_api_indexing_indexing_result_id_errorlog_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexing_result_id** | **int**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **indexing_job_get_log_api_indexing_indexing_result_id_log_get**
> str indexing_job_get_log_api_indexing_indexing_result_id_log_get(indexing_result_id)

Indexing Job Get Log

### Example


```python
import openapi_client
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
    api_instance = openapi_client.ProcessingApi(api_client)
    indexing_result_id = 56 # int | 

    try:
        # Indexing Job Get Log
        api_response = await api_instance.indexing_job_get_log_api_indexing_indexing_result_id_log_get(indexing_result_id)
        print("The response of ProcessingApi->indexing_job_get_log_api_indexing_indexing_result_id_log_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessingApi->indexing_job_get_log_api_indexing_indexing_result_id_log_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexing_result_id** | **int**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **indexing_job_queue_for_data_set_api_indexing_post**
> JsonCreateIndexingForDataSetOutput indexing_job_queue_for_data_set_api_indexing_post(json_create_indexing_for_data_set_input)

Indexing Job Queue For Data Set

### Example


```python
import openapi_client
from openapi_client.models.json_create_indexing_for_data_set_input import JsonCreateIndexingForDataSetInput
from openapi_client.models.json_create_indexing_for_data_set_output import JsonCreateIndexingForDataSetOutput
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
    api_instance = openapi_client.ProcessingApi(api_client)
    json_create_indexing_for_data_set_input = openapi_client.JsonCreateIndexingForDataSetInput() # JsonCreateIndexingForDataSetInput | 

    try:
        # Indexing Job Queue For Data Set
        api_response = await api_instance.indexing_job_queue_for_data_set_api_indexing_post(json_create_indexing_for_data_set_input)
        print("The response of ProcessingApi->indexing_job_queue_for_data_set_api_indexing_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessingApi->indexing_job_queue_for_data_set_api_indexing_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_create_indexing_for_data_set_input** | [**JsonCreateIndexingForDataSetInput**](JsonCreateIndexingForDataSetInput.md)|  | 

### Return type

[**JsonCreateIndexingForDataSetOutput**](JsonCreateIndexingForDataSetOutput.md)

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

# **indexing_job_still_running_api_indexing_indexing_result_id_still_running_post**
> JsonIndexingJobUpdateOutput indexing_job_still_running_api_indexing_indexing_result_id_still_running_post(indexing_result_id, json_indexing_result_still_running)

Indexing Job Still Running

### Example


```python
import openapi_client
from openapi_client.models.json_indexing_job_update_output import JsonIndexingJobUpdateOutput
from openapi_client.models.json_indexing_result_still_running import JsonIndexingResultStillRunning
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
    api_instance = openapi_client.ProcessingApi(api_client)
    indexing_result_id = 56 # int | 
    json_indexing_result_still_running = openapi_client.JsonIndexingResultStillRunning() # JsonIndexingResultStillRunning | 

    try:
        # Indexing Job Still Running
        api_response = await api_instance.indexing_job_still_running_api_indexing_indexing_result_id_still_running_post(indexing_result_id, json_indexing_result_still_running)
        print("The response of ProcessingApi->indexing_job_still_running_api_indexing_indexing_result_id_still_running_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessingApi->indexing_job_still_running_api_indexing_indexing_result_id_still_running_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexing_result_id** | **int**|  | 
 **json_indexing_result_still_running** | [**JsonIndexingResultStillRunning**](JsonIndexingResultStillRunning.md)|  | 

### Return type

[**JsonIndexingJobUpdateOutput**](JsonIndexingJobUpdateOutput.md)

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

# **merge_job_get_log_api_merging_merge_result_id_log_get**
> str merge_job_get_log_api_merging_merge_result_id_log_get(merge_result_id)

Merge Job Get Log

### Example


```python
import openapi_client
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
    api_instance = openapi_client.ProcessingApi(api_client)
    merge_result_id = 56 # int | 

    try:
        # Merge Job Get Log
        api_response = await api_instance.merge_job_get_log_api_merging_merge_result_id_log_get(merge_result_id)
        print("The response of ProcessingApi->merge_job_get_log_api_merging_merge_result_id_log_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessingApi->merge_job_get_log_api_merging_merge_result_id_log_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merge_result_id** | **int**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_indexing_jobs_api_indexing_get**
> JsonReadIndexingResultsOutput read_indexing_jobs_api_indexing_get(status=status, beamtime_id=beamtime_id, with_files=with_files)

Read Indexing Jobs

### Example


```python
import openapi_client
from openapi_client.models.db_job_status import DBJobStatus
from openapi_client.models.json_read_indexing_results_output import JsonReadIndexingResultsOutput
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
    api_instance = openapi_client.ProcessingApi(api_client)
    status = openapi_client.DBJobStatus() # DBJobStatus |  (optional)
    beamtime_id = 56 # int |  (optional)
    with_files = False # bool |  (optional) (default to False)

    try:
        # Read Indexing Jobs
        api_response = await api_instance.read_indexing_jobs_api_indexing_get(status=status, beamtime_id=beamtime_id, with_files=with_files)
        print("The response of ProcessingApi->read_indexing_jobs_api_indexing_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessingApi->read_indexing_jobs_api_indexing_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**DBJobStatus**](.md)|  | [optional] 
 **beamtime_id** | **int**|  | [optional] 
 **with_files** | **bool**|  | [optional] [default to False]

### Return type

[**JsonReadIndexingResultsOutput**](JsonReadIndexingResultsOutput.md)

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

# **read_indexing_parameters_api_indexing_parameters_data_set_id_get**
> JsonReadIndexingParametersOutput read_indexing_parameters_api_indexing_parameters_data_set_id_get(data_set_id)

Read Indexing Parameters

### Example


```python
import openapi_client
from openapi_client.models.json_read_indexing_parameters_output import JsonReadIndexingParametersOutput
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
    api_instance = openapi_client.ProcessingApi(api_client)
    data_set_id = 56 # int | 

    try:
        # Read Indexing Parameters
        api_response = await api_instance.read_indexing_parameters_api_indexing_parameters_data_set_id_get(data_set_id)
        print("The response of ProcessingApi->read_indexing_parameters_api_indexing_parameters_data_set_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessingApi->read_indexing_parameters_api_indexing_parameters_data_set_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_set_id** | **int**|  | 

### Return type

[**JsonReadIndexingParametersOutput**](JsonReadIndexingParametersOutput.md)

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

