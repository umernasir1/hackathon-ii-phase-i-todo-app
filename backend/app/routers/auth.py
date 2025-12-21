from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from app.models import User, UserCreate, UserLogin, Token, UserResponse
from app.database import get_session
from app.auth import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=Token, status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate, session: Session = Depends(get_session)):
    """Register a new user"""

    # Check if user already exists
    statement = select(User).where(User.email == user_data.email)
    existing_user = session.exec(statement).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # Create new user
    hashed_password = hash_password(user_data.password)
    new_user = User(email=user_data.email, password_hash=hashed_password)

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    # Create access token (sub must be a string per JWT spec)
    access_token = create_access_token(data={"sub": str(new_user.id)})

    return Token(
        access_token=access_token,
        user=UserResponse(
            id=new_user.id,
            email=new_user.email,
            created_at=new_user.created_at
        )
    )


@router.post("/login", response_model=Token)
def login(user_data: UserLogin, session: Session = Depends(get_session)):
    """Login an existing user"""

    # Find user by email
    statement = select(User).where(User.email == user_data.email)
    user = session.exec(statement).first()

    if not user or not verify_password(user_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create access token (sub must be a string per JWT spec)
    access_token = create_access_token(data={"sub": str(user.id)})

    return Token(
        access_token=access_token,
        user=UserResponse(
            id=user.id,
            email=user.email,
            created_at=user.created_at
        )
    )
