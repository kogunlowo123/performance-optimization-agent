# Performance Optimization Agent Architecture

Performance engineering agent that profiles applications, identifies bottlenecks, suggests optimizations for CPU, memory, I/O, and database queries, runs benchmarks, and generates performance regression tests.

## Domain Tools

- **profile_application**: Profile application for CPU, memory, and I/O hotspots
- **analyze_slow_queries**: Identify and optimize slow database queries
- **suggest_optimizations**: Suggest performance improvements for code
- **run_benchmark**: Run performance benchmarks and compare results
- **generate_load_test**: Generate load test scenarios (k6, Locust, Artillery)
- **detect_memory_leaks**: Analyze heap dumps and allocation patterns for leaks