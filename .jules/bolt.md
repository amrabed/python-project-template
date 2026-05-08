## 2025-05-14 - Initial Performance Audit
**Learning:** The project is a small Python template. Major overhead comes from `uv run` and `click` imports.
**Action:** Minimize overhead in CLI entry points and avoid unnecessary imports in hot paths.
