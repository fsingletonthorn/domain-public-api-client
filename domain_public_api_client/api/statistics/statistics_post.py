from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.statistics_post_data_body import StatisticsPostDataBody
from ...models.statistics_post_event import StatisticsPostEvent
from ...models.statistics_post_json_body import StatisticsPostJsonBody
from ...types import Response


def _get_kwargs(
    event: StatisticsPostEvent,
    *,
    body: Union[
        StatisticsPostJsonBody,
        StatisticsPostDataBody,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/v1/statistics/{event}",
    }

    if isinstance(body, StatisticsPostJsonBody):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, StatisticsPostDataBody):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.ACCEPTED:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    event: StatisticsPostEvent,
    *,
    client: AuthenticatedClient,
    body: Union[
        StatisticsPostJsonBody,
        StatisticsPostDataBody,
    ],
) -> Response[Any]:
    """Record a statistic event along with its associated metadata (if applicable)

    Args:
        event (StatisticsPostEvent):
        body (StatisticsPostJsonBody):
        body (StatisticsPostDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        event=event,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    event: StatisticsPostEvent,
    *,
    client: AuthenticatedClient,
    body: Union[
        StatisticsPostJsonBody,
        StatisticsPostDataBody,
    ],
) -> Response[Any]:
    """Record a statistic event along with its associated metadata (if applicable)

    Args:
        event (StatisticsPostEvent):
        body (StatisticsPostJsonBody):
        body (StatisticsPostDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        event=event,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
