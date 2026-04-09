# AGENTS.md

This file provides guidelines for AI coding agents (e.g., GitHub Copilot, Cursor, Codex) working in this repository.

## Dependencies

- Always use Poetry for dependency management (`poetry add <package>`)
- Use Pydantic for data models
- Use Pydantic-settings for environment variable configuration in a `settings.py` file

## Testing Guidelines

- Use pytest, not unittest
- Use `pytest` monkeypatch and `pytest-mock` for mocking instead of `unittest.MagicMock`
- Do not cheat! Never modify source code just to make a failing test pass. Fix real bugs in source code and fix incorrect assertions in tests

## Make Targets

Use `make` targets for all common workflows: lint, test, run locally, and deploy. Refer to `docs/README.md` for currently available targets. Add new targets to `Makefile` as needed.

## Notes

- Python 3.12+ required
- Dependencies are managed via `pyproject.toml` and locked in `poetry.lock`
- Do not edit `poetry.lock` directly; use `make update` to update dependencies

## Coding Conventions

### Field descriptions

Every field in a Pydantic model or pydantic-settings class must be documented using `Field(description="...")`. This makes descriptions machine-readable and visible in generated JSON schemas.

```python
from uuid import uuid4
from pydantic import BaseModel, Field

class Item(BaseModel, populate_by_name=True, alias_generator=to_camel):
    id: str = Field(description="Unique item identifier.", default_factory=lambda:str(uuid4()))
    name: str = Field(description="Human-readable item name.")
```

### camelCase alias convention

All `BaseModel` subclasses must be defined with `populate_by_name=True` and `alias_generator=to_camel` so that JSON payloads can use camelCase while Python attributes use snake_case. Always serialise with `model_dump(by_alias=True, exclude_none=True)` to produce camelCase JSON output and omit unset optional fields.

```python
from uuid import uuid4
from pydantic import BaseModel, Field
from pydantic.alias_generators import to_camel

class Item(BaseModel, populate_by_name=True, alias_generator=to_camel):
    item_id: str = Field(description="Unique item identifier.", default_factory=str(uuid4()))
    # Accepts {"itemId": "..."} from JSON; attribute is item.item_id
    # model_dump() → {"item_id": ...}
    # model_dump(by_alias=True, exclude_none=True) → {"itemId": ...}
```

### No `model_config` class attribute

Do not use `model_config = ConfigDict(...)` or `model_config = SettingsConfigDict(...)`. Pass configuration options as keyword arguments to the base class instead.

```python
# Good
class Item(BaseModel, extra="allow", populate_by_name=True, alias_generator=to_camel): ...
class Settings(BaseSettings, case_sensitive=False): ...

# Bad
class Item(BaseModel):
    model_config = ConfigDict(extra="allow")
```

### Import style

Do not add unnecessary imports like `from __future__ import annotations`. Always use explicit `from x import y` form:

```python
from json import dumps, loads
from pytest import fixture, main, raises
from aws_cdk.aws_lambda import Code, Function, Runtime
```

### Test file main block

Every test file must end with:

```python
if __name__ == "__main__":
    main()
```
