# Mezzoic Clean Architecture Template

A Python project template implementing Clean Architecture principles, designed for rapid application development with a clear separation of concerns. This template provides a solid starting point for building maintainable, testable, and scalable applications.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Architecture](#architecture)
4. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
   - [Configuration](#configuration)
5. [Project Structure](#project-structure)
6. [Usage](#usage)
   - [Running the Application](#running-the-application)
   - [Environment Variables](#environment-variables)
7. [Testing](#testing)
8. [Linting & Formatting](#linting--formatting)
9. [Docker Support](#docker-support)
10. [Continuous Integration](#continuous-integration)
11. [Contributing](#contributing)
12. [License](#license)

---

## Project Overview

This template provides an opinionated setup for Python applications following Clean Architecture:

- **Dependency Rule:** Inner layers never depend on outer layers.
- **Separation of Concerns:** Entities, use cases, interface adapters, and frameworks/external interfaces are decoupled.
- **Testability:** Core business logic is independent of frameworks, making unit testing straightforward.

Use this template to bootstrap services, APIs, command-line tools, or any domain-driven application.

---

## Features

- Python 3.10+ compatibility
- FastAPI example setup for HTTP APIs
- SQLAlchemy for persistence
- Repository pattern for data access
- Pydantic models for validation
- Dockerized development environment
- Preconfigured GitHub Actions for CI
- Structured logging with `loguru`
- Environment-based configuration with `python-dotenv`
- Automated testing with pytest

---

## Architecture

```
┌─────────────────────────┐       ┌───────────────────┐
│     Presentation        │◀────▶│   Application     │
│   (FastAPI Controllers, │       │   (Use Cases)     │
│    FastMCP Handlers)    │       │                   │
└─────────────────────────┘       └───────────────────┘
           ▲                                   ▲
           │                                   │
┌─────────────────────────┐      ┌───────────────────┐
│   Infrastructure        │────▶│     Domain        │
│   (DB, External APIs)   │      │   (Entities)      │
└─────────────────────────┘      └───────────────────┘
```

- **Domain Layer:** Business entities and domain logic.
- **Application Layer:** Use cases orchestrating domain logic.
- **Interfaces/Adapters:** Controllers, repositories, and external service clients.
- **Infrastructure Layer:** DB implementations, external APIs, frameworks.
- **Presentation Layer:** API and MCP endpoints.
---

## Getting Started

### Prerequisites

- Python 3.10 or higher

### Installation

1. **Clone the repo**

   ```bash
   git clone https://https://github.com/mezzoic/demo_mcp_server.git
   cd demo_mcp_server
   ```

2. **Set up environment**

   ```bash
   uv venv
   # Update .venv with your configuration
   ```

3. **Install dependencies**

   ```bash
   uv pip install      
   ```

---

## Project Structure

```
├── app
│   ├── config             # configuration
│   ├── infrastructure     # DB adapters, external integrations
│   |     ├── api          # FastAPI route handlers
|   |     └── persistence  # DB adapters
│   ├── use_cases          # Application use case implementations
│   ├── domain             # Core business entities
|   ├── static             # static files, images, css, favicon
│   └── interfaces         # Interfaces
│   |     ├── controllers  # Api interfaces
|   |     └── repositories # Repository Interfaces
|   └── main.py            # entry point for the server app
|   
├── client
|     └── client.py        # client for the server app
├── tests                  # Unit and integration tests
├── pyproject.toml         # Poetry configuration
└── README.md
```

---

## Usage

### Running the Application

- **Locally:**
  ```bash
  uvicorn app.main:app --reload
  ```

- **Client:**
  ```bash
  python client/client.py

  ```

### Environment Variables

| Variable       | Description                       | Default |
| -------------- | --------------------------------- | ------- |
| `DB_SERVER`    | Database server uri               |         |
| `DB_NAME`      | database name                     |         |  
| `DB_USER`      | database user with permissions    |         |
| `DB_PASSWORD`  | user password                     |         |
---

## Testing

Run tests with:

```bash
pytest --cov=app
```

Coverage report will be output under `coverage/`.

---


## Docker Support

Build and run with Docker Compose:

```bash
docker-compose up --build
```

---

## Continuous Integration

A GitHub Actions workflow (`.github/workflows/ci.yml`) is preconfigured to run tests, lint, and type checks on every push.

---

## Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

Please follow the [Code of Conduct](CODE_OF_CONDUCT.md) and [Contribution Guidelines](CONTRIBUTING.md).

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

