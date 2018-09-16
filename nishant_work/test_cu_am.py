from cur_con import curr

def test_con():
    result = curr(10)
    assert result == 720

    result_neg = curr(12)
    assert result_neg != 222

    result1 = curr(-10)
    assert result1 == 'no negative value allowed'