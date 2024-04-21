import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.listings_bypropertyid_sale_mode import ListingsBypropertyidSaleMode
from ...models.listings_v2_listing import ListingsV2Listing
from ...types import UNSET, Response, Unset


def _get_kwargs(
    property_id: str,
    *,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    listed_since: Union[Unset, datetime.datetime] = UNSET,
    sale_mode: Union[Unset, ListingsBypropertyidSaleMode] = ListingsBypropertyidSaleMode.BOTH,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_updated_since: Union[Unset, str] = UNSET
    if not isinstance(updated_since, Unset):
        json_updated_since = updated_since.isoformat()
    params["updatedSince"] = json_updated_since

    json_listed_since: Union[Unset, str] = UNSET
    if not isinstance(listed_since, Unset):
        json_listed_since = listed_since.isoformat()
    params["listedSince"] = json_listed_since

    json_sale_mode: Union[Unset, str] = UNSET
    if not isinstance(sale_mode, Unset):
        json_sale_mode = sale_mode.value

    params["saleMode"] = json_sale_mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/properties/{property_id}/listings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["ListingsV2Listing"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ListingsV2Listing.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["ListingsV2Listing"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    property_id: str,
    *,
    client: AuthenticatedClient,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    listed_since: Union[Unset, datetime.datetime] = UNSET,
    sale_mode: Union[Unset, ListingsBypropertyidSaleMode] = ListingsBypropertyidSaleMode.BOTH,
) -> Response[List["ListingsV2Listing"]]:
    """Retrieve list of listings for the given property id

    Args:
        property_id (str):
        updated_since (Union[Unset, datetime.datetime]):
        listed_since (Union[Unset, datetime.datetime]):
        sale_mode (Union[Unset, ListingsBypropertyidSaleMode]):  Default:
            ListingsBypropertyidSaleMode.BOTH.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['ListingsV2Listing']]
    """

    kwargs = _get_kwargs(
        property_id=property_id,
        updated_since=updated_since,
        listed_since=listed_since,
        sale_mode=sale_mode,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    property_id: str,
    *,
    client: AuthenticatedClient,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    listed_since: Union[Unset, datetime.datetime] = UNSET,
    sale_mode: Union[Unset, ListingsBypropertyidSaleMode] = ListingsBypropertyidSaleMode.BOTH,
) -> Optional[List["ListingsV2Listing"]]:
    """Retrieve list of listings for the given property id

    Args:
        property_id (str):
        updated_since (Union[Unset, datetime.datetime]):
        listed_since (Union[Unset, datetime.datetime]):
        sale_mode (Union[Unset, ListingsBypropertyidSaleMode]):  Default:
            ListingsBypropertyidSaleMode.BOTH.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['ListingsV2Listing']
    """

    return sync_detailed(
        property_id=property_id,
        client=client,
        updated_since=updated_since,
        listed_since=listed_since,
        sale_mode=sale_mode,
    ).parsed


async def asyncio_detailed(
    property_id: str,
    *,
    client: AuthenticatedClient,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    listed_since: Union[Unset, datetime.datetime] = UNSET,
    sale_mode: Union[Unset, ListingsBypropertyidSaleMode] = ListingsBypropertyidSaleMode.BOTH,
) -> Response[List["ListingsV2Listing"]]:
    """Retrieve list of listings for the given property id

    Args:
        property_id (str):
        updated_since (Union[Unset, datetime.datetime]):
        listed_since (Union[Unset, datetime.datetime]):
        sale_mode (Union[Unset, ListingsBypropertyidSaleMode]):  Default:
            ListingsBypropertyidSaleMode.BOTH.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['ListingsV2Listing']]
    """

    kwargs = _get_kwargs(
        property_id=property_id,
        updated_since=updated_since,
        listed_since=listed_since,
        sale_mode=sale_mode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    property_id: str,
    *,
    client: AuthenticatedClient,
    updated_since: Union[Unset, datetime.datetime] = UNSET,
    listed_since: Union[Unset, datetime.datetime] = UNSET,
    sale_mode: Union[Unset, ListingsBypropertyidSaleMode] = ListingsBypropertyidSaleMode.BOTH,
) -> Optional[List["ListingsV2Listing"]]:
    """Retrieve list of listings for the given property id

    Args:
        property_id (str):
        updated_since (Union[Unset, datetime.datetime]):
        listed_since (Union[Unset, datetime.datetime]):
        sale_mode (Union[Unset, ListingsBypropertyidSaleMode]):  Default:
            ListingsBypropertyidSaleMode.BOTH.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['ListingsV2Listing']
    """

    return (
        await asyncio_detailed(
            property_id=property_id,
            client=client,
            updated_since=updated_since,
            listed_since=listed_since,
            sale_mode=sale_mode,
        )
    ).parsed
