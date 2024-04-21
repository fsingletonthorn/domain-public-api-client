from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.enquiries_v1_enquiry_report import EnquiriesV1EnquiryReport
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    page_number: Union[Unset, int] = 1,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["pageNumber"] = page_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v1/listings/{id}/enquiries",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["EnquiriesV1EnquiryReport"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = EnquiriesV1EnquiryReport.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["EnquiriesV1EnquiryReport"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    page_number: Union[Unset, int] = 1,
) -> Response[List["EnquiriesV1EnquiryReport"]]:
    """Retrieve details of all enquiries received for a specific listing

    Args:
        id (int):
        page_number (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['EnquiriesV1EnquiryReport']]
    """

    kwargs = _get_kwargs(
        id=id,
        page_number=page_number,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    page_number: Union[Unset, int] = 1,
) -> Optional[List["EnquiriesV1EnquiryReport"]]:
    """Retrieve details of all enquiries received for a specific listing

    Args:
        id (int):
        page_number (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['EnquiriesV1EnquiryReport']
    """

    return sync_detailed(
        id=id,
        client=client,
        page_number=page_number,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    page_number: Union[Unset, int] = 1,
) -> Response[List["EnquiriesV1EnquiryReport"]]:
    """Retrieve details of all enquiries received for a specific listing

    Args:
        id (int):
        page_number (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['EnquiriesV1EnquiryReport']]
    """

    kwargs = _get_kwargs(
        id=id,
        page_number=page_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    page_number: Union[Unset, int] = 1,
) -> Optional[List["EnquiriesV1EnquiryReport"]]:
    """Retrieve details of all enquiries received for a specific listing

    Args:
        id (int):
        page_number (Union[Unset, int]):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['EnquiriesV1EnquiryReport']
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            page_number=page_number,
        )
    ).parsed
