from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.webhooks_v1_add_subscription_request import WebhooksV1AddSubscriptionRequest
from ...models.webhooks_v1_webhook_subscription import WebhooksV1WebhookSubscription
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: Union[
        WebhooksV1AddSubscriptionRequest,
        WebhooksV1AddSubscriptionRequest,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/v1/webhooks/{id}/subscriptions",
    }

    if isinstance(body, WebhooksV1AddSubscriptionRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, WebhooksV1AddSubscriptionRequest):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[WebhooksV1WebhookSubscription]:
    if response.status_code == HTTPStatus.OK:
        response_200 = WebhooksV1WebhookSubscription.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.CREATED:
        response_201 = WebhooksV1WebhookSubscription.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[WebhooksV1WebhookSubscription]:
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
        WebhooksV1AddSubscriptionRequest,
        WebhooksV1AddSubscriptionRequest,
    ],
) -> Response[WebhooksV1WebhookSubscription]:
    """Create a subscription to notifications

    Args:
        id (str):
        body (WebhooksV1AddSubscriptionRequest): AddSubscriptionRequest
        body (WebhooksV1AddSubscriptionRequest): AddSubscriptionRequest

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhooksV1WebhookSubscription]
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
        WebhooksV1AddSubscriptionRequest,
        WebhooksV1AddSubscriptionRequest,
    ],
) -> Optional[WebhooksV1WebhookSubscription]:
    """Create a subscription to notifications

    Args:
        id (str):
        body (WebhooksV1AddSubscriptionRequest): AddSubscriptionRequest
        body (WebhooksV1AddSubscriptionRequest): AddSubscriptionRequest

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhooksV1WebhookSubscription
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
        WebhooksV1AddSubscriptionRequest,
        WebhooksV1AddSubscriptionRequest,
    ],
) -> Response[WebhooksV1WebhookSubscription]:
    """Create a subscription to notifications

    Args:
        id (str):
        body (WebhooksV1AddSubscriptionRequest): AddSubscriptionRequest
        body (WebhooksV1AddSubscriptionRequest): AddSubscriptionRequest

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhooksV1WebhookSubscription]
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
        WebhooksV1AddSubscriptionRequest,
        WebhooksV1AddSubscriptionRequest,
    ],
) -> Optional[WebhooksV1WebhookSubscription]:
    """Create a subscription to notifications

    Args:
        id (str):
        body (WebhooksV1AddSubscriptionRequest): AddSubscriptionRequest
        body (WebhooksV1AddSubscriptionRequest): AddSubscriptionRequest

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhooksV1WebhookSubscription
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
