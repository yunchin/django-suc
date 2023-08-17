from tests.testapp.models import MyModel


def test_auto_name():
    assert MyModel._meta.constraints[0].name == 'testapp_mymodel_field1_field2_2b52998b_uniq'


def test_given_name():
    assert MyModel._meta.constraints[1].name == 'MY_UNIQ_NAME'
