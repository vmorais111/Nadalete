import pytest
from Email import Email
from Person import Person
from PersonDAO import PersonDAO

class TestPersonDAO:
    def test_valid_person_ok(self):
        p = Person(id=1, name="Ana Maria", age=30, emails=[Email(1, "ana@maria.com")])
        assert PersonDAO.isValidToInclude(p) == []

    @pytest.mark.parametrize("name", ["Ana", "  Só   ", ""])
    def test_name_must_have_at_least_two_parts(self, name):
        p = Person(id=1, name=name, age=20, emails=[Email(1, "a@b.com")])
        erros = PersonDAO.isValidToInclude(p)
        assert "Nome deve conter ao menos duas partes." in erros

    @pytest.mark.parametrize("name", ["Ana Maria1", "A2a Maria", "Ana-Maria"])
    def test_name_parts_letters_only(self, name):
        p = Person(id=1, name=name, age=20, emails=[Email(1, "a@b.com")])
        erros = PersonDAO.isValidToInclude(p)
        assert "Nome deve conter apenas letras em cada parte." in erros

    @pytest.mark.parametrize("age", [0, -1, 201, 999])
    def test_age_interval_invalid(self, age):
        p = Person(id=1, name="Ana Maria", age=age, emails=[Email(1, "a@b.com")])
        erros = PersonDAO.isValidToInclude(p)
        assert "Idade deve estar no intervalo [1, 200]." in erros

    def test_age_border_values_valid(self):
        p1 = Person(id=1, name="Ana Maria", age=1, emails=[Email(1, "a@b.com")])
        p2 = Person(id=2, name="Ana Maria", age=200, emails=[Email(2, "a@b.com")])
        assert PersonDAO.isValidToInclude(p1) == []
        assert PersonDAO.isValidToInclude(p2) == []

    def test_at_least_one_email(self):
        p = Person(id=1, name="Ana Maria", age=20, emails=[])
        erros = PersonDAO.isValidToInclude(p)
        assert "Pessoa deve possuir ao menos um e-mail associado." in erros

    @pytest.mark.parametrize("email", ["abc", "a@b", "@b.com", "a@.com", "a@b.", "a b@c.com", "a@b@c.com"])
    def test_email_format(self, email):
        p = Person(id=1, name="Ana Maria", age=20, emails=[Email(1, email)])
        erros = PersonDAO.isValidToInclude(p)
        assert any("E-mail inválido" in e for e in erros)

    def test_save_persists_when_valid_and_raises_when_invalid(self):
        dao = PersonDAO()
        PersonDAO.clear_storage()
        valid = Person(id=1, name="Ana Maria", age=25, emails=[Email(1, "ana@maria.com")])
        dao.save(valid)
        all_people = PersonDAO.all()
        assert len(all_people) == 1
        assert all_people[0].name == "Ana Maria"
        assert all_people[0].age == 25
        assert all_people[0].emails[0].name == "ana@maria.com"
        invalid = Person(id=2, name="Ana", age=0, emails=[Email(2, "x")])
        with pytest.raises(ValueError) as exc:
            dao.save(invalid)
        assert "Objeto Person inválido" in str(exc.value)
