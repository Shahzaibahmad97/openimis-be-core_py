# Generated by Django 3.2.18 on 2023-05-15 13:03

import core.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('location', '0001_initial'),
        ('core', '0019_extended_field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='altlanguage',
            new_name='alt_language',
        ),
        migrations.AddField(
            model_name='interactiveuser',
            name='is_associated',
            field=models.BooleanField(blank=True, db_column='IsAssociated', help_text='has a claim admin or enrolment officer account', null=True),
        ),
        migrations.AddField(
            model_name='interactiveuser',
            name='language',
            field=models.ForeignKey(db_column='LanguageID', on_delete=django.db.models.deletion.DO_NOTHING, to='core.language'),
        ),
        migrations.AddField(
            model_name='interactiveuser',
            name='last_login',
            field=models.DateTimeField(db_column='LastLogin', null=True),
        ),
        migrations.AddField(
            model_name='interactiveuser',
            name='password',
            field=models.CharField(blank=True, db_column='StoredPassword', help_text='By default a SHA256 of the private key (salt) and password', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='interactiveuser',
            name='password_validity',
            field=models.DateTimeField(blank=True, db_column='PasswordValidity', null=True),
        ),
        migrations.AddField(
            model_name='interactiveuser',
            name='private_key',
            field=models.CharField(blank=True, db_column='PrivateKey', help_text='The private key is actually a password salt', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='interactiveuser',
            name='uuid',
            field=models.CharField(db_column='UserUUID', default=uuid.uuid4, max_length=36, unique=True),
        ),
        migrations.AddField(
            model_name='officer',
            name='address',
            field=models.CharField(blank=True, db_column='permanentaddress', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='officer',
            name='audit_user_id',
            field=models.IntegerField(db_column='AuditUserID'),
        ),
        migrations.AddField(
            model_name='officer',
            name='dob',
            field=models.DateField(blank=True, db_column='DOB', null=True),
        ),
        migrations.AddField(
            model_name='officer',
            name='email',
            field=models.CharField(blank=True, db_column='EmailId', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='officer',
            name='has_login',
            field=models.BooleanField(blank=True, db_column='HasLogin', null=True),
        ),
        migrations.AddField(
            model_name='officer',
            name='json_ext',
            field=models.JSONField(blank=True, db_column='JsonExt', null=True),
        ),
        migrations.AddField(
            model_name='officer',
            name='legacy_id',
            field=models.IntegerField(blank=True, db_column='LegacyID', null=True),
        ),
        migrations.AddField(
            model_name='officer',
            name='location',
            field=models.ForeignKey(blank=True, db_column='LocationId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='location.location'),
        ),
        migrations.AddField(
            model_name='officer',
            name='phone',
            field=models.CharField(blank=True, db_column='Phone', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='officer',
            name='phone_communication',
            field=models.BooleanField(blank=True, db_column='PhoneCommunication', null=True),
        ),
        migrations.AddField(
            model_name='officer',
            name='substitution_officer',
            field=models.ForeignKey(blank=True, db_column='OfficerIDSubst', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.officer'),
        ),
        migrations.AddField(
            model_name='officer',
            name='validity_from',
            field=core.fields.DateTimeField(db_column='ValidityFrom', default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='officer',
            name='validity_to',
            field=core.fields.DateTimeField(blank=True, db_column='ValidityTo', null=True),
        ),
        migrations.AddField(
            model_name='officer',
            name='veo_dob',
            field=models.DateField(blank=True, db_column='VEODOB', null=True),
        ),
        migrations.AddField(
            model_name='officer',
            name='veo_last_name',
            field=models.CharField(blank=True, db_column='VEOLastName', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='officer',
            name='veo_other_names',
            field=models.CharField(blank=True, db_column='VEOOtherNames', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='officer',
            name='veo_phone',
            field=models.CharField(blank=True, db_column='VEOPhone', max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='officer',
            name='works_to',
            field=models.DateTimeField(blank=True, db_column='WorksTo', null=True),
        ),
        migrations.AddField(
            model_name='usergroup',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auth.group'),
        ),
        migrations.AddField(
            model_name='usergroup',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.user'),
        ),
        migrations.AddField(
            model_name='userrole',
            name='role',
            field=models.ForeignKey(db_column='RoleID', on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_roles', to='core.role'),
        ),
        migrations.AddField(
            model_name='userrole',
            name='user',
            field=models.ForeignKey(db_column='UserID', on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_roles', to='core.interactiveuser'),
        ),
        migrations.AlterField(
            model_name='interactiveuser',
            name='login_name',
            field=models.CharField(db_column='LoginName', max_length=50),
        ),
        migrations.AlterField(
            model_name='interactiveuser',
            name='validity_from',
            field=core.fields.DateTimeField(db_column='ValidityFrom', default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='language',
            name='code',
            field=models.CharField(db_column='LanguageCode', max_length=5, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='officer',
            name='code',
            field=models.CharField(db_column='Code', max_length=50),
        ),
        migrations.AlterField(
            model_name='officer',
            name='veo_code',
            field=models.CharField(blank=True, db_column='VEOCode', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='uuid',
            field=models.CharField(db_column='RoleUUID', default=uuid.uuid4, max_length=36, unique=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='validity_from',
            field=core.fields.DateTimeField(db_column='ValidityFrom', default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='role',
            name='validity_to',
            field=core.fields.DateTimeField(blank=True, db_column='ValidityTo', null=True),
        ),
        migrations.AlterField(
            model_name='roleright',
            name='validity_from',
            field=core.fields.DateTimeField(db_column='ValidityFrom', default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='roleright',
            name='validity_to',
            field=core.fields.DateTimeField(blank=True, db_column='ValidityTo', null=True),
        ),
        migrations.AlterField(
            model_name='userrole',
            name='validity_from',
            field=core.fields.DateTimeField(db_column='ValidityFrom', default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='userrole',
            name='validity_to',
            field=core.fields.DateTimeField(blank=True, db_column='ValidityTo', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='usergroup',
            unique_together={('user', 'group')},
        ),
        migrations.AlterModelTable(
            name='usergroup',
            table='core_User_groups',
        ),
    ]
