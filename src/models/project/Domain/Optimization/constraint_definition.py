"""
constraint_definition.py
========================

Backward compatibility module.

This module re-exports the OptimizationConstraint
domain model.

Use OptimizationConstraint directly in new code.

Author : CDT-ROP Team
Version : 3.0.0
"""

from .optimization_constraint import OptimizationConstraint

__all__ = ["OptimizationConstraint"]