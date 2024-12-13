from my_scr.main  import Calculation, Text_Greeting
import pytest




@pytest.mark.calc
def test_sum():
    assert Calculation().sum(6, 4) == 10




@pytest.mark.calc
def test_sub():
    assert Calculation().sub(5, 3) == 2




@pytest.mark.calc
def test_mult():
    assert Calculation().multiply(5, 3) == 15




@pytest.mark.calc
def test_div():
    assert Calculation().div(20, 4) == 5




@pytest.mark.calc
def test_fpalyn():
    assert Calculation().find_palyndrome(True)




@pytest.mark.calc
@pytest.mark.skip()
def test_invisible():
    assert 33 == 5


#-----------НАЧАЛО ПРОВЕРКИ ВТОРОГО КЛАССА-----------#
@pytest.mark.greeting
@pytest.mark.parametrize('test_input,expected', [('Иван','Меня зовут Иван'),('Андрей','Меня зовут Андрей'),('Вадим','Меня зовут Мидам')])
def test_greeting(test_input,expected):
    assert Text_Greeting().greeting(test_input) == expected




@pytest.mark.greeting
def test_empty():
    assert  Text_Greeting.empty_string(True)


@pytest.mark.greeting
def  test_register():
    assert  Text_Greeting.register_check(True)




@pytest.mark.greeting
def test_long():
    assert Text_Greeting.register_check(True,"True")

@pytest.mark.greeting
def test_type():
    assert Text_Greeting.string_type(True)


@pytest.mark.greeting
@pytest.mark.skip()
def test_new_func():
    assert "Aboba" == "Anton"


@pytest.mark.greeting
@pytest.mark.skip()
def test_type():
    assert Text_Greeting().empty_string(True)
