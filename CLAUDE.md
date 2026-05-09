# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Setup
python -m venv venv
Windows: venv\Scripts\activate          # source venv/bin/activate
pip install -r requirements.txt

# Run dev server (port 5001)
python app.py

# Run all tests
pytest

# Run a specific test file
pytest tests/test_foo.py

# Run a specific test by name
pytest -k "test_name"
```

## Architecture

**Spendly** is a Flask + SQLite personal expense tracker, currently in early development. Many routes are stubs that students will implement incrementally.

### Key files

– 'app.py' – all routes live here. Implemented: 'landing', 'register', 'login', 'terms', 'privacy'. Stubs (return plain strings): 'logout', 'profile', 'add_expense', 'edit_expense', 'delete_expense'.
– 'database/db.py' – will contain three helpers: 'get_db()' (SQLite connection with row_factory + FK enforcement), 'init_db()' (CREATE TABLE IF NOT EXISTS), 'seed_db()' (sample data). Currently empty/placeholder.
– 'templates/base.html' – shared layout: navbar (Sign in / Get started links) + footer (Terms, Privacy). All other templates should extend this via '{% extends "base.html" %}'.
– 'static/css/style.css – global styles;
– 'static/js/main.js' – vanilla JS only. No JS frameworks are used in this project.

### Constraints

– \*\*No JS libraries or frameworks – all frontend interactivity must be vanilla JS.
– Templates use Jinja2 with 'url_for()' for all internal links.
– The app uses Google Fonts (DM Serif Display, DM Sans) loaded via CDN in 'base.html'.
