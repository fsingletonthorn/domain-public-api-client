from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bookings_v2_rate_for_new_listing import BookingsV2RateForNewListing
from ...models.bookings_v2_rate_for_new_listing_request import BookingsV2RateForNewListingRequest
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        BookingsV2RateForNewListingRequest,
        BookingsV2RateForNewListingRequest,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/products/ratefornewlisting",
    }

    if isinstance(body, BookingsV2RateForNewListingRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, BookingsV2RateForNewListingRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[BookingsV2RateForNewListing]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BookingsV2RateForNewListing.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[BookingsV2RateForNewListing]:
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
        BookingsV2RateForNewListingRequest,
        BookingsV2RateForNewListingRequest,
    ],
) -> Response[BookingsV2RateForNewListing]:
    """Get updated pricing information for a hypothetical listing

    Args:
        body (BookingsV2RateForNewListingRequest): Provide a summary of the intended listing for
            which to calculate a rate.
        body (BookingsV2RateForNewListingRequest): Provide a summary of the intended listing for
            which to calculate a rate.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BookingsV2RateForNewListing]
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
        BookingsV2RateForNewListingRequest,
        BookingsV2RateForNewListingRequest,
    ],
) -> Optional[BookingsV2RateForNewListing]:
    """Get updated pricing information for a hypothetical listing

    Args:
        body (BookingsV2RateForNewListingRequest): Provide a summary of the intended listing for
            which to calculate a rate.
        body (BookingsV2RateForNewListingRequest): Provide a summary of the intended listing for
            which to calculate a rate.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BookingsV2RateForNewListing
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        BookingsV2RateForNewListingRequest,
        BookingsV2RateForNewListingRequest,
    ],
) -> Response[BookingsV2RateForNewListing]:
    """Get updated pricing information for a hypothetical listing

    Args:
        body (BookingsV2RateForNewListingRequest): Provide a summary of the intended listing for
            which to calculate a rate.
        body (BookingsV2RateForNewListingRequest): Provide a summary of the intended listing for
            which to calculate a rate.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BookingsV2RateForNewListing]
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
        BookingsV2RateForNewListingRequest,
        BookingsV2RateForNewListingRequest,
    ],
) -> Optional[BookingsV2RateForNewListing]:
    """Get updated pricing information for a hypothetical listing

    Args:
        body (BookingsV2RateForNewListingRequest): Provide a summary of the intended listing for
            which to calculate a rate.
        body (BookingsV2RateForNewListingRequest): Provide a summary of the intended listing for
            which to calculate a rate.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BookingsV2RateForNewListing
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
