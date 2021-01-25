from service import reverse_json


def test_reverse_json():
    payload = {'key1': 1, 'key2': 2}
    expected = {'key2': 2, 'key1': 1}

    res = reverse_json(payload)

    assert res == expected


def test_reverse_json_one_el():
    payload = {'key1': 1}

    res = reverse_json(payload)

    assert res == payload


def test_reverse_json_none():
    res = reverse_json()

    assert res == {}
