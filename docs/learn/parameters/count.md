# Count parameter

The count parameter includes the total number of items matching the current query.

It is commonly used in combination with [pagination](./skip.md#pagination) to display the total number of available
results.

!!! note

    When combined with parameters such as `filter`, the `count` reflects the number of results *after* filtering.

=== "REST"

    ```urlencoded
    count=value: Boolean
    ```

=== "QL"

    ```funql
    count(value: Boolean)
    ```

## Usage

In this example, the response includes a total count of the number of matching results.

This count reflects the total number of items matching the current query. It does not necessarily equal the number of
items returned in the response, especially when using parameters such as [`limit`](./limit.md) or `filter`.

To retrieve subsets of results along with the total count, see [pagination](./skip.md#pagination).

=== "REST"

    ```urlencoded
    GET https://api.play.funql.io/v1beta1/sets?count=true
    ```

    <div class="result" markdown>
    
    ```json
    HTTP/1.1 200 OK
    Content-Type: application/json
    Total-Count: 70

    [
      --8<-- "learn/snippets/sets.json"
    ]
    ```

    !!! note

        In REST responses, the total count is included in the `Total-Count` header.

    [:material-flask-outline: Try](https://play.funql.io/?item=listSets&filter=&sort=&skip=&limit=&count=true "Try this example in our Playground"){: target="_blank" }

    </div>

=== "QL"

    ```funql
    POST https://api.play.funql.io/funql
    Content-Type: text/plain

    listSets(
      count(true)
    )
    ```

    <div class="result" markdown>

    ```json
    HTTP/1.1 200 OK
    Content-Type: application/json
    
    {
      "data": [
        --8<-- "learn/snippets/sets.json"
      ],
      "metadata": {
        "totalCount": 70
      }
    }
    ```

    !!! note

        In QL responses, the total count is included in the `metadata.totalCount` property.

    </div>