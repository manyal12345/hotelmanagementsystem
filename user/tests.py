from django.test import TestCase

# Create your tests here.
import pytest
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_create_user():
    email = 'test@example.com'
    password = 'password123'
    user = User.objects.create_user(email, password=password)
    assert user.email == email
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser

@pytest.mark.django_db
def test_create_superuser():
    email = 'test@example.com'
    password = 'password123'
    user = User.objects.create_superuser(email, password=password)
    assert user.email == email
    assert user.is_active
    assert user.is_staff
    assert user.is_superuser