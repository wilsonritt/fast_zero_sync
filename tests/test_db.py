from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='batata', email='batata@teste.com', password='senhasegura'
    )

    session.add(user)
    session.commit()
    # session.refresh(user) # Atualiza o objeto com os dados do BD

    result = session.scalar(
        select(User).where(User.email == 'batata@teste.com')
    )

    assert result.username == 'batata'
