---
description: |
  Explore FunQL field functions for sorting and filtering. Learn DateTime, Math, and String functions to extract dates,
  round numbers, and modify text case.
---

# Field functions

Field functions allow users to manipulate and extract data from fields when applying sorting and filtering operations.
This section describes the available functions and their usage with the FunQL language.

## Datetime functions

These functions extract specific components from `DateTime` values, such as the year, month, or hour.

### Function list

| Name                          | Summary                                                       |
|-------------------------------|---------------------------------------------------------------|
| [`year`](#year)               | Returns the year component of a `DateTime` value.             |
| [`month`](#month)             | Returns the month component of a `DateTime` value.            |
| [`day`](#day)                 | Returns the day of the month component of a `DateTime` value. |
| [`hour`](#hour)               | Returns the hour component of a `DateTime` value.             |
| [`minute`](#minute)           | Returns the minute component of a `DateTime` value.           |
| [`second`](#second)           | Returns the second component of a `DateTime` value.           |
| [`millisecond`](#millisecond) | Returns the millisecond component of a `DateTime` value.      |

### year

The `year` function returns the year component of a `DateTime` parameter value.

```funql
year(field: DateTime): Integer
```

For example:

```json title="set.json" hl_lines="5"
--8<-- "learn/snippets/set-millennium-falcon.json"
```

<div class="result" markdown>

```funql
year(launchTime)
```

Returns `#!js 2017`.

</div>

**Usage**

Return all sets that were launched in 2017:

=== "REST"

    ```urlencoded
    GET https://api.play.funql.io/v1beta1/sets?filter=eq(year(launchTime), 2017)
    ```

    <div class="result" markdown>
    
    [:material-flask-outline: Try](https://play.funql.io/?request=listSets&filter=eq(year(launchTime),%202017)&sort=&skip=&limit=&count= "Try this example in our Playground"){: target="_blank" }
    
    </div>

=== "QL"

    ```funql
    POST https://api.play.funql.io/funql
    Content-Type: text/plain

    listSets(
      filter(
        eq(year(launchTime), 2017)
      )
    )
    ```

### month

The `month` function returns the month component of a `DateTime` parameter value as an integer from 1 (January) to 12
(December).

```funql
month(field: DateTime): Integer
```

For example:

```json title="set.json" hl_lines="5"
--8<-- "learn/snippets/set-millennium-falcon.json"
```

<div class="result" markdown>

```funql
month(launchTime)
```

Returns `#!js 10`.

</div>

**Usage**

Return all sets that were launched in October, the 10th month of the year:

=== "REST"

    ```urlencoded
    GET https://api.play.funql.io/v1beta1/sets?filter=eq(month(launchTime), 10)
    ```

    <div class="result" markdown>
    
    [:material-flask-outline: Try](https://play.funql.io/?request=listSets&filter=eq(month(launchTime),%2010)&sort=&skip=&limit=&count= "Try this example in our Playground"){: target="_blank" }
    
    </div>

=== "QL"

    ```funql
    POST https://api.play.funql.io/funql
    Content-Type: text/plain

    listSets(
      filter(
        eq(month(launchTime), 10)
      )
    )
    ```

### day

The `day` function returns the day component of a `DateTime` parameter value as an integer from 1 to 31.

```funql
day(field: DateTime): Integer
```

For example:

```json title="set.json" hl_lines="5"
--8<-- "learn/snippets/set-millennium-falcon.json"
```

<div class="result" markdown>

```funql
day(launchTime)
```

Returns `#!js 1`.

</div>

**Usage**

Return all sets that were launched on the 1st day of a month:

=== "REST"

    ```urlencoded
    GET https://api.play.funql.io/v1beta1/sets?filter=eq(day(launchTime), 1)
    ```

    <div class="result" markdown>
    
    [:material-flask-outline: Try](https://play.funql.io/?request=listSets&filter=eq(day(launchTime),%201)&sort=&skip=&limit=&count= "Try this example in our Playground"){: target="_blank" }
    
    </div>

=== "QL"

    ```funql
    POST https://api.play.funql.io/funql
    Content-Type: text/plain

    listSets(
      filter(
        eq(day(launchTime), 1)
      )
    )
    ```

### hour

The `hour` function returns the hour component of a `DateTime` parameter value as an integer from 0 (12:00 A.M.) to 23
(11:00 P.M.).

```funql
hour(field: DateTime): Integer
```

For example:

```json title="set.json" hl_lines="5"
--8<-- "learn/snippets/set-millennium-falcon.json"
```

<div class="result" markdown>

```funql
hour(launchTime)
```

Returns `#!js 14`.

</div>

**Usage**

Return all sets that were launched in the 14th hour of a day:

=== "REST"

    ```urlencoded
    GET https://api.play.funql.io/v1beta1/sets?filter=eq(hour(launchTime), 14)
    ```

    <div class="result" markdown>
    
    [:material-flask-outline: Try](https://play.funql.io/?request=listSets&filter=eq(hour(launchTime),%2014)&sort=&skip=&limit=&count= "Try this example in our Playground"){: target="_blank" }
    
    </div>

=== "QL"

    ```funql
    POST https://api.play.funql.io/funql
    Content-Type: text/plain

    listSets(
      filter(
        eq(hour(launchTime), 14)
      )
    )
    ```

### minute

The `minute` function returns the minute component of a `DateTime` parameter value as an integer from 0 to 59.

```funql
minute(field: DateTime): Integer
```

For example:

```json title="set.json" hl_lines="5"
--8<-- "learn/snippets/set-millennium-falcon.json"
```

<div class="result" markdown>

```funql
minute(launchTime)
```

Returns `#!js 15`.

</div>

**Usage**

Return all sets that were launched in the 15th minute of any hour on any day:

=== "REST"

    ```urlencoded
    GET https://api.play.funql.io/v1beta1/sets?filter=eq(minute(launchTime), 15)
    ```

    <div class="result" markdown>
    
    [:material-flask-outline: Try](https://play.funql.io/?request=listSets&filter=eq(minute(launchTime),%2015)&sort=&skip=&limit=&count= "Try this example in our Playground"){: target="_blank" }
    
    </div>

=== "QL"

    ```funql
    POST https://api.play.funql.io/funql
    Content-Type: text/plain

    listSets(
      filter(
        eq(minute(launchTime), 15)
      )
    )
    ```

### second

The `second` function returns the second component of a `DateTime` parameter value as an integer from 0 to 59.

```funql
second(field: DateTime): Integer
```

For example:

```json title="set.json" hl_lines="5"
--8<-- "learn/snippets/set-millennium-falcon.json"
```

<div class="result" markdown>

```funql
second(launchTime)
```

Returns `#!js 30`.

</div>

**Usage**

Return all sets that were launched in the 30th second of any minute of any hour on any day:

=== "REST"

    ```urlencoded
    GET https://api.play.funql.io/v1beta1/sets?filter=eq(second(launchTime), 30)
    ```

    <div class="result" markdown>
    
    [:material-flask-outline: Try](https://play.funql.io/?request=listSets&filter=eq(second(launchTime),%2030)&sort=&skip=&limit=&count= "Try this example in our Playground"){: target="_blank" }
    
    </div>

=== "QL"

    ```funql
    POST https://api.play.funql.io/funql
    Content-Type: text/plain

    listSets(
      filter(
        eq(second(launchTime), 30)
      )
    )
    ```

### millisecond

The `millisecond` function returns the millisecond component of a `DateTime` parameter value as an integer from 0 to
999.

```funql
millisecond(field: DateTime): Integer
```

For example:

```json title="set.json" hl_lines="5"
--8<-- "learn/snippets/set-millennium-falcon.json"
```

<div class="result" markdown>

```funql
millisecond(launchTime)
```

Returns `#!js 500`.

</div>

**Usage**

Return all sets that were launched in the 500th millisecond of any second of any minute of any hour on any day:

=== "REST"

    ```urlencoded
    GET https://api.play.funql.io/v1beta1/sets?filter=eq(millisecond(launchTime), 500)
    ```

    <div class="result" markdown>
    
    [:material-flask-outline: Try](https://play.funql.io/?request=listSets&filter=eq(millisecond(launchTime),%20500)&sort=&skip=&limit=&count= "Try this example in our Playground"){: target="_blank" }
    
    </div>

=== "QL"

    ```funql
    POST https://api.play.funql.io/funql
    Content-Type: text/plain

    listSets(
      filter(
        eq(millisecond(launchTime), 500)
      )
    )
    ```

---

## Math functions

These functions round numerical values in different ways.

### Function list

| Name                   | Summary                                      |
|------------------------|----------------------------------------------|
| [`round`](#round)      | Rounds a number to the nearest integer.      |
| [`floor`](#floor)      | Rounds a number down to the nearest integer. |
| [`ceiling`](#ceiling)  | Rounds a number up to the nearest integer.   |

### round

The `round` function rounds the input parameter numeric value to the nearest numeric value with no decimal component.

FunQL uses away-from-zero rounding, meaning midpoint values (e.g., 0.5) are rounded to the next whole number away from
zero. For example, 0.5 is rounded to 1 and ‑0.5 is rounded to -1.

```funql
round(field: Float): Integer
```

For example:

```json title="set.json" hl_lines="4"
--8<-- "learn/snippets/set-millennium-falcon.json"
```

<div class="result" markdown>

```funql
round(price)
```

Returns `#!js 850`.

</div>

**Usage**

Return all sets that have a price that rounds to 850:

=== "REST"

    ```urlencoded
    GET https://api.play.funql.io/v1beta1/sets?filter=eq(round(price), 850)
    ```

    <div class="result" markdown>
    
    [:material-flask-outline: Try](https://play.funql.io/?request=listSets&filter=eq(round(price),%20850)&sort=&skip=&limit=&count= "Try this example in our Playground"){: target="_blank" }
    
    </div>

=== "QL"

    ```funql
    POST https://api.play.funql.io/funql
    Content-Type: text/plain

    listSets(
      filter(
        eq(round(price), 850)
      )
    )
    ```

### floor

The `floor` function rounds the input parameter numeric value down to the nearest numeric value with no decimal
component.

```funql
floor(field: Float): Integer
```

For example:

```json title="set.json" hl_lines="4"
--8<-- "learn/snippets/set-millennium-falcon.json"
```

<div class="result" markdown>

```funql
floor(price)
```

Returns `#!js 849`.

</div>

**Usage**

Return all sets that have a price that rounds down to 849:

=== "REST"

    ```urlencoded
    GET https://api.play.funql.io/v1beta1/sets?filter=eq(floor(price), 849)
    ```

    <div class="result" markdown>
    
    [:material-flask-outline: Try](https://play.funql.io/?request=listSets&filter=eq(floor(price),%20849)&sort=&skip=&limit=&count= "Try this example in our Playground"){: target="_blank" }
    
    </div>

=== "QL"

    ```funql
    POST https://api.play.funql.io/funql
    Content-Type: text/plain

    listSets(
      filter(
        eq(floor(price), 849)
      )
    )
    ```

### ceiling

The `ceiling` function rounds the input parameter numeric value up to the nearest numeric value with no decimal
component.

```funql
ceiling(field: Float): Integer
```

For example:

```json title="set.json" hl_lines="4"
--8<-- "learn/snippets/set-millennium-falcon.json"
```

<div class="result" markdown>

```funql
ceiling(price)
```

Returns `#!js 850`.

</div>

**Usage**

Return all sets that have a price that rounds up to 850:

=== "REST"

    ```urlencoded
    GET https://api.play.funql.io/v1beta1/sets?filter=eq(ceiling(price), 850)
    ```

    <div class="result" markdown>
    
    [:material-flask-outline: Try](https://play.funql.io/?request=listSets&filter=eq(ceiling(price),%20850)&sort=&skip=&limit=&count= "Try this example in our Playground"){: target="_blank" }
    
    </div>

=== "QL"

    ```funql
    POST https://api.play.funql.io/funql
    Content-Type: text/plain

    listSets(
      filter(
        eq(ceiling(price), 850)
      )
    )
    ```

---

## String functions

These functions modify string values by changing their case.

### Function list

| Name                  | Summary                         |
|-----------------------|---------------------------------|
| [`lower`](#lower)     | Converts a string to lowercase. |
| [`upper`](#upper)     | Converts a string to uppercase. |

### lower

The `lower` function returns the input parameter string value with all uppercase characters converted to lowercase
according to Unicode rules.

```funql
lower(field: String): String
```

For example:

```json title="set.json" hl_lines="2"
--8<-- "learn/snippets/set-millennium-falcon.json"
```

<div class="result" markdown>

```funql
lower(name)
```

Returns `#!js "lego star wars millennium falcon"`.

</div>

**Usage**

Return all sets that have a name that equals 'lego star wars millennium falcon' once any uppercase characters have been
converted to lowercase:

=== "REST"

    ```urlencoded
    GET https://api.play.funql.io/v1beta1/sets?filter=eq(lower(name), "lego star wars millennium falcon")
    ```

    <div class="result" markdown>
    
    [:material-flask-outline: Try](https://play.funql.io/?request=listSets&filter=eq(lower(name),%20%22lego%20star%20wars%20millennium%20falcon%22)&sort=&skip=&limit=&count= "Try this example in our Playground"){: target="_blank" }
    
    </div>

=== "QL"

    ```funql
    POST https://api.play.funql.io/funql
    Content-Type: text/plain

    listSets(
      filter(
        eq(lower(name), "lego star wars millennium falcon")
      )
    )
    ```

### upper

The `upper` function returns the input parameter string value with all lowercase characters converted to uppercase
according to Unicode rules.

```funql
upper(field: String): String
```

For example:

```json title="set.json" hl_lines="2"
--8<-- "learn/snippets/set-millennium-falcon.json"
```

<div class="result" markdown>

```funql
upper(name)
```

Returns `#!js "LEGO STAR WARS MILLENNIUM FALCON"`.

</div>

**Usage**

Return all sets that have a name that equals 'LEGO STAR WARS MILLENNIUM FALCON' once any lowercase characters have been
converted to uppercase:

=== "REST"

    ```urlencoded
    GET https://api.play.funql.io/v1beta1/sets?filter=eq(upper(name), "LEGO STAR WARS MILLENNIUM FALCON")
    ```

    <div class="result" markdown>
    
    [:material-flask-outline: Try](https://play.funql.io/?request=listSets&filter=eq(upper(name),%20%22LEGO%20STAR%20WARS%20MILLENNIUM%20FALCON%22)&sort=&skip=&limit=&count= "Try this example in our Playground"){: target="_blank" }
    
    </div>

=== "QL"

    ```funql
    POST https://api.play.funql.io/funql
    Content-Type: text/plain

    listSets(
      filter(
        eq(upper(name), "LEGO STAR WARS MILLENNIUM FALCON")
      )
    )
    ```