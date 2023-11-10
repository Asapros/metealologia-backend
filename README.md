# MeteALOlogia-API
API service of the "MeteALOlogia" project. The project's goal is to create a weather station along with a website to view live measurements. This repository aims at creating an HTTP REST API server managing the collected data.

## Installation
Use `poetry install` and `poetry run start` in order to run the project on `localhost:8080`. Endpoint docs are available on `/docs`

## Configuration files
The config files will contain all the static data of the weather stations:
- types of sensors
- station instances
- public keys

## Signatures
To minimise costs, we decided not to use an HTTPS certificate. Instead the `Authorization` header will contain:
 - station ID
 - a nonce to prevent resending the same payload
 - an encrypted signature of request's body and the two above, possible to be verified using a public key.

## Planned endpoints:

### GET /stations
Success: *200 OK*
```json
[
  {
    "id": station id,
    "name": station display name,
    "sensors":
    [
      {
        "id": sensor id,
        "type": sensor type,
        "name": sensor display name
      }
    ]
  }
]
```

### POST /stations/\<station id>/sensor/\<sensor_id>/reports

#### Request structure
```json
{
  "timestamp": measurement timestamp,
  "data": { ... }
}
```

#### Response
Success: *201 Created*

### GET /stations/\<station id>/sensor/\<sensor_id>/reports
Doesn't require authorization.

#### Request parameters
- before=timestamp
- after=timestamp

These will provide the requested range of reports.

#### Response
Success: *200 OK*
```json
[
  { ... as in POST reports}
]
```