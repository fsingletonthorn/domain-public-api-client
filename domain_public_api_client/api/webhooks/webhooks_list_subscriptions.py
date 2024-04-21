from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.webhooks_v1_webhook_subscription import WebhooksV1WebhookSubscription
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    page_number: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v1/webhooks/{id}/subscriptions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["WebhooksV1WebhookSubscription"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = WebhooksV1WebhookSubscription.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["WebhooksV1WebhookSubscription"]]:
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
    page_number: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
) -> Response[List["WebhooksV1WebhookSubscription"]]:
    """List all subscriptions to the specified webhook

    Args:
        id (str):
        page_number (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['WebhooksV1WebhookSubscription']]
    """

    kwargs = _get_kwargs(
        id=id,
        page_number=page_number,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    page_number: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
) -> Optional[List["WebhooksV1WebhookSubscription"]]:
    """List all subscriptions to the specified webhook

    Args:
        id (str):
        page_number (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['WebhooksV1WebhookSubscription']
    """

    return sync_detailed(
        id=id,
        client=client,
        page_number=page_number,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    page_number: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
) -> Response[List["WebhooksV1WebhookSubscription"]]:
    """List all subscriptions to the specified webhook

    Args:
        id (str):
        page_number (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['WebhooksV1WebhookSubscription']]
    """

    kwargs = _get_kwargs(
        id=id,
        page_number=page_number,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    page_number: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
) -> Optional[List["WebhooksV1WebhookSubscription"]]:
    """List all subscriptions to the specified webhook

    Args:
        id (str):
        page_number (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['WebhooksV1WebhookSubscription']
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            page_number=page_number,
            page_size=page_size,
        )
    ).parsed
