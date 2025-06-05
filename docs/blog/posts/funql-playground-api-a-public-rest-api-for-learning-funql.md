---
title: 'FunQL Playground API: A public REST API for learning FunQL'
description: |
  Explore the hosted FunQL Playground API: a public REST API with sample data and OpenAPI docs to learn FunQL filtering,
  sorting, and pagination.
date: 2025-06-05
authors:
  - arjanvanbremen
  - mathijsvanbremen
slug: funql-playground-api-a-public-rest-api-for-learning-funql
categories:
  - General
---

# FunQL Playground API: A public REST API for learning FunQL

**The FunQL Playground API is now live — a hosted, no-setup environment for exploring FunQL, the Functional Query
Language that simplifies and enhances how you query APIs.**

Whether you want to try filtering, sorting, pagination, or just understand how FunQL behaves in practice, the Playground
API offers a clean RESTful interface backed by real-world data and a complete OpenAPI Specification (OAS). The
Playground API is fully [open source on GitHub][playground-api].

<!-- more -->

## What is the FunQL Playground API?

The Playground API is the core of the FunQL Playground — an interactive, hosted environment where developers can learn
FunQL by example. It lets you try FunQL queries directly, without installing anything locally or writing a single line
of code.

Using standard REST endpoints, the API shows how FunQL's expressive query parameters work in practice — including
advanced filtering, sorting on multiple fields, and robust pagination.

It is ideal for experimenting with FunQL in a live, realistic setting.

## What can you do with it?

The Playground API currently exposes endpoints for three data sets:

- **Sets** — A list of LEGO sets with metadata
- **Minifigures** — Individual figures associated with sets
- **Designers** — People who designed the sets

Each of these endpoints supports FunQL-style query parameters. The OpenAPI Specification (OAS) defines which fields
support filtering or sorting and includes example values.

Here is an example of a FunQL query in action:

```funql
GET https://api.play.funql.io/v1beta1/sets?filter=
  and(
    eq(theme, "STAR_WARS"),
    gte(price, 500),
    gt(year(launchTime), 2010)
  )
  &sort=desc(price)
```

<div class="result" markdown>

```json
HTTP/1.1 200 OK
Content-Type: application/json

[
  {
    "id": "041a9eed-1665-40e5-876e-1875460cf730",
    "name": "LEGO Star Wars Millennium Falcon",
    "setNumber": 75192,
    "itemNumber": {
      "EUROPE": 6175770,
      "NORTH_AMERICA": 6175771
    },
    "pieces": 7541,
    "price": 849.99,
    "designerId": "ee6f6c30-f413-414f-a58c-ae3abf7776a3",
    "designer": {
      "id": "ee6f6c30-f413-414f-a58c-ae3abf7776a3",
      "name": "Hans Burkhard Schlömer"
    },
    "launchTime": "2017-10-01T00:00:00Z",
    "packagingType": "BOX",
    "theme": "STAR_WARS",
    "categories": [
      "VEHICLES",
      "ULTIMATE_COLLECTOR_SERIES",
      "MOVIES"
    ],
    "minifigures": [
      {
        "id": "146c0e19-7b76-4d23-8676-a5c38a0565d2",
        "name": "SW0878: Princess Leia (Hoth Outfit White)",
        "quantity": 1
      },
      ...
    ]
  }
]
```

</div>

## Explore with Postman or your browser

You do not need to write any code to start experimenting.

- Use our [hosted OpenAPI docs][api-docs] to explore all available endpoints
- Use our public [Postman Collection][postman-collection] to send requests from Postman
- Or simply open your browser and call [api.play.funql.io/v1beta1/sets](https://api.play.funql.io/v1beta1/sets) to get
  started

## What's in the GitHub repository?

The [`funql-playground-api`][playground-api] repository contains everything needed to run, understand, and extend the
Playground API:

### OpenAPI Specification (OAS)

- A structured, modular OpenAPI spec organized by paths, schemas, and parameters
- Documentation of supported filters, sorting options, and pagination behavior

### Database design

- PostgreSQL schema defined in SQL files
- Seed data for sets, minifigures, and designers in CSV format
- Migration scripts for initializing the database

### C# Application

- `Domain` layer — Entity models based on the database
- `Infrastructure` layer — Maps entities to PostgreSQL using Entity Framework Core
- `Application` layer — Defines query models, request handlers, and response types
- `WebApi` layer — Defines API endpoints and handles HTTP requests

### Postman

- A Postman Collection for exploring the API without writing any code

## What's next?

This is the first in a series of blog posts about the FunQL Playground. Upcoming posts will explore:

- How the OpenAPI Specification (OAS) is structured — and the conventions we follow
- Using GitHub Actions and Redocly CLI to publish OpenAPI docs automatically
- Using GitHub Actions and Docker to build the Web API and publish container images to Google Cloud Platform (GCP)
- The upcoming FunQL Playground UI — a visual frontend for exploring queries

Stay tuned — and in the meantime, give the Playground API a spin!

[Use the Postman Collection][postman-collection]{ .md-button .md-button--primary }
[Explore the API docs][api-docs]{ .md-button }

  [playground-api]: https://github.com/funql/funql-playground-api
  [api-docs]: https://oas.play.funql.io/
  [postman-collection]: https://www.postman.com/funqlio/funql/collection/hb88ymo/funql-playground-api