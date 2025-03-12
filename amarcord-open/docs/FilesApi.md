# openapi_client.FilesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_file_api_files_post**](FilesApi.md#create_file_api_files_post) | **POST** /api/files | Create File
[**create_file_simple_api_files_simple_extension_post**](FilesApi.md#create_file_simple_api_files_simple_extension_post) | **POST** /api/files/simple/{extension} | Create File Simple
[**delete_file_api_files_delete**](FilesApi.md#delete_file_api_files_delete) | **DELETE** /api/files | Delete File


# **create_file_api_files_post**
> JsonCreateFileOutput create_file_api_files_post(file, description, deduplicate)

Create File

### Example


```python
import openapi_client
from openapi_client.models.json_create_file_output import JsonCreateFileOutput
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
    api_instance = openapi_client.FilesApi(api_client)
    file = None # bytearray | 
    description = 'description_example' # str | 
    deduplicate = 'deduplicate_example' # str | 

    try:
        # Create File
        api_response = await api_instance.create_file_api_files_post(file, description, deduplicate)
        print("The response of FilesApi->create_file_api_files_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->create_file_api_files_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 
 **description** | **str**|  | 
 **deduplicate** | **str**|  | 

### Return type

[**JsonCreateFileOutput**](JsonCreateFileOutput.md)

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

# **create_file_simple_api_files_simple_extension_post**
> JsonCreateFileOutput create_file_simple_api_files_simple_extension_post(extension)

Create File Simple

This endpoint was specifically crafted to upload files in a simple way from external scripts, such as the CrystFEL scripts.
    It doesn't need a multipart request and the file extension can be set using the path parameter (which is used to generate nice
    .mtz and .pdb download URLs).

### Example


```python
import openapi_client
from openapi_client.models.json_create_file_output import JsonCreateFileOutput
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
    api_instance = openapi_client.FilesApi(api_client)
    extension = 'extension_example' # str | 

    try:
        # Create File Simple
        api_response = await api_instance.create_file_simple_api_files_simple_extension_post(extension)
        print("The response of FilesApi->create_file_simple_api_files_simple_extension_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->create_file_simple_api_files_simple_extension_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension** | **str**|  | 

### Return type

[**JsonCreateFileOutput**](JsonCreateFileOutput.md)

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

# **delete_file_api_files_delete**
> JsonDeleteFileOutput delete_file_api_files_delete(json_delete_file_input)

Delete File

### Example


```python
import openapi_client
from openapi_client.models.json_delete_file_input import JsonDeleteFileInput
from openapi_client.models.json_delete_file_output import JsonDeleteFileOutput
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
    api_instance = openapi_client.FilesApi(api_client)
    json_delete_file_input = openapi_client.JsonDeleteFileInput() # JsonDeleteFileInput | 

    try:
        # Delete File
        api_response = await api_instance.delete_file_api_files_delete(json_delete_file_input)
        print("The response of FilesApi->delete_file_api_files_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->delete_file_api_files_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_delete_file_input** | [**JsonDeleteFileInput**](JsonDeleteFileInput.md)|  | 

### Return type

[**JsonDeleteFileOutput**](JsonDeleteFileOutput.md)

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

