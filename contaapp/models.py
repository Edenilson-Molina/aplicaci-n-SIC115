from django.db import models

# Create your models here.
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Clasificacion(models.Model):
    id_clas = models.IntegerField(db_column='ID_CLAS', primary_key=True)  # Field name made lowercase.       
    nomclas = models.CharField(db_column='NOMCLAS', max_length=250)  # Field name made lowercase.
    valor = models.FloatField(db_column='VALOR', blank=True, null=True)  # Field name made lowercase.        

    class Meta:
        managed = False
        db_table = 'clasificacion'


class Cuenta(models.Model):
    idcuenta = models.IntegerField(db_column='IDCUENTA', primary_key=True)  # Field name made lowercase.     
    idrubro = models.ForeignKey('Rubro', models.DO_NOTHING, db_column='IDRUBRO')  # Field name made lowercase.
    nomcuenta = models.CharField(db_column='NOMCUENTA', max_length=250)  # Field name made lowercase.        
    debecuenta = models.FloatField(db_column='DEBECUENTA', blank=True, null=True)  # Field name made lowercase.
    habercuenta = models.FloatField(db_column='HABERCUENTA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cuenta'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Rubro(models.Model):
    idrubro = models.IntegerField(db_column='IDRUBRO', primary_key=True)  # Field name made lowercase.       
    id_clas = models.ForeignKey(Clasificacion, models.DO_NOTHING, db_column='ID_CLAS')  # Field name made lowercase.
    nomrubro = models.CharField(db_column='NOMRUBRO', max_length=250)  # Field name made lowercase.
    valor_rubro = models.FloatField(db_column='VALOR_RUBRO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rubro'


class Subcuenta(models.Model):
    idsubcuenta = models.IntegerField(db_column='IDSUBCUENTA', primary_key=True)  # Field name made lowercase.
    idcuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='IDCUENTA')  # Field name made lowercase.
    nomsubcuenta = models.CharField(db_column='NOMSUBCUENTA', max_length=250)  # Field name made lowercase.  
    debe_subcuenta = models.FloatField(db_column='DEBE_SUBCUENTA', blank=True, null=True)  # Field name made lowercase.
    haber_subcuenta = models.FloatField(db_column='HABER_SUBCUENTA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subcuenta'