"""
This module will hold prompt templates for AI/ML concepts.
Each entry will map a concept name (e.g. 'gradient_descent')
to a descriptive text prompt we send to Gemini.
"""

# prompts.py
"""
Prompt templates for AI/ML concepts.

Each entry maps a concept name (e.g. 'gradient_descent')
to a descriptive text prompt suitable for Gemini.
"""

PROMPTS = {
    "gradient_descent": (
        "Create a simple whiteboard-style diagram showing gradient descent: "
        "a ball rolling down a curved loss function toward the minimum. "
        "Add arrows to indicate steps, but keep it clean and schematic."
    ),
    "eigenvectors": (
        "Create a whiteboard-style diagram that explains eigenvectors: "
        "draw a 2D vector being stretched along the same line after a matrix transformation. "
        "Use arrows and axes to make it clear and simple."
    ),
}
