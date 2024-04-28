# domain-public-api-client
A client library for accessing Domain Public API generated using https://github.com/openapi-generators/openapi-python-client.

This client was generated using https://developer.domain.com.au/static/latest/media/lastet/openapi.json on 2024-04-21, which includes V1 and V2 of the API.

## Installation

...

## Usage

To access the Domain APIs you will need to first sign up for a developer account at https://developer.domain.com.au/.

Then, create a new project at https://developer.domain.com.au/projects/,  and set up credentials for your project in the Projects tab. The easiest way to consistently access this project - although not the most secure - is via a simple API key.

Once you have created an API key, you can then create a client using `AuthenticatedClient`, providing your API key as the token as per the below code chunk:

```python
from domain_public_api_client import AuthenticatedClient

client = AuthenticatedClient(
    base_url="https://api.domain.com.au/", 
    token="SuperSecretToken",
    auth_header_name='X-Api-Key',
    prefix=''
)

```

Now you can run a simple query for a property using a property ID like the below:

```python
from domain_public_api_client.api.listings import listings_get

listings_get.sync_detailed('2013958589', client = client)
```

Or call your endpoint and use your models:

```python

from domain_public_api_client.models import listings_v2_listing
from domain_public_api_client.api.listings import listings_get
from domain_public_api_client.types import Response

with client as client:
    my_data: listings_v2_listing = listings_get.sync(id = '2013958589', client=client)
    # or if you need more info (e.g. status_code)
    response: Response[listings_v2_listing] = listings_get.sync_detailed(id = '2013958589', client=client)

```

Or do the same thing with an async version:

```python
from domain_public_api_client.models import MyDataModel
from domain_public_api_client.api.my_tag import get_my_data_model
from domain_public_api_client.types import Response

async with client as client:
    my_data: MyDataModel = await get_my_data_model.asyncio(client=client)
    response: Response[MyDataModel] = await get_my_data_model.asyncio_detailed(client=client)
```

By default, when you're calling an HTTPS API it will attempt to verify that SSL is working correctly. Using certificate verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com", 
    token="SuperSecretToken",
    verify_ssl="/path/to/certificate_bundle.pem",
)
```

You can also disable certificate validation altogether, but beware that **this is a security risk**.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com", 
    token="SuperSecretToken", 
    verify_ssl=False
)
```

Things to know:
1. Every path/method combo becomes a Python module with four functions:
    1. `sync`: Blocking request that returns parsed data (if successful) or `None`
    1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
    1. `asyncio`: Like `sync` but async instead of blocking
    1. `asyncio_detailed`: Like `sync_detailed` but async instead of blocking

1. All path/query params, and bodies become method arguments.
1. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)
1. Any endpoint which did not have a tag will be in `domain_public_api_client.api.default`

## Advanced customizations

There are more settings on the generated `Client` class which let you control more runtime behavior, check out the docstring on that class for more info. You can also customize the underlying `httpx.Client` or `httpx.AsyncClient` (depending on your use-case):

```python
from domain_public_api_client import Client

def log_request(request):
    print(f"Request event hook: {request.method} {request.url} - Waiting for response")

def log_response(response):
    request = response.request
    print(f"Response event hook: {request.method} {request.url} - Status {response.status_code}")

client = Client(
    base_url="https://api.example.com",
    httpx_args={"event_hooks": {"request": [log_request], "response": [log_response]}},
)

# Or get the underlying httpx client to modify directly with client.get_httpx_client() or client.get_async_httpx_client()
```

You can even set the httpx client directly, but beware that this will override any existing settings (e.g., base_url):

```python
import httpx
from domain_public_api_client import Client

client = Client(
    base_url="https://api.example.com",
)
# Note that base_url needs to be re-set, as would any shared cookies, headers, etc.
client.set_httpx_client(httpx.Client(base_url="https://api.example.com", proxies="http://localhost:8030"))
```

## Updating this package
This project uses [Poetry](https://python-poetry.org/) to manage dependencies  and packaging.  Here are the basics:
1. Update the metadata in pyproject.toml (e.g. authors, version)
1. If you're using a private repository, configure it with Poetry
    1. `poetry config repositories.<your-repository-name> <url-to-your-repository>`
    1. `poetry config http-basic.<your-repository-name> <username> <password>`
1. Publish the client with `poetry publish --build -r <your-repository-name>` or, if for public PyPI, just `poetry publish --build`

If you want to install this client into another project without publishing it (e.g. for development) then:
1. If that project **is using Poetry**, you can simply do `poetry add <path-to-this-client>` from that project
1. If that project is not using Poetry:
    1. Build a wheel with `poetry build -f wheel`
    1. Install that wheel from the other project `pip install <path-to-wheel>`

## Developing
If you have a virtual environment, activate it before running poetry to avoid creating additional virutal envs (e.g., `.venv/Scripts/Activate`)
To develop in this package, make your changes, then update by running poetry install.