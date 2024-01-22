# Map Reduce principles
## Map
- Map is a function that takes a set of data and converts it into another set of data, where individual elements are broken down into tuples (key/value pairs).
- Map function is applied to each element in the list.
- Example: 
    - Map function: `f(x) = (x, 1)`
    - Input: [1, 2, 3, 4, 5]
    - Output: [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1)]
- Map function is also called as `mapper` or `map task`.
  
## Grouping and Sorting
- Grouping and sorting is a process of grouping the data based on keys and sorting the values in ascending or descending order.
- Example:
    - Input: [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1)]
    - Output: [(1, [1]), (2, [1]), (3, [1]), (4, [1]), (5, [1])]
- Grouping and sorting is also called as `shuffle and sort`.

## Reduce
- Reduce is a function that takes the output from the map as an input and combines those data tuples into a smaller set of tuples.
- Reduce function is applied to each element in the list.
- Example:
    - Reduce function: `f(x, y) = x + y`
    - Input: [(1, [1]), (2, [1]), (3, [1]), (4, [1]), (5, [1])]
    - Output: [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1)]

# Word Count Example

```bash
map(key, value):
    # key: document name
    # value: document contents
    for each word w in value:
        EmitIntermediate(w, "1");



reduce(key, values):
    # key: a word
    # values: a list of counts
    int result = 0;
    for each v in values:
        result += ParseInt(v);
    Emit(AsString(result));
```
