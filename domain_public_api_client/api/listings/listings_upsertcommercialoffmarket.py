from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.listing_admin_v2_commercial_off_market_listing import ListingAdminV2CommercialOffMarketListing
from ...models.listing_admin_v2_listing_response import ListingAdminV2ListingResponse
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        ListingAdminV2CommercialOffMarketListing,
        ListingAdminV2CommercialOffMarketListing,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v2/listings/commercial/offmarket",
    }

    if isinstance(body, ListingAdminV2CommercialOffMarketListing):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, ListingAdminV2CommercialOffMarketListing):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ListingAdminV2ListingResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListingAdminV2ListingResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = ListingAdminV2ListingResponse.from_dict(response.json())

        return response_202
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ListingAdminV2ListingResponse]]:
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
        ListingAdminV2CommercialOffMarketListing,
        ListingAdminV2CommercialOffMarketListing,
    ],
) -> Response[Union[Any, ListingAdminV2ListingResponse]]:
    """Creates an externally sold or leased commercial listing; or takes an existing commercial listing off
    the market.

    Args:
        body (ListingAdminV2CommercialOffMarketListing): Commercial off market listing
        body (ListingAdminV2CommercialOffMarketListing): Commercial off market listing

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListingAdminV2ListingResponse]]
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
        ListingAdminV2CommercialOffMarketListing,
        ListingAdminV2CommercialOffMarketListing,
    ],
) -> Optional[Union[Any, ListingAdminV2ListingResponse]]:
    """Creates an externally sold or leased commercial listing; or takes an existing commercial listing off
    the market.

    Args:
        body (ListingAdminV2CommercialOffMarketListing): Commercial off market listing
        body (ListingAdminV2CommercialOffMarketListing): Commercial off market listing

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListingAdminV2ListingResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        ListingAdminV2CommercialOffMarketListing,
        ListingAdminV2CommercialOffMarketListing,
    ],
) -> Response[Union[Any, ListingAdminV2ListingResponse]]:
    """Creates an externally sold or leased commercial listing; or takes an existing commercial listing off
    the market.

    Args:
        body (ListingAdminV2CommercialOffMarketListing): Commercial off market listing
        body (ListingAdminV2CommercialOffMarketListing): Commercial off market listing

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListingAdminV2ListingResponse]]
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
        ListingAdminV2CommercialOffMarketListing,
        ListingAdminV2CommercialOffMarketListing,
    ],
) -> Optional[Union[Any, ListingAdminV2ListingResponse]]:
    """Creates an externally sold or leased commercial listing; or takes an existing commercial listing off
    the market.

    Args:
        body (ListingAdminV2CommercialOffMarketListing): Commercial off market listing
        body (ListingAdminV2CommercialOffMarketListing): Commercial off market listing

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListingAdminV2ListingResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
