def test_home_page():
    """Verifie que la page d'accueil retourne une reponse valide."""
    from app import app

    client = app.test_client()
    response = client.get('/')

    assert response.status_code == 200


def test_app_is_created():
    """Verifie que l'application Flask est bien creee."""
    from app import app

    assert app is not None
