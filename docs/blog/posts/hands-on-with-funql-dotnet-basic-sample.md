---
title: 'Hands-on with FunQL .NET Basic sample'
description: |
  Get started with FunQL .NET in C#. Use the Basic sample to run functional queries with filter and sort on in-memory
  data collections.
date: 2025-04-16
authors:
  - arjanvanbremen
  - mathijsvanbremen
slug: hands-on-with-funql-dotnet-basic-sample
categories:
  - General
links:
  - blog/posts/funql-dotnet-just-landed.md
  - blog/posts/introducing-the-first-funql-dotnet-sample.md
---

# Hands-on with FunQL .NET Basic sample

**FunQL .NET lets you easily add filtering, sorting, and pagination to your API — using a simple, functional query
language that works out of the box. If you want to explore FunQL .NET without doing a deep dive, the new Basic sample is
the place to start.**

The Basic sample defines a simple FunQL schema and runs a query on an in-memory list of LEGO sets using `filter` and
`sort` parameters. The results are printed to the console as formatted JSON. No HTTP. No EF Core. Just the basics.

<!-- more -->

## Before we begin

The steps below walk you through the core concepts demonstrated in the [Basic sample][basic-sample]. We show you how to
define a FunQL schema, set up a queryable collection, and execute a request using `filter` and `sort` parameters — just
like in the sample. This gives you a minimal, self-contained starting point for working with FunQL .NET.

This guide is for C# developers who want to explore FunQL .NET without setting up a full API backend. The Basic sample
is part of the [FunQL .NET 1.1.0 release](https://github.com/funql/funql-dotnet/releases/tag/1.1.0).

## Exploring the basics

To use [FunQL .NET][funql-dotnet], you only need two things: a queryable collection of data and a FunQL schema. The
schema serves as the main entry point for handling FunQL requests. It defines the configuration for fields, available
functions like filtering and sorting, and features such as LINQ support.

### 1. Install the FunQL package

FunQL .NET is available on [NuGet](https://www.nuget.org/profiles/funql). To get started, first add the [FunQL](
https://www.nuget.org/packages/FunQL) package to your project by running the following command:

```shell
dotnet add package FunQL
```

### 2. Define your data model and FunQL schema

Next, define your data model and configure a FunQL schema that describes the structure of your data and which fields can
be filtered and sorted:

```csharp
// Data model representing the objects you want to query
public sealed record Set(string Name, double Price, DateTime LaunchTime);

// FunQL schema configuration for the 'listSets()' request
public sealed class ApiSchema : Schema
{
    protected override void OnInitializeSchema(ISchemaConfigBuilder schema)
    {
        // Add core parsing, validation, and execution features
        schema.AddCoreFeatures();
        
        // Add LINQ feature for translating FunQL queries into LINQ expressions
        schema.AddLinqFeature();
        
        // Define the listSets() request, enable filter and sort, and configure its available fields
        schema.Request("listSets")
            .SupportsFilter()
            .SupportsSort()
            .ReturnsListOfObjects<Set>(set =>
            {
                // Configure the Name field to support String filter and sort functions (like eq, gt, has, lower)
                set.SimpleField(it => it.Name)
                    .HasName("name")
                    .SupportsFilter(it => it.SupportsStringFilterFunctions())
                    .SupportsSort(it => it.SupportsStringFieldFunctions());
                
                // Configure the Price field to support Double filter and sort functions (like eq, gt, floor)
                set.SimpleField(it => it.Price)
                    .HasName("price")
                    .SupportsFilter(it => it.SupportsDoubleFilterFunctions())
                    .SupportsSort(it => it.SupportsDoubleFieldFunctions());
                
                // Configure the LaunchTime field to support DateTime filter and sort functions (like eq, gt, year)
                set.SimpleField(it => it.LaunchTime)
                    .HasName("launchTime")
                    .SupportsFilter(it => it.SupportsDateTimeFilterFunctions())
                    .SupportsSort(it => it.SupportsDateTimeFieldFunctions());
            });
    }
}
```

### 3. Prepare your data and query parameters

Then, prepare a collection of data that you want to query and define the parameters of the request.

In this example, we define an in-memory list of LEGO sets. In real-world scenarios this would be, for example, an Entity
Framework Core `DbSet<Set>`. In that case, FunQL .NET can directly query the database.

Our list is converted to an `IQueryable<Set>`, so FunQL .NET can apply LINQ expressions (like `Where()` and `OrderBy()`)
based on the `filter` and `sort` parameters:

```csharp
// Prepare the data source
IQueryable<Set> sets = new List<Set>
{
    new("LEGO Star Wars Millennium Falcon", 849.99, DateTime.Parse("2017-10-01")),
    new("LEGO Star Wars The Razor Crest", 599.99, DateTime.Parse("2022-10-03")),
    new("LEGO DC Batman Batmobile Tumbler", 269.99, DateTime.Parse("2021-11-01")),
    new("LEGO Harry Potter Hogwarts Castle", 469.99, DateTime.Parse("2018-09-01")),
}.AsQueryable();

// Define the FunQL filter and sort parameters
// This filter selects Star Wars sets with a price >= 500 and launch year after 2010
const string filter = "and(has(upper(name), \"STAR WARS\"), gte(price, 500), gt(year(launchTime), 2010))";

// Sort results by price in descending order
const string sort = "desc(price)";
```

### 4. Execute the query using FunQL .NET

Finally, create the FunQL schema and execute a filter and sort request using FunQL .NET:

```csharp
// Create the FunQL schema that defines the available requests and fields
var schema = new ApiSchema();

// Execute the FunQL request using the schema and parameters
var result = await sets
    .ExecuteRequestForParameters(schema, requestName: "listSets", filter: filter, sort: sort);

// Print the filtered and sorted result as JSON
var jsonSerializerOptions = new JsonSerializerOptions(JsonSerializerDefaults.Web) { WriteIndented = true };
Console.WriteLine(JsonSerializer.Serialize(result.Data, jsonSerializerOptions));
```

### 5. View the result

The result includes all LEGO sets where:

- The uppercased `name` contains `"STAR WARS"`
- The `price` is greater than or equal to `500`
- The `launchTime`'s year is greater than `2010`

The items are sorted by price in descending order:

```json
[
  {
    "name": "LEGO Star Wars Millennium Falcon",
    "price": 849.99,
    "launchTime": "2017-10-01T00:00:00"
  },
  {
    "name": "LEGO Star Wars The Razor Crest",
    "price": 599.99,
    "launchTime": "2022-10-03T00:00:00"
  }
]
```

## Try it now!

Ready to get your hands dirty? Clone the [Basic sample][basic-sample] and see how [FunQL .NET][funql-dotnet] works in
just a few lines of C# code. You can also check out the [WebApi sample](
https://github.com/funql/funql-dotnet/tree/main/samples/WebApi) to see how FunQL .NET works in a REST API setup.

[Explore on GitHub][basic-sample]{ .md-button .md-button--primary }

  [funql-dotnet]: https://github.com/funql/funql-dotnet
  [basic-sample]: https://github.com/funql/funql-dotnet/tree/main/samples/Basic