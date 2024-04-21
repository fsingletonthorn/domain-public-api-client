import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agencies_get_listings_listing_status_filter import AgenciesGetListingsListingStatusFilter
from ...models.domain_public_adapter_web_api_models_v1_listings_listing import (
    DomainPublicAdapterWebApiModelsV1ListingsListing,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    listing_status_filter: Union[Unset, AgenciesGetListingsListingStatusFilter] = UNSET,
    date_updated_since: Union[Unset, datetime.datetime] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_listing_status_filter: Union[Unset, str] = UNSET
    if not isinstance(listing_status_filter, Unset):
        json_listing_status_filter = listing_status_filter.value

    params["listingStatusFilter"] = json_listing_status_filter

    json_date_updated_since: Union[Unset, str] = UNSET
    if not isinstance(date_updated_since, Unset):
        json_date_updated_since = date_updated_since.isoformat()
    params["dateUpdatedSince"] = json_date_updated_since

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v1/agencies/{id}/listings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["DomainPublicAdapterWebApiModelsV1ListingsListing"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DomainPublicAdapterWebApiModelsV1ListingsListing.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["DomainPublicAdapterWebApiModelsV1ListingsListing"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    listing_status_filter: Union[Unset, AgenciesGetListingsListingStatusFilter] = UNSET,
    date_updated_since: Union[Unset, datetime.datetime] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[List["DomainPublicAdapterWebApiModelsV1ListingsListing"]]:
    """Retrieves listings across all channels for a specific agency matching specified criteria.

     Note that the result page size is clamped at 200.  Requesting a page size greater than this will be
    treated as if only a page size of 200 were requested.

    Args:
        id (int):
        listing_status_filter (Union[Unset, AgenciesGetListingsListingStatusFilter]):
        date_updated_since (Union[Unset, datetime.datetime]):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['DomainPublicAdapterWebApiModelsV1ListingsListing']]
    """

    kwargs = _get_kwargs(
        id=id,
        listing_status_filter=listing_status_filter,
        date_updated_since=date_updated_since,
        page_number=page_number,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    listing_status_filter: Union[Unset, AgenciesGetListingsListingStatusFilter] = UNSET,
    date_updated_since: Union[Unset, datetime.datetime] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[List["DomainPublicAdapterWebApiModelsV1ListingsListing"]]:
    """Retrieves listings across all channels for a specific agency matching specified criteria.

     Note that the result page size is clamped at 200.  Requesting a page size greater than this will be
    treated as if only a page size of 200 were requested.

    Args:
        id (int):
        listing_status_filter (Union[Unset, AgenciesGetListingsListingStatusFilter]):
        date_updated_since (Union[Unset, datetime.datetime]):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['DomainPublicAdapterWebApiModelsV1ListingsListing']
    """

    return sync_detailed(
        id=id,
        client=client,
        listing_status_filter=listing_status_filter,
        date_updated_since=date_updated_since,
        page_number=page_number,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    listing_status_filter: Union[Unset, AgenciesGetListingsListingStatusFilter] = UNSET,
    date_updated_since: Union[Unset, datetime.datetime] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[List["DomainPublicAdapterWebApiModelsV1ListingsListing"]]:
    """Retrieves listings across all channels for a specific agency matching specified criteria.

     Note that the result page size is clamped at 200.  Requesting a page size greater than this will be
    treated as if only a page size of 200 were requested.

    Args:
        id (int):
        listing_status_filter (Union[Unset, AgenciesGetListingsListingStatusFilter]):
        date_updated_since (Union[Unset, datetime.datetime]):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['DomainPublicAdapterWebApiModelsV1ListingsListing']]
    """

    kwargs = _get_kwargs(
        id=id,
        listing_status_filter=listing_status_filter,
        date_updated_since=date_updated_since,
        page_number=page_number,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    listing_status_filter: Union[Unset, AgenciesGetListingsListingStatusFilter] = UNSET,
    date_updated_since: Union[Unset, datetime.datetime] = UNSET,
    page_number: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[List["DomainPublicAdapterWebApiModelsV1ListingsListing"]]:
    """Retrieves listings across all channels for a specific agency matching specified criteria.

     Note that the result page size is clamped at 200.  Requesting a page size greater than this will be
    treated as if only a page size of 200 were requested.

    Args:
        id (int):
        listing_status_filter (Union[Unset, AgenciesGetListingsListingStatusFilter]):
        date_updated_since (Union[Unset, datetime.datetime]):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['DomainPublicAdapterWebApiModelsV1ListingsListing']
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            listing_status_filter=listing_status_filter,
            date_updated_since=date_updated_since,
            page_number=page_number,
            page_size=page_size,
        )
    ).parsed
