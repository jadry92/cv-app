"""
    View unit Test
"""
from django.contrib.auth import get_user_model

# Django
from django.urls import reverse

User = get_user_model()


def test_user_views(client):
    user = User.objects.create_user(username="testuser", password="testpass")

    # Test the login view
    url = reverse("account_login")
    response = client.get(url)
    assert response.status_code == 200
    assert "account/login.html" in [t.name for t in response.templates]

    # Test the signup view
    url = reverse("account_signup")
    response = client.get(url)
    assert response.status_code == 200
    assert "account/signup.html" in [t.name for t in response.templates]

    # Test the user detail view
    client.login(username="testuser", password="testpass")
    url = reverse("users:detail", args=[user.username])
    response = client.get(url)
    assert response.status_code == 200
    assert "users/user_detail.html" in [t.name for t in response.templates]
    assert user.username in str(response.content)
