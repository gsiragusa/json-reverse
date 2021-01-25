# JSON Reverse

This is a simple REST API service that takes an input JSON and reverses the order of elements in the JSON. 

For instance, an input JSON with the following content
```json
{
    "a":1,
    "b":1,
    "c":1,
    "d":1,
    "e":1
}
```

will be returned as follows
```json
{
    "e":1,
    "d":1,
    "c":1,
    "b":1,
    "a":1
}
```

The service also works with nested JSON objects, and reverses the order of the inner keys as well

## Endpoint
| Method | Signature | Authentication | Content-Type | Sample Body | Sample Response |   
| --- | --- | --- | --- | --- | --- |
| POST | /reverse | None | application/json | `{"a": 1, "b": 2}` | `{"b": 2, "a": 1}` |

## Responses
The endpoint returns the reversed JSON object received in the request. However, if an invalid request is submitted, or some other error occurs, it returns a JSON response in the following format
```json
{
  "message": string,
  "error_code": int
}
```

# Status Codes
The service returns the following status codes

| Status Code | Description |
| --- | --- |
| 200 | OK |
| 400 | BAD REQUEST |
| 404 | NOT FOUND |
| 405 | METHOD NOT ALLOWED |
| 500 | INTERNAL SERVER ERROR |