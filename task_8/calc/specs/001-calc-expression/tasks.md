# Tasks: Simple Expression Calculator

**Input**: Design documents from `/specs/001-calc-expression/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: This plan includes test tasks as TDD approach was indicated in the constitution.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project, as per plan.md structure.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project root `src/` and `tests/` directories
- [x] T002 Create `src/main.py`, `src/calculator.py`, `src/errors.py`
- [x] T003 Create `tests/unit/` and `tests/integration/` directories
- [x] T004 Create `tests/unit/test_calculator.py` and `tests/unit/test_errors.py`
- [x] T005 Create `tests/integration/test_cli.py`
- [x] T006 Initialize Python virtual environment
- [x] T007 Install `pytest` (using `pip install pytest`)
- [x] T008 [P] Configure basic `pytest` setup (e.g., `pytest.ini` if needed) at project root

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T009 Implement custom exception classes (e.g., `InvalidExpressionError`, `DivisionByZeroError`) in `src/errors.py`
- [x] T010 Create a basic structure for `src/calculator.py` with placeholder functions for operations (e.g., `evaluate_expression`)
- [x] T011 Create a basic structure for `src/main.py` to handle CLI interaction (e.g., argument parsing or taking input from stdin)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Evaluate Basic Arithmetic (Priority: P1) 🎯 MVP

**Goal**: Users can input a simple arithmetic expression and receive the calculated numerical result.

**Independent Test**: Provide string expressions like "5 + 3", "1 + 2 * 3", "(1 + 2) * 3" and verify the numerical output (8, 7, 9 respectively).

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T012 [US1] Write unit tests for `src/calculator.py` covering tokenization, parsing, and evaluation of valid arithmetic expressions (including order of operations and parentheses) in `tests/unit/test_calculator.py`.
- [x] T013 [US1] Write integration tests for `src/main.py` accepting valid expressions and returning correct results in `tests/integration/test_cli.py`.

### Implementation for User Story 1

- [x] T014 [US1] Implement the tokenizer/parser in `src/calculator.py` to convert an expression string into an ordered list of tokens.
- [x] T015 [US1] Implement the evaluation logic in `src/calculator.py` to process tokens and calculate the numerical result, correctly applying order of operations and handling parentheses.
- [ ] T016 [US1] Implement the core CLI logic in `src/main.py` to accept an expression string from the user and display the numerical result.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Handle Invalid Expressions (Priority: P2)

**Goal**: When an invalid arithmetic expression is input, the user receives a clear and understandable error message.

**Independent Test**: Provide various invalid string expressions (e.g., "1 +", "abc + 1", "1 / 0", "((1 + 2)") and check that appropriate, distinct error messages are displayed.

### Tests for User Story 2 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T017 [US2] Write unit tests for error handling in `src/calculator.py` and `src/errors.py` for invalid expression formats, invalid numbers, division by zero, mismatched parentheses, and unsupported operators in `tests/unit/test_calculator.py` and `tests/unit/test_errors.py`.
- [ ] T018 [US2] Write integration tests for `src/main.py` handling invalid expressions and displaying user-friendly error messages in `tests/integration/test_cli.py`.

### Implementation for User Story 2

- [ ] T019 [US2] Enhance the tokenizer/parser and evaluation logic in `src/calculator.py` to detect and raise specific custom errors (e.g., `InvalidExpressionError`, `DivisionByZeroError`) for invalid inputs.
- [ ] T020 [US2] Update `src/main.py` to catch custom exceptions from `calculator.py` and display user-friendly error messages to the standard error output.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T021 [P] Review and add comprehensive docstrings and comments to all functions/classes in `src/main.py`, `src/calculator.py`, and `src/errors.py`.
- [ ] T022 Review code for adherence to PEP8 standards in `src/`.
- [ ] T023 Update `README.md` (at project root) with instructions on how to install, run the application, and execute tests.

---

## Dependencies & Execution Order

### Phase Dependencies

-   **Setup (Phase 1)**: No dependencies - can start immediately.
-   **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories.
-   **User Story 1 (Phase 3)**: Depends on Foundational completion.
-   **User Story 2 (Phase 4)**: Depends on Foundational completion. May build upon US1 but should remain independently testable for its core error handling.
-   **Polish (Phase 5)**: Depends on all desired user stories being complete.

### User Story Dependencies

-   **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories.
-   **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but its core error handling functionality is independently testable.

### Within Each User Story

-   Tests MUST be written and FAIL before implementation.
-   Models (implicitly, error classes) before services (calculator logic).
-   Core calculator implementation before main CLI integration.

### Parallel Opportunities

-   All Setup tasks marked [P] (T008) can run in parallel.
-   Once Foundational phase completes, writing tests for User Story 1 (T012, T013) and User Story 2 (T017, T018) can occur in parallel.
-   T021 (docstrings/comments) can be initiated earlier once respective files are created, or run in parallel towards the end.

---

## Parallel Example: User Story 1

```bash
# Writing Tests (can run in parallel)
Task: T012 [US1] Write unit tests for src/calculator.py covering tokenization, parsing, and evaluation of valid arithmetic expressions in tests/unit/test_calculator.py
Task: T013 [US1] Write integration tests for src/main.py accepting valid expressions and returning correct results in tests/integration/test_cli.py

# Implementation (sequential within the story, but different files can be worked on in parallel)
Task: T014 [US1] Implement the tokenizer/parser in src/calculator.py
Task: T015 [US1] Implement the evaluation logic in src/calculator.py
Task: T016 [US1] Implement the core CLI logic in src/main.py
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1.  Complete Phase 1: Setup
2.  Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3.  Complete Phase 3: User Story 1
4.  **STOP and VALIDATE**: Test User Story 1 independently
5.  Deploy/demo if ready

### Incremental Delivery

1.  Complete Setup + Foundational → Foundation ready
2.  Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3.  Add User Story 2 → Test independently → Deploy/Demo
4.  Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1.  Team completes Setup + Foundational together
2.  Once Foundational is done:
    -   Developer A: User Story 1
    -   Developer B: User Story 2
3.  Stories complete and integrate independently

---

## Notes

-   [P] tasks = different files, no dependencies
-   [Story] label maps task to specific user story for traceability
-   Each user story should be independently completable and testable
-   Verify tests fail before implementing
-   Commit after each task or logical group
-   Stop at any checkpoint to validate story independently
-   Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
