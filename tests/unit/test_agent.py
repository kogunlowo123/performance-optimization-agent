"""Performance Optimization Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_profile_application():
    """Test Profile application for CPU, memory, and I/O hotspots."""
    tools = AgentTools()
    result = await tools.profile_application(target="test", profile_type="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_analyze_slow_queries():
    """Test Identify and optimize slow database queries."""
    tools = AgentTools()
    result = await tools.analyze_slow_queries(query_log="test", database_type="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_suggest_optimizations():
    """Test Suggest performance improvements for code."""
    tools = AgentTools()
    result = await tools.suggest_optimizations(code="test", bottleneck_type="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_run_benchmark():
    """Test Run performance benchmarks and compare results."""
    tools = AgentTools()
    result = await tools.run_benchmark(benchmark_suite="test", iterations=1)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.performance_optimization_agent_agent import PerformanceOptimizationAgentAgent
    agent = PerformanceOptimizationAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
