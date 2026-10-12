from models.profile import Profile, Experience
def test_profile_model():
    p = Profile(name='Test User', skills=['Python'], experience=[Experience(company='Example', role='Engineer')])
    assert p.name == 'Test User'
    assert p.experience[0].company == 'Example'
