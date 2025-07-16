# Skip parameter

The `skip` parameter specifies how many items to omit from the beginning of the result set before returning data.

It is commonly used for [pagination](#pagination) in combination with the [`limit`](./limit.md) parameter.

=== "REST"

    ```urlencoded
    skip=value: Integer
    ```

=== "QL"

    ```funql
    skip(value: Integer)
    ```

## Usage

In this example, the response skips the first item and returns the next one. The actual result depends on the sort
order. To ensure consistent results, combine `skip` with a `sort` clause.

=== "REST"

    ```urlencoded
    GET https://api.play.funql.io/v1beta1/sets?skip=1
    ```

    <div class="result" markdown>
    
    ```json
    HTTP/1.1 200 OK
    Content-Type: application/json
    
    [
      --8<-- "learn/snippets/set-r2d2.json"
    ]
    ```

    [:material-flask-outline: Try](https://play.funql.io/?item=listSets&filter=&sort=&skip=1&limit=&count= "Try this example in our Playground"){: target="_blank" }

    </div>

=== "QL"

    ```funql
    POST https://api.play.funql.io/funql
    Content-Type: text/plain

    listSets(
      skip(1)
    )
    ```

    <div class="result" markdown>

    ```json
    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "data": [
        --8<-- "learn/snippets/set-r2d2.json"
      ]
    }
    ```

    </div>

## Pagination

To retrieve additional pages of data, combine `skip` with the [`limit`](./limit.md) parameter. For example, use
`skip(10)` with `limit(10)` to get the second page of results in a paginated list (items 11-20).

=== "REST"

    ```urlencoded
    GET https://api.play.funql.io/v1beta1/sets?skip=10&limit=10
    ```

    <div class="result" markdown>
    
    ```json
    HTTP/1.1 200 OK
    Content-Type: application/json
    
    [
      --8<-- "learn/snippets/set-millennium-falcon.json"
    ]
    ```

    [:material-flask-outline: Try](https://play.funql.io/?item=listSets&filter=&sort=&skip=10&limit=10&count= "Try this example in our Playground"){: target="_blank" }

    </div>

=== "QL"

    ```funql
    POST https://api.play.funql.io/funql
    Content-Type: text/plain

    listSets(
      skip(10),
      limit(10)
    )
    ```

    <div class="result" markdown>

    ```json
    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "data": [
        --8<-- "learn/snippets/set-millennium-falcon.json"
      ]
    }
    ```

    </div>