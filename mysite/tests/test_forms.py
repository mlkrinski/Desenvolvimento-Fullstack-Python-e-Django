from contacts.forms import NameForm


def test_name_form_sucess():
    # Given
    data = {"your_name": "John"}
    form = NameForm(data=data)
    # When
    is_valid = form.is_valid()

    # Then
    assert is_valid is True


def test_name_form_your_name_max_length():
    # Given
    data = {"your_name": "John" * 30}
    form = NameForm(data=data)
    # When
    is_valid = form.is_valid()
    # Then
    assert is_valid is False
    assert form.errors == {
        "your_name": ["Certifique-se de que o valor tenha no máximo 100 caracteres (ele possui 120)."]
    }


def test_name_form_failure():
    # Given
    data = {}
    form = NameForm(data=data)

    # When
    is_bound = form.is_bound
    is_valid = form.is_valid()

    # Then
    assert is_valid is False
    assert is_bound is True
