def noise3d(x:int,y:int,z:int,seed:int = 0,amp:int = 1,) -> int:
    """
    Deterministic integer noise in the range [-amplitude, amplitude].
    """

    if amp < 0:
        raise ValueError("Amplitude cannot be negative")

    value = (
        x * 374761393
        + y * 668265263
        + z * 2147483647
        + seed * 1274126177
    )

    value = (value ^ (value >> 13)) * 1274126177
    value = value ^ (value >> 16)

    # Convert to a stable non-negative integer.
    value &= 0xFFFFFFFF

    # Convert to [0, 2 * amplitude].
    return (value % (2 * amp + 1)) - amp