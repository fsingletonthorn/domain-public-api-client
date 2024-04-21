from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agencies_v2_agency_summary import AgenciesV2AgencySummary
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: Union[Unset, str] = UNSET,
    page_number: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["q"] = q

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/agencies",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["AgenciesV2AgencySummary"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AgenciesV2AgencySummary.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["AgenciesV2AgencySummary"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, str] = UNSET,
    page_number: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
) -> Response[List["AgenciesV2AgencySummary"]]:
    r"""Retrieves summary of agencies matching the specified criteria.

     <br>The ```q``` parameter supports:
    <ul>
      <li>name: search by name eg. ```name:\"Agency XYZ\"```</li>
      <li>providerId: search by providerId. eg. ```providerId:\"ABC Software\"```</li>
      <li>domainUrl: search by domainUrl. eg. ```domainUrl:\"agency-xyz\"```</li>
      <li>dateUpdated: search by dateUpdated. eg. ```dateUpdated:\"2016-12-25\"```</li>
      <li>suburbId: search by suburbId. Lists supported.  eg. ```suburbId:1``` eg. ```suburbId:(1 OR 2
    OR 3)```.  Can include related suburbs by adding ```in:related```</li>
      <li>accountType: search by account type. Lists supported.  eg. ```accountType:residential``` eg.
    ```accountType:(residential OR commercial)``` Valid values are: none, residential, commerciallight,
    commercialfull, developer, holiday, business</li>
      <li>
        ```in:all``` includes archived agencies (archived agencies excluded by default)</li>
      <li>
        ```-is:selfservice``` excludes selfservice</li>
    </ul>

    Args:
        q (Union[Unset, str]):
        page_number (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['AgenciesV2AgencySummary']]
    """

    kwargs = _get_kwargs(
        q=q,
        page_number=page_number,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, str] = UNSET,
    page_number: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
) -> Optional[List["AgenciesV2AgencySummary"]]:
    r"""Retrieves summary of agencies matching the specified criteria.

     <br>The ```q``` parameter supports:
    <ul>
      <li>name: search by name eg. ```name:\"Agency XYZ\"```</li>
      <li>providerId: search by providerId. eg. ```providerId:\"ABC Software\"```</li>
      <li>domainUrl: search by domainUrl. eg. ```domainUrl:\"agency-xyz\"```</li>
      <li>dateUpdated: search by dateUpdated. eg. ```dateUpdated:\"2016-12-25\"```</li>
      <li>suburbId: search by suburbId. Lists supported.  eg. ```suburbId:1``` eg. ```suburbId:(1 OR 2
    OR 3)```.  Can include related suburbs by adding ```in:related```</li>
      <li>accountType: search by account type. Lists supported.  eg. ```accountType:residential``` eg.
    ```accountType:(residential OR commercial)``` Valid values are: none, residential, commerciallight,
    commercialfull, developer, holiday, business</li>
      <li>
        ```in:all``` includes archived agencies (archived agencies excluded by default)</li>
      <li>
        ```-is:selfservice``` excludes selfservice</li>
    </ul>

    Args:
        q (Union[Unset, str]):
        page_number (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['AgenciesV2AgencySummary']
    """

    return sync_detailed(
        client=client,
        q=q,
        page_number=page_number,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, str] = UNSET,
    page_number: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
) -> Response[List["AgenciesV2AgencySummary"]]:
    r"""Retrieves summary of agencies matching the specified criteria.

     <br>The ```q``` parameter supports:
    <ul>
      <li>name: search by name eg. ```name:\"Agency XYZ\"```</li>
      <li>providerId: search by providerId. eg. ```providerId:\"ABC Software\"```</li>
      <li>domainUrl: search by domainUrl. eg. ```domainUrl:\"agency-xyz\"```</li>
      <li>dateUpdated: search by dateUpdated. eg. ```dateUpdated:\"2016-12-25\"```</li>
      <li>suburbId: search by suburbId. Lists supported.  eg. ```suburbId:1``` eg. ```suburbId:(1 OR 2
    OR 3)```.  Can include related suburbs by adding ```in:related```</li>
      <li>accountType: search by account type. Lists supported.  eg. ```accountType:residential``` eg.
    ```accountType:(residential OR commercial)``` Valid values are: none, residential, commerciallight,
    commercialfull, developer, holiday, business</li>
      <li>
        ```in:all``` includes archived agencies (archived agencies excluded by default)</li>
      <li>
        ```-is:selfservice``` excludes selfservice</li>
    </ul>

    Args:
        q (Union[Unset, str]):
        page_number (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['AgenciesV2AgencySummary']]
    """

    kwargs = _get_kwargs(
        q=q,
        page_number=page_number,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, str] = UNSET,
    page_number: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
) -> Optional[List["AgenciesV2AgencySummary"]]:
    r"""Retrieves summary of agencies matching the specified criteria.

     <br>The ```q``` parameter supports:
    <ul>
      <li>name: search by name eg. ```name:\"Agency XYZ\"```</li>
      <li>providerId: search by providerId. eg. ```providerId:\"ABC Software\"```</li>
      <li>domainUrl: search by domainUrl. eg. ```domainUrl:\"agency-xyz\"```</li>
      <li>dateUpdated: search by dateUpdated. eg. ```dateUpdated:\"2016-12-25\"```</li>
      <li>suburbId: search by suburbId. Lists supported.  eg. ```suburbId:1``` eg. ```suburbId:(1 OR 2
    OR 3)```.  Can include related suburbs by adding ```in:related```</li>
      <li>accountType: search by account type. Lists supported.  eg. ```accountType:residential``` eg.
    ```accountType:(residential OR commercial)``` Valid values are: none, residential, commerciallight,
    commercialfull, developer, holiday, business</li>
      <li>
        ```in:all``` includes archived agencies (archived agencies excluded by default)</li>
      <li>
        ```-is:selfservice``` excludes selfservice</li>
    </ul>

    Args:
        q (Union[Unset, str]):
        page_number (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['AgenciesV2AgencySummary']
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            page_number=page_number,
            page_size=page_size,
        )
    ).parsed
