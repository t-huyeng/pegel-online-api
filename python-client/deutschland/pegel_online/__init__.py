# coding: utf-8

# flake8: noqa

"""
    Pegel-Online API

    API für das bundesweite Messstellennetz der Wasserstraßen- und Schifffahrtsverwaltung des Bundes.  Die API stellt drei verschiedene Ressourcen zur Verfügung: __Station__, __Measurement__, __Water__. ### Authentifizierung / Autorisierung / API Limitierung Es ist keine Authentifizierung oder Autorisierung notwendig. Aktuell besteht keine API Limitierung. ### Allgemeine Query-Parameter Zusätzlich zu den angegebenen Parametern sind ebenfalls allgemeine Parameter für alle Schnittstellen verfügbar ([Dokumentation](https://www.pegelonline.wsv.de/webservice/dokuRestapi;jsessionid=A294589CCEF6630142D2589F49BFA2EC#urlParameter)). - `charset`: Gibt die Kodierung der Response an. Standard ist hier _UTF-8_. Möglich ist z.B. auch _ISO-8859-1_. - `prettyprint`: Kann die zur besseren Lesbarkeit standardmäßig aktivierte Teilung der Response in mehreren Zeilen deaktivieren: _prettyprint=false_. Diese Einstellung wird für den produktiven Einsatz empfohlen. - `limit/offset`: Einschränkung der Anzahl der Ergebnisse. Hiermit kann 'Pagination' realisiert werden. `limit` gibt dabei die Anzahl der zurückgegebenen Elemente an. `offset` ermöglicht einen Offset vom Startwert. Beispiel: _limit=10&offset=20_ bedeutet, dass 10 Elemente beginnend mit dem 21. Element zurückgegeben werden.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""

__version__ = "0.1.0"

# import ApiClient
from deutschland.pegel_online.api_client import ApiClient

# import Configuration
from deutschland.pegel_online.configuration import Configuration

# import exceptions
from deutschland.pegel_online.exceptions import (
    ApiAttributeError,
    ApiException,
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    OpenApiException,
)
