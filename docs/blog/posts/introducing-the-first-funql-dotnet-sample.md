---
title: 'Introducing the first FunQL .NET sample'
description: |
  Learn how to integrate FunQL into a .NET API with the new WebApi sample. A hands-on guide for filtering, sorting, and
  querying data in ASP.NET Core.
date: 2025-04-02
authors:
  - mathijsvanbremen
slug: introducing-the-first-funql-dotnet-sample
categories:
  - General
links:
  - blog/posts/funql-dotnet-just-landed.md
---

# Introducing the first FunQL .NET sample

**We are excited to announce the release of the first official FunQL .NET sample project: WebApi. This sample
demonstrates how to integrate FunQL into a modern RESTful ASP.NET Core Web API.**

FunQL is a powerful functional query language that simplifies filtering, sorting, and data retrieval in APIs. With the
release of [FunQL .NET][funql-dotnet], developers can seamlessly integrate FunQL into their .NET applications. However,
we know that setting up a new technology can be challenging, so we created WebApi as a hands-on example to help
developers get started quickly.

<!-- more -->

## What this sample covers

The WebApi sample demonstrates how to build a FunQL-powered REST API using:

- **Entity Framework Core (EF Core)** – Handling database operations.
- **Noda Time** – Enhancing date and time handling in FunQL queries.
- **System.Text.Json** – Configuring serialization.
- **Minimal APIs** – Keeping the API lightweight and easy to understand.

The project includes:

- **A fully functional REST API** that processes FunQL query parameters.
- **A sample data model** (LEGO sets) with predefined datasets.
- **A ready-to-run example** that you can test immediately with `cURL`, Postman, or an HTTP client.

## How to get started

Follow these steps to run the WebApi sample on your local machine.

### 1. Clone the repository

```shell
git clone https://github.com/funql/funql-dotnet.git
cd funql-dotnet/samples/WebApi
```

### 2. Build and run the API

```shell
dotnet run
```

### 3. Test the API

The API exposes endpoints that accept FunQL query parameters. You can test it using tools like Postman or cURL, or use
the WebApi.http file included with the sample project.

```shell
curl "http://localhost:5107/sets?filter=and(has(upper(name),\"STAR%20WARS\"),gte(price,500),gt(year(launchTime),2010))&sort=desc(price)"
```

The response includes all LEGO sets where:

- The name contains "STAR WARS".
- The price is at least 500.
- The launchTime is later than 2010.

The results are sorted by price in descending order.

```funql
GET https://localhost:5107/sets?filter=
  and(
    has(upper(name), "STAR WARS"),
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
    "id": 1,
    "name": "LEGO Star Wars Millennium Falcon",
    "setNumber": 75192,
    "pieces": 7541,
    "price": 849.99,
    "launchTime": "2017-10-01T00:00:00Z"
  },
  {
    "id": 2,
    "name": "LEGO Star Wars The Razor Crest",
    "setNumber": 75331,
    "pieces": 6187,
    "price": 599.99,
    "launchTime": "2022-10-03T00:00:00Z"
  }
]
```

</div>

## More samples coming soon

The WebApi sample is the first in a series of [FunQL .NET][funql-dotnet] examples. We plan to release additional samples
covering different use cases and integrations.

## Try it now!

Check out the [FunQL .NET][funql-dotnet] WebApi sample today and see how easy it is to add powerful query capabilities
to your .NET applications.

[Explore on GitHub](https://github.com/funql/funql-dotnet/tree/main/samples/WebApi){ .md-button .md-button--primary }

  [funql-dotnet]: https://github.com/funql/funql-dotnet