# API DOCUMENTATION

Welcome to the API documentation for a person management API called MyAPI. This API allows you perform Create, Read, Update, Delete (CRUD) operations on persons records

The **base URL** for all endpoints is "https://maryamsanni.pythonanywhere.com/api"

## Endpoints

### Create a new person

- Endpoint: `/api`

- Method: POST

- Description: Add a new person's record

- Request Body:

    - `name` (string, required): The person's name

    - `age` (integer): The person's age

    - `email` (string): The person's email address
    
    - `country` (string): The person's country of origin

#### An example request

``` http
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

``` http
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
``` http
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

``` http
GET /api/1
```
#### Example response

``` http
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
``` http
PUT /api/1
Content-Type: application/json

{
    "country": "Updated country"
}
```

#### Example Response

``` http
{
    "id": 1,
    "name": "Mary Jane"
    "age": 27,
    "country": "Updated country",
    "email": "maryjane@example.com"
}
```

### Delete Person by ID
- Endpoint: `/api/person_id`
- Method: DELETE
- Description: Delete a person by id

#### Example Request
``` http
DELETE /api/1
```
#### Example Response

``` http
{
 "message": "Person deleted successfully"
}
```

## Limitations

- Currently, there is no authentication implemented for these endpoints. Thes can be implemented if needed, for instance, in production use
- Getting person by name is case sensitive

## Setting up and running MyAPI locally

To set up and run this API, follow these steps

1. Clone the repository to your local machine

``` bash
git clone https://github.com/ayoblvck/CRUD-task.git
```

2. Ensure all dependencies are installed, if not, install them

``` bash
pip install -r requirements.txt

```

3. Configure the database, ensure that SQLite is set up

4. Run the API

5. Access teh API lically, by defailt it should be at http://localhost:5000/

6. Test the API using Postman or any other API testing tool to test that all CRUD operations work as expected

7. Dont forget to stop the local server after testing using 'Ctrl + C'