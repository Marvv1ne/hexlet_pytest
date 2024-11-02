from hexlet_pytest.example import reverse

def test_reverse():
    assert reverse('Hexlet') == 'telxeH'

def test_reverse_for_empty_string():
    assert reverse('') == ''

def test_reverse_with_fixture():
    fixture_path = 'tests/fixtures/before.txt'
    correct_answer_path = 'tests/fixtures/after.txt'
    with open(fixture_path, encoding='utf8') as f:
        with open(correct_answer_path, encoding='utf8') as a:
            string = f.readline().strip()
            reversed_string = a.readline().strip()
            assert reverse(string) == reversed_string

