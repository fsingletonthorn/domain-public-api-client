from domain_public_api_client import Client

client = AuthenticatedClient(
    base_url="https://internal_api.example.com", 
    token="SuperSecretToken", 
    verify_ssl=False
)