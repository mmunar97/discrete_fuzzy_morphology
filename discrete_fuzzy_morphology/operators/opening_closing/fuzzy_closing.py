import numpy

from discrete_fuzzy_operators.base.operators.binary_operators.suboperators.fuzzy_implication_operator import DiscreteFuzzyImplicationOperator
from discrete_fuzzy_operators.base.operators.binary_operators.suboperators.fuzzy_aggregation_operator import DiscreteFuzzyAggregationBinaryOperator
from discrete_fuzzy_morphology.base.structuring_element import StructuringElement
from discrete_fuzzy_morphology.operators.erosion_dilation.fuzzy_dilation import fuzzy_image_dilation
from discrete_fuzzy_morphology.operators.erosion_dilation.fuzzy_erosion import fuzzy_image_erosion


def fuzzy_image_closing(image: numpy.ndarray,
                        structuring_element: StructuringElement,
                        iterations: int,
                        erosion_implication: DiscreteFuzzyImplicationOperator,
                        dilation_tnorm: DiscreteFuzzyAggregationBinaryOperator):
    """
    Applies the fuzzy closing to a grayscale image.

    Args:
        image: A numpy array, representing the image to be opened.
        structuring_element: A StructuringElement object, representing the properties and the shape of the
                             structuring element to be used.
        iterations: An integer, representing the number of times that the opening has to be applied to the image.
        erosion_implication: A DiscreteFuzzyImplicationOperator object, representing the implication to be used in the
                             erosion.
        dilation_tnorm: A DiscreteFuzzyAggregationBinaryOperator object, representing the t-norm to be used in the
                        dilation.

    References:
        González-Hidalgo, M., & Massanet, S. (2014).
        A fuzzy mathematical morphology based on discrete t-norms: fundamentals and applications to image processing.
        Soft Computing, 18 (11), 2297–2311. https://doi.org/10.1007/s00500-013-1204-6

    Returns:
        An image with the same dimension as the input image, representing the opened image.
    """
    result = image.copy()
    for _ in range(0, iterations):
        dilation = fuzzy_image_dilation(image=result,
                                        structuring_element=structuring_element,
                                        iterations=1,
                                        t_norm=dilation_tnorm)
        erosion = fuzzy_image_erosion(image=dilation,
                                      structuring_element=structuring_element.get_reflected_structuring_element(),
                                      iterations=1,
                                      implication=erosion_implication)

        result = erosion
    return result


