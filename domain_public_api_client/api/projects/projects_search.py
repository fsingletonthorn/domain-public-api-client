from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.listings_v2_project import ListingsV2Project
from ...models.projects_search_project_status import ProjectsSearchProjectStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    agency_id: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
    project_status: Union[Unset, ProjectsSearchProjectStatus] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["agencyId"] = agency_id

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    json_project_status: Union[Unset, str] = UNSET
    if not isinstance(project_status, Unset):
        json_project_status = project_status.value

    params["projectStatus"] = json_project_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["ListingsV2Project"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ListingsV2Project.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["ListingsV2Project"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    agency_id: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
    project_status: Union[Unset, ProjectsSearchProjectStatus] = UNSET,
) -> Response[List["ListingsV2Project"]]:
    """Searches projects

     Note that the result page size is clamped at 100.  Requesting a page size greater than this will be
    treated as if only a page size of 100 were requested.

    Args:
        agency_id (Union[Unset, int]):
        page_number (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 20.
        project_status (Union[Unset, ProjectsSearchProjectStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['ListingsV2Project']]
    """

    kwargs = _get_kwargs(
        agency_id=agency_id,
        page_number=page_number,
        page_size=page_size,
        project_status=project_status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    agency_id: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
    project_status: Union[Unset, ProjectsSearchProjectStatus] = UNSET,
) -> Optional[List["ListingsV2Project"]]:
    """Searches projects

     Note that the result page size is clamped at 100.  Requesting a page size greater than this will be
    treated as if only a page size of 100 were requested.

    Args:
        agency_id (Union[Unset, int]):
        page_number (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 20.
        project_status (Union[Unset, ProjectsSearchProjectStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['ListingsV2Project']
    """

    return sync_detailed(
        client=client,
        agency_id=agency_id,
        page_number=page_number,
        page_size=page_size,
        project_status=project_status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    agency_id: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
    project_status: Union[Unset, ProjectsSearchProjectStatus] = UNSET,
) -> Response[List["ListingsV2Project"]]:
    """Searches projects

     Note that the result page size is clamped at 100.  Requesting a page size greater than this will be
    treated as if only a page size of 100 were requested.

    Args:
        agency_id (Union[Unset, int]):
        page_number (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 20.
        project_status (Union[Unset, ProjectsSearchProjectStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['ListingsV2Project']]
    """

    kwargs = _get_kwargs(
        agency_id=agency_id,
        page_number=page_number,
        page_size=page_size,
        project_status=project_status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    agency_id: Union[Unset, int] = UNSET,
    page_number: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
    project_status: Union[Unset, ProjectsSearchProjectStatus] = UNSET,
) -> Optional[List["ListingsV2Project"]]:
    """Searches projects

     Note that the result page size is clamped at 100.  Requesting a page size greater than this will be
    treated as if only a page size of 100 were requested.

    Args:
        agency_id (Union[Unset, int]):
        page_number (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 20.
        project_status (Union[Unset, ProjectsSearchProjectStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['ListingsV2Project']
    """

    return (
        await asyncio_detailed(
            client=client,
            agency_id=agency_id,
            page_number=page_number,
            page_size=page_size,
            project_status=project_status,
        )
    ).parsed
