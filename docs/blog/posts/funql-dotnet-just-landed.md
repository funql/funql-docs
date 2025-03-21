---
title: 'FunQL .NET just landed'
date: 2025-03-21
authors:
  - mathijsvanbremen
slug: funql-dotnet-just-landed
categories:
  - General
---

# FunQL .NET just landed

**We are thrilled to announce the initial public release of [FunQL .NET][funql-dotnet], the official .NET implementation
of FunQL — the open-source Functional Query Language designed to simplify and enhance API querying.**

With this release, developers can now integrate powerful, structured, and intuitive query capabilities directly into
their .NET applications. Whether you want to enhance an existing REST API with robust filtering and sorting or build a
dedicated FunQL-powered API, FunQL .NET provides a flexible and efficient solution. Designed to work seamlessly with
LINQ and Entity Framework Core, it enables developers to write expressive, optimized queries with minimal effort.

<!-- more -->

## Why FunQL .NET?

REST APIs are a cornerstone of modern application development, but they often require custom query parameters, complex
filters, and hand-crafted solutions for sorting and pagination. The FunQL specification defines a standardized,
expressive query language designed to address these challenges. FunQL .NET, as its official .NET implementation,
seamlessly integrates this specification with .NET, allowing developers to enhance their APIs with powerful query
capabilities while maintaining full flexibility and control.

## Open source

FunQL .NET is fully open source, built with the community in mind. By making it open source, we aim to foster
collaboration, transparency, and innovation. We welcome contributions from developers who want to improve FunQL .NET,
expand its capabilities, and tailor it to new use cases. Whether you are reporting issues, suggesting enhancements, or
contributing code, your involvement helps shape the future of FunQL .NET and ensures it evolves to meet real-world API
needs.

## Key features

With FunQL .NET, you can:

- **Enhance existing REST APIs** with built-in support for filtering, sorting, pagination, and more.
- **Build dedicated FunQL APIs** that leverage the full expressiveness of the FunQL Query Language.
- **Integrate with LINQ and EF Core** to transform FunQL queries into efficient database queries.
- **Maintain full control over API behavior**, with an extensible architecture that fits your needs.
- **Enjoy a lightweight and efficient implementation**, designed to be easy to use and integrate.

## Getting started

FunQL .NET is available as a [NuGet package](https://www.nuget.org/packages/FunQL), making it easy to add to your
project. To install it using the .NET CLI, simply run:

```shell
dotnet add package FunQL
```

For more detailed documentation and examples, visit [dotnet.funql.io](https://dotnet.funql.io/).

## What's next?

This is just the beginning! We are committed to continuously improving [FunQL .NET][funql-dotnet] and expanding its
capabilities. Here are some of the exciting updates planned for future releases:

- **Comprehensive guides and best practices** to help you get the most out of FunQL .NET.
- **FunQL Playground** to provide an interactive environment for testing and experimenting with FunQL queries, making it
  easier to learn and debug.
- **Standalone FunQL Query Language support** to enable developers to create APIs that expose FunQL directly,
  independent of traditional REST endpoints.

We are excited to see what you build with [FunQL .NET][funql-dotnet]! Try it out, share your feedback, and let us know
how we can make it even better.

**Start using FunQL .NET today and transform how your .NET APIs handle queries!**

[Get started](https://dotnet.funql.io/learn/getting-started/){ .md-button .md-button--primary }

  [funql-dotnet]: https://github.com/funql/funql-dotnet