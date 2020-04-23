import numpy
from matchms import Spikes


def select_by_relative_intensity(spectrum_in, intensity_from=0.0, intensity_to=1.0):

    if spectrum_in is None:
        return None

    spectrum = spectrum_in.clone()

    assert intensity_from >= 0.0, "'intensity_from' should be larger than or equal to 0."
    assert intensity_to <= 1.0, "'intensity_to' should be smaller than or equal to 1.0."
    assert intensity_from <= intensity_to, "'intensity_from' should be smaller than or equal to 'intensity_to'."

    scale_factor = numpy.max(spectrum.peaks.intensities)
    intensities = spectrum.peaks.intensities / scale_factor

    condition = numpy.logical_and(intensity_from <= intensities, intensities <= intensity_to)

    spectrum.peaks = Spikes(mz=spectrum.peaks.mz[condition],
                            intensities=spectrum.peaks.intensities[condition])

    return spectrum
