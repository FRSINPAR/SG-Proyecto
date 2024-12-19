# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Documentos(models.Model):
    pundocumento = models.IntegerField(db_column='PunDocumento')  # Field name made lowercase.
    pungrupo = models.IntegerField(db_column='PunGrupo', blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    revision = models.IntegerField(db_column='Revision', blank=True, null=True)  # Field name made lowercase.
    vigencia = models.DateTimeField(db_column='Vigencia', blank=True, null=True)  # Field name made lowercase.
    linkpdf = models.CharField(db_column='LinkPDF', max_length=150, blank=True, null=True)  # Field name made lowercase.
    linkxls = models.CharField(db_column='LinkXLS', max_length=150, blank=True, null=True)  # Field name made lowercase.
    linkdoc = models.CharField(db_column='LinkDOC', max_length=150, blank=True, null=True)  # Field name made lowercase.
    linkplantilla = models.CharField(db_column='LinkPlantilla', max_length=150, blank=True, null=True)  # Field name made lowercase.
    borrado = models.IntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Documentos'


class Grupodocumento(models.Model):
    pungrupo = models.IntegerField(db_column='PunGrupo')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    borrado = models.IntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GrupoDocumento'


class Idpallets(models.Model):
    punmovimiento = models.IntegerField(db_column='PunMovimiento')  # Field name made lowercase.
    nropallet = models.IntegerField(db_column='NroPallet', blank=True, null=True)  # Field name made lowercase.
    nroop = models.IntegerField(db_column='NroOp', blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    vencimiento = models.CharField(db_column='Vencimiento', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ubicacion = models.IntegerField(db_column='Ubicacion', blank=True, null=True)  # Field name made lowercase.
    completo = models.CharField(db_column='Completo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    color = models.IntegerField(db_column='Color', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IdPallets'


class Kardexmovimientos(models.Model):
    punmovimiento = models.IntegerField(db_column='PunMovimiento')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    procesado = models.IntegerField(db_column='Procesado', blank=True, null=True)  # Field name made lowercase.
    fechaprocesado = models.DateTimeField(db_column='FechaProcesado', blank=True, null=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT', blank=True, null=True)  # Field name made lowercase.
    coincidepreseleccionado = models.IntegerField(db_column='CoincidePreseleccionado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KardexMovimientos'


class Palletscantidades(models.Model):
    punasignacion = models.IntegerField(db_column='PunAsignacion')  # Field name made lowercase.
    punmovimiento = models.IntegerField(db_column='PunMovimiento', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    tipo = models.IntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PalletsCantidades'


class Re(models.Model):
    pungrupo = models.IntegerField(db_column='PunGrupo', blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    revision = models.IntegerField(db_column='Revision', blank=True, null=True)  # Field name made lowercase.
    vigencia = models.DateTimeField(db_column='Vigencia', blank=True, null=True)  # Field name made lowercase.
    linkpdf = models.CharField(db_column='LinkPDF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    linkdoc = models.CharField(db_column='LinkDOC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    linkxls = models.CharField(db_column='LinkXLS', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RE$'


class Registrocombustible(models.Model):
    punregistro = models.IntegerField(db_column='PunRegistro')  # Field name made lowercase.
    dominio = models.CharField(db_column='Dominio', max_length=8, blank=True, null=True)  # Field name made lowercase.
    kilometros = models.IntegerField(db_column='Kilometros', blank=True, null=True)  # Field name made lowercase.
    nafta = models.IntegerField(db_column='Nafta', blank=True, null=True)  # Field name made lowercase.
    diesel = models.IntegerField(db_column='Diesel', blank=True, null=True)  # Field name made lowercase.
    gnc = models.IntegerField(db_column='GNC', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RegistroCombustible'


class Ubicacionespallets(models.Model):
    idubicacion = models.IntegerField(db_column='IdUbicacion')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UbicacionesPallets'
