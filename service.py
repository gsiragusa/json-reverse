import collections


def reverse_json(obj=None):
    """
    Given a dict, reverse the order of the elements inside the dict
    :param obj: a dict, e.g. “{A:1, B:1, C:1, D:1, E:1}”
    :return: the dict with the elements reversed
    """

    if obj is None:
        return {}
    # extract the keys from the dict
    reversed_keys = [*obj]
    # reverse their order
    reversed_keys.reverse()
    # create the object that will be returned by the function
    out = collections.OrderedDict()
    # iterate through each element of the dict to generate the output
    for k in reversed_keys:
        # if the element is another dict, recursively call this function
        if isinstance(obj[k], dict):
            out[k] = reverse_json(obj[k])
            continue
        # otherwise store it in the ordered dict
        out[k] = obj[k]
    # return result
    return out
