

## Complex Queries
```
SELECT rate_ladder_element->>'rate' AS rate, market_element ->>'market' as market, rate_ladder_element->>'category' as categ
 FROM merchants,
      jsonb_array_elements(overridden_selling_fees) AS market_element,
      jsonb_array_elements(market_element->'rate_ladder') AS rate_ladder_element
 WHERE  id= '<id>'  and market_element ->>'market' = 'SE' and rate_ladder_
 element->>'category' in ('123')

eg : {
                "rate": 400,
                "category": "917",
                "from_amount_inclusive": 0
            },
```
