# API DOCUMENTATION

Welcome to my API documentation for a test API. This API allows yoy perform Create, Read, Update, Delete (CRUD) operations on person records

The **base URL** for all endpoints is []("https://maryamsanni.pythonanywhere.com/api")

## Endpoints

### Create a new person

- Endpoint: '/api'

- Method: POST

- Description: Add a new persons record and detais

- Request Body:

    - **name** (string, required): The person's name

    - **age** (integer): The person's age

    - **email** (string): the person's email address
    
    - **country** (string): the person's country of origin

#### An example request

```
POST /api
Content-Type: application/json

{
    "name": "Mary Jane",
    "age": 27,
    "country": "Nigeria",
    "email": "maryjane@example.com"
}

```

#### An example response

```
"message": "Person added successfully"
"person": {
    "id": 1,
    "name": "Mary Jane"
    "age": 27,
    "country": "Nigeria",
    "email": "maryjane@example.com"
}
```
### Get details of all persons

- Endpoint: `/api/persons`
- Method: GET
- Description: Gets a list of all persons in the database

#### Example request

``` http
GET /api/persons
```
#### Example response
```
[
    {
        "id": 1,
        "name": "Mary Jane"
        "age": 27,
        "country": "Nigeria",
        "email": "maryjane@example.com"
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "age": 25,
        "country": "America",
        "email": "janesmith@example.com"
    }
]

```
### Get details by id

- Endpoint: `/api/person_id`
- Method: GET
- Description: Gets the details of a persons by id

#### Example request

```
GET /api/1
```
#### Example response

```
{
    "id": 1,
    "name": "Mary Jane"
    "age": 27,
    "country": "Nigeria",
    "email": "maryjane@example.com"
},
```

### Update Person by ID

- Endpoint: `/api/person_id`
- Method: PUT
- Description: Updates the details of a person by id
- Request Body: Any of the following fields (name, age, country, email) can be included to update.

#### Example Request
```
PUT /api/1
Content-Type: application/json

{
    "country": "Updated country"
}
```

#### Example Response

```
{
    "id": 1,
    "name": "Mary Jane"
    "age": 27,
    "country": "Updated country",
    "email": "maryjane@example.com"
},
```

### Delete Person by ID
- Endpoint: `/api/person_id`
- Method: DELETE
- Description: Delete a person by id

#### Example Request
```
DELETE /api/1
```
#### Example Response

```
{
 "message": "Person deleted successfully"
}
```

## Limitations

- Currently, there is no authentication implemented for these endpoints. Thes can be implemented if needed, for instance, in production use