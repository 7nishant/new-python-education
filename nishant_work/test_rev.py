from rev_input import lst
def test_lst():

    result = lst('hello there i am robot')
    assert result == ' tobor ma i ereht olleh'

    result_neg = lst('hello')
    assert result_neg != 'helol'

    result1 = lst('12hello')
    assert result1 != "no number allowed"