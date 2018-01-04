# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-04 21:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0010_auto_20180104_2138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currency',
            old_name='shortName',
            new_name='short_name',
        ),
        migrations.RenameField(
            model_name='customergrouptransform',
            old_name='fromCustomerGroup',
            new_name='from_customer_group',
        ),
        migrations.RenameField(
            model_name='customergrouptransform',
            old_name='toCustomerGroup',
            new_name='to_customer_group',
        ),
        migrations.RenameField(
            model_name='price',
            old_name='customerGroup',
            new_name='customer_group',
        ),
        migrations.RenameField(
            model_name='price',
            old_name='validfrom',
            new_name='valid_from',
        ),
        migrations.RenameField(
            model_name='price',
            old_name='validuntil',
            new_name='valid_until',
        ),
        migrations.RenameField(
            model_name='tax',
            old_name='accountActiva',
            new_name='account_activa',
        ),
        migrations.RenameField(
            model_name='tax',
            old_name='accountPassiva',
            new_name='account_passiva',
        ),
        migrations.RenameField(
            model_name='tax',
            old_name='taxrate',
            new_name='tax_rate',
        ),
        migrations.RenameField(
            model_name='unit',
            old_name='fractionFactorToNextHigherUnit',
            new_name='fraction_factor_to_next_higher_unit',
        ),
        migrations.RenameField(
            model_name='unit',
            old_name='isAFractionOf',
            new_name='is_a_fraction_of',
        ),
        migrations.RenameField(
            model_name='unit',
            old_name='shortName',
            new_name='short_name',
        ),
        migrations.RenameField(
            model_name='unittransform',
            old_name='fromUnit',
            new_name='from_unit',
        ),
        migrations.RenameField(
            model_name='unittransform',
            old_name='toUnit',
            new_name='to_unit',
        ),
    ]
