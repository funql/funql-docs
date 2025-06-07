# Limit parameter

The `limit` parameter restricts the maximum number of items returned in a single response.

It is commonly used to retrieve a subset of results, such as the first few items from a list.

=== "REST"

    ```urlencoded
    limit=value: Integer
    ```

=== "QL"

    ```funql
    limit(value: Integer)
    ```

## Usage

In this example, the response is limited to a single item. The actual item returned depends on the sort order. To ensure
consistent results, combine `limit` with a `sort` clause.

=== "REST"

    ```urlencoded
    GET https://api.play.funql.io/v1beta1/sets?limit=1
    ```

    <div class="result" markdown>
    
    ```json
    HTTP/1.1 200 OK
    Content-Type: application/json
    
    --8<-- "learn/snippets/set-millennium-falcon.json"
    ```

    [:material-flask-outline: Try](https://api.play.funql.io/v1beta1/sets?limit=1 "Try this example in our Playground")

    </div>

=== "QL"

    ```funql
    POST https://api.play.funql.io/funql
    Content-Type: text/plain

    listSets(
      limit(1)
    )
    ```

    <div class="result" markdown>

    ```json
    HTTP/1.1 200 OK
    Content-Type: application/json
    
    --8<-- "learn/snippets/set-millennium-falcon.json"
    ```

    </div>

## Pagination

To paginate results, combine `limit` with the [`skip`](skip.md) parameter. For example, to fetch the second page of a
paginated list (items 11–20), use `skip(10)` and `limit(10)`.

See the [`skip`](skip.md#pagination) parameter for a full example.