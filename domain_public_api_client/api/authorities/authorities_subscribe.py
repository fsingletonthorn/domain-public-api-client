from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.authorities_v1_subscription_request import AuthoritiesV1SubscriptionRequest
from ...models.authorities_v1_subscription_response import AuthoritiesV1SubscriptionResponse
from ...types import Response


def _get_kwargs(
    *,
    body: AuthoritiesV1SubscriptionRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/v1/authorities/webhooks/subscription",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, AuthoritiesV1SubscriptionResponse]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = AuthoritiesV1SubscriptionResponse.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, AuthoritiesV1SubscriptionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AuthoritiesV1SubscriptionRequest,
) -> Response[Union[Any, AuthoritiesV1SubscriptionResponse]]:
    """Subscribe to an agency for all its authorities

     Subscribe to an agency to get notified on changes made to the authorities in that agencies scope.

    Args:
        body (AuthoritiesV1SubscriptionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AuthoritiesV1SubscriptionResponse]]
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
    body: AuthoritiesV1SubscriptionRequest,
) -> Optional[Union[Any, AuthoritiesV1SubscriptionResponse]]:
    """Subscribe to an agency for all its authorities

     Subscribe to an agency to get notified on changes made to the authorities in that agencies scope.

    Args:
        body (AuthoritiesV1SubscriptionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AuthoritiesV1SubscriptionResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AuthoritiesV1SubscriptionRequest,
) -> Response[Union[Any, AuthoritiesV1SubscriptionResponse]]:
    """Subscribe to an agency for all its authorities

     Subscribe to an agency to get notified on changes made to the authorities in that agencies scope.

    Args:
        body (AuthoritiesV1SubscriptionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AuthoritiesV1SubscriptionResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AuthoritiesV1SubscriptionRequest,
) -> Optional[Union[Any, AuthoritiesV1SubscriptionResponse]]:
    """Subscribe to an agency for all its authorities

     Subscribe to an agency to get notified on changes made to the authorities in that agencies scope.

    Args:
        body (AuthoritiesV1SubscriptionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AuthoritiesV1SubscriptionResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
