# coding: utf-8

"""
    Pegel-Online API

    API für das bundesweite Messstellennetz der Wasserstraßen- und Schifffahrtsverwaltung des Bundes.  Die API stellt drei verschiedene Ressourcen zur Verfügung: __Station__, __Measurement__, __Water__. ### Authentifizierung / Autorisierung / API Limitierung Es ist keine Authentifizierung oder Autorisierung notwendig. Aktuell besteht keine API Limitierung. ### Allgemeine Query-Parameter Zusätzlich zu den angegebenen Parametern sind ebenfalls allgemeine Parameter für alle Schnittstellen verfügbar ([Dokumentation](https://www.pegelonline.wsv.de/webservice/dokuRestapi;jsessionid=A294589CCEF6630142D2589F49BFA2EC#urlParameter)). - `charset`: Gibt die Kodierung der Response an. Standard ist hier _UTF-8_. Möglich ist z.B. auch _ISO-8859-1_. - `prettyprint`: Kann die zur besseren Lesbarkeit standardmäßig aktivierte Teilung der Response in mehreren Zeilen deaktivieren: _prettyprint=false_. Diese Einstellung wird für den produktiven Einsatz empfohlen. - `limit/offset`: Einschränkung der Anzahl der Ergebnisse. Hiermit kann 'Pagination' realisiert werden. `limit` gibt dabei die Anzahl der zurückgegebenen Elemente an. `offset` ermöglicht einen Offset vom Startwert. Beispiel: _limit=10&offset=20_ bedeutet, dass 10 Elemente beginnend mit dem 21. Element zurückgegeben werden.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""

import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import uuid  # noqa: F401
from datetime import date, datetime  # noqa: F401

import frozendict  # noqa: F401
import typing_extensions  # noqa: F401
from pegel_online import schemas  # noqa: F401

class MeasurementResult(schemas.ListSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        class items(schemas.DictSchema):
            class MetaOapg:
                class properties:
                    timestamp = schemas.StrSchema
                    value = schemas.Float32Schema
                    __annotations__ = {
                        "timestamp": timestamp,
                        "value": value,
                    }
            @typing.overload
            def __getitem__(
                self, name: typing_extensions.Literal["timestamp"]
            ) -> MetaOapg.properties.timestamp: ...
            @typing.overload
            def __getitem__(
                self, name: typing_extensions.Literal["value"]
            ) -> MetaOapg.properties.value: ...
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            def __getitem__(
                self,
                name: typing.Union[
                    typing_extensions.Literal[
                        "timestamp",
                        "value",
                    ],
                    str,
                ],
            ):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            @typing.overload
            def get_item_oapg(
                self, name: typing_extensions.Literal["timestamp"]
            ) -> typing.Union[MetaOapg.properties.timestamp, schemas.Unset]: ...
            @typing.overload
            def get_item_oapg(
                self, name: typing_extensions.Literal["value"]
            ) -> typing.Union[MetaOapg.properties.value, schemas.Unset]: ...
            @typing.overload
            def get_item_oapg(
                self, name: str
            ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            def get_item_oapg(
                self,
                name: typing.Union[
                    typing_extensions.Literal[
                        "timestamp",
                        "value",
                    ],
                    str,
                ],
            ):
                return super().get_item_oapg(name)
            def __new__(
                cls,
                *args: typing.Union[
                    dict,
                    frozendict.frozendict,
                ],
                timestamp: typing.Union[
                    MetaOapg.properties.timestamp, str, schemas.Unset
                ] = schemas.unset,
                value: typing.Union[
                    MetaOapg.properties.value,
                    decimal.Decimal,
                    int,
                    float,
                    schemas.Unset,
                ] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[
                    schemas.AnyTypeSchema,
                    dict,
                    frozendict.frozendict,
                    str,
                    date,
                    datetime,
                    uuid.UUID,
                    int,
                    float,
                    decimal.Decimal,
                    None,
                    list,
                    tuple,
                    bytes,
                ],
            ) -> "items":
                return super().__new__(
                    cls,
                    *args,
                    timestamp=timestamp,
                    value=value,
                    _configuration=_configuration,
                    **kwargs,
                )
    def __new__(
        cls,
        arg: typing.Union[
            typing.Tuple[
                typing.Union[
                    MetaOapg.items,
                    dict,
                    frozendict.frozendict,
                ]
            ],
            typing.List[
                typing.Union[
                    MetaOapg.items,
                    dict,
                    frozendict.frozendict,
                ]
            ],
        ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> "MeasurementResult":
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )
    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
