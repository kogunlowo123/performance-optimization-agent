# Performance Optimization Agent

[![CI](https://github.com/kogunlowo123/performance-optimization-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/performance-optimization-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Software Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Performance engineering agent that profiles applications, identifies bottlenecks, suggests optimizations for CPU, memory, I/O, and database queries, runs benchmarks, and generates performance regression tests.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `profile_application` | Profile application for CPU, memory, and I/O hotspots |
| `analyze_slow_queries` | Identify and optimize slow database queries |
| `suggest_optimizations` | Suggest performance improvements for code |
| `run_benchmark` | Run performance benchmarks and compare results |
| `generate_load_test` | Generate load test scenarios (k6, Locust, Artillery) |
| `detect_memory_leaks` | Analyze heap dumps and allocation patterns for leaks |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/profile` | Profile application performance |
| `POST` | `/api/v1/queries/analyze` | Analyze slow database queries |
| `POST` | `/api/v1/optimize` | Suggest optimizations |
| `POST` | `/api/v1/benchmark` | Run performance benchmarks |
| `POST` | `/api/v1/load-test` | Generate load test |
| `POST` | `/api/v1/memory/analyze` | Detect memory leaks |

## Features

- Profiling
- Bottleneck Detection
- Query Optimization
- Benchmark Generation
- Regression Testing

## Integrations

- Apm Connector
- Profiler
- Database Analyzer
- Load Test Runner

## Architecture

```
performance-optimization-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── performance_optimization_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 6 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 6 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 4 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**LLM + Profiling Tools + APM**

---

Built as part of the Enterprise AI Agent Platform.
