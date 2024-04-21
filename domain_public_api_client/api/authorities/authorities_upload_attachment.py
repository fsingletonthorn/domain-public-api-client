from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.authorities_v1_attachments import AuthoritiesV1Attachments
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: List["AuthoritiesV1Attachments"],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/v1/authorities/{id}/attachments",
    }

    _body = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _body.append(body_item)

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["AuthoritiesV1Attachments"]]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = []
        _response_201 = response.json()
        for response_201_item_data in _response_201:
            response_201_item = AuthoritiesV1Attachments.from_dict(response_201_item_data)

            response_201.append(response_201_item)

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, List["AuthoritiesV1Attachments"]]]:
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
    body: List["AuthoritiesV1Attachments"],
) -> Response[Union[Any, List["AuthoritiesV1Attachments"]]]:
    """Upload multiple files to an authority.

     Upload multiple files to be attached to an authority based on the given `id`.

    Args:
        id (str):
        body (List['AuthoritiesV1Attachments']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['AuthoritiesV1Attachments']]]
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
    body: List["AuthoritiesV1Attachments"],
) -> Optional[Union[Any, List["AuthoritiesV1Attachments"]]]:
    """Upload multiple files to an authority.

     Upload multiple files to be attached to an authority based on the given `id`.

    Args:
        id (str):
        body (List['AuthoritiesV1Attachments']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['AuthoritiesV1Attachments']]
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
    body: List["AuthoritiesV1Attachments"],
) -> Response[Union[Any, List["AuthoritiesV1Attachments"]]]:
    """Upload multiple files to an authority.

     Upload multiple files to be attached to an authority based on the given `id`.

    Args:
        id (str):
        body (List['AuthoritiesV1Attachments']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['AuthoritiesV1Attachments']]]
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
    body: List["AuthoritiesV1Attachments"],
) -> Optional[Union[Any, List["AuthoritiesV1Attachments"]]]:
    """Upload multiple files to an authority.

     Upload multiple files to be attached to an authority based on the given `id`.

    Args:
        id (str):
        body (List['AuthoritiesV1Attachments']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['AuthoritiesV1Attachments']]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
