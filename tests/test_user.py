from userhero import heros


def test_heros():

    heros = heros.load()
    
    for hero in heros:
        assert hero.name
        assert hero.email
        assert hero.avatar