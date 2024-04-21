from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domain_public_adapter_web_api_models_v1_listings_business_listing import (
    DomainPublicAdapterWebApiModelsV1ListingsBusinessListing,
)
from ...models.domain_public_adapter_web_api_models_v1_listings_business_search_request import (
    DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequest,
)
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequest,
        DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequest,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/listings/business/_search",
    }

    if isinstance(body, DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequest):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["DomainPublicAdapterWebApiModelsV1ListingsBusinessListing"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DomainPublicAdapterWebApiModelsV1ListingsBusinessListing.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["DomainPublicAdapterWebApiModelsV1ListingsBusinessListing"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequest,
        DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequest,
    ],
) -> Response[List["DomainPublicAdapterWebApiModelsV1ListingsBusinessListing"]]:
    """Retrieves business listings matching the specified criteria.

    Args:
        body (DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequest): Represents a CRE
            Business Search Request
        body (DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequest): Represents a CRE
            Business Search Request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['DomainPublicAdapterWebApiModelsV1ListingsBusinessListing']]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: Union[
        DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequest,
        DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequest,
    ],
) -> Optional[List["DomainPublicAdapterWebApiModelsV1ListingsBusinessListing"]]:
    """Retrieves business listings matching the specified criteria.

    Args:
        body (DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequest): Represents a CRE
            Business Search Request
        body (DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequest): Represents a CRE
            Business Search Request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['DomainPublicAdapterWebApiModelsV1ListingsBusinessListing']
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequest,
        DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequest,
    ],
) -> Response[List["DomainPublicAdapterWebApiModelsV1ListingsBusinessListing"]]:
    """Retrieves business listings matching the specified criteria.

    Args:
        body (DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequest): Represents a CRE
            Business Search Request
        body (DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequest): Represents a CRE
            Business Search Request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['DomainPublicAdapterWebApiModelsV1ListingsBusinessListing']]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union[
        DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequest,
        DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequest,
    ],
) -> Optional[List["DomainPublicAdapterWebApiModelsV1ListingsBusinessListing"]]:
    """Retrieves business listings matching the specified criteria.

    Args:
        body (DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequest): Represents a CRE
            Business Search Request
        body (DomainPublicAdapterWebApiModelsV1ListingsBusinessSearchRequest): Represents a CRE
            Business Search Request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['DomainPublicAdapterWebApiModelsV1ListingsBusinessListing']
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
