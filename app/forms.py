from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Email, Length, Optional

class LoginForm(FlaskForm):
    username = StringField("Nom d'utilisateur ou Email", validators=[InputRequired()])
    password = PasswordField('Mot de passe', validators=[InputRequired(), Length(min=6, max=80)])
    remember = BooleanField('Se rappeller de moi')

class RegisterForm(FlaskForm):
    name = StringField('Prénom', validators=[InputRequired()])
    surname = StringField('Nom', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('Mot de passe', validators=[InputRequired(), Length(min=6, max=80)])
    password_confirm = PasswordField('', validators=[InputRequired(), Length(min=6, max=80)])


class ChangeSelfInformationsForm(FlaskForm):
    name = StringField('Prénom')
    surname = StringField('Nom')
    username = StringField("Nom d'utilisateur")
    email = StringField('Email', validators=[Optional(), Email(message='Invalid email'), Length(max=50)])
    current_password = PasswordField('Mot de passe actuel *', validators=[InputRequired(), Length(min=6, max=80)])
    new_password = PasswordField('Nouveau mot de passe', validators=[Optional(), Length(min=6, max=80)])
    new_password_confirm = PasswordField('Confirmer votre nouveau mot de passe', validators=[Optional(), Length(min=6, max=80)])

class RequestResetPasswordForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired()])

class ResetPasswordForm(FlaskForm):
    new_password = PasswordField('Nouveau mot de passe', validators=[InputRequired(), Length(min=6, max=80)])
    new_password_confirm = PasswordField('Confirmer votre nouveau mot de passe', validators=[InputRequired(), Length(min=6, max=80)])
    submit = SubmitField('Réinitialiser mon mot de passe')