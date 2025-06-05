![FunQL logo](assets/logo.png){ width="300" }

# Complex queries made simple

FunQL, the Functional Query Language, is an open-source [specification](./learn/index.md) and
[software implementation](./code/index.md) that standardizes API query design and provides ready-to-use software
components for filtering, sorting, pagination, and more.

Designed for usability, flexibility and seamless integration, FunQL simplifies complex query logic. Use it to enhance an
existing REST API or build a new API with powerful, well-structured query capabilities using the FunQL Query Language.

[Get started](./learn/index.md){ .md-button .md-button--primary }
[:material-flask-outline: Explore Playground](./play/index.md){ .md-button }

## Everything is a function

FunQL is both powerful and simple. Its functions are easy to learn, intuitive to use, and built to handle everything
from simple search to complex queries. Looking for LEGO **Star Wars** sets that cost at least **€ 500** and were
**launched after 2010**, sorted by price? Just ask:

=== "REST"

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
    
    --8<-- "snippets/sets.json"
    ```

    [:material-flask-outline: Try](https://api.play.funql.io/v1beta1/sets?filter=and(eq(theme,%22STAR_WARS%22),gte(price,500),gt(year(launchTime),2010))&sort=desc(price) "Try this example in our Playground")

    </div>

=== "QL"

    ```funql
    POST https://api.play.funql.io/funql
    Content-Type: text/plain

    listSets(
      filter(
        and(
          eq(theme, "STAR_WARS"),
          gte(price, 500),
          gt(year(launchTime), 2010)
        )
      ),
      sort(
        desc(price)
      )
    )
    ```

    <div class="result" markdown>

    ```json
    HTTP/1.1 200 OK
    Content-Type: application/json
    
    --8<-- "snippets/sets.json"
    ```

    </div>