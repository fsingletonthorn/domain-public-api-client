from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domain_public_adapter_web_api_models_v1_listings_commercial_listing import (
    DomainPublicAdapterWebApiModelsV1ListingsCommercialListing,
)
from ...models.domain_public_adapter_web_api_models_v1_listings_commercial_search_request import (
    DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest,
)
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest,
        DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/listings/commercial/_search",
    }

    if isinstance(body, DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["DomainPublicAdapterWebApiModelsV1ListingsCommercialListing"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DomainPublicAdapterWebApiModelsV1ListingsCommercialListing.from_dict(
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
) -> Response[List["DomainPublicAdapterWebApiModelsV1ListingsCommercialListing"]]:
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
        DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest,
        DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest,
    ],
) -> Response[List["DomainPublicAdapterWebApiModelsV1ListingsCommercialListing"]]:
    """Retrieves commercial listings matching the specified criteria.

    Args:
        body (DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest): Listing search
            criteria
        body (DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest): Listing search
            criteria

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['DomainPublicAdapterWebApiModelsV1ListingsCommercialListing']]
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
        DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest,
        DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest,
    ],
) -> Optional[List["DomainPublicAdapterWebApiModelsV1ListingsCommercialListing"]]:
    """Retrieves commercial listings matching the specified criteria.

    Args:
        body (DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest): Listing search
            criteria
        body (DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest): Listing search
            criteria

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['DomainPublicAdapterWebApiModelsV1ListingsCommercialListing']
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest,
        DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest,
    ],
) -> Response[List["DomainPublicAdapterWebApiModelsV1ListingsCommercialListing"]]:
    """Retrieves commercial listings matching the specified criteria.

    Args:
        body (DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest): Listing search
            criteria
        body (DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest): Listing search
            criteria

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['DomainPublicAdapterWebApiModelsV1ListingsCommercialListing']]
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
        DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest,
        DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest,
    ],
) -> Optional[List["DomainPublicAdapterWebApiModelsV1ListingsCommercialListing"]]:
    """Retrieves commercial listings matching the specified criteria.

    Args:
        body (DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest): Listing search
            criteria
        body (DomainPublicAdapterWebApiModelsV1ListingsCommercialSearchRequest): Listing search
            criteria

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['DomainPublicAdapterWebApiModelsV1ListingsCommercialListing']
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
