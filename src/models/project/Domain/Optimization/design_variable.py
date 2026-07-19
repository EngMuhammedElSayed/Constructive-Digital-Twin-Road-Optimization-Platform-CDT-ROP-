"""
design_variable.py
==================

Backward compatibility module.

Historically, optimization variables may be referred to
as Design Variables.

The CDT-ROP domain model uses the term DecisionVariable,
which is the standard terminology in optimization theory.

Author : CDT-ROP Team
Version : 3.0.0
"""

from .decision_variable import DecisionVariable

__all__ = ["DecisionVariable"]