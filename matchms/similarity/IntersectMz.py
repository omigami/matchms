class IntersectMz:
    """IntersectMz function factory"""

    def __init__(self):
        """constructor"""

    def __call__(self, spectrum, reference_spectrum):
        """call method"""
        mz = set(spectrum.peaks.mz)
        mz_ref = set(reference_spectrum.peaks.mz)
        intersected = mz.intersection(mz_ref)
        unioned = mz.union(mz_ref)

        if len(unioned) == 0:
            return 0

        return len(intersected) / len(unioned)
