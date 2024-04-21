from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pre_market_v1_listing_response import PreMarketV1ListingResponse
from ...models.pre_market_v1_problem_details import PreMarketV1ProblemDetails
from ...types import Response


def _get_kwargs(
    id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/premarket/listings/{id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PreMarketV1ListingResponse, PreMarketV1ProblemDetails]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PreMarketV1ListingResponse.from_dict(response.text)

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = PreMarketV1ProblemDetails.from_dict(response.text)

        return response_404
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = PreMarketV1ProblemDetails.from_dict(response.text)

        return response_409
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = PreMarketV1ProblemDetails.from_dict(response.text)

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, PreMarketV1ListingResponse, PreMarketV1ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, PreMarketV1ListingResponse, PreMarketV1ProblemDetails]]:
    """Retrieves a pre-portal listing.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PreMarketV1ListingResponse, PreMarketV1ProblemDetails]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, PreMarketV1ListingResponse, PreMarketV1ProblemDetails]]:
    """Retrieves a pre-portal listing.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PreMarketV1ListingResponse, PreMarketV1ProblemDetails]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, PreMarketV1ListingResponse, PreMarketV1ProblemDetails]]:
    """Retrieves a pre-portal listing.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PreMarketV1ListingResponse, PreMarketV1ProblemDetails]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, PreMarketV1ListingResponse, PreMarketV1ProblemDetails]]:
    """Retrieves a pre-portal listing.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PreMarketV1ListingResponse, PreMarketV1ProblemDetails]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
