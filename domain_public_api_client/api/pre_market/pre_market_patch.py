from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pre_market_v1_listing_request import PreMarketV1ListingRequest
from ...models.pre_market_v1_listing_request_json_patch_document import PreMarketV1ListingRequestJsonPatchDocument
from ...models.pre_market_v1_problem_details import PreMarketV1ProblemDetails
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: Union[
        PreMarketV1ListingRequestJsonPatchDocument,
        PreMarketV1ListingRequestJsonPatchDocument,
        PreMarketV1ListingRequestJsonPatchDocument,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/v2/premarket/listings/{id}",
    }

    if isinstance(body, PreMarketV1ListingRequestJsonPatchDocument):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, PreMarketV1ListingRequestJsonPatchDocument):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, PreMarketV1ListingRequestJsonPatchDocument):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PreMarketV1ListingRequest, PreMarketV1ProblemDetails]]:
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = PreMarketV1ListingRequest.from_dict(response.text)

        return response_202
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = PreMarketV1ProblemDetails.from_dict(response.text)

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = PreMarketV1ProblemDetails.from_dict(response.text)

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = PreMarketV1ProblemDetails.from_dict(response.text)

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, PreMarketV1ListingRequest, PreMarketV1ProblemDetails]]:
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
    body: Union[
        PreMarketV1ListingRequestJsonPatchDocument,
        PreMarketV1ListingRequestJsonPatchDocument,
        PreMarketV1ListingRequestJsonPatchDocument,
    ],
) -> Response[Union[Any, PreMarketV1ListingRequest, PreMarketV1ProblemDetails]]:
    """Patches a pre-portal listing.

    Args:
        id (str):
        body (PreMarketV1ListingRequestJsonPatchDocument):
        body (PreMarketV1ListingRequestJsonPatchDocument):
        body (PreMarketV1ListingRequestJsonPatchDocument):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PreMarketV1ListingRequest, PreMarketV1ProblemDetails]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        PreMarketV1ListingRequestJsonPatchDocument,
        PreMarketV1ListingRequestJsonPatchDocument,
        PreMarketV1ListingRequestJsonPatchDocument,
    ],
) -> Optional[Union[Any, PreMarketV1ListingRequest, PreMarketV1ProblemDetails]]:
    """Patches a pre-portal listing.

    Args:
        id (str):
        body (PreMarketV1ListingRequestJsonPatchDocument):
        body (PreMarketV1ListingRequestJsonPatchDocument):
        body (PreMarketV1ListingRequestJsonPatchDocument):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PreMarketV1ListingRequest, PreMarketV1ProblemDetails]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        PreMarketV1ListingRequestJsonPatchDocument,
        PreMarketV1ListingRequestJsonPatchDocument,
        PreMarketV1ListingRequestJsonPatchDocument,
    ],
) -> Response[Union[Any, PreMarketV1ListingRequest, PreMarketV1ProblemDetails]]:
    """Patches a pre-portal listing.

    Args:
        id (str):
        body (PreMarketV1ListingRequestJsonPatchDocument):
        body (PreMarketV1ListingRequestJsonPatchDocument):
        body (PreMarketV1ListingRequestJsonPatchDocument):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PreMarketV1ListingRequest, PreMarketV1ProblemDetails]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        PreMarketV1ListingRequestJsonPatchDocument,
        PreMarketV1ListingRequestJsonPatchDocument,
        PreMarketV1ListingRequestJsonPatchDocument,
    ],
) -> Optional[Union[Any, PreMarketV1ListingRequest, PreMarketV1ProblemDetails]]:
    """Patches a pre-portal listing.

    Args:
        id (str):
        body (PreMarketV1ListingRequestJsonPatchDocument):
        body (PreMarketV1ListingRequestJsonPatchDocument):
        body (PreMarketV1ListingRequestJsonPatchDocument):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PreMarketV1ListingRequest, PreMarketV1ProblemDetails]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
