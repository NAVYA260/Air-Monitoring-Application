from flask_wtf import FlaskForm 
from wtforms import SelectField,FloatField,SubmitField 
from wtforms.validators import DataRequired 
from wtforms.validators import DataRequired 


class CarbonFootPrintForm(FlaskForm):
    body_type = SelectField('Body Type', choices=[
        ('underweight', 'Underweight'),
        ('obese', 'Obese'),
        ('normal', 'Normal')
    ], validators=[DataRequired()])
    sex = SelectField('Sex', choices=[
        ('female', 'Female'),
        ('male', 'Male')
    ], validators=[DataRequired()])
    diet = SelectField('Diet', choices=[
        ('pescatarian', 'Pescatarian'),
        ('vegan', 'Vegan'),
        ('omnivore', 'Omnivore'),
        ('vegetarian', 'Vegetarian')
    ], validators=[DataRequired()])
    shower = SelectField('How Often Shower (days)', choices=[
        ('daily', 'Daily'),
        ('twice a day', 'Twice a day'),
        ('less frequently', 'Less frequently'),
        ('more frequently', 'More frequently')
    ], validators=[DataRequired()])
    heating_energy_source = SelectField('Heating Energy Source', choices=[
        ('electricity', 'Electricity'),
        ('coal', 'Coal'),
        ('wood', 'Wood'),
        ('natural gas', 'Natural gas')
    ], validators=[DataRequired()])
    transport = SelectField('Transport', choices=[
        ('walk/bicycle', 'Walk/Bicycle'),
        ('public', 'Public'),
        ('private', 'Private')
    ], validators=[DataRequired()])
    vehicle_type = SelectField('Vehicle Type', choices=[
        ('lpg', 'LPG'),
        ('electric', 'Electric'),
        ('petrol', 'Petrol'),
        ('hybrid', 'Hybrid'),
        ('diesel', 'Diesel')
    ],validators=[DataRequired()])
    social_activity = SelectField(
        'Social Activity',
        choices=[('often', 'Often'), ('sometimes', 'Sometimes'), ('rarely', 'Rarely'), ('never', 'Never')],
        validators=[DataRequired()]
    )
    grocery_bill = FloatField('Monthly Grocery Bill', validators=[DataRequired()])
    air_travel = SelectField(
        'Frequency of Traveling by Air',
        choices=[('very frequently', 'Very Frequently'), ('frequently', 'Frequently'), ('rarely', 'Rarely'), ('never', 'Never')],
        validators=[DataRequired()]
    )
    vehicle_distance = FloatField('Vehicle Monthly Distance (KM)', validators=[DataRequired()])
    waste_bag_size = SelectField(
        'Waste Bag Size',
        choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large'), ('extra large', 'Extra Large')],
        validators=[DataRequired()]
    )
    waste_bag_count = FloatField('Waste Bag Weekly Count', validators=[DataRequired()])
    tv_pc_hours = FloatField('How Long TV/PC Daily (hours)', validators=[DataRequired()])
    new_clothes = FloatField('How Many New Clothes Monthly', validators=[DataRequired()])
    internet_hours = FloatField('How Long Internet Daily (hours)', validators=[DataRequired()])
    energy_efficiency = SelectField(
        'Energy Efficiency',
        choices=[('No', 'No'), ('Sometimes', 'Sometimes'), ('Yes', 'Yes')],
        validators=[DataRequired()]
    )
    submit = SubmitField('Predict')