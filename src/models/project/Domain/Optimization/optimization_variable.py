"""
optimization_variable.py
========================

Optimization Variable Compatibility Module

CDT-ROP
Constructive Digital Twin Road Optimization Platform

This module is provided for backward compatibility.

The official Optimization Domain model uses
DecisionVariable as the standard representation of
optimization variables.

Author : CDT-ROP Team
Version : 3.0.0
"""

from .decision_variable import DecisionVariable

__all__ = ["DecisionVariable"]