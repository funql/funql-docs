# Limit parameter

The `limit` parameter restricts the maximum number of items returned in a single response.

It is commonly used to retrieve a subset of results, such as the first item in a list.

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