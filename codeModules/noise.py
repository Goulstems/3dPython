from functools import lru_cache
from math import floor, sqrt
from random import Random


_GRADIENTS = (
    (1 / sqrt(2), 1 / sqrt(2)),
    (-1 / sqrt(2), 1 / sqrt(2)),
    (1 / sqrt(2), -1 / sqrt(2)),
    (-1 / sqrt(2), -1 / sqrt(2)),
    (1.0, 0.0),
    (-1.0, 0.0),
    (0.0, 1.0),
    (0.0, -1.0),
)


@lru_cache(maxsize=32)
def _permutation(seed: int) -> tuple[int, ...]:
    values = list(range(256))
    Random(seed).shuffle(values)
    return tuple(values + values)


def _gradient_dot(
    permutation: tuple[int, ...],
    x: int,
    z: int,
    offset_x: float,
    offset_z: float,
) -> float:
    gradient_index = permutation[permutation[x & 255] + (z & 255)] & 7
    gradient_x, gradient_z = _GRADIENTS[gradient_index]
    return gradient_x * offset_x + gradient_z * offset_z


def _fade(value: float) -> float:
    return value * value * value * (value * (value * 6 - 15) + 10)


def _lerp(start: float, end: float, amount: float) -> float:
    return start + amount * (end - start)


def noise(x: float, z: float, seed: int = 0) -> float:
    """
    Generate seeded, continuous 2D Perlin noise at an X/Z coordinate.

    Nearby coordinates produce smoothly varying values. The same coordinates
    and seed always produce the same value, approximately within [-1, 1].

    Args:
        x: Continuous X-coordinate to sample.
        z: Continuous Z-coordinate to sample.
        seed: Integer used to select the noise pattern.

    Returns:
        A deterministic Perlin noise value approximately between -1 and 1.
    """
    x_floor = floor(x)
    z_floor = floor(z)
    offset_x = x - x_floor
    offset_z = z - z_floor
    permutation = _permutation(seed)

    lower_left = _gradient_dot(permutation, x_floor, z_floor, offset_x, offset_z)
    lower_right = _gradient_dot(permutation, x_floor + 1, z_floor, offset_x - 1, offset_z)
    upper_left = _gradient_dot(permutation, x_floor, z_floor + 1, offset_x, offset_z - 1)
    upper_right = _gradient_dot(
        permutation, x_floor + 1, z_floor + 1, offset_x - 1, offset_z - 1
    )

    blend_x = _fade(offset_x)
    blend_z = _fade(offset_z)
    lower = _lerp(lower_left, lower_right, blend_x)
    upper = _lerp(upper_left, upper_right, blend_x)
    return _lerp(lower, upper, blend_z)