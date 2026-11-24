"""SHARP: Shift-weighted Hierarchical Attribution with Relative Propagation correction.

Thin wrapper that delegates to the sharp-rca package (https://github.com/png261/SHARP).
"""

from typing import Any

from sharp.core import sharp as _sharp_core


def sharp(
    data: Any,
    inject_time: int | None = None,
    dataset: str | None = None,
    **kwargs: Any,
) -> dict[str, Any]:
    return _sharp_core(data, inject_time=inject_time, dataset=dataset, **kwargs)
