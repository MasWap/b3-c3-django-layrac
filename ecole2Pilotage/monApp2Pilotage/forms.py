from wtforms.validators import DataRequired, Email, Length
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from django.contrib.auth.models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message='Adresse email invalide')])
    password = PasswordField('Mot de passe', validators=[DataRequired(message='Champ obligatoire'), Length(min=6, message='Le mot de passe doit contenir au moins 6 caractères')])
    submit = SubmitField('Se connecter')

    def validate(self):
        if not FlaskForm.validate(self):
            return False

        # Vérification du couple email/mot de passe dans la base de données
        user = User.query.filter_by(email=self.email.data).first()
        if user is None or not user.check_password(self.password.data):
            self.email.errors.append("Adresse email ou mot de passe incorrect")
            return False

        return True
