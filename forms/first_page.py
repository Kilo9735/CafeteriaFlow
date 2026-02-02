from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired


class First_page(FlaskForm):
    # menu = SubmitField('Меню')
    basket = SubmitField('Корзина')
    profile = SubmitField('Профиль')
    top_up_acc = SubmitField('Пополнить')
    reviews = SubmitField('Отзывы')
    lunch = SubmitField('Обед')
    breakfast = SubmitField('Завтрак')