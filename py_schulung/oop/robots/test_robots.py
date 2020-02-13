from robots import Robot


def test_Robot():
    r = Robot("Marvin", "Nürnberg")
    assert r.name == "Marvin"
    assert r.city == "Nürnberg"
