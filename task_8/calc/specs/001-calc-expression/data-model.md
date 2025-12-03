# Data Model: Simple Expression Calculator

## Entities

### Expression

*   **Description**: The raw input string provided by the user, containing numbers, arithmetic operators, and potentially parentheses.
*   **Attributes**:
    *   `value`: string (e.g., "1 + 2 * (3 - 4)")
*   **Relationships**: Parsed into multiple `Token` entities.

### Token

*   **Description**: An atomic unit derived from parsing the `Expression`. Tokens can be numbers, operators, or parentheses.
*   **Attributes**:
    *   `type`: enum (e.g., `NUMBER`, `OPERATOR`, `LPAREN`, `RPAREN`)
    *   `value`: string (e.g., "1", "+", "(", "3.14")
*   **Relationships**: Part of an `Expression`'s parsed structure.

### Result

*   **Description**: The final numerical outcome of evaluating the `Expression`.
*   **Attributes**:
    *   `value`: number (e.g., 7, -5.2)
*   **Relationships**: Derived from the evaluation of an `Expression`.
