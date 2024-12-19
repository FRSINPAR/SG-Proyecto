from django.db import models
from django.db.backends.signals import connection_created
from django.dispatch import receiver
import random

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.BooleanField(default=True) #default=True como opcion si deseas que se setee siempre en este valor, sin necesidad de instanciar el objeto
    image = models.ImageField(upload_to='intel', verbose_name='Imagen')

    def __str__(self) -> str:
        return self.name
    class Meta:
         verbose_name = 'Producto'
         verbose_name_plural = 'Productos'
         

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self) -> str:
            return self.name
   
class Afipcodigo(models.Model):
    afipcodigo = models.IntegerField(db_column='AfipCodigo', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    puntipoiva = models.IntegerField(db_column='punTipoIVA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AFIPCodigo'


class Afipcodigosregimeniva(models.Model):
    codigo = models.IntegerField(db_column='Codigo', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AFIPCodigosRegimenIVA'


# class Afipmiscomprobantestmp(models.Model):
#     idoperacion = models.IntegerField(db_column='IDOperacion', blank=True, null=True)  # Field name made lowercase.
#     id = models.AutoField(primary_key=True, db_column='ID')  # Field name made lowercase.
#     marca = models.SmallIntegerField(db_column='Marca', blank=True, null=True)  # Field name made lowercase.
#     fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
#     fce = models.SmallIntegerField(db_column='FCE', blank=True, null=True)  # Field name made lowercase.
#     tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     tipoabc = models.CharField(db_column='TipoABC', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     prefijo = models.CharField(db_column='Prefijo', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     sufijo = models.CharField(db_column='Sufijo', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     gravado = models.DecimalField(db_column='Gravado', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     nogravado = models.DecimalField(db_column='NoGravado', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     exento = models.DecimalField(db_column='Exento', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     otrosimpuestos = models.DecimalField(db_column='OtrosImpuestos', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     iva = models.DecimalField(db_column='Iva', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     porcentajeiva = models.DecimalField(db_column='PorcentajeIva', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     cae = models.CharField(db_column='CAE', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     fechavtocae = models.DateTimeField(db_column='FechaVtoCae', blank=True, null=True)  # Field name made lowercase.
#     nrodocemisor = models.CharField(db_column='NroDocEmisor', max_length=14, blank=True, null=True)  # Field name made lowercase.
#     nombreemisor = models.CharField(db_column='NombreEmisor', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     erptipoproveedor = models.CharField(db_column='ERPTipoProveedor', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     erpproveedor = models.CharField(db_column='ERPProveedor', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     accion = models.CharField(db_column='Accion', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     validacion = models.CharField(db_column='Validacion', max_length=2000, blank=True, null=True)  # Field name made lowercase.
#     afiptipocomprobante = models.IntegerField(db_column='AfipTipoCOmprobante', blank=True, null=True)  # Field name made lowercase.
#     puntipocomprobante = models.IntegerField(db_column='PunTipoCOmprobante', blank=True, null=True)  # Field name made lowercase.
#     erppuntipoproveedor = models.SmallIntegerField(db_column='ERPPunTipoProveedor', blank=True, null=True)  # Field name made lowercase.
#     erppunproveedor = models.IntegerField(db_column='ERPPunProveedor', blank=True, null=True)  # Field name made lowercase.
#     tipodocemisor = models.SmallIntegerField(db_column='TipoDocEmisor', blank=True, null=True)  # Field name made lowercase.
#     cuentagastos = models.CharField(db_column='CuentaGastos', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     ccuentagastos = models.CharField(db_column='cCuentaGastos', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     cuentadistribuible = models.SmallIntegerField(db_column='CuentaDistribuible', blank=True, null=True)  # Field name made lowercase.
#     fechavencimiento = models.DateTimeField(db_column='FechaVencimiento', blank=True, null=True)  # Field name made lowercase.
#     punmoneda = models.IntegerField(db_column='PunMOneda', blank=True, null=True)  # Field name made lowercase.
#     moneda = models.CharField(db_column='MOneda', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     punaccion = models.IntegerField(db_column='PunAccion', blank=True, null=True)  # Field name made lowercase.
#     punvalidacion = models.IntegerField(db_column='PunValidacion', blank=True, null=True)  # Field name made lowercase.
#     punejercicio = models.IntegerField(db_column='PunEjercicio', blank=True, null=True)  # Field name made lowercase.
#     punplancuentas = models.IntegerField(db_column='PunPLanCuentas', blank=True, null=True)  # Field name made lowercase.
#     puntipoiva = models.IntegerField(db_column='PunTIpoiva', blank=True, null=True)  # Field name made lowercase.
#     puncai = models.IntegerField(db_column='PunCai', blank=True, null=True)  # Field name made lowercase.
#     puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
#     cargamanual = models.SmallIntegerField(db_column='CargaManual', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'AFIPMisComprobantesTMP'


class Afiptipocomprobante(models.Model):
    tipoabc = models.CharField(db_column='TipoABC', max_length=1, primary_key=True)  # Field name made lowercase.
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=2)  # Field name made lowercase.
    afiptipocomprobante = models.IntegerField(db_column='AFIPTipoComprobante', blank=True, null=True)  # Field name made lowercase.
    admitecai = models.SmallIntegerField(db_column='AdmiteCAI')  # Field name made lowercase.
    rg3685afiptipo = models.IntegerField(db_column='RG3685AFIPTipo', blank=True, null=True)  # Field name made lowercase.
    fce = models.BooleanField(db_column='FCE', blank=True, null=True)  # Field name made lowercase.
    afipdescripcion = models.CharField(db_column='AFIPDescripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    codigoarciba = models.SmallIntegerField(db_column='CodigoArciba', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AFIPTipoComprobante'


class Afiptipocomprobante2(models.Model):
    tipoabc = models.CharField(db_column='TipoABC', max_length=1)  # Field name made lowercase.
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=2)  # Field name made lowercase.
    afiptipocomprobante = models.IntegerField(db_column='AFIPTipoComprobante', blank=True, null=True)  # Field name made lowercase.
    admitecai = models.SmallIntegerField(db_column='AdmiteCAI')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AFIPTipoComprobante2'


class Afiptipodocumento(models.Model):
    afipcodigo = models.IntegerField(db_column='AfipCodigo')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    puntipodocumento = models.IntegerField(db_column='punTipoDocumento', blank=True, null=True)  # Field name made lowercase.
    punprovincia = models.IntegerField(db_column='PunProvincia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AFIPTipoDocumento'


class Accionafiladocausa(models.Model):
    puncausaaccion = models.AutoField(db_column='PunCausaAccion', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AccionAfiladoCausa'


class Actividadesfce(models.Model):
    punactividadfce = models.AutoField(db_column='PunActividadFCE', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ActividadesFCE'


class Actividadesganancias(models.Model):
    punganancias = models.IntegerField(db_column='PunGanancias')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    tabla = models.FloatField(db_column='Tabla', blank=True, null=True)  # Field name made lowercase.
    minimoaretenerconcuit = models.DecimalField(db_column='MinimoARetenerConCuit', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    minimoaretenersincuit = models.DecimalField(db_column='MinimoARetenerSinCuit', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ActividadesGanancias'


class Aduanas(models.Model):
    punaduana = models.AutoField(db_column='PunAduana', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Aduanas'


class Afipalicuotaiva(models.Model):
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AfipAlicuotaIVA'


class Afipmiscomprobantes(models.Model):
    punproceso = models.IntegerField(db_column='PunProceso', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    punorigen = models.SmallIntegerField(db_column='PunOrigen', blank=True, null=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    cargamanual = models.SmallIntegerField(db_column='CargaManual', blank=True, null=True)  # Field name made lowercase.
    archivo = models.CharField(db_column='Archivo', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AfipMisComprobantes'


class Archivoestructura(models.Model):
    punestructura = models.IntegerField(db_column='punEstructura')  # Field name made lowercase.
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    storedprocedure = models.CharField(db_column='storedProcedure', max_length=255, blank=True, null=True)  # Field name made lowercase.
    punmenu = models.IntegerField(db_column='PunMenu', blank=True, null=True)  # Field name made lowercase.
    pedirrangofechas = models.BooleanField(db_column='PedirRangoFechas', blank=True, null=True)  # Field name made lowercase.
    punestructurarelacionada = models.IntegerField(db_column='PunEstructuraRelacionada', blank=True, null=True)  # Field name made lowercase.
    orden = models.SmallIntegerField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.
    reporte = models.CharField(db_column='Reporte', max_length=80, blank=True, null=True)  # Field name made lowercase.
    nombrearchivo = models.CharField(db_column='NombreArchivo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    archivounico = models.BooleanField(db_column='ArchivoUnico', blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    pedirempresa = models.BooleanField(db_column='PedirEmpresa', blank=True, null=True)  # Field name made lowercase.
    cantdecimales = models.IntegerField(db_column='CantDecimales', blank=True, null=True)  # Field name made lowercase.
    separadordecimales = models.CharField(db_column='SeparadorDecimales', max_length=1, blank=True, null=True)  # Field name made lowercase.
    punestructurarelacionadaxitem = models.IntegerField(db_column='punEstructuraRelacionadaXItem', blank=True, null=True)  # Field name made lowercase.
    separador = models.CharField(db_column='Separador', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mostrarfilaencabezado = models.SmallIntegerField(db_column='MostrarFilaEncabezado', blank=True, null=True)  # Field name made lowercase.
    filablancaalfinal = models.SmallIntegerField(db_column='FilaBlancaAlFinal', blank=True, null=True)  # Field name made lowercase.
    pedirdatosadicionales = models.BooleanField(db_column='PedirDatosAdicionales', blank=True, null=True)  # Field name made lowercase.
    cadenaseparadorareg = models.CharField(db_column='CadenaSeparadoraReg', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ubicacionseparadorreg = models.CharField(db_column='UbicacionSeparadorReg', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ArchivoEstructura'


class Archivoestructuraitem(models.Model):
    punestructura = models.IntegerField(db_column='punEstructura')  # Field name made lowercase.
    punitem = models.AutoField(db_column='punItem', primary_key=True)  # Field name made lowercase.
    orden = models.IntegerField()
    desde = models.IntegerField(db_column='Desde')  # Field name made lowercase.
    hasta = models.IntegerField(db_column='Hasta')  # Field name made lowercase.
    longitud = models.IntegerField(db_column='Longitud')  # Field name made lowercase.
    tipovalor = models.IntegerField(db_column='TipoValor')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    detalle = models.CharField(db_column='Detalle', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    campostoredprocedure = models.CharField(db_column='CampoStoredProcedure', max_length=100, blank=True, null=True)  # Field name made lowercase.
    completarconceros = models.SmallIntegerField(db_column='CompletarConCeros', blank=True, null=True)  # Field name made lowercase.
    nocompletar = models.SmallIntegerField(db_column='NoCompletar', blank=True, null=True)  # Field name made lowercase.
    blancosinohayvalor = models.BooleanField(db_column='BlancoSiNoHayValor', blank=True, null=True)  # Field name made lowercase.
    cantdecimales = models.IntegerField(db_column='CantDecimales', blank=True, null=True)  # Field name made lowercase.
    separadordecimales = models.CharField(db_column='SeparadorDecimales', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ArchivoEstructuraItem'


class Artnew(models.Model):
    punarticulo = models.FloatField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ubicacionfisica = models.CharField(db_column='UbicacionFisica', max_length=255, blank=True, null=True)  # Field name made lowercase.
    descripcionant = models.CharField(db_column='DescripcionAnt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ubicacionfisicaant = models.CharField(db_column='UbicacionFisicaAnt', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ArtNew'


class ArtEnfab(models.Model):
    punarticulo = models.AutoField(db_column='PunArticulo', primary_key=True)  # Field name made lowercase.
    punrubro = models.IntegerField(db_column='PunRubro')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=8)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150)  # Field name made lowercase.
    punlineaproduccion = models.IntegerField(db_column='PunLineaProduccion')  # Field name made lowercase.
    punfamilia = models.IntegerField(db_column='PunFamilia')  # Field name made lowercase.
    pungrupo = models.IntegerField(db_column='PunGrupo')  # Field name made lowercase.
    origen = models.SmallIntegerField(db_column='Origen')  # Field name made lowercase.
    tipo = models.SmallIntegerField(db_column='Tipo')  # Field name made lowercase.
    cuentacompra = models.CharField(db_column='CuentaCompra', max_length=9)  # Field name made lowercase.
    cuentaventa = models.CharField(db_column='CuentaVenta', max_length=9)  # Field name made lowercase.
    pununidad = models.IntegerField(db_column='PunUnidad')  # Field name made lowercase.
    stockminimo = models.DecimalField(db_column='StockMinimo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    stockcritico = models.DecimalField(db_column='StockCritico', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    stockmaximo = models.DecimalField(db_column='StockMaximo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    alicuotaiva = models.IntegerField(db_column='AlicuotaIVA')  # Field name made lowercase.
    codigobarras = models.CharField(db_column='CodigoBarras', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ubicacionfisica = models.CharField(db_column='UbicacionFisica', max_length=10, blank=True, null=True)  # Field name made lowercase.
    codigoalternativo = models.CharField(db_column='CodigoAlternativo', max_length=8, blank=True, null=True)  # Field name made lowercase.
    critico = models.SmallIntegerField(db_column='Critico', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=255, blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    enfabricacion = models.DecimalField(db_column='EnFabricacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    consumopromedio = models.DecimalField(db_column='ConsumoPromedio', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tiemporeposicion = models.DecimalField(db_column='TiempoReposicion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Art_EnFab'


class Articulompse(models.Model):
    punmpse = models.AutoField(db_column='PunMPSE', primary_key=True)  # Field name made lowercase.
    punarticulo = models.ForeignKey('Articulos', models.DO_NOTHING, db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    punrubro = models.ForeignKey('Rubrosarticulos', models.DO_NOTHING, db_column='PunRubro', blank=True, null=True)  # Field name made lowercase.
    punarticuloasignado = models.ForeignKey('Articulos', models.DO_NOTHING, db_column='punArticuloAsignado', related_name='articulompse_punarticuloasignado_set', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ArticuloMPSE'


class Articulompsetmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    punmpse = models.IntegerField(db_column='PunMPSE', blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    punrubro = models.IntegerField(db_column='PunRubro', blank=True, null=True)  # Field name made lowercase.
    punarticuloasignado = models.IntegerField(db_column='punArticuloAsignado', blank=True, null=True)  # Field name made lowercase.
    modoabm = models.SmallIntegerField(db_column='ModoABM')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ArticuloMPSEtmp'


class Articulos(models.Model):
    punarticulo = models.AutoField(db_column='PunArticulo', primary_key=True)  # Field name made lowercase.
    punrubro = models.IntegerField(db_column='PunRubro')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    punlineaproduccion = models.IntegerField(db_column='PunLineaProduccion')  # Field name made lowercase.
    punfamilia = models.IntegerField(db_column='PunFamilia')  # Field name made lowercase.
    pungrupo = models.IntegerField(db_column='PunGrupo')  # Field name made lowercase.
    origen = models.SmallIntegerField(db_column='Origen')  # Field name made lowercase.
    tipo = models.SmallIntegerField(db_column='Tipo')  # Field name made lowercase.
    cuentacompra = models.CharField(db_column='CuentaCompra', max_length=9, blank=True, null=True)  # Field name made lowercase.
    cuentaventa = models.CharField(db_column='CuentaVenta', max_length=9, blank=True, null=True)  # Field name made lowercase.
    pununidad = models.IntegerField(db_column='PunUnidad')  # Field name made lowercase.
    stockminimo = models.DecimalField(db_column='StockMinimo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    stockcritico = models.DecimalField(db_column='StockCritico', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    stockmaximo = models.DecimalField(db_column='StockMaximo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    alicuotaiva = models.IntegerField(db_column='AlicuotaIVA')  # Field name made lowercase.
    codigobarras = models.CharField(db_column='CodigoBarras', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ubicacionfisica = models.CharField(db_column='UbicacionFisica', max_length=100, blank=True, null=True)  # Field name made lowercase.
    codigoalternativo = models.CharField(db_column='CodigoAlternativo', max_length=16, blank=True, null=True)  # Field name made lowercase.
    critico = models.SmallIntegerField(db_column='Critico', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=255, blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    enfabricacion = models.DecimalField(db_column='EnFabricacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    consumopromedio = models.DecimalField(db_column='ConsumoPromedio', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tiemporeposicion = models.DecimalField(db_column='TiempoReposicion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    caractadicionales = models.CharField(db_column='CaractAdicionales', max_length=255, blank=True, null=True)  # Field name made lowercase.
    generastock = models.BooleanField(db_column='GeneraStock')  # Field name made lowercase.
    peso = models.DecimalField(db_column='Peso', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pununidadalternativa = models.IntegerField(db_column='PunUnidadAlternativa', blank=True, null=True)  # Field name made lowercase.
    coeficiente = models.DecimalField(db_column='Coeficiente', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    puntipoot = models.IntegerField(db_column='PunTipoOT', blank=True, null=True)  # Field name made lowercase.
    punplanosinparvigente = models.ForeignKey('Planosinpar', models.DO_NOTHING, db_column='PunPlanoSinParVigente', blank=True, null=True)  # Field name made lowercase.
    posicionarancelaria = models.CharField(db_column='PosicionArancelaria', max_length=50, blank=True, null=True)  # Field name made lowercase.
    puntipompse = models.ForeignKey('Hctipompse', models.DO_NOTHING, db_column='PunTipoMPSE', blank=True, null=True)  # Field name made lowercase.
    unidadesporenvase = models.IntegerField(db_column='UnidadesPorEnvase', blank=True, null=True)  # Field name made lowercase.
    unidadreferenciafe = models.CharField(db_column='UnidadReferenciaFE', max_length=6, blank=True, null=True)  # Field name made lowercase.
    codigofe = models.CharField(db_column='CodigoFE', max_length=14, blank=True, null=True)  # Field name made lowercase.
    pununidadmedidafe = models.IntegerField(db_column='PunUnidadMedidaFE', blank=True, null=True)  # Field name made lowercase.
    codigobonofiscal = models.CharField(db_column='CodigoBonoFiscal', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cotcodigo = models.CharField(db_column='COTCodigo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cotcodigounidad = models.SmallIntegerField(db_column='COTCodigoUnidad', blank=True, null=True)  # Field name made lowercase.
    cotobligatorio = models.BooleanField(db_column='COTObligatorio', blank=True, null=True)  # Field name made lowercase.
    punsubclasificacion = models.IntegerField(db_column='PunSubClasificacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Articulos'


class Articulosn(models.Model):
    punarticulo = models.AutoField(db_column='PunArticulo', primary_key=True)  # Field name made lowercase.
    punrubro = models.IntegerField(db_column='PunRubro')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=12, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150)  # Field name made lowercase.
    punlineaproduccion = models.IntegerField(db_column='PunLineaProduccion')  # Field name made lowercase.
    punfamilia = models.IntegerField(db_column='PunFamilia')  # Field name made lowercase.
    pungrupo = models.IntegerField(db_column='PunGrupo')  # Field name made lowercase.
    origen = models.SmallIntegerField(db_column='Origen')  # Field name made lowercase.
    tipo = models.SmallIntegerField(db_column='Tipo')  # Field name made lowercase.
    cuentacompra = models.CharField(db_column='CuentaCompra', max_length=9, blank=True, null=True)  # Field name made lowercase.
    cuentaventa = models.CharField(db_column='CuentaVenta', max_length=9, blank=True, null=True)  # Field name made lowercase.
    pununidad = models.IntegerField(db_column='PunUnidad')  # Field name made lowercase.
    stockminimo = models.DecimalField(db_column='StockMinimo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    stockcritico = models.DecimalField(db_column='StockCritico', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    stockmaximo = models.DecimalField(db_column='StockMaximo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    alicuotaiva = models.IntegerField(db_column='AlicuotaIVA')  # Field name made lowercase.
    codigobarras = models.CharField(db_column='CodigoBarras', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ubicacionfisica = models.CharField(db_column='UbicacionFisica', max_length=10, blank=True, null=True)  # Field name made lowercase.
    codigoalternativo = models.CharField(db_column='CodigoAlternativo', max_length=8, blank=True, null=True)  # Field name made lowercase.
    critico = models.SmallIntegerField(db_column='Critico', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=255, blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    enfabricacion = models.DecimalField(db_column='EnFabricacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    consumopromedio = models.DecimalField(db_column='ConsumoPromedio', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tiemporeposicion = models.DecimalField(db_column='TiempoReposicion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    caractadicionales = models.CharField(db_column='CaractAdicionales', max_length=255, blank=True, null=True)  # Field name made lowercase.
    generastock = models.BooleanField(db_column='GeneraStock')  # Field name made lowercase.
    peso = models.DecimalField(db_column='Peso', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pununidadalternativa = models.IntegerField(db_column='PunUnidadAlternativa', blank=True, null=True)  # Field name made lowercase.
    coeficiente = models.DecimalField(db_column='Coeficiente', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    puntipoot = models.IntegerField(db_column='PunTipoOT', blank=True, null=True)  # Field name made lowercase.
    punplanosinparvigente = models.IntegerField(db_column='PunPlanoSinParVigente', blank=True, null=True)  # Field name made lowercase.
    puntipompse = models.IntegerField(db_column='PunTipoMPSE')  # Field name made lowercase.
    posicionarancelaria = models.CharField(db_column='PosicionArancelaria', max_length=13, blank=True, null=True)  # Field name made lowercase.
    punteroorig = models.IntegerField(db_column='PunteroOrig', blank=True, null=True)  # Field name made lowercase.
    insumo = models.BooleanField(db_column='Insumo', blank=True, null=True)  # Field name made lowercase.
    bys = models.BooleanField(db_column='ByS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ArticulosN'


class ArticulosX(models.Model):
    punarticulo = models.AutoField(db_column='PunArticulo', primary_key=True)  # Field name made lowercase.
    punrubro = models.IntegerField(db_column='PunRubro')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150)  # Field name made lowercase.
    punlineaproduccion = models.IntegerField(db_column='PunLineaProduccion')  # Field name made lowercase.
    punfamilia = models.IntegerField(db_column='PunFamilia')  # Field name made lowercase.
    pungrupo = models.IntegerField(db_column='PunGrupo')  # Field name made lowercase.
    origen = models.SmallIntegerField(db_column='Origen')  # Field name made lowercase.
    tipo = models.SmallIntegerField(db_column='Tipo')  # Field name made lowercase.
    cuentacompra = models.CharField(db_column='CuentaCompra', max_length=9, blank=True, null=True)  # Field name made lowercase.
    cuentaventa = models.CharField(db_column='CuentaVenta', max_length=9, blank=True, null=True)  # Field name made lowercase.
    pununidad = models.IntegerField(db_column='PunUnidad')  # Field name made lowercase.
    stockminimo = models.DecimalField(db_column='StockMinimo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    stockcritico = models.DecimalField(db_column='StockCritico', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    stockmaximo = models.DecimalField(db_column='StockMaximo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    alicuotaiva = models.IntegerField(db_column='AlicuotaIVA')  # Field name made lowercase.
    codigobarras = models.CharField(db_column='CodigoBarras', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ubicacionfisica = models.CharField(db_column='UbicacionFisica', max_length=10, blank=True, null=True)  # Field name made lowercase.
    codigoalternativo = models.CharField(db_column='CodigoAlternativo', max_length=16, blank=True, null=True)  # Field name made lowercase.
    critico = models.SmallIntegerField(db_column='Critico', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=255, blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    enfabricacion = models.DecimalField(db_column='EnFabricacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    consumopromedio = models.DecimalField(db_column='ConsumoPromedio', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tiemporeposicion = models.DecimalField(db_column='TiempoReposicion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    caractadicionales = models.CharField(db_column='CaractAdicionales', max_length=255, blank=True, null=True)  # Field name made lowercase.
    generastock = models.BooleanField(db_column='GeneraStock')  # Field name made lowercase.
    peso = models.DecimalField(db_column='Peso', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pununidadalternativa = models.IntegerField(db_column='PunUnidadAlternativa', blank=True, null=True)  # Field name made lowercase.
    coeficiente = models.DecimalField(db_column='Coeficiente', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    puntipoot = models.IntegerField(db_column='PunTipoOT', blank=True, null=True)  # Field name made lowercase.
    punplanosinparvigente = models.IntegerField(db_column='PunPlanoSinParVigente', blank=True, null=True)  # Field name made lowercase.
    posicionarancelaria = models.CharField(db_column='PosicionArancelaria', max_length=50, blank=True, null=True)  # Field name made lowercase.
    puntipompse = models.IntegerField(db_column='PunTipoMPSE', blank=True, null=True)  # Field name made lowercase.
    unidadesporenvase = models.IntegerField(db_column='UnidadesPorEnvase', blank=True, null=True)  # Field name made lowercase.
    unidadreferenciafe = models.CharField(db_column='UnidadReferenciaFE', max_length=6, blank=True, null=True)  # Field name made lowercase.
    codigofe = models.CharField(db_column='CodigoFE', max_length=14, blank=True, null=True)  # Field name made lowercase.
    pununidadmedidafe = models.IntegerField(db_column='PunUnidadMedidaFE', blank=True, null=True)  # Field name made lowercase.
    codigobonofiscal = models.CharField(db_column='CodigoBonoFiscal', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cotcodigo = models.CharField(db_column='COTCodigo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cotcodigounidad = models.SmallIntegerField(db_column='COTCodigoUnidad', blank=True, null=True)  # Field name made lowercase.
    cotobligatorio = models.BooleanField(db_column='COTObligatorio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Articulos_X'


class ArticulosControlGrupos(models.Model):
    punarticulo = models.IntegerField(db_column='PunArticulo', primary_key=True)  # Field name made lowercase.
    punrubro = models.IntegerField(db_column='PunRubro')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=8)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150)  # Field name made lowercase.
    punlineaproduccion = models.IntegerField(db_column='PunLineaProduccion')  # Field name made lowercase.
    punfamilia = models.IntegerField(db_column='PunFamilia')  # Field name made lowercase.
    pungrupo = models.IntegerField(db_column='PunGrupo')  # Field name made lowercase.
    origen = models.SmallIntegerField(db_column='Origen')  # Field name made lowercase.
    tipo = models.SmallIntegerField(db_column='Tipo')  # Field name made lowercase.
    cuentacompra = models.CharField(db_column='CuentaCompra', max_length=9)  # Field name made lowercase.
    cuentaventa = models.CharField(db_column='CuentaVenta', max_length=9)  # Field name made lowercase.
    pununidad = models.IntegerField(db_column='PunUnidad')  # Field name made lowercase.
    stockminimo = models.DecimalField(db_column='StockMinimo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    stockcritico = models.DecimalField(db_column='StockCritico', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    stockmaximo = models.DecimalField(db_column='StockMaximo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    alicuotaiva = models.IntegerField(db_column='AlicuotaIVA')  # Field name made lowercase.
    codigobarras = models.CharField(db_column='CodigoBarras', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ubicacionfisica = models.CharField(db_column='UbicacionFisica', max_length=10, blank=True, null=True)  # Field name made lowercase.
    codigoalternativo = models.CharField(db_column='CodigoAlternativo', max_length=8, blank=True, null=True)  # Field name made lowercase.
    critico = models.SmallIntegerField(db_column='Critico', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=255, blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    enfabricacion = models.DecimalField(db_column='EnFabricacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    consumopromedio = models.DecimalField(db_column='ConsumoPromedio', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Articulos_control_grupos'


class Asientoajustetmp(models.Model):
    cuenta = models.CharField(db_column='Cuenta', max_length=9, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=300, blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    orden = models.SmallIntegerField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='IDOperacion', blank=True, null=True)  # Field name made lowercase.
    punejercicio = models.IntegerField(db_column='PunEjercicio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AsientoAjusteTMP'


class Auximpresioncomprobantes(models.Model):
    idoperacion = models.IntegerField(db_column='IdOperacion', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    comprobante = models.CharField(db_column='Comprobante', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cliente = models.CharField(db_column='Cliente', max_length=150, blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ot = models.CharField(db_column='OT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    tipomph = models.IntegerField(db_column='TipoMPH', blank=True, null=True)  # Field name made lowercase.
    fechaingreso = models.DateTimeField(db_column='FechaIngreso', blank=True, null=True)  # Field name made lowercase.
    importesiniva = models.DecimalField(db_column='ImporteSinIVA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AuxImpresionComprobantes'


class Auxiliarconsultas(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id')  # Field name made lowercase.
    intref = models.IntegerField(db_column='IntRef', blank=True, null=True)  # Field name made lowercase.
    charref = models.CharField(db_column='CharRef', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tag = models.CharField(db_column='Tag', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AuxiliarConsultas'


class Avisodestinatario(models.Model):
    pundestinatario = models.AutoField(db_column='PunDestinatario', primary_key=True)  # Field name made lowercase.
    puntipoaviso = models.ForeignKey('Tipoaviso', models.DO_NOTHING, db_column='PunTipoAviso')  # Field name made lowercase.
    punusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='PunUsuario', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avisoporpantalla = models.BooleanField(db_column='AvisoPorPantalla')  # Field name made lowercase.
    avisoporemail = models.BooleanField(db_column='AvisoPorEMail')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AvisoDestinatario'


class Avisodestinatariotmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    pundestinatario = models.IntegerField(db_column='PunDestinatario', blank=True, null=True)  # Field name made lowercase.
    puntipoaviso = models.IntegerField(db_column='PunTipoAviso', blank=True, null=True)  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='PunUsuario', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    avisoporpantalla = models.BooleanField(db_column='AvisoPorPantalla')  # Field name made lowercase.
    avisoporemail = models.BooleanField(db_column='AvisoPorEMail')  # Field name made lowercase.
    modoabm = models.SmallIntegerField(db_column='ModoABM')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AvisoDestinatarioTMP'


class Avisoreposicion(models.Model):
    punaviso = models.AutoField(db_column='PunAviso', primary_key=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    punpedido = models.IntegerField(db_column='PunPedido')  # Field name made lowercase.
    cuentas = models.CharField(db_column='Cuentas', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AvisoReposicion'


class Avisoreposiciondetalle(models.Model):
    punavisodetalle = models.AutoField(db_column='PunAvisoDetalle', primary_key=True)  # Field name made lowercase.
    punaviso = models.IntegerField(db_column='PunAviso')  # Field name made lowercase.
    punitempedido = models.IntegerField(db_column='PunItemPedido')  # Field name made lowercase.
    cantidadareponer = models.DecimalField(db_column='CantidadAReponer', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AvisoReposicionDetalle'


class Avisoreposiciondetalletmp(models.Model):
    punavisodetalle = models.IntegerField(db_column='PunAvisoDetalle', blank=True, null=True)  # Field name made lowercase.
    punaviso = models.IntegerField(db_column='PunAviso', blank=True, null=True)  # Field name made lowercase.
    punitempedido = models.IntegerField(db_column='PunItemPedido')  # Field name made lowercase.
    cantidadareponer = models.DecimalField(db_column='CantidadAReponer', max_digits=19, decimal_places=4)  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='IDOperacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AvisoReposicionDetalleTMP'


class Bcobancos(models.Model):
    punbanco = models.AutoField(db_column='PunBanco', primary_key=True)  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    nrocuenta = models.CharField(db_column='NroCuenta', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda', blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    puntipoiva = models.IntegerField(db_column='PunTipoIVA', blank=True, null=True)  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='PunProveedor')  # Field name made lowercase.
    punbcotipocuenta = models.IntegerField(db_column='PunBCOTipoCuenta', blank=True, null=True)  # Field name made lowercase.
    nroextracto = models.IntegerField(db_column='NroExtracto', blank=True, null=True)  # Field name made lowercase.
    cbu = models.CharField(db_column='CBU', max_length=22, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BCOBancos'


class Bcochequeras(models.Model):
    punchequera = models.AutoField(db_column='PunChequera', primary_key=True)  # Field name made lowercase.
    punbanco = models.IntegerField(db_column='PunBanco')  # Field name made lowercase.
    habilitada = models.SmallIntegerField(db_column='Habilitada', blank=True, null=True)  # Field name made lowercase.
    diferida = models.SmallIntegerField(db_column='Diferida', blank=True, null=True)  # Field name made lowercase.
    nroprimercheque = models.IntegerField(db_column='NroPrimerCheque', blank=True, null=True)  # Field name made lowercase.
    nroultimocheque = models.IntegerField(db_column='NroUltimoCheque', blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    nrochequera = models.IntegerField(db_column='NroChequera')  # Field name made lowercase.
    fechaalta = models.DateTimeField(db_column='FechaAlta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BCOChequeras'


class Bcochequerastmp(models.Model):
    punchequera = models.IntegerField(db_column='PunChequera')  # Field name made lowercase.
    punbanco = models.IntegerField(db_column='PunBanco')  # Field name made lowercase.
    habilitada = models.SmallIntegerField(db_column='Habilitada', blank=True, null=True)  # Field name made lowercase.
    diferida = models.SmallIntegerField(db_column='Diferida', blank=True, null=True)  # Field name made lowercase.
    nroprimercheque = models.IntegerField(db_column='NroPrimerCheque', blank=True, null=True)  # Field name made lowercase.
    nroultimocheque = models.IntegerField(db_column='NroUltimoCheque', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BCOChequerasTMP'


class Bcocheques(models.Model):
    punchequera = models.IntegerField(db_column='PunChequera')  # Field name made lowercase.
    nrocheque = models.IntegerField(db_column='NroCheque')  # Field name made lowercase.
    fechacheque = models.DateTimeField(db_column='FechaCheque')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    punorigen = models.IntegerField(db_column='PunOrigen', blank=True, null=True)  # Field name made lowercase.
    fechaemision = models.DateTimeField(db_column='FechaEmision')  # Field name made lowercase.
    efectivizado = models.SmallIntegerField(db_column='Efectivizado', blank=True, null=True)  # Field name made lowercase.
    noalaorden = models.SmallIntegerField(db_column='NoALaOrden')  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado')  # Field name made lowercase.
    punasientoefectivizacion = models.IntegerField(db_column='PunAsientoEfectivizacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BCOCheques'


class Bcochequestmp(models.Model):
    idoperacion = models.IntegerField(db_column='IdOperacion')  # Field name made lowercase.
    punchequera = models.IntegerField(db_column='PunChequera')  # Field name made lowercase.
    nrocheque = models.IntegerField(db_column='NroCheque')  # Field name made lowercase.
    fechacheque = models.DateTimeField(db_column='FechaCheque')  # Field name made lowercase.
    fechaemision = models.DateTimeField(db_column='FechaEmision')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    noalaorden = models.SmallIntegerField(db_column='NoALaOrden')  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    punbanco = models.IntegerField(db_column='PunBanco', blank=True, null=True)  # Field name made lowercase.
    punasientoefectivizacion = models.IntegerField(db_column='PunAsientoEfectivizacion', blank=True, null=True)  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa', blank=True, null=True)  # Field name made lowercase.
    idoperacion2 = models.IntegerField(db_column='IDOperacion2', blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BCOChequesTMP'


class Bcodeposito(models.Model):
    pundeposito = models.AutoField(db_column='PunDeposito', primary_key=True)  # Field name made lowercase.
    sufijo = models.CharField(db_column='Sufijo', max_length=8, blank=True, null=True)  # Field name made lowercase.
    punbanco = models.IntegerField(db_column='PunBanco')  # Field name made lowercase.
    nrocomprobante = models.CharField(db_column='NroComprobante', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    puncaja = models.IntegerField(db_column='PunCaja', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BCODeposito'


class Bcoextractodetalle(models.Model):
    punmovimiento = models.AutoField(db_column='PunMovimiento', primary_key=True)  # Field name made lowercase.
    punextracto = models.IntegerField(db_column='PunExtracto')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    punconcepto = models.IntegerField(db_column='PunConcepto')  # Field name made lowercase.
    nrocomprobante = models.CharField(db_column='NroComprobante', max_length=20)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    conciliado = models.SmallIntegerField(db_column='Conciliado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BCOExtractoDetalle'


class Bcoextractodetalletmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    punmovimiento = models.IntegerField(db_column='PunMovimiento')  # Field name made lowercase.
    punextracto = models.IntegerField(db_column='PunExtracto')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    punconcepto = models.IntegerField(db_column='PunConcepto')  # Field name made lowercase.
    nrocomprobante = models.CharField(db_column='NroComprobante', max_length=20)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    conciliado = models.SmallIntegerField(db_column='Conciliado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BCOExtractoDetalleTMP'


class Bcoextractos(models.Model):
    punextracto = models.AutoField(db_column='PunExtracto', primary_key=True)  # Field name made lowercase.
    nroextracto = models.IntegerField(db_column='NroExtracto', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    hojadesde = models.IntegerField(db_column='HojaDesde', blank=True, null=True)  # Field name made lowercase.
    hojahasta = models.IntegerField(db_column='HojaHasta', blank=True, null=True)  # Field name made lowercase.
    punbanco = models.IntegerField(db_column='PunBanco')  # Field name made lowercase.
    saldoinicial = models.DecimalField(db_column='SaldoInicial', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    saldofinal = models.DecimalField(db_column='SaldoFinal', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BCOExtractos'


class Bcomovanulartmp(models.Model):
    idoperacion = models.IntegerField(db_column='IdOperacion')  # Field name made lowercase.
    puntipomovimiento = models.IntegerField(db_column='PunTipoMovimiento', blank=True, null=True)  # Field name made lowercase.
    punmovimientobanco = models.IntegerField(db_column='PunMovimientoBanco', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BCOMovAnularTMP'


class Bcomovimientos(models.Model):
    punmovimientobanco = models.AutoField(db_column='PunMovimientoBanco', primary_key=True)  # Field name made lowercase.
    punbanco = models.IntegerField(db_column='PunBanco')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    puntipomovimiento = models.IntegerField(db_column='PunTipoMovimiento')  # Field name made lowercase.
    nrocomprobantebanco = models.CharField(db_column='NroComprobanteBanco', max_length=20, blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punasiento = models.IntegerField(db_column='PunAsiento')  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    punorigen = models.IntegerField(db_column='PunOrigen', blank=True, null=True)  # Field name made lowercase.
    impuesto = models.SmallIntegerField(db_column='Impuesto', blank=True, null=True)  # Field name made lowercase.
    punextracto = models.IntegerField(db_column='PunExtracto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BCOMovimientos'


class Bcomovimientostmp(models.Model):
    punbanco = models.IntegerField(db_column='PunBanco')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    puntipomovimiento = models.IntegerField(db_column='PunTipoMovimiento')  # Field name made lowercase.
    nrocomprobantebanco = models.CharField(db_column='NroComprobanteBanco', max_length=20, blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punasiento = models.IntegerField(db_column='PunAsiento', blank=True, null=True)  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    punorigen = models.IntegerField(db_column='PunOrigen', blank=True, null=True)  # Field name made lowercase.
    movimientotran = models.IntegerField(db_column='MovimientoTran')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa', blank=True, null=True)  # Field name made lowercase.
    idoperacion2 = models.IntegerField(db_column='IDOperacion2', blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BCOMovimientosTMP'


class Bcotipocuenta(models.Model):
    punbcotipocuenta = models.AutoField(db_column='PunBCOTipoCuenta', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    etiqueta = models.CharField(db_column='Etiqueta', max_length=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BCOTipoCuenta'


class Bcotipomovimiento(models.Model):
    puntipomovimiento = models.AutoField(db_column='PunTipoMovimiento', primary_key=True)  # Field name made lowercase.
    etiqueta = models.CharField(db_column='Etiqueta', max_length=4)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BCOTipoMovimiento'


class Bal(models.Model):
    idoperacion = models.IntegerField(db_column='IdOperacion', blank=True, null=True)  # Field name made lowercase.
    cuenta = models.CharField(db_column='Cuenta', max_length=9, blank=True, null=True)  # Field name made lowercase.
    cuentasumariza = models.CharField(db_column='CuentaSumariza', max_length=9, blank=True, null=True)  # Field name made lowercase.
    debe = models.DecimalField(db_column='Debe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    haber = models.DecimalField(db_column='Haber', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    proceso = models.SmallIntegerField(db_column='Proceso', blank=True, null=True)  # Field name made lowercase.
    orden = models.IntegerField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bal'


class Bancosemisores(models.Model):
    punbancoemisor = models.AutoField(db_column='PunBancoEmisor', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BancosEmisores'


class Bienesamortizacionrev(models.Model):
    punamortizacionrev = models.AutoField(db_column='PunAmortizacionRev', primary_key=True)  # Field name made lowercase.
    punbiendeuso = models.IntegerField(db_column='PunBienDeUso')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    punasiento = models.IntegerField(db_column='PunAsiento')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    tipo = models.SmallIntegerField(db_column='Tipo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BienesAmortizacionRev'


class Bienesdeuso(models.Model):
    punbiendeuso = models.AutoField(db_column='PunBienDeUso', primary_key=True)  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    puntipobien = models.IntegerField(db_column='PunTipoBien')  # Field name made lowercase.
    fechacompra = models.DateTimeField(db_column='FechaCompra')  # Field name made lowercase.
    valororigen = models.DecimalField(db_column='ValorOrigen', max_digits=19, decimal_places=4)  # Field name made lowercase.
    periodoamortizacion = models.IntegerField(db_column='PeriodoAmortizacion')  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BienesDeUso'


class Bienesyservicios(models.Model):
    punbys = models.AutoField(db_column='PunByS', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200)  # Field name made lowercase.
    punrubro = models.IntegerField(db_column='PunRubro')  # Field name made lowercase.
    pununidadcompra = models.IntegerField(db_column='PunUnidadCompra')  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=8)  # Field name made lowercase.
    cuentacompra = models.CharField(db_column='CuentaCompra', max_length=9)  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BienesYServicios'


class Cajaimportes(models.Model):
    puncaja = models.IntegerField(db_column='PunCaja')  # Field name made lowercase.
    puntipopago = models.IntegerField(db_column='PunTipoPago')  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    importeapertura = models.DecimalField(db_column='ImporteApertura', max_digits=19, decimal_places=4)  # Field name made lowercase.
    importecierre = models.DecimalField(db_column='ImporteCierre', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importediferencia = models.DecimalField(db_column='ImporteDiferencia', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CAJAImportes'


class Cajaimportestmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    puntipopago = models.IntegerField(db_column='PunTipoPago')  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    importeapertura = models.DecimalField(db_column='ImporteApertura', max_digits=19, decimal_places=4)  # Field name made lowercase.
    importecierre = models.DecimalField(db_column='ImporteCierre', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importediferencia = models.DecimalField(db_column='ImporteDiferencia', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    puncaja = models.IntegerField(db_column='PunCaja', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CAJAImportesTMP'


class Cajamovimientos(models.Model):
    puncaja = models.IntegerField(db_column='PunCaja')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    puntipopago = models.IntegerField(db_column='PunTipoPago')  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punorigen = models.IntegerField(db_column='PunOrigen', blank=True, null=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    puncheque = models.IntegerField(db_column='PunCheque', blank=True, null=True)  # Field name made lowercase.
    punasiento = models.IntegerField(db_column='PunAsiento', blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nromovimiento = models.CharField(db_column='NroMovimiento', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CAJAMovimientos'


class CjCalipsoEstad(models.Model):
    fecha = models.DateTimeField(db_column='FECHA', blank=True, null=True)  # Field name made lowercase.
    zona = models.CharField(db_column='ZONA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cliente = models.CharField(db_column='CLIENTE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    grupo = models.CharField(db_column='GRUPO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rubro = models.CharField(db_column='RUBRO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    talle = models.CharField(db_column='TALLE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    detalle = models.CharField(db_column='DETALLE', max_length=35, blank=True, null=True)  # Field name made lowercase.
    cod_art = models.CharField(db_column='COD_ART', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vendedor = models.CharField(db_column='VENDEDOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    xyear = models.FloatField(db_column='XYEAR', blank=True, null=True)  # Field name made lowercase.
    xmonth = models.CharField(db_column='XMONTH', max_length=12, blank=True, null=True)  # Field name made lowercase.
    sucursal = models.CharField(db_column='SUCURSAL', max_length=4, blank=True, null=True)  # Field name made lowercase.
    mes = models.CharField(db_column='MES', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ano_mes = models.CharField(db_column='ANO_MES', max_length=20, blank=True, null=True)  # Field name made lowercase.
    xday = models.CharField(db_column='XDAY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    imported = models.FloatField(db_column='IMPORTED', blank=True, null=True)  # Field name made lowercase.
    importex = models.FloatField(db_column='IMPORTEX', blank=True, null=True)  # Field name made lowercase.
    costo = models.FloatField(db_column='COSTO', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.FloatField(db_column='CANTIDAD', blank=True, null=True)  # Field name made lowercase.
    importe = models.FloatField(db_column='IMPORTE', blank=True, null=True)  # Field name made lowercase.
    benefic = models.FloatField(db_column='BENEFIC', blank=True, null=True)  # Field name made lowercase.
    trimestr = models.CharField(db_column='TRIMESTR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    semana = models.CharField(db_column='SEMANA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    provin = models.CharField(db_column='PROVIN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='REGION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dia = models.CharField(db_column='DIA', max_length=14, blank=True, null=True)  # Field name made lowercase.
    canal = models.CharField(db_column='CANAL', max_length=15, blank=True, null=True)  # Field name made lowercase.
    empresa = models.CharField(db_column='EMPRESA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    cod_cli = models.CharField(db_column='COD_CLI', max_length=6, blank=True, null=True)  # Field name made lowercase.
    proveedor = models.CharField(db_column='PROVEEDOR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    conversion = models.FloatField(db_column='CONVERSION', blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CJ_calipso_estad'


class Clibonificaciones(models.Model):
    puncliente = models.IntegerField(db_column='PunCliente')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    punrubro = models.IntegerField(db_column='PunRubro', blank=True, null=True)  # Field name made lowercase.
    orden = models.SmallIntegerField(db_column='Orden')  # Field name made lowercase.
    descuento = models.DecimalField(db_column='Descuento', max_digits=19, decimal_places=4)  # Field name made lowercase.
    pungrupo = models.IntegerField(db_column='punGrupo', blank=True, null=True)  # Field name made lowercase.
    punfamilia = models.IntegerField(db_column='punFamilia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIBonificaciones'


class Clibonificacionestmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    punrubro = models.IntegerField(db_column='PunRubro', blank=True, null=True)  # Field name made lowercase.
    orden = models.SmallIntegerField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.
    descuento = models.DecimalField(db_column='Descuento', max_digits=19, decimal_places=4)  # Field name made lowercase.
    pungrupo = models.IntegerField(db_column='punGrupo', blank=True, null=True)  # Field name made lowercase.
    punfamilia = models.IntegerField(db_column='punFamilia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIBonificacionesTMP'


class Cliclasificacion(models.Model):
    punclasificacion = models.AutoField(db_column='PunClasificacion', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIClasificacion'


class Cliclientes(models.Model):
    puncliente = models.AutoField(db_column='PunCliente', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=150)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    entrecalles = models.CharField(db_column='EntreCalles', max_length=150, blank=True, null=True)  # Field name made lowercase.
    telefonos = models.CharField(db_column='Telefonos', max_length=150, blank=True, null=True)  # Field name made lowercase.
    codigopostal = models.CharField(db_column='CodigoPostal', max_length=20, blank=True, null=True)  # Field name made lowercase.
    punpais = models.SmallIntegerField(db_column='PunPais', blank=True, null=True)  # Field name made lowercase.
    punprovincia = models.SmallIntegerField(db_column='PunProvincia', blank=True, null=True)  # Field name made lowercase.
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punzona = models.IntegerField(db_column='PunZona', blank=True, null=True)  # Field name made lowercase.
    punsubzona = models.IntegerField(db_column='PunSubZona', blank=True, null=True)  # Field name made lowercase.
    tiporecorrido = models.CharField(db_column='TipoRecorrido', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lugarentrega = models.CharField(db_column='LugarEntrega', max_length=150, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=500, blank=True, null=True)  # Field name made lowercase.
    punactividad = models.SmallIntegerField(db_column='PunActividad', blank=True, null=True)  # Field name made lowercase.
    fechaalta = models.DateTimeField(db_column='FechaAlta', blank=True, null=True)  # Field name made lowercase.
    puntipoiva = models.IntegerField(db_column='PunTipoIVA', blank=True, null=True)  # Field name made lowercase.
    puntipodocumento = models.IntegerField(db_column='PunTipoDocumento', blank=True, null=True)  # Field name made lowercase.
    cuit = models.CharField(db_column='Cuit', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nrodocumento = models.IntegerField(db_column='NroDocumento', blank=True, null=True)  # Field name made lowercase.
    punjurisdiccionib = models.SmallIntegerField(db_column='PunJurisdiccionIB', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    punclasificacion = models.IntegerField(db_column='PunClasificacion', blank=True, null=True)  # Field name made lowercase.
    delexterior = models.SmallIntegerField(db_column='DelExterior', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    credito = models.DecimalField(db_column='Credito', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punlistaprecio = models.IntegerField(db_column='PunListaPrecio', blank=True, null=True)  # Field name made lowercase.
    percepcioniva = models.SmallIntegerField(db_column='PercepcionIva', blank=True, null=True)  # Field name made lowercase.
    tipocliente = models.SmallIntegerField(db_column='TipoCliente')  # Field name made lowercase.
    punrecorrido = models.IntegerField(db_column='PunRecorrido', blank=True, null=True)  # Field name made lowercase.
    punmonedafactura = models.IntegerField(db_column='PunMonedaFactura', blank=True, null=True)  # Field name made lowercase.
    puncondicionventa = models.IntegerField(db_column='PunCondicionVenta', blank=True, null=True)  # Field name made lowercase.
    percepcionib = models.SmallIntegerField(db_column='PercepcionIB', blank=True, null=True)  # Field name made lowercase.
    distribuidor = models.SmallIntegerField(db_column='Distribuidor', blank=True, null=True)  # Field name made lowercase.
    punleyenda = models.IntegerField(blank=True, null=True)
    zonafranca = models.SmallIntegerField(db_column='ZonaFranca', blank=True, null=True)  # Field name made lowercase.
    preciounitario = models.SmallIntegerField(db_column='PrecioUnitario', blank=True, null=True)  # Field name made lowercase.
    subtotal = models.SmallIntegerField(db_column='SubTotal', blank=True, null=True)  # Field name made lowercase.
    netomercaderia = models.SmallIntegerField(db_column='NetoMercaderia', blank=True, null=True)  # Field name made lowercase.
    leyendatipocambio = models.SmallIntegerField(db_column='LeyendaTipoCambio', blank=True, null=True)  # Field name made lowercase.
    leyendatipocambio2 = models.SmallIntegerField(db_column='LeyendaTipoCambio2', blank=True, null=True)  # Field name made lowercase.
    nombrefantasia = models.CharField(db_column='NombreFantasia', max_length=150, blank=True, null=True)  # Field name made lowercase.
    web = models.CharField(db_column='Web', max_length=150, blank=True, null=True)  # Field name made lowercase.
    servicioafilado = models.SmallIntegerField(db_column='ServicioAfilado', blank=True, null=True)  # Field name made lowercase.
    emailfactura = models.CharField(db_column='EMailFactura', max_length=500, blank=True, null=True)  # Field name made lowercase.
    idimpositivo = models.CharField(db_column='IDImpositivo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    punlocalidad = models.IntegerField(db_column='PunLocalidad', blank=True, null=True)  # Field name made lowercase.
    nroingbrutos = models.CharField(db_column='NroIngBrutos', max_length=20, blank=True, null=True)  # Field name made lowercase.
    punsituacioniibb = models.SmallIntegerField(db_column='PunSituacionIIBB', blank=True, null=True)  # Field name made lowercase.
    exencioniibb = models.BooleanField(db_column='ExencionIIBB', blank=True, null=True)  # Field name made lowercase.
    exencioniibbdesde = models.DateTimeField(db_column='ExencionIIBBDesde', blank=True, null=True)  # Field name made lowercase.
    exencioniibbhasta = models.DateTimeField(db_column='ExencionIIBBHasta', blank=True, null=True)  # Field name made lowercase.
    puntipoclientefce = models.SmallIntegerField(db_column='PunTipoClienteFCE', blank=True, null=True)  # Field name made lowercase.
    punactividadfce = models.IntegerField(db_column='PunActividadFCE', blank=True, null=True)  # Field name made lowercase.
    importeminimofce = models.DecimalField(db_column='ImporteMinimoFCE', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fechaultimaconsultafce = models.DateTimeField(db_column='FechaUltimaConsultaFCE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIClientes'


class Clicompacobrartmp(models.Model):
    idoperacion = models.IntegerField(db_column='IdOperacion')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    retencioniva = models.DecimalField(db_column='RetencionIVA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importefa = models.DecimalField(db_column='ImporteFA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    condebito = models.SmallIntegerField(db_column='ConDebito', blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='punMoneda', blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cotizacioncobro = models.DecimalField(db_column='CotizacionCobro', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importecobro = models.DecimalField(db_column='ImporteCobro', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importedescuento = models.DecimalField(db_column='ImporteDescuento', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    numerocertificado = models.CharField(db_column='NumeroCertificado', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLICompACobrarTMP'


class Clicompreferenciastmp(models.Model):
    idoperacion = models.IntegerField(db_column='IdOperacion')  # Field name made lowercase.
    punreferencia = models.IntegerField(db_column='PunReferencia')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=18, decimal_places=2)  # Field name made lowercase.
    condicionventa = models.IntegerField(db_column='CondicionVenta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLICompReferenciasTMP'


class Clicomprobanteavisodeuda(models.Model):
    puncomprobanteaviso = models.AutoField(db_column='punComprobanteAviso', primary_key=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    fechavto = models.DateTimeField(db_column='FechaVto', blank=True, null=True)  # Field name made lowercase.
    punavisodeuda = models.SmallIntegerField(db_column='PunAvisoDeuda', blank=True, null=True)  # Field name made lowercase.
    fechaaviso = models.DateTimeField(db_column='FechaAviso', blank=True, null=True)  # Field name made lowercase.
    diasvencidos = models.SmallIntegerField(db_column='DiasVencidos', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIComprobanteAvisoDeuda'


class Clicomprobantediaspago(models.Model):
    punreferencia = models.IntegerField(db_column='PunReferencia', blank=True, null=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dias = models.IntegerField(db_column='Dias', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIComprobanteDiasPago'


class Clicomprobanteexportacion(models.Model):
    puncomprobanteexportacion = models.AutoField(db_column='PunComprobanteExportacion', primary_key=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    punidioma = models.SmallIntegerField(db_column='PunIdioma')  # Field name made lowercase.
    punincoterm = models.SmallIntegerField(db_column='PunIncoterm')  # Field name made lowercase.
    poseepermisoaduanero = models.BooleanField(db_column='PoseePermisoAduanero')  # Field name made lowercase.
    punpaisdestino = models.IntegerField(db_column='PunPaisDestino')  # Field name made lowercase.
    puntipoexportacion = models.SmallIntegerField(db_column='PunTipoExportacion')  # Field name made lowercase.
    exportasimple = models.BooleanField(db_column='ExportaSimple', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIComprobanteExportacion'


class Clicomprobanteimportes(models.Model):
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    punreferencia = models.IntegerField(db_column='PunReferencia')  # Field name made lowercase.
    puntipoimporte = models.IntegerField(db_column='PunTipoImporte')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    punjurisdiccionib = models.IntegerField(db_column='PunJurisdiccionIB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIComprobanteImportes'


class Clicomprobanteopcionales(models.Model):
    puncomprobanteopcional = models.AutoField(db_column='PunComprobanteOpcional', primary_key=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    id = models.CharField(db_column='Id', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=1024)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIComprobanteOpcionales'


class Clicomprobanteperiodo(models.Model):
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    fechadesde = models.DateTimeField(db_column='FechaDesde', blank=True, null=True)  # Field name made lowercase.
    fechahasta = models.DateTimeField(db_column='FechaHasta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIComprobantePeriodo'


class Clicomprobantevencimientos(models.Model):
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    punreferencia = models.IntegerField(db_column='PunReferencia')  # Field name made lowercase.
    fechavto = models.DateTimeField(db_column='FechaVto')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIComprobanteVencimientos'


class Clicomprobantevencimientostmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    punreferencia = models.IntegerField(db_column='PunReferencia', blank=True, null=True)  # Field name made lowercase.
    fechavto = models.DateTimeField(db_column='FechaVto')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    modoabm = models.IntegerField(db_column='ModoABM')  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    punsubcliente = models.IntegerField(db_column='PunSubcliente', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIComprobanteVencimientosTMP'


class Clicomprobantes(models.Model):
    puncomprobante = models.AutoField(db_column='PunComprobante', primary_key=True)  # Field name made lowercase.
    tipoabc = models.CharField(db_column='TipoABC', max_length=1)  # Field name made lowercase.
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=2)  # Field name made lowercase.
    prefijo = models.CharField(db_column='Prefijo', max_length=4)  # Field name made lowercase.
    sufijo = models.CharField(db_column='Sufijo', max_length=8)  # Field name made lowercase.
    punasiento = models.IntegerField(db_column='PunAsiento')  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    tiponcnd = models.SmallIntegerField(db_column='TipoNCND', blank=True, null=True)  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    punsubcliente = models.IntegerField(db_column='PunSubcliente', blank=True, null=True)  # Field name made lowercase.
    nrorecibo = models.CharField(db_column='NroRecibo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    punagrupado = models.IntegerField(db_column='PunAgrupado', blank=True, null=True)  # Field name made lowercase.
    fechaingreso = models.DateTimeField(db_column='FechaIngreso', blank=True, null=True)  # Field name made lowercase.
    fechaanulacion = models.DateTimeField(db_column='FechaAnulacion', blank=True, null=True)  # Field name made lowercase.
    condebito = models.SmallIntegerField(db_column='ConDebito', blank=True, null=True)  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='PunUsuario', blank=True, null=True)  # Field name made lowercase.
    punvendedor = models.IntegerField(db_column='PunVendedor', blank=True, null=True)  # Field name made lowercase.
    afiptipocomprobante = models.IntegerField(db_column='AFIPTipoComprobante', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIComprobantes'


class Clicomprobantesleyendas(models.Model):
    punleyenda = models.AutoField(db_column='PunLeyenda', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    leyenda = models.CharField(db_column='Leyenda', max_length=500)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIComprobantesLeyendas'


class Clicomprobantestmp(models.Model):
    tipoabc = models.CharField(db_column='TipoABC', max_length=1)  # Field name made lowercase.
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=2)  # Field name made lowercase.
    prefijo = models.CharField(db_column='Prefijo', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sufijo = models.CharField(db_column='Sufijo', max_length=8, blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='IdOperacion')  # Field name made lowercase.
    punasiento = models.IntegerField(db_column='PunAsiento', blank=True, null=True)  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    punsubcliente = models.IntegerField(db_column='PunSubcliente', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    condicionventa = models.SmallIntegerField(db_column='CondicionVenta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIComprobantesTMP'


class Clicuentacorriente(models.Model):
    puncliente = models.IntegerField(db_column='PunCliente')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    punreferencia = models.IntegerField(db_column='PunReferencia')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punmoneda = models.SmallIntegerField(db_column='PunMoneda')  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4)  # Field name made lowercase.
    condicionventa = models.SmallIntegerField(db_column='CondicionVenta', blank=True, null=True)  # Field name made lowercase.
    punsubcliente = models.IntegerField(db_column='PunSubCliente', blank=True, null=True)  # Field name made lowercase.
    observacioncc = models.CharField(db_column='ObservacionCC', max_length=2000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLICuentaCorriente'


class Clidescuentoimportes(models.Model):
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    punreferencia = models.IntegerField(db_column='PunReferencia')  # Field name made lowercase.
    puntipoimporte = models.IntegerField(db_column='PunTipoImporte')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    puncomprobantenc = models.IntegerField(db_column='PunComprobanteNC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIDescuentoImportes'


class Clidescuentos(models.Model):
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    puntipoimporte = models.IntegerField(db_column='PunTipoImporte')  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIDescuentos'


class Clidevolucionitem(models.Model):
    pundevolucionitem = models.AutoField(db_column='PunDevolucionItem', primary_key=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4)  # Field name made lowercase.
    preciooriginal = models.DecimalField(db_column='PrecioOriginal', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcentajeiva = models.DecimalField(db_column='PorcentajeIVA', max_digits=19, decimal_places=4)  # Field name made lowercase.
    orden = models.SmallIntegerField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.
    bonificacion = models.DecimalField(db_column='Bonificacion', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIDevolucionItem'


class Clidiferenciacambioimportes(models.Model):
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    punreferencia = models.IntegerField(db_column='PunReferencia')  # Field name made lowercase.
    puntipoimporte = models.IntegerField(db_column='PunTipoImporte')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    puncomprobantencnd = models.IntegerField(db_column='PunComprobanteNCND', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIDiferenciaCambioImportes'


class Clidistribuidorvendedores(models.Model):
    pundistribuidor = models.IntegerField(db_column='PunDistribuidor')  # Field name made lowercase.
    punvendedor = models.IntegerField(db_column='PunVendedor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIDistribuidorVendedores'
        unique_together = (('pundistribuidor', 'punvendedor'),)


class Clidistribuidores(models.Model):
    pundistribuidor = models.AutoField(db_column='PunDistribuidor', primary_key=True)  # Field name made lowercase.
    razonsocial = models.CharField(db_column='RazonSocial', max_length=100)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    te = models.CharField(db_column='TE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punprovincia = models.IntegerField(db_column='PunProvincia', blank=True, null=True)  # Field name made lowercase.
    cuit = models.CharField(db_column='CUIT', max_length=15, blank=True, null=True)  # Field name made lowercase.
    puntipoiva = models.IntegerField(db_column='PunTipoIva', blank=True, null=True)  # Field name made lowercase.
    localidad = models.CharField(db_column='Localidad', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cp = models.CharField(db_column='CP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    pundepositocentral = models.IntegerField(db_column='PunDepositoCentral', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIDistribuidores'


class Cliexpresos(models.Model):
    puncliente = models.IntegerField(db_column='PunCliente')  # Field name made lowercase.
    punexpreso = models.IntegerField(db_column='PunExpreso')  # Field name made lowercase.
    predeterminado = models.SmallIntegerField(db_column='Predeterminado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIExpresos'


class Cliexpresostmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    punexpreso = models.IntegerField(db_column='PunExpreso', blank=True, null=True)  # Field name made lowercase.
    predeterminado = models.SmallIntegerField(db_column='Predeterminado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIExpresosTMP'


class Clijurisdiccionescm(models.Model):
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    punjurisdiccionib = models.IntegerField(db_column='PunJurisdiccionIB', blank=True, null=True)  # Field name made lowercase.
    exencion = models.BooleanField(db_column='Exencion', blank=True, null=True)  # Field name made lowercase.
    fechadesde = models.DateTimeField(db_column='FechaDesde', blank=True, null=True)  # Field name made lowercase.
    fechahasta = models.DateTimeField(db_column='FechaHasta', blank=True, null=True)  # Field name made lowercase.
    punconcepto = models.IntegerField(db_column='PunCOncepto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIJurisdiccionesCM'


class Clipagos(models.Model):
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=2)  # Field name made lowercase.
    puntipopago = models.IntegerField(db_column='PunTipoPago')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punbanco = models.IntegerField(db_column='PunBanco', blank=True, null=True)  # Field name made lowercase.
    nrocheque = models.IntegerField(db_column='NroCheque', blank=True, null=True)  # Field name made lowercase.
    puncomprobanteorigen = models.IntegerField(db_column='PunComprobanteOrigen', blank=True, null=True)  # Field name made lowercase.
    nroretganancias = models.CharField(db_column='NroRetGanancias', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pundeposito = models.IntegerField(db_column='PunDeposito', blank=True, null=True)  # Field name made lowercase.
    punagrupado = models.IntegerField(db_column='PunAgrupado', blank=True, null=True)  # Field name made lowercase.
    puntiporetencion = models.SmallIntegerField(db_column='PunTipoRetencion', blank=True, null=True)  # Field name made lowercase.
    numerocertificado = models.CharField(db_column='NumeroCertificado', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIPagos'


class Clipagosib(models.Model):
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    punjurisdiccionib = models.IntegerField(db_column='PunJurisdiccionIB')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    nroretencion = models.CharField(db_column='NroRetencion', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIPagosIB'


class Clipedidobonificaciones(models.Model):
    punpedido = models.IntegerField(db_column='PunPedido')  # Field name made lowercase.
    punitempedido = models.IntegerField(db_column='PunItemPedido', blank=True, null=True)  # Field name made lowercase.
    orden = models.SmallIntegerField(db_column='Orden')  # Field name made lowercase.
    descuento = models.DecimalField(db_column='Descuento', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIPedidoBonificaciones'


class Clipedidobonificacionestmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    punpedido = models.IntegerField(db_column='PunPedido', blank=True, null=True)  # Field name made lowercase.
    punitempedido = models.IntegerField(db_column='PunItemPedido', blank=True, null=True)  # Field name made lowercase.
    orden = models.SmallIntegerField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.
    descuento = models.DecimalField(db_column='Descuento', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIPedidoBonificacionesTMP'


class Clipedidodocumentacion(models.Model):
    punarchivo = models.AutoField(db_column='PunArchivo', primary_key=True)  # Field name made lowercase.
    punpedido = models.IntegerField(db_column='PunPedido')  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='PunUsuario')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    version = models.IntegerField(db_column='Version')  # Field name made lowercase.
    pathdestino = models.CharField(db_column='PathDestino', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nombrearchivo = models.CharField(db_column='NombreArchivo', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIPedidoDocumentacion'


class Clipedidodocumentaciontmp(models.Model):
    idoperacion = models.IntegerField(db_column='idOperacion')  # Field name made lowercase.
    punarchivo = models.IntegerField(db_column='PunArchivo', blank=True, null=True)  # Field name made lowercase.
    punpedido = models.IntegerField(db_column='PunPedido')  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='PunUsuario')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    version = models.IntegerField(db_column='Version')  # Field name made lowercase.
    pathdestino = models.CharField(db_column='PathDestino', max_length=500, blank=True, null=True)  # Field name made lowercase.
    nombrearchivo = models.CharField(db_column='NombreArchivo', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIPedidoDocumentacionTMP'


class Clipedidoitem(models.Model):
    punitempedido = models.AutoField(db_column='PunItemPedido', primary_key=True)  # Field name made lowercase.
    punpedido = models.IntegerField(db_column='PunPedido')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.
    cantidadpedida = models.DecimalField(db_column='CantidadPedida', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cantidadenviada = models.DecimalField(db_column='CantidadEnviada', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcentajeiva = models.DecimalField(db_column='PorcentajeIVA', max_digits=19, decimal_places=4)  # Field name made lowercase.
    preciooriginal = models.DecimalField(db_column='PrecioOriginal', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cantidadaenviar = models.DecimalField(db_column='CantidadAEnviar', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    orden = models.SmallIntegerField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.
    bonificacion = models.DecimalField(db_column='Bonificacion', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fechaentrega = models.DateTimeField(db_column='FechaEntrega', blank=True, null=True)  # Field name made lowercase.
    seguimientovto = models.SmallIntegerField(db_column='SeguimientoVto')  # Field name made lowercase.
    fechaentregaoriginal = models.DateTimeField(db_column='FechaEntregaOriginal', blank=True, null=True)  # Field name made lowercase.
    msgoftecnica = models.CharField(db_column='MsgOfTecnica', max_length=255, blank=True, null=True)  # Field name made lowercase.
    msgadeposito = models.CharField(db_column='MsgADeposito', max_length=255, blank=True, null=True)  # Field name made lowercase.
    msginterno = models.CharField(db_column='MsgInterno', max_length=255, blank=True, null=True)  # Field name made lowercase.
    punplanocliente = models.IntegerField(db_column='PunPlanoCliente', blank=True, null=True)  # Field name made lowercase.
    nroplanonuevo = models.CharField(db_column='NroPlanoNuevo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nrorevisionnuevo = models.CharField(db_column='NroRevisionNuevo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fecharevisionnuevo = models.DateTimeField(db_column='FechaRevisionNuevo', blank=True, null=True)  # Field name made lowercase.
    punplanoaccion = models.ForeignKey('Hcplanoaccion', models.DO_NOTHING, db_column='PunPlanoAccion', blank=True, null=True)  # Field name made lowercase.
    preciominimo = models.DecimalField(db_column='PrecioMinimo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punmonedapreciominimo = models.IntegerField(db_column='PunMonedaPrecioMinimo', blank=True, null=True)  # Field name made lowercase.
    bloqueado = models.BooleanField(db_column='Bloqueado', blank=True, null=True)  # Field name made lowercase.
    nroot = models.CharField(db_column='NroOT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    archivoplanonuevo = models.CharField(db_column='ArchivoPlanoNuevo', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    preciolista = models.DecimalField(db_column='PrecioLista', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    monedapreciolista = models.IntegerField(db_column='MonedaPrecioLista', blank=True, null=True)  # Field name made lowercase.
    stockdeposito1 = models.DecimalField(db_column='StockDeposito1', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    estadomodifitem = models.SmallIntegerField(db_column='EstadoModifItem', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIPedidoItem'


class Clipedidoitemreserva(models.Model):
    net_address = models.CharField(db_column='Net_Address', max_length=12)  # Field name made lowercase.
    login_time = models.DateTimeField(db_column='Login_Time')  # Field name made lowercase.
    punitempedido = models.IntegerField(db_column='PunItemPedido')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.
    pundeposito = models.IntegerField(db_column='PunDeposito')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='PunUsuario', blank=True, null=True)  # Field name made lowercase.
    lock_time = models.DateTimeField(db_column='Lock_Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIPedidoItemReserva'


class Clipedidoitemtmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    punitempedido = models.IntegerField(db_column='PunItemPedido', blank=True, null=True)  # Field name made lowercase.
    punpedido = models.IntegerField(db_column='PunPedido', blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    cantidadpedida = models.DecimalField(db_column='CantidadPedida', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidadenviada = models.DecimalField(db_column='CantidadEnviada', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda', blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porcentajeiva = models.DecimalField(db_column='PorcentajeIVA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    preciooriginal = models.DecimalField(db_column='PrecioOriginal', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nroremito = models.IntegerField(db_column='NroRemito', blank=True, null=True)  # Field name made lowercase.
    cantidadaenviar = models.DecimalField(db_column='CantidadAEnviar', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    idoperacion2 = models.IntegerField(db_column='IDOperacion2', blank=True, null=True)  # Field name made lowercase.
    modoabm = models.SmallIntegerField(db_column='ModoABM', blank=True, null=True)  # Field name made lowercase.
    orden = models.SmallIntegerField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.
    seguimientovto = models.SmallIntegerField(db_column='SeguimientoVto', blank=True, null=True)  # Field name made lowercase.
    fechaentrega = models.DateTimeField(db_column='FechaEntrega', blank=True, null=True)  # Field name made lowercase.
    punmotivocambiofecha = models.IntegerField(db_column='punMotivoCambioFecha', blank=True, null=True)  # Field name made lowercase.
    msgoftecnica = models.CharField(db_column='MsgOfTecnica', max_length=255, blank=True, null=True)  # Field name made lowercase.
    msgadeposito = models.CharField(db_column='MsgADeposito', max_length=255, blank=True, null=True)  # Field name made lowercase.
    msginterno = models.CharField(db_column='MsgInterno', max_length=255, blank=True, null=True)  # Field name made lowercase.
    punplanocliente = models.IntegerField(db_column='punPlanoCliente', blank=True, null=True)  # Field name made lowercase.
    nroplanonuevo = models.CharField(db_column='NroPlanoNuevo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nrorevisionnuevo = models.CharField(db_column='NroRevisionNuevo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fecharevisionnuevo = models.DateTimeField(db_column='FechaRevisionNuevo', blank=True, null=True)  # Field name made lowercase.
    punplanoaccion = models.IntegerField(db_column='punPlanoAccion', blank=True, null=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='punOrdenT', blank=True, null=True)  # Field name made lowercase.
    preciominimo = models.DecimalField(db_column='PrecioMinimo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punmonedapreciominimo = models.IntegerField(db_column='punMonedaPrecioMinimo', blank=True, null=True)  # Field name made lowercase.
    bloqueado = models.BooleanField(db_column='Bloqueado', blank=True, null=True)  # Field name made lowercase.
    autorizacionrevisada = models.BooleanField(db_column='AutorizacionRevisada', blank=True, null=True)  # Field name made lowercase.
    nroot = models.CharField(db_column='NroOT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    archivocentralplano = models.CharField(db_column='ArchivoCentralPlano', max_length=350, blank=True, null=True)  # Field name made lowercase.
    archivoplanonuevo = models.CharField(db_column='ArchivoPlanoNuevo', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    preciolista = models.DecimalField(db_column='PrecioLista', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    monedapreciolista = models.IntegerField(db_column='MonedaPrecioLista', blank=True, null=True)  # Field name made lowercase.
    stockdeposito1 = models.DecimalField(db_column='StockDeposito1', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    estadomodifitem = models.SmallIntegerField(db_column='EstadoModifItem', blank=True, null=True)  # Field name made lowercase.
    itemprecioconsolidado = models.DecimalField(db_column='ItemPrecioCOnsolidado', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    preciominimoconsolidado = models.DecimalField(db_column='PrecioMinimoConsolidado', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIPedidoItemTMP'


class Clipedidovariaciondatos(models.Model):
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='PunUsuario', blank=True, null=True)  # Field name made lowercase.
    punpedido = models.IntegerField(db_column='PunPedido', blank=True, null=True)  # Field name made lowercase.
    punitempedido = models.IntegerField(db_column='PunItemPedido', blank=True, null=True)  # Field name made lowercase.
    puncampo = models.IntegerField(db_column='PunCampo', blank=True, null=True)  # Field name made lowercase.
    campo = models.CharField(db_column='Campo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    valoranterior = models.TextField(db_column='ValorAnterior', blank=True, null=True)  # Field name made lowercase.
    valorposterior = models.TextField(db_column='ValorPosterior', blank=True, null=True)  # Field name made lowercase.
    punvariacion = models.AutoField(db_column='PunVariacion', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIPedidoVariacionDatos'


class Clipedidos(models.Model):
    punpedido = models.IntegerField(db_column='PunPedido', unique=True)  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    fechaestimadaentrega = models.DateTimeField(db_column='FechaEstimadaEntrega')  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    tiporecorrido = models.CharField(db_column='TipoRecorrido', max_length=1)  # Field name made lowercase.
    punvendedor = models.IntegerField(db_column='PunVendedor')  # Field name made lowercase.
    seguimientovto = models.SmallIntegerField(db_column='SeguimientoVto')  # Field name made lowercase.
    referencia = models.CharField(db_column='Referencia', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    punrecorrido = models.IntegerField(db_column='PunRecorrido', blank=True, null=True)  # Field name made lowercase.
    punmonedafactura = models.IntegerField(db_column='PunMonedaFactura', blank=True, null=True)  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='PunUsuario', blank=True, null=True)  # Field name made lowercase.
    puncondicionventa = models.IntegerField(db_column='PunCondicionVenta', blank=True, null=True)  # Field name made lowercase.
    bonificacion = models.DecimalField(db_column='Bonificacion', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punpedidorecupero = models.IntegerField(db_column='PunPedidoRecupero', blank=True, null=True)  # Field name made lowercase.
    msginterno = models.CharField(db_column='MsgInterno', max_length=255, blank=True, null=True)  # Field name made lowercase.
    altapedido = models.DateTimeField(db_column='AltaPedido', blank=True, null=True)  # Field name made lowercase.
    puntipomensaje = models.IntegerField(db_column='PunTipoMensaje', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIPedidos'
        unique_together = (('puncliente', 'punpedido'),)


class Clipedidosaux(models.Model):
    punpedidoaux = models.AutoField(db_column='PunPedidoAux', primary_key=True)  # Field name made lowercase.
    punpedido = models.IntegerField(db_column='PunPedido')  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    fechaestimadaentrega = models.DateTimeField(db_column='FechaEstimadaEntrega')  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tiporecorrido = models.CharField(db_column='TipoRecorrido', max_length=1)  # Field name made lowercase.
    punvendedor = models.IntegerField(db_column='PunVendedor')  # Field name made lowercase.
    seguimientovto = models.SmallIntegerField(db_column='SeguimientoVto')  # Field name made lowercase.
    referencia = models.CharField(db_column='Referencia', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punrecorrido = models.IntegerField(db_column='PunRecorrido', blank=True, null=True)  # Field name made lowercase.
    punmonedafactura = models.IntegerField(db_column='PunMonedaFactura', blank=True, null=True)  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='PunUsuario', blank=True, null=True)  # Field name made lowercase.
    puncondicionventa = models.IntegerField(db_column='PunCondicionVenta', blank=True, null=True)  # Field name made lowercase.
    bonificacion = models.DecimalField(db_column='Bonificacion', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIPedidosAux'


class Clipedidosbloqueados(models.Model):
    punpedido = models.IntegerField(db_column='PunPedido', blank=True, null=True)  # Field name made lowercase.
    login_time = models.DateTimeField(db_column='Login_Time')  # Field name made lowercase.
    net_address = models.CharField(db_column='Net_Address', max_length=12)  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='PunUsuario')  # Field name made lowercase.
    lock_time = models.DateTimeField(db_column='Lock_Time')  # Field name made lowercase.
    modulo = models.SmallIntegerField(db_column='Modulo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIPedidosBloqueados'


class Clipedidostmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    punpedido = models.IntegerField(db_column='PunPedido')  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    fechaestimadaentrega = models.DateTimeField(db_column='FechaEstimadaEntrega')  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    tiporecorrido = models.CharField(db_column='TipoRecorrido', max_length=1)  # Field name made lowercase.
    punvendedor = models.IntegerField(db_column='PunVendedor')  # Field name made lowercase.
    seguimientovto = models.SmallIntegerField(db_column='SeguimientoVto')  # Field name made lowercase.
    referencia = models.CharField(db_column='Referencia', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    punrecorrido = models.IntegerField(db_column='PunRecorrido', blank=True, null=True)  # Field name made lowercase.
    punmonedafactura = models.IntegerField(db_column='PunMonedaFactura', blank=True, null=True)  # Field name made lowercase.
    puncondicionventa = models.IntegerField(db_column='PunCondicionVenta', blank=True, null=True)  # Field name made lowercase.
    bonificacion = models.DecimalField(db_column='Bonificacion', max_digits=19, decimal_places=4)  # Field name made lowercase.
    msginterno = models.CharField(db_column='MsgInterno', max_length=255, blank=True, null=True)  # Field name made lowercase.
    altapedido = models.DateTimeField(db_column='AltaPedido', blank=True, null=True)  # Field name made lowercase.
    puntipomensaje = models.IntegerField(db_column='PunTipoMensaje', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIPedidosTMP'


class Cliremitocot(models.Model):
    puntero = models.AutoField(db_column='Puntero', primary_key=True)  # Field name made lowercase.
    punremito = models.IntegerField(db_column='PunRemito', blank=True, null=True)  # Field name made lowercase.
    codigocot = models.CharField(db_column='CodigoCOT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    punhojarutacot = models.IntegerField(db_column='PunHojaRutaCOT', blank=True, null=True)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIRemitoCOT'


class Cliremitopedidoitem(models.Model):
    punremitoitem = models.AutoField(db_column='PunRemitoItem', primary_key=True)  # Field name made lowercase.
    punremito = models.IntegerField(db_column='PunRemito')  # Field name made lowercase.
    punpedido = models.IntegerField(db_column='PunPedido')  # Field name made lowercase.
    punitempedido = models.IntegerField(db_column='PunItemPedido')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    referencia = models.CharField(db_column='Referencia', max_length=100, blank=True, null=True)  # Field name made lowercase.
    valorfob = models.DecimalField(db_column='ValorFOB', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punmonedafob = models.IntegerField(db_column='PunMonedaFOB', blank=True, null=True)  # Field name made lowercase.
    nroitem = models.IntegerField(db_column='NroItem', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIRemitoPedidoItem'


class Cliremitopedidoitemtmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    punremitoitem = models.IntegerField(db_column='PunRemitoItem', blank=True, null=True)  # Field name made lowercase.
    punremito = models.IntegerField(db_column='PunRemito', blank=True, null=True)  # Field name made lowercase.
    punpedido = models.IntegerField(db_column='PunPedido', blank=True, null=True)  # Field name made lowercase.
    punitempedido = models.IntegerField(db_column='PunItemPedido', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIRemitoPedidoItemTMP'


class Cliremitos(models.Model):
    punremito = models.AutoField(db_column='PunRemito', primary_key=True)  # Field name made lowercase.
    puntiporemito = models.IntegerField(db_column='PunTipoRemito')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    fechaentrega = models.DateTimeField(db_column='FechaEntrega', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pundeposito = models.IntegerField(db_column='PunDeposito')  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    prefijo = models.CharField(db_column='Prefijo', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sufijo = models.CharField(db_column='Sufijo', max_length=8, blank=True, null=True)  # Field name made lowercase.
    pundistribuidor = models.IntegerField(db_column='PunDistribuidor', blank=True, null=True)  # Field name made lowercase.
    punmotivoanulacion = models.IntegerField(db_column='PunMotivoAnulacion', blank=True, null=True)  # Field name made lowercase.
    punremitotransporte = models.IntegerField(db_column='PunRemitoTransporte', blank=True, null=True)  # Field name made lowercase.
    puntiporesponsableentrega = models.IntegerField(db_column='PunTipoResponsableEntrega', blank=True, null=True)  # Field name made lowercase.
    puntero = models.IntegerField(db_column='Puntero', blank=True, null=True)  # Field name made lowercase.
    paquetes = models.CharField(db_column='Paquetes', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nropaquete = models.CharField(db_column='NroPaquete', max_length=5, blank=True, null=True)  # Field name made lowercase.
    bultos = models.IntegerField(db_column='Bultos', blank=True, null=True)  # Field name made lowercase.
    peso = models.DecimalField(db_column='Peso', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punoperario = models.IntegerField(db_column='PunOperario', blank=True, null=True)  # Field name made lowercase.
    fechapreparacion = models.DateTimeField(db_column='FechaPreparacion', blank=True, null=True)  # Field name made lowercase.
    punhojaruta = models.IntegerField(db_column='PunHojaRuta', blank=True, null=True)  # Field name made lowercase.
    fechaoperacion = models.DateTimeField(db_column='FechaOperacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIRemitos'


class Cliremitostmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    punremito = models.IntegerField(db_column='PunRemito', blank=True, null=True)  # Field name made lowercase.
    puntiporemito = models.IntegerField(db_column='PunTipoRemito', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    fechaentrega = models.DateTimeField(db_column='FechaEntrega', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pundeposito = models.IntegerField(db_column='PunDeposito', blank=True, null=True)  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    prefijo = models.CharField(db_column='Prefijo', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sufijo = models.CharField(db_column='Sufijo', max_length=8, blank=True, null=True)  # Field name made lowercase.
    pundistribuidor = models.IntegerField(db_column='PunDistribuidor', blank=True, null=True)  # Field name made lowercase.
    punmotivoanulacion = models.IntegerField(db_column='PunMotivoAnulacion', blank=True, null=True)  # Field name made lowercase.
    punremitotransporte = models.IntegerField(db_column='PunRemitoTransporte', blank=True, null=True)  # Field name made lowercase.
    puntiporesponsableentrega = models.IntegerField(db_column='PunTipoResponsableEntrega', blank=True, null=True)  # Field name made lowercase.
    puntero = models.IntegerField(db_column='Puntero', blank=True, null=True)  # Field name made lowercase.
    paquetes = models.CharField(db_column='Paquetes', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nropaquete = models.CharField(db_column='NroPaquete', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIRemitosTMP'


class Clisubclientes(models.Model):
    punsubcliente = models.AutoField(db_column='PunSubCliente', primary_key=True)  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=120)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLISubClientes'


class Cliunidadnegocio(models.Model):
    pununidadnegocio = models.AutoField(db_column='PunUnidadNegocio', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    borrado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'CLIUnidadNegocio'


class Clivariaciondatos(models.Model):
    punvariacion = models.AutoField(db_column='PunVariacion', primary_key=True)  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='PunUsuario', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    variable = models.CharField(db_column='Variable', max_length=50, blank=True, null=True)  # Field name made lowercase.
    valoranterior = models.IntegerField(db_column='ValorAnterior', blank=True, null=True)  # Field name made lowercase.
    valorposterior = models.IntegerField(db_column='ValorPosterior', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIVariacionDatos'


class Clivendedores(models.Model):
    puncliente = models.IntegerField(db_column='PunCliente')  # Field name made lowercase.
    punvendedor = models.IntegerField(db_column='PunVendedor')  # Field name made lowercase.
    predeterminado = models.SmallIntegerField(db_column='Predeterminado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIVendedores'


class Clivendedoresbak(models.Model):
    puncliente = models.IntegerField(db_column='PunCliente')  # Field name made lowercase.
    punvendedor = models.IntegerField(db_column='PunVendedor')  # Field name made lowercase.
    predeterminado = models.SmallIntegerField(db_column='Predeterminado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIVendedoresBAK'


class Clivendedorestmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    punvendedor = models.IntegerField(db_column='PunVendedor', blank=True, null=True)  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    predeterminado = models.SmallIntegerField(db_column='Predeterminado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIVendedoresTMP'


class Conasientoajustecambio(models.Model):
    punasiento = models.IntegerField(db_column='PunAsiento')  # Field name made lowercase.
    punejercicio = models.IntegerField(db_column='PunEjercicio')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    cotizacionajuste = models.DecimalField(db_column='CotizacionAjuste', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cotizacionanterior = models.DecimalField(db_column='CotizacionAnterior', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONAsientoAjusteCambio'


class Conasientoajusteinf(models.Model):
    punejercicio = models.IntegerField(db_column='PunEjercicio', blank=True, null=True)  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa', blank=True, null=True)  # Field name made lowercase.
    puntipocuenta = models.IntegerField(db_column='PunTipoCuenta', blank=True, null=True)  # Field name made lowercase.
    punasiento = models.IntegerField(db_column='PunAsiento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONAsientoAjusteInf'


class Conasientos(models.Model):
    punejercicio = models.IntegerField(db_column='PunEjercicio')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa', blank=True, null=True)  # Field name made lowercase.
    punasiento = models.AutoField(db_column='PunAsiento', primary_key=True)  # Field name made lowercase.
    asientolibrodiario = models.IntegerField(db_column='AsientoLibroDiario', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    leyenda = models.CharField(db_column='Leyenda', max_length=100, blank=True, null=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    punorigen = models.IntegerField(db_column='PunOrigen', blank=True, null=True)  # Field name made lowercase.
    nroasiento = models.IntegerField(db_column='NroAsiento')  # Field name made lowercase.
    bloqueado = models.IntegerField(db_column='Bloqueado', blank=True, null=True)  # Field name made lowercase.
    punasientoresumen = models.IntegerField(db_column='PunAsientoResumen', blank=True, null=True)  # Field name made lowercase.
    esresumen = models.SmallIntegerField(db_column='EsResumen')  # Field name made lowercase.
    punmodulo = models.SmallIntegerField(db_column='PunModulo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONAsientos'


class Conasientosnobalanceantmp(models.Model):
    punejercicio = models.IntegerField(db_column='PunEjercicio')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa', blank=True, null=True)  # Field name made lowercase.
    asientotran = models.IntegerField(db_column='AsientoTran')  # Field name made lowercase.
    pasetran = models.IntegerField(db_column='PaseTran')  # Field name made lowercase.
    punasiento = models.IntegerField(db_column='PunAsiento', blank=True, null=True)  # Field name made lowercase.
    cuenta = models.CharField(db_column='Cuenta', max_length=9)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    leyendapase = models.CharField(db_column='LeyendaPase', max_length=100, blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    leyendaasiento = models.CharField(db_column='LeyendaAsiento', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nroasiento = models.IntegerField(db_column='NroAsiento', blank=True, null=True)  # Field name made lowercase.
    puncentrocosto = models.IntegerField(db_column='PunCentroCosto', blank=True, null=True)  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    punsubcliente = models.IntegerField(db_column='PunSubcliente', blank=True, null=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT', blank=True, null=True)  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='PunProveedor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONAsientosNoBalanceanTMP'


class Conasientostmp(models.Model):
    punejercicio = models.IntegerField(db_column='PunEjercicio')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa', blank=True, null=True)  # Field name made lowercase.
    asientotran = models.IntegerField(db_column='AsientoTran')  # Field name made lowercase.
    pasetran = models.IntegerField(db_column='PaseTran')  # Field name made lowercase.
    punasiento = models.IntegerField(db_column='PunAsiento', blank=True, null=True)  # Field name made lowercase.
    cuenta = models.CharField(db_column='Cuenta', max_length=9)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    leyendapase = models.CharField(db_column='LeyendaPase', max_length=100, blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    leyendaasiento = models.CharField(db_column='LeyendaAsiento', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nroasiento = models.IntegerField(db_column='NroAsiento', blank=True, null=True)  # Field name made lowercase.
    puncentrocosto = models.IntegerField(db_column='PunCentroCosto', blank=True, null=True)  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    punsubcliente = models.IntegerField(db_column='PunSubcliente', blank=True, null=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT', blank=True, null=True)  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='PunProveedor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONAsientosTMP'


class Concentrocostos(models.Model):
    puncentrocosto = models.AutoField(db_column='PunCentroCosto', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONCentroCostos'


class Concuentasasientosautomaticos(models.Model):
    punplancuentas = models.IntegerField(db_column='PunPlanCuentas')  # Field name made lowercase.
    etiqueta = models.CharField(db_column='Etiqueta', max_length=20)  # Field name made lowercase.
    cuenta = models.CharField(db_column='Cuenta', max_length=9, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONCuentasAsientosAutomaticos'


class Conejerciciocierre(models.Model):
    punejercicio = models.IntegerField(db_column='PunEjercicio')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    punasientocierregastos = models.IntegerField(db_column='PunAsientoCierreGastos', blank=True, null=True)  # Field name made lowercase.
    punasientocierrepatr = models.IntegerField(db_column='PunAsientoCierrePatr', blank=True, null=True)  # Field name made lowercase.
    punasientoapertura = models.IntegerField(db_column='PunAsientoApertura', blank=True, null=True)  # Field name made lowercase.
    nroasiento = models.IntegerField(db_column='NroAsiento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONEjercicioCierre'


class Conejercicios(models.Model):
    punejercicio = models.AutoField(primary_key=True, db_column='PunEjercicio')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fechainicio = models.DateTimeField(db_column='FechaInicio')  # Field name made lowercase.
    fechacierre = models.DateTimeField(db_column='FechaCierre')  # Field name made lowercase.
    asientoapertura = models.IntegerField(db_column='AsientoApertura', blank=True, null=True)  # Field name made lowercase.
    asientocierre = models.IntegerField(db_column='AsientoCierre', blank=True, null=True)  # Field name made lowercase.
    fechabloqueo = models.DateTimeField(db_column='FechaBloqueo', blank=True, null=True)  # Field name made lowercase.
    punplancuentas = models.IntegerField(db_column='PunPlanCuentas')  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    ultimoasiento = models.IntegerField(db_column='UltimoAsiento', blank=True, null=True)  # Field name made lowercase.
    fechabloqueocont = models.DateTimeField(db_column='FechaBloqueoCont', blank=True, null=True)  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONEjercicios'


class Conmodeloasientos(models.Model):
    punmodeloasiento = models.AutoField(primary_key=True, db_column='PunModeloAsiento')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150)  # Field name made lowercase.
    punplancuentas = models.IntegerField(db_column='PunPlanCuentas')  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONModeloAsientos'


class Conmodelopases(models.Model):
    punmodeloasiento = models.IntegerField(db_column='PunModeloAsiento')  # Field name made lowercase.
    cuenta = models.CharField(db_column='Cuenta', max_length=9)  # Field name made lowercase.
    debehaber = models.SmallIntegerField(db_column='DebeHaber')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONModeloPases'


class Conmodelopasestmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    punmodeloasiento = models.IntegerField(db_column='PunModeloAsiento', blank=True, null=True)  # Field name made lowercase.
    cuenta = models.CharField(db_column='Cuenta', max_length=9)  # Field name made lowercase.
    debehaber = models.SmallIntegerField(db_column='DebeHaber')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONModeloPasesTMP'


class Conpases(models.Model):
    punasiento = models.IntegerField(db_column='PunAsiento')  # Field name made lowercase.
    pase = models.IntegerField(db_column='Pase')  # Field name made lowercase.
    cuenta = models.CharField(db_column='Cuenta', max_length=9)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    leyenda = models.CharField(db_column='Leyenda', max_length=100, blank=True, null=True)  # Field name made lowercase.
    puncentrocosto = models.IntegerField(db_column='PunCentroCosto', blank=True, null=True)  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    punsubcliente = models.IntegerField(db_column='PunSubcliente', blank=True, null=True)  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='PunProveedor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONPases'


class Conplancuentas(models.Model):
    punplancuentas = models.IntegerField(db_column='PunPlanCuentas')  # Field name made lowercase.
    cuenta = models.CharField(db_column='Cuenta', max_length=9)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    aceptamovimientos = models.SmallIntegerField(db_column='AceptaMovimientos', blank=True, null=True)  # Field name made lowercase.
    puntipocuenta = models.SmallIntegerField(db_column='PunTipoCuenta', blank=True, null=True)  # Field name made lowercase.
    cuentasumariza = models.CharField(db_column='CuentaSumariza', max_length=9, blank=True, null=True)  # Field name made lowercase.
    cuentadistribuible = models.SmallIntegerField(db_column='CuentaDistribuible')  # Field name made lowercase.
    ajustaporinflacion = models.SmallIntegerField(db_column='AjustaPorInflacion', blank=True, null=True)  # Field name made lowercase.
    cuentaqueajusta = models.CharField(db_column='CuentaQueAjusta', max_length=9, blank=True, null=True)  # Field name made lowercase.
    cuentaajusteinflacion = models.CharField(db_column='CuentaAjusteInflacion', max_length=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONPlanCuentas'


class Contipocuentacontable(models.Model):
    puntipocuenta = models.IntegerField(db_column='PunTipoCuenta')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTipoCuentaContable'


class Contipoplancuentas(models.Model):
    punplancuentas = models.AutoField(primary_key=True, db_column='PunPlanCuentas')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTipoPlanCuentas'


class Caja(models.Model):
    puncaja = models.AutoField(primary_key=True, db_column='PunCaja')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    fechaapertura = models.DateTimeField(db_column='FechaApertura')  # Field name made lowercase.
    fechacierre = models.DateTimeField(db_column='FechaCierre', blank=True, null=True)  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punasiento = models.IntegerField(db_column='PunAsiento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Caja'


class Canalventaclasificacion(models.Model):
    puncanalventa = models.IntegerField(db_column='PunCanalVenta', blank=True, null=True)  # Field name made lowercase.
    punclasificacion = models.IntegerField(db_column='PunClasificacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CanalVentaClasificacion'


class Canalventaclasificaciontmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDoperacion', blank=True, null=True)  # Field name made lowercase.
    puncanalventa = models.IntegerField(db_column='PunCanalVenta', blank=True, null=True)  # Field name made lowercase.
    punclasificacion = models.IntegerField(db_column='PunClasificacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CanalVentaClasificacionTMP'


class Canalesventa(models.Model):
    puncanalventa = models.AutoField(primary_key=True, db_column='PunCanalVenta')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CanalesVenta'


class Cargaproyectada(models.Model):
    punordent = models.IntegerField(db_column='PunOrdenT', blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    punoperacion = models.IntegerField(db_column='PunOperacion', blank=True, null=True)  # Field name made lowercase.
    inicio = models.DateTimeField(db_column='Inicio', blank=True, null=True)  # Field name made lowercase.
    fin = models.DateTimeField(db_column='Fin', blank=True, null=True)  # Field name made lowercase.
    minutos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CargaProyectada'


class Carteracheques(models.Model):
    puncheque = models.AutoField(primary_key=True, db_column='PunCheque')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    nrocheque = models.CharField(db_column='NroCheque', max_length=20)  # Field name made lowercase.
    punbancoemisor = models.IntegerField(db_column='PunBancoEmisor')  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    fechaemision = models.DateTimeField(db_column='FechaEmision')  # Field name made lowercase.
    fechacheque = models.DateTimeField(db_column='FechaCheque')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    puncomprobanteorigen = models.IntegerField(db_column='PunComprobanteOrigen', blank=True, null=True)  # Field name made lowercase.
    puncomprobantedestino = models.IntegerField(db_column='PunComprobanteDestino', blank=True, null=True)  # Field name made lowercase.
    punbancodeposito = models.IntegerField(db_column='PunBancoDeposito', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    fechastatus = models.DateTimeField(db_column='FechaStatus', blank=True, null=True)  # Field name made lowercase.
    clearing = models.SmallIntegerField(db_column='Clearing')  # Field name made lowercase.
    pundestino = models.IntegerField(db_column='PunDestino', blank=True, null=True)  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    puncomprobanterechazo = models.IntegerField(db_column='PunComprobanteRechazo', blank=True, null=True)  # Field name made lowercase.
    fechaingreso = models.DateTimeField(db_column='FechaIngreso', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=255, blank=True, null=True)  # Field name made lowercase.
    punmotivorechazo = models.IntegerField(db_column='PunMotivoRechazo', blank=True, null=True)  # Field name made lowercase.
    noalaorden = models.SmallIntegerField(db_column='NoALaOrden', blank=True, null=True)  # Field name made lowercase.
    aforo = models.SmallIntegerField(db_column='Aforo', blank=True, null=True)  # Field name made lowercase.
    punorigen = models.IntegerField(db_column='PunOrigen')  # Field name made lowercase.
    punasiento = models.IntegerField(db_column='PunAsiento')  # Field name made lowercase.
    puncaja = models.IntegerField(db_column='PunCaja', blank=True, null=True)  # Field name made lowercase.
    fechaoriginalchq = models.DateTimeField(db_column='FechaOriginalChq', blank=True, null=True)  # Field name made lowercase.
    cuitemisor = models.CharField(db_column='CuitEmisor', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CarteraCheques'


class Carterachequesnuevo(models.Model):
    puncheque = models.IntegerField(db_column='PunCheque')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    nrocheque = models.CharField(db_column='NroCheque', max_length=20)  # Field name made lowercase.
    punbancoemisor = models.IntegerField(db_column='PunBancoEmisor')  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    fechaemision = models.DateTimeField(db_column='FechaEmision')  # Field name made lowercase.
    fechacheque = models.DateTimeField(db_column='FechaCheque')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    puncomprobanteorigen = models.IntegerField(db_column='PunComprobanteOrigen', blank=True, null=True)  # Field name made lowercase.
    puncomprobantedestino = models.IntegerField(db_column='PunComprobanteDestino', blank=True, null=True)  # Field name made lowercase.
    punbancodeposito = models.IntegerField(db_column='PunBancoDeposito', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    fechastatus = models.DateTimeField(db_column='FechaStatus', blank=True, null=True)  # Field name made lowercase.
    clearing = models.SmallIntegerField(db_column='Clearing')  # Field name made lowercase.
    pundestino = models.IntegerField(db_column='PunDestino', blank=True, null=True)  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    puncomprobanterechazo = models.IntegerField(db_column='PunComprobanteRechazo', blank=True, null=True)  # Field name made lowercase.
    fechaingreso = models.DateTimeField(db_column='FechaIngreso', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=255, blank=True, null=True)  # Field name made lowercase.
    punmotivorechazo = models.IntegerField(db_column='PunMotivoRechazo', blank=True, null=True)  # Field name made lowercase.
    noalaorden = models.SmallIntegerField(db_column='NoALaOrden', blank=True, null=True)  # Field name made lowercase.
    aforo = models.SmallIntegerField(db_column='Aforo', blank=True, null=True)  # Field name made lowercase.
    punorigen = models.IntegerField(db_column='PunOrigen')  # Field name made lowercase.
    punasiento = models.IntegerField(db_column='PunAsiento')  # Field name made lowercase.
    puncaja = models.IntegerField(db_column='PunCaja', blank=True, null=True)  # Field name made lowercase.
    fechaoriginalchq = models.DateTimeField(db_column='FechaOriginalChq', blank=True, null=True)  # Field name made lowercase.
    cuitemisor = models.CharField(db_column='CuitEmisor', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CarteraChequesNuevo'


class Carterachequesstatus(models.Model):
    id = models.AutoField(primary_key=True, db_column='Id')  # Field name made lowercase.
    puncheque = models.IntegerField(db_column='PunCheque', blank=True, null=True)  # Field name made lowercase.
    puncaja = models.IntegerField(db_column='PunCAja', blank=True, null=True)  # Field name made lowercase.
    tipomovimiento = models.IntegerField(db_column='TipoMovimiento', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CarteraChequesStatus'


class Carterachequestmp(models.Model):
    puncheque = models.IntegerField(db_column='PunCheque', blank=True, null=True)  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    nrocheque = models.CharField(db_column='NroCheque', max_length=20)  # Field name made lowercase.
    punbancoemisor = models.IntegerField(db_column='PunBancoEmisor')  # Field name made lowercase.
    fechaemision = models.DateTimeField(db_column='FechaEmision')  # Field name made lowercase.
    fechacheque = models.DateTimeField(db_column='FechaCheque')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    puncomprobanteorigen = models.IntegerField(db_column='PunComprobanteOrigen', blank=True, null=True)  # Field name made lowercase.
    puncomprobantedestino = models.IntegerField(db_column='PunComprobanteDestino', blank=True, null=True)  # Field name made lowercase.
    punbancodeposito = models.IntegerField(db_column='PunBancoDeposito', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    fechastatus = models.DateTimeField(db_column='FechaStatus', blank=True, null=True)  # Field name made lowercase.
    clearing = models.SmallIntegerField(db_column='Clearing', blank=True, null=True)  # Field name made lowercase.
    chequetran = models.IntegerField(db_column='ChequeTran')  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda', blank=True, null=True)  # Field name made lowercase.
    noalaorden = models.SmallIntegerField(db_column='NoALaOrden', blank=True, null=True)  # Field name made lowercase.
    agregarimporte = models.SmallIntegerField(db_column='AgregarImporte', blank=True, null=True)  # Field name made lowercase.
    fechaoriginalchq = models.DateTimeField(db_column='FechaOriginalChq', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=255, blank=True, null=True)  # Field name made lowercase.
    punmotivorechazo = models.IntegerField(db_column='PunMotivoRechazo', blank=True, null=True)  # Field name made lowercase.
    punorigen = models.IntegerField(db_column='PunOrigen', blank=True, null=True)  # Field name made lowercase.
    aforo = models.SmallIntegerField(db_column='Aforo', blank=True, null=True)  # Field name made lowercase.
    nrocomprobante = models.CharField(db_column='NroComprobante', max_length=20, blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='IDOperacion', blank=True, null=True)  # Field name made lowercase.
    centralizado = models.SmallIntegerField(db_column='Centralizado', blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cuitemisor = models.CharField(db_column='CuitEmisor', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CarteraChequesTMP'


class Cashflow(models.Model):
    puncashflow = models.AutoField(primary_key=True, db_column='PunCashflow')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    fechavto = models.DateTimeField(db_column='FechaVto')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    tipoingresoegreso = models.SmallIntegerField(db_column='TipoIngresoEgreso')  # Field name made lowercase.
    punorigen = models.IntegerField(db_column='PunOrigen')  # Field name made lowercase.
    punclienteproveedor = models.IntegerField(db_column='PunClienteProveedor', blank=True, null=True)  # Field name made lowercase.
    punreferenciacashflow = models.IntegerField(db_column='PunReferenciaCashflow', blank=True, null=True)  # Field name made lowercase.
    realestimado = models.SmallIntegerField(db_column='RealEstimado')  # Field name made lowercase.
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=2)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.SmallIntegerField(db_column='PunMoneda')  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fechavtooriginal = models.DateTimeField(db_column='FechaVtoOriginal', blank=True, null=True)  # Field name made lowercase.
    punreferencia = models.IntegerField(db_column='PunReferencia', blank=True, null=True)  # Field name made lowercase.
    tiporeferencia = models.CharField(db_column='TipoReferencia', max_length=2, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cashflow'


class Cashflow2(models.Model):
    puncashflow = models.AutoField(primary_key=True, db_column='PunCashflow')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    fechavto = models.DateTimeField(db_column='FechaVto')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    tipoingresoegreso = models.SmallIntegerField(db_column='TipoIngresoEgreso')  # Field name made lowercase.
    punorigen = models.IntegerField(db_column='PunOrigen')  # Field name made lowercase.
    punclienteproveedor = models.IntegerField(db_column='PunClienteProveedor', blank=True, null=True)  # Field name made lowercase.
    punreferenciacashflow = models.IntegerField(db_column='PunReferenciaCashflow', blank=True, null=True)  # Field name made lowercase.
    realestimado = models.SmallIntegerField(db_column='RealEstimado')  # Field name made lowercase.
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=2)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.SmallIntegerField(db_column='PunMoneda')  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fechavtooriginal = models.DateTimeField(db_column='FechaVtoOriginal', blank=True, null=True)  # Field name made lowercase.
    punreferencia = models.IntegerField(db_column='PunReferencia', blank=True, null=True)  # Field name made lowercase.
    tiporeferencia = models.CharField(db_column='TipoReferencia', max_length=2, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cashflow2'


class Categoriasoperario(models.Model):
    puncategoria = models.AutoField(primary_key=True, db_column='PunCategoria')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CategoriasOperario'


class Chequesmotivorechazo(models.Model):
    punmotivorechazo = models.AutoField(primary_key=True, db_column='PunMotivoRechazo')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pidedescripcion = models.BooleanField(db_column='pideDescripcion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChequesMotivoRechazo'


class Cierreotauxiliartmp(models.Model):
    idoperacion = models.IntegerField(db_column='idOperacion', blank=True, null=True)  # Field name made lowercase.
    maquinavalorhora = models.DecimalField(db_column='MaquinaValorHora', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    maquinavalorhorapunmoneda = models.IntegerField(db_column='MaquinaValorHoraPunMoneda', blank=True, null=True)  # Field name made lowercase.
    maquinacotizacion = models.DecimalField(db_column='MaquinaCotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    operariovalorhorapunmoneda = models.IntegerField(db_column='OperarioValorHoraPunMoneda', blank=True, null=True)  # Field name made lowercase.
    operariovalorhora = models.DecimalField(db_column='OperarioValorHora', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    operariocotizacion = models.DecimalField(db_column='OperarioCotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punpartediarioitem = models.IntegerField(db_column='PunParteDiarioItem', blank=True, null=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT', blank=True, null=True)  # Field name made lowercase.
    abrir = models.BooleanField(db_column='Abrir', blank=True, null=True)  # Field name made lowercase.
    horasdecimal = models.FloatField(db_column='HorasDecimal', blank=True, null=True)  # Field name made lowercase.
    maquinatotal = models.DecimalField(db_column='MaquinaTotal', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    operariototal = models.DecimalField(db_column='OperarioTotal', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    minutos = models.IntegerField(db_column='Minutos', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CierreOTAuxiliarTMP'


class Cierreotauxiliaresnoreabrir(models.Model):
    punordent = models.IntegerField(db_column='PunOrdenT')  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='IdOperacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CierreOTAuxiliaresNoReAbrir'


class Cliclaves(models.Model):
    punclave = models.AutoField(primary_key=True, db_column='punClave')  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='punCliente')  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='punUsuario')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    claves = models.CharField(db_column='Claves', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    borrado = models.IntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CliClaves'


class Cliclavestmp(models.Model):
    puncliente = models.IntegerField(db_column='punCliente', blank=True, null=True)  # Field name made lowercase.
    punclave = models.IntegerField(db_column='punClave', blank=True, null=True)  # Field name made lowercase.
    claves = models.CharField(db_column='Claves', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='idOperacion', blank=True, null=True)  # Field name made lowercase.
    modoabm = models.IntegerField(db_column='ModoABM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CliClavesTMP'


class Cliclientesinactivosexcepcion(models.Model):
    puncliente = models.IntegerField(db_column='punCliente', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CliClientesInactivosExcepcion'


class Clicontactocontactos(models.Model):
    puncontactocontacto = models.AutoField(primary_key=True, db_column='punContactoContacto')  # Field name made lowercase.
    puncontacto = models.IntegerField(db_column='punContacto')  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='punUsuario')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    contacto = models.CharField(db_column='Contacto', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    borrado = models.IntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CliContactoContactos'


class Clicontactocontactostmp(models.Model):
    puncontacto = models.IntegerField(db_column='punContacto', blank=True, null=True)  # Field name made lowercase.
    puncontactocontacto = models.IntegerField(db_column='punContactoContacto', blank=True, null=True)  # Field name made lowercase.
    contacto = models.CharField(db_column='Contacto', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='idOperacion', blank=True, null=True)  # Field name made lowercase.
    idoperacion2 = models.IntegerField(db_column='idOperacion2', blank=True, null=True)  # Field name made lowercase.
    modoabm = models.IntegerField(db_column='ModoABM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CliContactoContactosTMP'


class Clicontactofamilias(models.Model):
    punfamilia = models.AutoField(primary_key=True, db_column='punFamilia')  # Field name made lowercase.
    puncontacto = models.IntegerField(db_column='punContacto')  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='punUsuario')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    familia = models.CharField(db_column='Familia', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    borrado = models.IntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CliContactoFamilias'


class Clicontactofamiliastmp(models.Model):
    puncontacto = models.IntegerField(db_column='punContacto', blank=True, null=True)  # Field name made lowercase.
    punfamilia = models.IntegerField(db_column='punFamilia', blank=True, null=True)  # Field name made lowercase.
    familia = models.CharField(db_column='Familia', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='idOperacion', blank=True, null=True)  # Field name made lowercase.
    idoperacion2 = models.IntegerField(db_column='idOperacion2', blank=True, null=True)  # Field name made lowercase.
    modoabm = models.IntegerField(db_column='ModoABM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CliContactoFamiliasTMP'


class Clicontactogustospersonales(models.Model):
    pungustopersonal = models.AutoField(primary_key=True, db_column='punGustoPersonal')  # Field name made lowercase.
    puncontacto = models.IntegerField(db_column='punContacto')  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='punUsuario')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    gustospersonales = models.CharField(db_column='GustosPersonales', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    borrado = models.IntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CliContactoGustosPersonales'


class Clicontactogustospersonalestmp(models.Model):
    puncontacto = models.IntegerField(db_column='punContacto', blank=True, null=True)  # Field name made lowercase.
    pungustopersonal = models.IntegerField(db_column='punGustoPersonal', blank=True, null=True)  # Field name made lowercase.
    gustospersonales = models.CharField(db_column='GustosPersonales', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='idOperacion', blank=True, null=True)  # Field name made lowercase.
    idoperacion2 = models.IntegerField(db_column='idOperacion2', blank=True, null=True)  # Field name made lowercase.
    modoabm = models.IntegerField(db_column='ModoABM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CliContactoGustosPersonalesTMP'


class Clicontactonotas(models.Model):
    punnota = models.AutoField(primary_key=True, db_column='punNota')  # Field name made lowercase.
    puncontacto = models.IntegerField(db_column='punContacto')  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='punUsuario')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    notas = models.CharField(db_column='Notas', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    borrado = models.IntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CliContactoNotas'


class Clicontactonotastmp(models.Model):
    puncontacto = models.IntegerField(db_column='punContacto', blank=True, null=True)  # Field name made lowercase.
    punnota = models.IntegerField(db_column='punNota', blank=True, null=True)  # Field name made lowercase.
    notas = models.CharField(db_column='Notas', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='idOperacion', blank=True, null=True)  # Field name made lowercase.
    idoperacion2 = models.IntegerField(db_column='idOperacion2', blank=True, null=True)  # Field name made lowercase.
    modoabm = models.IntegerField(db_column='ModoABM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CliContactoNotasTMP'


class Clicontactos(models.Model):
    puncontacto = models.AutoField(primary_key=True, db_column='punContacto')  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='punCliente', blank=True, null=True)  # Field name made lowercase.
    cargo = models.CharField(db_column='Cargo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nombres = models.CharField(db_column='Nombres', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apellidos = models.CharField(db_column='Apellidos', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefonos = models.CharField(db_column='Telefonos', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    direccionprivada = models.CharField(db_column='DireccionPrivada', max_length=100, blank=True, null=True)  # Field name made lowercase.
    codigopostalprivado = models.CharField(db_column='CodigoPostalPrivado', max_length=20, blank=True, null=True)  # Field name made lowercase.
    localidadprivada = models.CharField(db_column='LocalidadPrivada', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punprovinciaprivada = models.IntegerField(db_column='punProvinciaPrivada', blank=True, null=True)  # Field name made lowercase.
    punpaisprivado = models.IntegerField(db_column='punPaisPrivado', blank=True, null=True)  # Field name made lowercase.
    telefonosprivados = models.CharField(db_column='TelefonosPrivados', max_length=150, blank=True, null=True)  # Field name made lowercase.
    faxprivado = models.CharField(db_column='FaxPrivado', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emailprivado = models.CharField(db_column='EMailPrivado', max_length=255, blank=True, null=True)  # Field name made lowercase.
    borrado = models.IntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    punlocalidad = models.IntegerField(db_column='PunLocalidad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CliContactos'


class Clicontactostmp(models.Model):
    puncontacto = models.IntegerField(db_column='punContacto', blank=True, null=True)  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='punCliente', blank=True, null=True)  # Field name made lowercase.
    cargo = models.CharField(db_column='Cargo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nombres = models.CharField(db_column='Nombres', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apellidos = models.CharField(db_column='Apellidos', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefonos = models.CharField(db_column='Telefonos', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    direccionprivada = models.CharField(db_column='DireccionPrivada', max_length=100, blank=True, null=True)  # Field name made lowercase.
    codigopostalprivado = models.CharField(db_column='CodigoPostalPrivado', max_length=20, blank=True, null=True)  # Field name made lowercase.
    localidadprivada = models.CharField(db_column='LocalidadPrivada', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punprovinciaprivada = models.IntegerField(db_column='punProvinciaPrivada', blank=True, null=True)  # Field name made lowercase.
    punpaisprivado = models.IntegerField(db_column='punPaisPrivado', blank=True, null=True)  # Field name made lowercase.
    telefonosprivados = models.CharField(db_column='TelefonosPrivados', max_length=150, blank=True, null=True)  # Field name made lowercase.
    faxprivado = models.CharField(db_column='FaxPrivado', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emailprivado = models.CharField(db_column='EMailPrivado', max_length=255, blank=True, null=True)  # Field name made lowercase.
    borrado = models.IntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='idOperacion', blank=True, null=True)  # Field name made lowercase.
    idoperacion2 = models.IntegerField(db_column='idOperacion2', blank=True, null=True)  # Field name made lowercase.
    modoabm = models.IntegerField(db_column='ModoABM', blank=True, null=True)  # Field name made lowercase.
    punlocalidad = models.IntegerField(db_column='PunLocalidad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CliContactosTMP'


class Cliencuestas(models.Model):
    punencuesta = models.AutoField(primary_key=True, db_column='punEncuesta')  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='punCliente', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    resultado = models.CharField(db_column='Resultado', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    borrado = models.IntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CliEncuestas'


class Cliencuestastmp(models.Model):
    punencuesta = models.IntegerField(db_column='punEncuesta', blank=True, null=True)  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='punCliente', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    resultado = models.CharField(db_column='Resultado', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    borrado = models.IntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='idOperacion', blank=True, null=True)  # Field name made lowercase.
    modoabm = models.IntegerField(db_column='ModoABM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CliEncuestasTMP'


# class Cliexp(models.Model):
#     puncliente = models.FloatField(db_column='punCliente', blank=True, null=True)  # Field name made lowercase.
#     nombre = models.CharField(db_column='Nombre', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     direcci├│n = models.CharField(db_column='Direcci├│n', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     c├│digo_postal = models.FloatField(db_column='C├│digo Postal', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     punpais = models.FloatField(db_column='punPais', blank=True, null=True)  # Field name made lowercase.
#     punprovincia = models.FloatField(db_column='PunProvincia', blank=True, null=True)  # Field name made lowercase.
#     localidad_field = models.CharField(db_column='Localidad ', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     tiporecorrido = models.CharField(db_column='TipoRecorrido', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     lugar_entrega = models.CharField(db_column='Lugar Entrega', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'CliExp'


class Clihorarios(models.Model):
    punhorario = models.AutoField(primary_key=True, db_column='punHorario')  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='punCliente')  # Field name made lowercase.
    puntipohorario = models.IntegerField(db_column='PunTipoHorario')  # Field name made lowercase.
    horarios = models.CharField(db_column='Horarios', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dias = models.CharField(db_column='Dias', max_length=100, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    codigopostal = models.CharField(db_column='CodigoPostal', max_length=20, blank=True, null=True)  # Field name made lowercase.
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punprovincia = models.IntegerField(db_column='punProvincia', blank=True, null=True)  # Field name made lowercase.
    punpais = models.IntegerField(db_column='punPais', blank=True, null=True)  # Field name made lowercase.
    telefonos = models.CharField(db_column='Telefonos', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMail', max_length=500, blank=True, null=True)  # Field name made lowercase.
    borrado = models.IntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    punlocalidad = models.IntegerField(db_column='PunLocalidad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CliHorarios'
        unique_together = (('puncliente', 'puntipohorario'),)


class Clihorariostmp(models.Model):
    puntipohorario = models.IntegerField(db_column='PunTipoHorario')  # Field name made lowercase.
    horarios = models.CharField(db_column='Horarios', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dias = models.CharField(db_column='Dias', max_length=100, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    codigopostal = models.CharField(db_column='CodigoPostal', max_length=20, blank=True, null=True)  # Field name made lowercase.
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punprovincia = models.IntegerField(db_column='punProvincia', blank=True, null=True)  # Field name made lowercase.
    punpais = models.IntegerField(db_column='punPais', blank=True, null=True)  # Field name made lowercase.
    telefonos = models.CharField(db_column='Telefonos', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMail', max_length=500, blank=True, null=True)  # Field name made lowercase.
    borrado = models.IntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='punCliente', blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='idOperacion', blank=True, null=True)  # Field name made lowercase.
    modoabm = models.IntegerField(db_column='ModoABM', blank=True, null=True)  # Field name made lowercase.
    punlocalidad = models.IntegerField(db_column='PunLocalidad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CliHorariosTMP'


class Clinotas(models.Model):
    punnota = models.AutoField(primary_key=True, db_column='punNota')  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='punCliente')  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='punUsuario')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    notas = models.CharField(db_column='Notas', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    borrado = models.IntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CliNotas'


class Clinotastmp(models.Model):
    puncliente = models.IntegerField(db_column='punCliente', blank=True, null=True)  # Field name made lowercase.
    punnota = models.IntegerField(db_column='punNota', blank=True, null=True)  # Field name made lowercase.
    notas = models.CharField(db_column='Notas', max_length=8000, blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='idOperacion', blank=True, null=True)  # Field name made lowercase.
    modoabm = models.IntegerField(db_column='ModoABM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CliNotasTMP'


class Clipedidosreposiciontmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion', blank=True, null=True)  # Field name made lowercase.
    punpedido = models.IntegerField(db_column='PunPedido', blank=True, null=True)  # Field name made lowercase.
    punitempedido = models.IntegerField(db_column='PunItemPEdido', blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CliPEdidosReposicionTMP'


class Clipedidoitemhistorial(models.Model):
    punitempedido = models.IntegerField(db_column='punItemPedido')  # Field name made lowercase.
    fechaanterior = models.DateTimeField(db_column='FechaAnterior', blank=True, null=True)  # Field name made lowercase.
    fechanueva = models.DateTimeField(db_column='FechaNueva', blank=True, null=True)  # Field name made lowercase.
    punmotivo = models.IntegerField(db_column='PunMotivo', blank=True, null=True)  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='punUsuario', blank=True, null=True)  # Field name made lowercase.
    instante = models.DateTimeField(db_column='Instante', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CliPedidoItemHistorial'


class Configsistema(models.Model):
    punconfig = models.DecimalField(db_column='punConfig', max_digits=18, decimal_places=0)  # Field name made lowercase.
    propiedad = models.CharField(db_column='Propiedad', max_length=50, blank=True, null=True)  # Field name made lowercase.
    valor = models.CharField(db_column='Valor', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConfigSistema'


class Cosos(models.Model):
    puncoso = models.AutoField(primary_key=True, db_column='PunCoso')  # Field name made lowercase.
    descrip = models.CharField(db_column='Descrip', max_length=80, blank=True, null=True)  # Field name made lowercase.
    cantcosos = models.IntegerField(db_column='CantCosos')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cosos'


class Cotizaciones(models.Model):
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    punmoneda2 = models.IntegerField(db_column='PunMoneda2')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cotizaciones'


class Cuentastmp(models.Model):
    idoperacion = models.IntegerField(db_column='IdOperacion')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=20)  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    enero = models.DecimalField(db_column='Enero', max_digits=9, decimal_places=2)  # Field name made lowercase.
    febrero = models.DecimalField(db_column='Febrero', max_digits=9, decimal_places=2)  # Field name made lowercase.
    marzo = models.DecimalField(db_column='Marzo', max_digits=9, decimal_places=2)  # Field name made lowercase.
    abril = models.DecimalField(db_column='Abril', max_digits=9, decimal_places=2)  # Field name made lowercase.
    mayo = models.DecimalField(db_column='Mayo', max_digits=9, decimal_places=2)  # Field name made lowercase.
    junio = models.DecimalField(db_column='Junio', max_digits=9, decimal_places=2)  # Field name made lowercase.
    julio = models.DecimalField(db_column='Julio', max_digits=9, decimal_places=2)  # Field name made lowercase.
    agosto = models.DecimalField(db_column='Agosto', max_digits=9, decimal_places=2)  # Field name made lowercase.
    septiembre = models.DecimalField(db_column='Septiembre', max_digits=9, decimal_places=2)  # Field name made lowercase.
    octubre = models.DecimalField(db_column='Octubre', max_digits=9, decimal_places=2)  # Field name made lowercase.
    noviembre = models.DecimalField(db_column='Noviembre', max_digits=9, decimal_places=2)  # Field name made lowercase.
    diciembre = models.DecimalField(db_column='Diciembre', max_digits=9, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CuentasTMP'


class Dgicontribucionespattmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=20)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DGIContribucionesPatTMP'


class Dgigeneraciones(models.Model):
    pungeneracion = models.AutoField(primary_key=True, db_column='PunGeneracion')  # Field name made lowercase.
    anio = models.SmallIntegerField(db_column='Anio')  # Field name made lowercase.
    mes = models.SmallIntegerField(db_column='Mes')  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DGIGeneraciones'


class Departamentos(models.Model):
    pundepartamento = models.AutoField(primary_key=True, db_column='PunDepartamento')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Departamentos'


class Depuracionjuan20031216Noborrar(models.Model):
    punpedido = models.IntegerField(db_column='PunPedido')  # Field name made lowercase.
    punitempedido = models.IntegerField(db_column='PunItemPedido', blank=True, null=True)  # Field name made lowercase.
    orden = models.SmallIntegerField(db_column='Orden')  # Field name made lowercase.
    descuento = models.DecimalField(db_column='Descuento', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DepuracionJuan_20031216_NoBorrar'


class Despachantes(models.Model):
    pundespachante = models.AutoField(primary_key=True, db_column='PunDespachante')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=150)  # Field name made lowercase.
    te = models.CharField(db_column='TE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Despachantes'


class Devolucionentregas(models.Model):
    pundevolucion = models.AutoField(primary_key=True, db_column='PunDevolucion')  # Field name made lowercase.
    tiporemito = models.SmallIntegerField(db_column='TipoRemito')  # Field name made lowercase.
    punremito = models.IntegerField(db_column='PunRemito')  # Field name made lowercase.
    fechadevolucion = models.DateTimeField(db_column='FechaDevolucion')  # Field name made lowercase.
    fechaentrega = models.DateTimeField(db_column='FechaEntrega')  # Field name made lowercase.
    puntiporesponsableentrega = models.IntegerField(db_column='PunTipoResponsableEntrega')  # Field name made lowercase.
    puntero = models.IntegerField(db_column='Puntero', blank=True, null=True)  # Field name made lowercase.
    punmotivo = models.IntegerField(db_column='PunMotivo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DevolucionEntregas'


class Diarecorrido(models.Model):
    pundia = models.AutoField(primary_key=True, db_column='PunDia')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=80, blank=True, null=True)  # Field name made lowercase.
    abreviado = models.CharField(db_column='Abreviado', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DiaRecorrido'


class Diarecorridotmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    pundia = models.IntegerField(db_column='PunDia', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=80, blank=True, null=True)  # Field name made lowercase.
    abreviado = models.CharField(db_column='Abreviado', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DiaRecorridoTMP'


class Diasemana(models.Model):
    pundia = models.IntegerField(db_column='PunDia', primary_key=True)  # Field name made lowercase.
    dia = models.CharField(db_column='Dia', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DiaSemana'


class Diasrecorrido(models.Model):
    punrecorrido = models.IntegerField(db_column='PunRecorrido')  # Field name made lowercase.
    pundia = models.IntegerField(db_column='PunDia')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DiasRecorrido'


class Empresaimputaciontmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    idoperaciongral = models.IntegerField(db_column='IDOperacionGral', blank=True, null=True)  # Field name made lowercase.
    punempresaprestamo = models.IntegerField(db_column='PunEmpresaPrestamo', blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='punMoneda', blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmpresaImputacionTMP'


class Empresaresolucionesjurisdicciones(models.Model):
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    punresolucion = models.IntegerField(db_column='PunResolucion')  # Field name made lowercase.
    punjurisdiccion = models.IntegerField(db_column='PunJurisdiccion')  # Field name made lowercase.
    percibe = models.BooleanField(db_column='Percibe')  # Field name made lowercase.
    retiene = models.BooleanField(db_column='Retiene')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmpresaResolucionesJurisdicciones'


class Empresas(models.Model):
    punempresa = models.AutoField(primary_key=True, db_column='PunEmpresa')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=80)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado')  # Field name made lowercase.
    punprovincia = models.IntegerField(db_column='PunProvincia', blank=True, null=True)  # Field name made lowercase.
    localidad = models.CharField(db_column='Localidad', max_length=50, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=120, blank=True, null=True)  # Field name made lowercase.
    codigopostal = models.CharField(db_column='CodigoPostal', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cuit = models.CharField(db_column='Cuit', max_length=15, blank=True, null=True)  # Field name made lowercase.
    puntipoiva = models.IntegerField(db_column='PunTipoIva', blank=True, null=True)  # Field name made lowercase.
    agenteretencioniva = models.SmallIntegerField(db_column='AgenteRetencionIVA')  # Field name made lowercase.
    empleador = models.SmallIntegerField(db_column='Empleador')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Empresas'


class ErroresDts(models.Model):
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    nombredts = models.CharField(db_column='NombreDTS', max_length=128, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Errores_DTS'


class Estadisticabase(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion', blank=True, null=True)  # Field name made lowercase.
    punsucursal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EstadisticaBase'


class Estadisticasbase(models.Model):
    idoperacion = models.IntegerField(db_column='IdOperacion', blank=True, null=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    punmonedaoriginal = models.IntegerField(db_column='PunMonedaOriginal', blank=True, null=True)  # Field name made lowercase.
    punmonedafactura = models.IntegerField(db_column='PunMonedaFactura', blank=True, null=True)  # Field name made lowercase.
    punvendedor = models.IntegerField(db_column='PunVendedor', blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    punrubro = models.IntegerField(db_column='PunRubro', blank=True, null=True)  # Field name made lowercase.
    pungrupo = models.IntegerField(db_column='PunGrupo', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importesiniva = models.DecimalField(db_column='ImporteSinIva', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    preciooriginal = models.DecimalField(db_column='PrecioOriginal', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bonificacion = models.DecimalField(db_column='Bonificacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punfamilia = models.IntegerField(db_column='punFamilia', blank=True, null=True)  # Field name made lowercase.
    punlineaproduccion = models.IntegerField(db_column='punLineaProduccion', blank=True, null=True)  # Field name made lowercase.
    puninsumo = models.IntegerField(db_column='punInsumo', blank=True, null=True)  # Field name made lowercase.
    punbys = models.IntegerField(db_column='PunByS', blank=True, null=True)  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='PunProveedor', blank=True, null=True)  # Field name made lowercase.
    tipo = models.IntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    puntipompse = models.IntegerField(db_column='PunTipoMPSE', blank=True, null=True)  # Field name made lowercase.
    origen = models.IntegerField(db_column='Origen', blank=True, null=True)  # Field name made lowercase.
    punsucursal = models.IntegerField(db_column='punSucursal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EstadisticasBase'


class EtiqCircularesstd(models.Model):
    punarticulo = models.IntegerField(db_column='Punarticulo', blank=True, null=True)  # Field name made lowercase.
    diametro = models.IntegerField(db_column='Diametro', blank=True, null=True)  # Field name made lowercase.
    espesor = models.DecimalField(db_column='Espesor', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    buje = models.IntegerField(db_column='Buje', blank=True, null=True)  # Field name made lowercase.
    paso = models.DecimalField(db_column='Paso', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    zeta = models.IntegerField(db_column='Zeta', blank=True, null=True)  # Field name made lowercase.
    dtetipo = models.CharField(db_column='DteTipo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    terminacion = models.CharField(db_column='Terminacion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Etiq_CircularesSTD'


class EtiqCircularesstd3(models.Model):
    punarticulo = models.IntegerField(db_column='Punarticulo', blank=True, null=True)  # Field name made lowercase.
    diametro = models.IntegerField(db_column='Diametro', blank=True, null=True)  # Field name made lowercase.
    espesor = models.FloatField(db_column='Espesor', blank=True, null=True)  # Field name made lowercase.
    buje = models.IntegerField(db_column='Buje', blank=True, null=True)  # Field name made lowercase.
    paso = models.FloatField(db_column='Paso', blank=True, null=True)  # Field name made lowercase.
    zeta = models.IntegerField(db_column='Zeta', blank=True, null=True)  # Field name made lowercase.
    dtetipo = models.CharField(db_column='DteTipo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    terminacion = models.CharField(db_column='Terminacion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Etiq_CircularesSTD3'


# class EtiqGarlopasstd(models.Model):
#     punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
#     c├│digo = models.CharField(db_column='C├│digo', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     medida = models.CharField(db_column='Medida', max_length=50, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Etiq_GarlopasSTD'


class FeCodigosgenericos(models.Model):
    puncodigo = models.SmallAutoField(primary_key=True, db_column='PunCodigo')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=14)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FE_CodigosGenericos'


class FeComprobanteelectronico(models.Model):
    punfe = models.AutoField(primary_key=True, db_column='punFe')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='punComprobante')  # Field name made lowercase.
    cae = models.CharField(db_column='CAE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fechavto = models.DateTimeField(db_column='FechaVto', blank=True, null=True)  # Field name made lowercase.
    punlote = models.IntegerField(db_column='PunLote', blank=True, null=True)  # Field name made lowercase.
    esregimenfe = models.BooleanField(db_column='EsRegimenFE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FE_ComprobanteElectronico'


class FeComprobanteqr(models.Model):
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    punorigen = models.SmallIntegerField(db_column='PunOrigen', blank=True, null=True)  # Field name made lowercase.
    imagenqr = models.BinaryField(db_column='ImagenQR', blank=True, null=True)  # Field name made lowercase.
    jsonqr = models.CharField(db_column='JsonQR', max_length=512, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FE_ComprobanteQR'


class FeLotedetalle(models.Model):
    punlotedetalle = models.AutoField(primary_key=True, db_column='PunLoteDetalle')  # Field name made lowercase.
    punlote = models.IntegerField(db_column='PunLote')  # Field name made lowercase.
    punfe = models.IntegerField(db_column='PunFE')  # Field name made lowercase.
    codigoerror = models.CharField(db_column='CodigoError', max_length=10, blank=True, null=True)  # Field name made lowercase.
    descripcionerror = models.CharField(db_column='DescripcionError', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FE_LoteDetalle'


class FeLotes(models.Model):
    punlote = models.AutoField(primary_key=True, db_column='PunLote')  # Field name made lowercase.
    numero = models.IntegerField(db_column='Numero')  # Field name made lowercase.
    fechaproceso = models.DateTimeField(db_column='FechaProceso')  # Field name made lowercase.
    fecharespuesta = models.DateTimeField(db_column='FechaRespuesta', blank=True, null=True)  # Field name made lowercase.
    reprocesar = models.CharField(db_column='Reprocesar', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FE_Lotes'


class FeParametros(models.Model):
    punparametro = models.AutoField(primary_key=True, db_column='PunParametro')  # Field name made lowercase.
    etiqueta = models.CharField(db_column='Etiqueta', max_length=20)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    valornumerico = models.FloatField(db_column='ValorNumerico', blank=True, null=True)  # Field name made lowercase.
    valorcaracter = models.CharField(db_column='ValorCaracter', max_length=255, blank=True, null=True)  # Field name made lowercase.
    valorfecha = models.DateTimeField(db_column='ValorFecha', blank=True, null=True)  # Field name made lowercase.
    valorboolean = models.SmallIntegerField(db_column='ValorBoolean', blank=True, null=True)  # Field name made lowercase.
    valortexto = models.TextField(db_column='ValorTexto', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tipovalor = models.IntegerField(db_column='TipoValor', blank=True, null=True)  # Field name made lowercase.
    storedproc = models.CharField(db_column='StoredProc', max_length=80, blank=True, null=True)  # Field name made lowercase.
    spbusquedatabla = models.CharField(db_column='SPBusquedaTabla', max_length=80, blank=True, null=True)  # Field name made lowercase.
    campoadditem = models.CharField(db_column='CampoAddItem', max_length=30, blank=True, null=True)  # Field name made lowercase.
    campoitemdata = models.CharField(db_column='CampoItemData', max_length=30, blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FE_Parametros'


class Factu(models.Model):
    punproveedor = models.FloatField(db_column='PunProveedor', blank=True, null=True)  # Field name made lowercase.
    proveedor = models.CharField(db_column='Proveedor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tipocomp = models.CharField(db_column='TipoComp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    numero = models.FloatField(db_column='Numero', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    sufijo = models.CharField(db_column='Sufijo', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Factu'


class Familiasarticulos(models.Model):
    punfamilia = models.AutoField(primary_key=True, db_column='PunFamilia')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=4)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FamiliasArticulos'


class Familiasinsumos(models.Model):
    punfamilia = models.AutoField(primary_key=True, db_column='PunFamilia')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=4)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FamiliasInsumos'


class Feriados(models.Model):
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Feriados'


class Gcsarticulos(models.Model):
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    descripciontipo = models.CharField(db_column='DescripcionTipo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    unidadesporenvase = models.IntegerField(db_column='UnidadesPorEnvase', blank=True, null=True)  # Field name made lowercase.
    posicionarancelaria = models.CharField(db_column='PosicionArancelaria', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cotcodigo = models.CharField(db_column='COTCodigo', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GCSArticulos'


class Gcsbonif1(models.Model):
    puncliente = models.FloatField(db_column='punCliente', blank=True, null=True)  # Field name made lowercase.
    codcliente = models.FloatField(db_column='CodCliente', blank=True, null=True)  # Field name made lowercase.
    descliente = models.CharField(db_column='Descliente', max_length=255, blank=True, null=True)  # Field name made lowercase.
    punrubro = models.FloatField(db_column='punRubro', blank=True, null=True)  # Field name made lowercase.
    codrubro = models.CharField(db_column='CodRubro', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desrubro = models.CharField(db_column='DesRubro', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pungrupo = models.FloatField(db_column='punGrupo', blank=True, null=True)  # Field name made lowercase.
    codgrupo = models.CharField(db_column='CodGrupo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desgrupo = models.CharField(db_column='DesGrupo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    punfamilia = models.FloatField(db_column='punFamilia', blank=True, null=True)  # Field name made lowercase.
    codfamilia = models.CharField(db_column='CodFamilia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desfamilia = models.CharField(db_column='DesFamilia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.FloatField(db_column='punArticulo', blank=True, null=True)  # Field name made lowercase.
    codarticulo = models.CharField(db_column='CodArticulo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desarticulo = models.CharField(db_column='DesArticulo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bonif01 = models.FloatField(db_column='Bonif01', blank=True, null=True)  # Field name made lowercase.
    bonif02 = models.FloatField(db_column='Bonif02', blank=True, null=True)  # Field name made lowercase.
    bonif03 = models.FloatField(db_column='Bonif03', blank=True, null=True)  # Field name made lowercase.
    bonif04 = models.FloatField(db_column='Bonif04', blank=True, null=True)  # Field name made lowercase.
    bonif05 = models.FloatField(db_column='Bonif05', blank=True, null=True)  # Field name made lowercase.
    bonif06 = models.FloatField(db_column='Bonif06', blank=True, null=True)  # Field name made lowercase.
    bonif07 = models.FloatField(db_column='Bonif07', blank=True, null=True)  # Field name made lowercase.
    bonif08 = models.FloatField(db_column='Bonif08', blank=True, null=True)  # Field name made lowercase.
    bonif09 = models.FloatField(db_column='Bonif09', blank=True, null=True)  # Field name made lowercase.
    bonif10 = models.FloatField(db_column='Bonif10', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GCSBonif1'


class Gcsbonifold(models.Model):
    puncliente = models.FloatField(db_column='punCliente', blank=True, null=True)  # Field name made lowercase.
    codcliente = models.FloatField(db_column='CodCliente', blank=True, null=True)  # Field name made lowercase.
    descliente = models.CharField(db_column='Descliente', max_length=255, blank=True, null=True)  # Field name made lowercase.
    punrubro = models.FloatField(db_column='punRubro', blank=True, null=True)  # Field name made lowercase.
    codrubro = models.CharField(db_column='CodRubro', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desrubro = models.CharField(db_column='DesRubro', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pungrupo = models.FloatField(db_column='punGrupo', blank=True, null=True)  # Field name made lowercase.
    codgrupo = models.CharField(db_column='CodGrupo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desgrupo = models.CharField(db_column='DesGrupo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    punfamilia = models.FloatField(db_column='punFamilia', blank=True, null=True)  # Field name made lowercase.
    codfamilia = models.CharField(db_column='CodFamilia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desfamilia = models.CharField(db_column='DesFamilia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.FloatField(db_column='punArticulo', blank=True, null=True)  # Field name made lowercase.
    codarticulo = models.CharField(db_column='CodArticulo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desarticulo = models.CharField(db_column='DesArticulo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bonif01 = models.FloatField(db_column='Bonif01', blank=True, null=True)  # Field name made lowercase.
    bonif02 = models.FloatField(db_column='Bonif02', blank=True, null=True)  # Field name made lowercase.
    bonif03 = models.FloatField(db_column='Bonif03', blank=True, null=True)  # Field name made lowercase.
    bonif04 = models.FloatField(db_column='Bonif04', blank=True, null=True)  # Field name made lowercase.
    bonif05 = models.FloatField(db_column='Bonif05', blank=True, null=True)  # Field name made lowercase.
    bonif06 = models.FloatField(db_column='Bonif06', blank=True, null=True)  # Field name made lowercase.
    bonif07 = models.FloatField(db_column='Bonif07', blank=True, null=True)  # Field name made lowercase.
    bonif08 = models.FloatField(db_column='Bonif08', blank=True, null=True)  # Field name made lowercase.
    bonif09 = models.FloatField(db_column='Bonif09', blank=True, null=True)  # Field name made lowercase.
    bonif10 = models.FloatField(db_column='Bonif10', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GCSBonifOLD'


class Gcsgisesaldo(models.Model):
    punreferencia = models.IntegerField(db_column='PUNREFERENCIA')  # Field name made lowercase.
    saldo = models.DecimalField(db_column='SALDO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GCSGISESALDO'


class GcsArticulos06052018(models.Model):
    punarticulo = models.AutoField(primary_key=True, db_column='PunArticulo')  # Field name made lowercase.
    punrubro = models.IntegerField(db_column='PunRubro')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150)  # Field name made lowercase.
    punlineaproduccion = models.IntegerField(db_column='PunLineaProduccion')  # Field name made lowercase.
    punfamilia = models.IntegerField(db_column='PunFamilia')  # Field name made lowercase.
    pungrupo = models.IntegerField(db_column='PunGrupo')  # Field name made lowercase.
    origen = models.SmallIntegerField(db_column='Origen')  # Field name made lowercase.
    tipo = models.SmallIntegerField(db_column='Tipo')  # Field name made lowercase.
    cuentacompra = models.CharField(db_column='CuentaCompra', max_length=9, blank=True, null=True)  # Field name made lowercase.
    cuentaventa = models.CharField(db_column='CuentaVenta', max_length=9, blank=True, null=True)  # Field name made lowercase.
    pununidad = models.IntegerField(db_column='PunUnidad')  # Field name made lowercase.
    stockminimo = models.DecimalField(db_column='StockMinimo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    stockcritico = models.DecimalField(db_column='StockCritico', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    stockmaximo = models.DecimalField(db_column='StockMaximo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    alicuotaiva = models.IntegerField(db_column='AlicuotaIVA')  # Field name made lowercase.
    codigobarras = models.CharField(db_column='CodigoBarras', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ubicacionfisica = models.CharField(db_column='UbicacionFisica', max_length=10, blank=True, null=True)  # Field name made lowercase.
    codigoalternativo = models.CharField(db_column='CodigoAlternativo', max_length=16, blank=True, null=True)  # Field name made lowercase.
    critico = models.SmallIntegerField(db_column='Critico', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=255, blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    enfabricacion = models.DecimalField(db_column='EnFabricacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    consumopromedio = models.DecimalField(db_column='ConsumoPromedio', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tiemporeposicion = models.DecimalField(db_column='TiempoReposicion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    caractadicionales = models.CharField(db_column='CaractAdicionales', max_length=255, blank=True, null=True)  # Field name made lowercase.
    generastock = models.BooleanField(db_column='GeneraStock')  # Field name made lowercase.
    peso = models.DecimalField(db_column='Peso', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pununidadalternativa = models.IntegerField(db_column='PunUnidadAlternativa', blank=True, null=True)  # Field name made lowercase.
    coeficiente = models.DecimalField(db_column='Coeficiente', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    puntipoot = models.IntegerField(db_column='PunTipoOT', blank=True, null=True)  # Field name made lowercase.
    punplanosinparvigente = models.IntegerField(db_column='PunPlanoSinParVigente', blank=True, null=True)  # Field name made lowercase.
    posicionarancelaria = models.CharField(db_column='PosicionArancelaria', max_length=50, blank=True, null=True)  # Field name made lowercase.
    puntipompse = models.IntegerField(db_column='PunTipoMPSE', blank=True, null=True)  # Field name made lowercase.
    unidadesporenvase = models.IntegerField(db_column='UnidadesPorEnvase', blank=True, null=True)  # Field name made lowercase.
    unidadreferenciafe = models.CharField(db_column='UnidadReferenciaFE', max_length=6, blank=True, null=True)  # Field name made lowercase.
    codigofe = models.CharField(db_column='CodigoFE', max_length=14, blank=True, null=True)  # Field name made lowercase.
    pununidadmedidafe = models.IntegerField(db_column='PunUnidadMedidaFE', blank=True, null=True)  # Field name made lowercase.
    codigobonofiscal = models.CharField(db_column='CodigoBonoFiscal', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cotcodigo = models.CharField(db_column='COTCodigo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cotcodigounidad = models.SmallIntegerField(db_column='COTCodigoUnidad', blank=True, null=True)  # Field name made lowercase.
    cotobligatorio = models.BooleanField(db_column='COTObligatorio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GCS_ARTICULOS06052018'


class GcsAsientosncmal(models.Model):
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    nroasiento = models.IntegerField(db_column='NroAsiento')  # Field name made lowercase.
    leyenda = models.CharField(db_column='Leyenda', max_length=100, blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punasiento = models.IntegerField(db_column='PunAsiento')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GCS_AsientosNCMal'


class GcsCambioart30012020(models.Model):
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.
    punrubro = models.IntegerField(db_column='PunRubro')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150)  # Field name made lowercase.
    punlineaproduccion = models.IntegerField(db_column='PunLineaProduccion')  # Field name made lowercase.
    punfamilia = models.IntegerField(db_column='PunFamilia')  # Field name made lowercase.
    pungrupo = models.IntegerField(db_column='PunGrupo')  # Field name made lowercase.
    origen = models.SmallIntegerField(db_column='Origen')  # Field name made lowercase.
    tipo = models.SmallIntegerField(db_column='Tipo')  # Field name made lowercase.
    cuentacompra = models.CharField(db_column='CuentaCompra', max_length=9, blank=True, null=True)  # Field name made lowercase.
    cuentaventa = models.CharField(db_column='CuentaVenta', max_length=9, blank=True, null=True)  # Field name made lowercase.
    pununidad = models.IntegerField(db_column='PunUnidad')  # Field name made lowercase.
    stockminimo = models.DecimalField(db_column='StockMinimo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    stockcritico = models.DecimalField(db_column='StockCritico', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    stockmaximo = models.DecimalField(db_column='StockMaximo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    alicuotaiva = models.IntegerField(db_column='AlicuotaIVA')  # Field name made lowercase.
    codigobarras = models.CharField(db_column='CodigoBarras', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ubicacionfisica = models.CharField(db_column='UbicacionFisica', max_length=10, blank=True, null=True)  # Field name made lowercase.
    codigoalternativo = models.CharField(db_column='CodigoAlternativo', max_length=16, blank=True, null=True)  # Field name made lowercase.
    critico = models.SmallIntegerField(db_column='Critico', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=255, blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    enfabricacion = models.DecimalField(db_column='EnFabricacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    consumopromedio = models.DecimalField(db_column='ConsumoPromedio', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tiemporeposicion = models.DecimalField(db_column='TiempoReposicion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    caractadicionales = models.CharField(db_column='CaractAdicionales', max_length=255, blank=True, null=True)  # Field name made lowercase.
    generastock = models.BooleanField(db_column='GeneraStock')  # Field name made lowercase.
    peso = models.DecimalField(db_column='Peso', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pununidadalternativa = models.IntegerField(db_column='PunUnidadAlternativa', blank=True, null=True)  # Field name made lowercase.
    coeficiente = models.DecimalField(db_column='Coeficiente', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    puntipoot = models.IntegerField(db_column='PunTipoOT', blank=True, null=True)  # Field name made lowercase.
    punplanosinparvigente = models.IntegerField(db_column='PunPlanoSinParVigente', blank=True, null=True)  # Field name made lowercase.
    posicionarancelaria = models.CharField(db_column='PosicionArancelaria', max_length=50, blank=True, null=True)  # Field name made lowercase.
    puntipompse = models.IntegerField(db_column='PunTipoMPSE', blank=True, null=True)  # Field name made lowercase.
    unidadesporenvase = models.IntegerField(db_column='UnidadesPorEnvase', blank=True, null=True)  # Field name made lowercase.
    unidadreferenciafe = models.CharField(db_column='UnidadReferenciaFE', max_length=6, blank=True, null=True)  # Field name made lowercase.
    codigofe = models.CharField(db_column='CodigoFE', max_length=14, blank=True, null=True)  # Field name made lowercase.
    pununidadmedidafe = models.IntegerField(db_column='PunUnidadMedidaFE', blank=True, null=True)  # Field name made lowercase.
    codigobonofiscal = models.CharField(db_column='CodigoBonoFiscal', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cotcodigo = models.CharField(db_column='COTCodigo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cotcodigounidad = models.SmallIntegerField(db_column='COTCodigoUnidad', blank=True, null=True)  # Field name made lowercase.
    cotobligatorio = models.BooleanField(db_column='COTObligatorio', blank=True, null=True)  # Field name made lowercase.
    punsubclasificacion = models.IntegerField(db_column='PunSubClasificacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GCS_CambioArt30012020'


class GcsListaprecioarticulos20231213(models.Model):
    punprecio = models.IntegerField(db_column='PunPrecio')  # Field name made lowercase.
    punlista = models.IntegerField(db_column='PunLista')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fechamodificacion = models.DateTimeField(db_column='FechaModificacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GCS_ListaPrecioArticulos20231213'


class GcsListaprecioarticulosArtborrados(models.Model):
    punprecio = models.AutoField(primary_key=True, db_column='PunPrecio')  # Field name made lowercase.
    punlista = models.IntegerField(db_column='PunLista')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fechamodificacion = models.DateTimeField(db_column='FechaModificacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GCS_ListaPrecioArticulos_ArtBorrados'


class GcsNcnovimebre2016(models.Model):
    detalle = models.CharField(max_length=23)
    puncomprobante = models.IntegerField(blank=True, null=True)
    sufijo = models.CharField(max_length=8)
    fecha = models.DateTimeField()
    importecc = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    importeci = models.DecimalField(db_column='Importeci', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importeas = models.DecimalField(db_column='ImporteAS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GCS_NCNovimebre2016'


class GcsNcoctubre2016(models.Model):
    detalle = models.CharField(max_length=23)
    puncomprobante = models.IntegerField(blank=True, null=True)
    sufijo = models.CharField(max_length=8)
    fecha = models.DateTimeField()
    importecc = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    importeci = models.DecimalField(db_column='Importeci', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importeas = models.DecimalField(db_column='ImporteAS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GCS_NCOctubre2016'


class GcsNcpositivas(models.Model):
    puncliente = models.IntegerField(db_column='PunCliente')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    punreferencia = models.IntegerField(db_column='PunReferencia')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punmoneda = models.SmallIntegerField(db_column='PunMoneda')  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4)  # Field name made lowercase.
    condicionventa = models.SmallIntegerField(db_column='CondicionVenta', blank=True, null=True)  # Field name made lowercase.
    punsubcliente = models.IntegerField(db_column='PunSubCliente', blank=True, null=True)  # Field name made lowercase.
    observacioncc = models.CharField(db_column='ObservacionCC', max_length=2000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GCS_NCPositivas'


class GcsNcpositivasimportes(models.Model):
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    punreferencia = models.IntegerField(db_column='PunReferencia')  # Field name made lowercase.
    puntipoimporte = models.IntegerField(db_column='PunTipoImporte')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    punjurisdiccionib = models.IntegerField(db_column='PunJurisdiccionIB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GCS_NCPositivasImportes'


class GcsNcpositivasvtos(models.Model):
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    punreferencia = models.IntegerField(db_column='PunReferencia')  # Field name made lowercase.
    fechavto = models.DateTimeField(db_column='FechaVto')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GCS_NCPositivasVtos'


class GcsNcseptiembre2016(models.Model):
    detalle = models.CharField(max_length=23)
    puncomprobante = models.IntegerField(blank=True, null=True)
    sufijo = models.CharField(max_length=8)
    fecha = models.DateTimeField()
    importecc = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    importeci = models.DecimalField(db_column='Importeci', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importeas = models.DecimalField(db_column='ImporteAS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GCS_NCSeptiembre2016'


class Gcs_Prvproveedoresacumulados(models.Model):
    punproveedor = models.IntegerField(db_column='PunProveedor')  # Field name made lowercase.
    pagosmes = models.SmallIntegerField(db_column='PagosMes', blank=True, null=True)  # Field name made lowercase.
    pagosanio = models.SmallIntegerField(db_column='PagosAnio', blank=True, null=True)  # Field name made lowercase.
    acumuladopagos = models.DecimalField(db_column='AcumuladoPagos', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    acumuladoretencion = models.DecimalField(db_column='AcumuladoRetencion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa', blank=True, null=True)  # Field name made lowercase.
    punactividadganancias = models.IntegerField(db_column='PunActividadGanancias', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GCS_PRVProveedoresAcumulados'


class GcsStockmov20200822(models.Model):
    punmovimiento = models.AutoField(primary_key=True, db_column='PunMovimiento')  # Field name made lowercase.
    pundeposito = models.IntegerField(db_column='PunDeposito')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    puntipomovimiento = models.IntegerField(db_column='PunTipoMovimiento')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punremitoitemventa = models.IntegerField(db_column='PunRemitoItemVenta', blank=True, null=True)  # Field name made lowercase.
    punremitoitemcompra = models.IntegerField(db_column='PunRemitoItemCompra', blank=True, null=True)  # Field name made lowercase.
    punmotivo = models.IntegerField(db_column='PunMotivo', blank=True, null=True)  # Field name made lowercase.
    nroordent = models.CharField(db_column='NroOrdenT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    punremitotransferencia = models.IntegerField(db_column='PunRemitoTransferencia', blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='IdOperacion', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punmovimientoencabezado = models.IntegerField(db_column='PunMovimientoEncabezado', blank=True, null=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT', blank=True, null=True)  # Field name made lowercase.
    tipostock = models.SmallIntegerField(db_column='TipoStock', blank=True, null=True)  # Field name made lowercase.
    punmovimientoorigen = models.IntegerField(db_column='PunMovimientoOrigen', blank=True, null=True)  # Field name made lowercase.
    punremitoitemcompraanterior = models.IntegerField(db_column='PunRemitoItemCompraAnterior', blank=True, null=True)  # Field name made lowercase.
    momento = models.DateTimeField(db_column='Momento', blank=True, null=True)  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='PunUsuario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GCS_StockMov20200822'


class GcsStocksinot20201130(models.Model):
    punmovimiento = models.IntegerField(db_column='PunMovimiento')  # Field name made lowercase.
    pundeposito = models.IntegerField(db_column='PunDeposito')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    puntipomovimiento = models.IntegerField(db_column='PunTipoMovimiento')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punremitoitemventa = models.IntegerField(db_column='PunRemitoItemVenta', blank=True, null=True)  # Field name made lowercase.
    punremitoitemcompra = models.IntegerField(db_column='PunRemitoItemCompra', blank=True, null=True)  # Field name made lowercase.
    punmotivo = models.IntegerField(db_column='PunMotivo', blank=True, null=True)  # Field name made lowercase.
    nroordent = models.CharField(db_column='NroOrdenT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    punremitotransferencia = models.IntegerField(db_column='PunRemitoTransferencia', blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='IdOperacion', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punmovimientoencabezado = models.IntegerField(db_column='PunMovimientoEncabezado', blank=True, null=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT', blank=True, null=True)  # Field name made lowercase.
    tipostock = models.SmallIntegerField(db_column='TipoStock', blank=True, null=True)  # Field name made lowercase.
    punmovimientoorigen = models.IntegerField(db_column='PunMovimientoOrigen', blank=True, null=True)  # Field name made lowercase.
    punremitoitemcompraanterior = models.IntegerField(db_column='PunRemitoItemCompraAnterior', blank=True, null=True)  # Field name made lowercase.
    momento = models.DateTimeField(db_column='Momento', blank=True, null=True)  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='PunUsuario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GCS_StockSinOT20201130'


class GcsStocksinot20201203(models.Model):
    punmovimiento = models.IntegerField(db_column='PunMovimiento')  # Field name made lowercase.
    pundeposito = models.IntegerField(db_column='PunDeposito')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    puntipomovimiento = models.IntegerField(db_column='PunTipoMovimiento')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punremitoitemventa = models.IntegerField(db_column='PunRemitoItemVenta', blank=True, null=True)  # Field name made lowercase.
    punremitoitemcompra = models.IntegerField(db_column='PunRemitoItemCompra', blank=True, null=True)  # Field name made lowercase.
    punmotivo = models.IntegerField(db_column='PunMotivo', blank=True, null=True)  # Field name made lowercase.
    nroordent = models.CharField(db_column='NroOrdenT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    punremitotransferencia = models.IntegerField(db_column='PunRemitoTransferencia', blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='IdOperacion', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punmovimientoencabezado = models.IntegerField(db_column='PunMovimientoEncabezado', blank=True, null=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT', blank=True, null=True)  # Field name made lowercase.
    tipostock = models.SmallIntegerField(db_column='TipoStock', blank=True, null=True)  # Field name made lowercase.
    punmovimientoorigen = models.IntegerField(db_column='PunMovimientoOrigen', blank=True, null=True)  # Field name made lowercase.
    punremitoitemcompraanterior = models.IntegerField(db_column='PunRemitoItemCompraAnterior', blank=True, null=True)  # Field name made lowercase.
    momento = models.DateTimeField(db_column='Momento', blank=True, null=True)  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='PunUsuario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GCS_StockSinOT20201203'


class GcsTemp(models.Model):
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    codigonuevo = models.CharField(db_column='CodigoNuevo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descripcionnueva = models.CharField(db_column='DescripcionNueva', max_length=250, blank=True, null=True)  # Field name made lowercase.
    origennuevo = models.CharField(db_column='ORIGenNuevo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    codigoactual = models.CharField(db_column='CodigoActual', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descripcionactual = models.CharField(db_column='DescripcionActual', max_length=250, blank=True, null=True)  # Field name made lowercase.
    punorigenactual = models.IntegerField(db_column='PunOrigenActual', blank=True, null=True)  # Field name made lowercase.
    punorigennuevo = models.IntegerField(db_column='PunOrigenNuevo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GCS_TEMP'


class GcArticulosprecios(models.Model):
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GC_ArticulosPrecios'


class Gastosinternos(models.Model):
    pungastointerno = models.AutoField(primary_key=True, db_column='PunGastoInterno')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    sumarizaen = models.SmallIntegerField(db_column='SumarizaEn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GastosInternos'


class Gastosinternosimputaciones(models.Model):
    punimputacion = models.AutoField(primary_key=True, db_column='PunImputacion')  # Field name made lowercase.
    pungastointerno = models.IntegerField(db_column='PunGastoInterno')  # Field name made lowercase.
    punresponsable = models.IntegerField(db_column='PunResponsable')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    punorigen = models.SmallIntegerField(db_column='PunOrigen')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    importe = models.FloatField(db_column='Importe')  # Field name made lowercase.
    punasiento = models.IntegerField(db_column='PunAsiento', blank=True, null=True)  # Field name made lowercase.
    cuenta = models.CharField(db_column='Cuenta', max_length=9, blank=True, null=True)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    pase = models.IntegerField(db_column='Pase', blank=True, null=True)  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GastosInternosImputaciones'


class Gastosinternosimputacionestmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    punimputacion = models.IntegerField(db_column='PunImputacion', blank=True, null=True)  # Field name made lowercase.
    pungastointerno = models.IntegerField(db_column='PunGastoInterno')  # Field name made lowercase.
    punresponsable = models.IntegerField(db_column='PunResponsable')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    punorigen = models.SmallIntegerField(db_column='PunOrigen')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    importe = models.FloatField(db_column='Importe')  # Field name made lowercase.
    punasiento = models.IntegerField(db_column='PunAsiento', blank=True, null=True)  # Field name made lowercase.
    cuenta = models.CharField(db_column='Cuenta', max_length=9, blank=True, null=True)  # Field name made lowercase.
    modoabm = models.SmallIntegerField(db_column='ModoABM', blank=True, null=True)  # Field name made lowercase.
    pase = models.IntegerField(db_column='Pase', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GastosInternosImputacionesTMP'


class Gcsclibonificaciones03062016(models.Model):
    puncliente = models.IntegerField(db_column='PunCliente')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    punrubro = models.IntegerField(db_column='PunRubro', blank=True, null=True)  # Field name made lowercase.
    orden = models.SmallIntegerField(db_column='Orden')  # Field name made lowercase.
    descuento = models.DecimalField(db_column='Descuento', max_digits=19, decimal_places=4)  # Field name made lowercase.
    pungrupo = models.IntegerField(db_column='punGrupo', blank=True, null=True)  # Field name made lowercase.
    punfamilia = models.IntegerField(db_column='punFamilia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GcsCLIBonificaciones03062016'


class Gcsclibonificaciones04032016(models.Model):
    puncliente = models.IntegerField(db_column='PunCliente')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    punrubro = models.IntegerField(db_column='PunRubro', blank=True, null=True)  # Field name made lowercase.
    orden = models.SmallIntegerField(db_column='Orden')  # Field name made lowercase.
    descuento = models.DecimalField(db_column='Descuento', max_digits=19, decimal_places=4)  # Field name made lowercase.
    pungrupo = models.IntegerField(db_column='punGrupo', blank=True, null=True)  # Field name made lowercase.
    punfamilia = models.IntegerField(db_column='punFamilia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GcsCLIBonificaciones04032016'


class Gcsclibonificaciones29122015(models.Model):
    puncliente = models.IntegerField(db_column='PunCliente')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    punrubro = models.IntegerField(db_column='PunRubro', blank=True, null=True)  # Field name made lowercase.
    orden = models.SmallIntegerField(db_column='Orden')  # Field name made lowercase.
    descuento = models.DecimalField(db_column='Descuento', max_digits=19, decimal_places=4)  # Field name made lowercase.
    pungrupo = models.IntegerField(db_column='punGrupo', blank=True, null=True)  # Field name made lowercase.
    punfamilia = models.IntegerField(db_column='punFamilia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GcsCLIBonificaciones29122015'


class Gcssubdiario279(models.Model):
    punorden = models.AutoField(primary_key=True, db_column='PunOrden')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    dia = models.IntegerField(db_column='Dia', blank=True, null=True)  # Field name made lowercase.
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=3, blank=True, null=True)  # Field name made lowercase.
    comprobante = models.CharField(db_column='Comprobante', max_length=20, blank=True, null=True)  # Field name made lowercase.
    comprobanteorden = models.CharField(db_column='ComprobanteOrden', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nrocomprobante = models.CharField(db_column='NroComprobante', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tipoabc = models.CharField(db_column='TipoABC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    proveedor = models.CharField(db_column='Proveedor', max_length=120, blank=True, null=True)  # Field name made lowercase.
    cai = models.CharField(db_column='CAI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cuit = models.CharField(db_column='CUIT', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gravado = models.DecimalField(db_column='Gravado', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    iva = models.DecimalField(db_column='Iva', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    exentoynoresp = models.DecimalField(db_column='ExentoYNoResp', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    respmonotributo = models.DecimalField(db_column='RespMonotributo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    percepcioniva = models.DecimalField(db_column='PercepcionIVA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    percepcionib = models.DecimalField(db_column='PercepcionIB', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totgral = models.DecimalField(db_column='TotGral', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    orden = models.IntegerField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa', blank=True, null=True)  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='PunProveedor', blank=True, null=True)  # Field name made lowercase.
    tipoprov = models.SmallIntegerField(db_column='TipoProv', blank=True, null=True)  # Field name made lowercase.
    puntipoiva = models.IntegerField(db_column='PunTipoIVA', blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tipoimporte = models.SmallIntegerField(db_column='TipoImporte', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GcsSubdiario279'


class Generaltmp(models.Model):
    idoperacion = models.IntegerField(db_column='IdOperacion')  # Field name made lowercase.
    puntero = models.IntegerField(db_column='Puntero')  # Field name made lowercase.
    dato = models.IntegerField(db_column='Dato', blank=True, null=True)  # Field name made lowercase.
    peso = models.FloatField(db_column='Peso', blank=True, null=True)  # Field name made lowercase.
    dato2 = models.IntegerField(db_column='Dato2', blank=True, null=True)  # Field name made lowercase.
    dato3 = models.IntegerField(db_column='Dato3', blank=True, null=True)  # Field name made lowercase.
    dato4 = models.FloatField(db_column='Dato4', blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GeneralTMP'


class Gruposarticulos(models.Model):
    pungrupo = models.AutoField(primary_key=True, db_column='PunGrupo')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=4)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GruposArticulos'


class Gruposinsumos(models.Model):
    pungrupo = models.AutoField(primary_key=True, db_column='PunGrupo')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=4)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GruposInsumos'


class Helpid(models.Model):
    form = models.CharField(db_column='Form', max_length=50)  # Field name made lowercase.
    control = models.CharField(db_column='Control', max_length=50)  # Field name made lowercase.
    helpcontextid = models.IntegerField(db_column='HelpContextID')  # Field name made lowercase.
    punmenu = models.IntegerField(db_column='PunMenu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HelpID'


class Hojarutacot(models.Model):
    punhojarutacot = models.AutoField(primary_key=True, db_column='PunHojaRutaCOT')  # Field name made lowercase.
    numero = models.IntegerField(db_column='Numero', blank=True, null=True)  # Field name made lowercase.
    punresponsable = models.IntegerField(db_column='PunResponsable', blank=True, null=True)  # Field name made lowercase.
    puntero = models.IntegerField(db_column='Puntero', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    pesototal = models.DecimalField(db_column='PesoTotal', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valortotal = models.DecimalField(db_column='ValorTotal', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    requierecot = models.BooleanField(db_column='RequiereCOT', blank=True, null=True)  # Field name made lowercase.
    fechasalida = models.DateTimeField(db_column='FechaSalida', blank=True, null=True)  # Field name made lowercase.
    fechavto = models.DateTimeField(db_column='FechaVto', blank=True, null=True)  # Field name made lowercase.
    punterokmsrecorrido = models.IntegerField(db_column='PunteroKmsRecorrido', blank=True, null=True)  # Field name made lowercase.
    statuscot = models.SmallIntegerField(db_column='StatusCOT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HojaRutaCOT'


class Idoperacion(models.Model):
    idoperacion = models.AutoField(primary_key=True, db_column='IDOperacion')  # Field name made lowercase.
    campo = models.CharField(db_column='Campo', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IDOperacion'


class Idclitransferenciainterna(models.Model):
    idclitransferenciainterna = models.AutoField(primary_key=True, db_column='IdCLITransferenciaInterna')  # Field name made lowercase.
    foo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IdCLITransferenciaInterna'


class Idtransferenciainterna(models.Model):
    idtransferenciainterna = models.IntegerField(db_column='IdTransferenciaInterna')  # Field name made lowercase.
    f = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'IdTransferenciaInterna'


class Impresorassistema(models.Model):
    idimpresora = models.AutoField(primary_key=True, db_column='IdImpresora')  # Field name made lowercase.
    etiqueta = models.CharField(db_column='Etiqueta', max_length=50, blank=True, null=True)  # Field name made lowercase.
    impresora = models.CharField(db_column='Impresora', max_length=255, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    usabandejas = models.SmallIntegerField(db_column='UsaBandejas', blank=True, null=True)  # Field name made lowercase.
    bandeja1 = models.SmallIntegerField(db_column='Bandeja1', blank=True, null=True)  # Field name made lowercase.
    bandeja2 = models.SmallIntegerField(db_column='Bandeja2', blank=True, null=True)  # Field name made lowercase.
    bandeja3 = models.SmallIntegerField(db_column='Bandeja3', blank=True, null=True)  # Field name made lowercase.
    bandeja4 = models.SmallIntegerField(db_column='Bandeja4', blank=True, null=True)  # Field name made lowercase.
    bandeja5 = models.SmallIntegerField(db_column='Bandeja5', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ImpresorasSistema'


class Indicesinflacion(models.Model):
    punindice = models.AutoField(primary_key=True, db_column='PunIndice')  # Field name made lowercase.
    punejercicio = models.IntegerField(db_column='PunEjercicio')  # Field name made lowercase.
    anio = models.IntegerField(db_column='Anio')  # Field name made lowercase.
    mes = models.SmallIntegerField(db_column='Mes')  # Field name made lowercase.
    indice = models.DecimalField(db_column='Indice', max_digits=15, decimal_places=4)  # Field name made lowercase.
    coeficiente = models.FloatField(db_column='Coeficiente', blank=True, null=True)  # Field name made lowercase.
    variacion = models.DecimalField(db_column='Variacion', max_digits=15, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IndicesInflacion'


class Indicesinflaciontmp(models.Model):
    idoperacion = models.IntegerField(db_column='IdOperacion')  # Field name made lowercase.
    punindice = models.IntegerField(db_column='PunIndice')  # Field name made lowercase.
    punejercicio = models.IntegerField(db_column='PunEjercicio')  # Field name made lowercase.
    anio = models.IntegerField(db_column='Anio')  # Field name made lowercase.
    mes = models.SmallIntegerField(db_column='Mes')  # Field name made lowercase.
    indice = models.DecimalField(db_column='Indice', max_digits=15, decimal_places=4)  # Field name made lowercase.
    coeficiente = models.FloatField(db_column='Coeficiente', blank=True, null=True)  # Field name made lowercase.
    variacion = models.DecimalField(db_column='Variacion', max_digits=15, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IndicesInflacionTMP'


class Indicesrevaluo(models.Model):
    punindice = models.AutoField(primary_key=True, db_column='PunIndice')  # Field name made lowercase.
    anio = models.IntegerField(db_column='Anio')  # Field name made lowercase.
    mes = models.SmallIntegerField(db_column='Mes')  # Field name made lowercase.
    indice = models.DecimalField(db_column='Indice', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IndicesRevaluo'


class Ingresosbrutostmp(models.Model):
    idoperacion = models.IntegerField(db_column='IdOperacion')  # Field name made lowercase.
    punjurisdiccion = models.IntegerField(db_column='PunJurisdiccion')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punmoneda = models.CharField(db_column='punMoneda', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IngresosBrutosTMP'


class Inspeccionrecepcioncontroles(models.Model):
    puninspeccioncontrol = models.AutoField(primary_key=True, db_column='PunInspeccionControl')  # Field name made lowercase.
    punsubclasificacion = models.IntegerField(db_column='PunSubClasificacion', blank=True, null=True)  # Field name made lowercase.
    caracteristica = models.CharField(db_column='Caracteristica', max_length=100, blank=True, null=True)  # Field name made lowercase.
    referencia = models.CharField(db_column='Referencia', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InspeccionRecepcionControles'


class Insumos(models.Model):
    puninsumo = models.AutoField(primary_key=True, db_column='PunInsumo')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=12, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150)  # Field name made lowercase.
    punrubro = models.IntegerField(db_column='PunRubro')  # Field name made lowercase.
    punfamilia = models.IntegerField(db_column='PunFamilia')  # Field name made lowercase.
    pungrupo = models.IntegerField(db_column='PunGrupo')  # Field name made lowercase.
    origen = models.SmallIntegerField(db_column='Origen')  # Field name made lowercase.
    tipo = models.SmallIntegerField(db_column='Tipo')  # Field name made lowercase.
    cuentacompra = models.CharField(db_column='CuentaCompra', max_length=9)  # Field name made lowercase.
    cuentaventa = models.CharField(db_column='CuentaVenta', max_length=9)  # Field name made lowercase.
    pununidad = models.IntegerField(db_column='PunUnidad')  # Field name made lowercase.
    stockminimo = models.DecimalField(db_column='StockMinimo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    stockcritico = models.DecimalField(db_column='StockCritico', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    stockmaximo = models.DecimalField(db_column='StockMaximo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    critico = models.SmallIntegerField(db_column='Critico', blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    tiemporeposicion = models.DateTimeField(db_column='TiempoReposicion', blank=True, null=True)  # Field name made lowercase.
    puntipompse = models.IntegerField(db_column='punTipoMPSE', blank=True, null=True)  # Field name made lowercase.
    posicionarancelaria = models.CharField(db_column='PosicionArancelaria', max_length=13, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Insumos'


class Intercompany(models.Model):
    punintercomp = models.AutoField(primary_key=True, db_column='PunInterComp')  # Field name made lowercase.
    prefijo = models.CharField(db_column='Prefijo', max_length=4)  # Field name made lowercase.
    sufijo = models.CharField(db_column='Sufijo', max_length=8)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    punasiento = models.IntegerField(db_column='PunAsiento')  # Field name made lowercase.
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InterCompany'


class Intercompanydet(models.Model):
    punintercomp = models.IntegerField(db_column='PunInterComp')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    punorigen = models.IntegerField(db_column='PunOrigen')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    punasiento = models.IntegerField(db_column='PunAsiento')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InterCompanyDet'


class Itemsdevoluciontmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion', blank=True, null=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    punremito = models.IntegerField(db_column='PunRemito', blank=True, null=True)  # Field name made lowercase.
    punpedido = models.IntegerField(db_column='PunPedido', blank=True, null=True)  # Field name made lowercase.
    punitempedido = models.IntegerField(db_column='PunItemPedido', blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    cantidadadevolver = models.DecimalField(db_column='CantidadADevolver', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    preciounitario = models.DecimalField(db_column='PrecioUnitario', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda', blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bonificacionpedido = models.DecimalField(db_column='bonificacionPedido', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    preciooriginal = models.DecimalField(db_column='PrecioOriginal', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tipoenvio = models.SmallIntegerField(db_column='TipoEnvio', blank=True, null=True)  # Field name made lowercase.
    porcentajeiva = models.DecimalField(db_column='PorcentajeIva', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punremitoitemventa = models.IntegerField(db_column='PunRemitoItemVenta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ItemsDevolucionTMP'


class Jurisdicciontipopadron(models.Model):
    punjurisdiccion = models.IntegerField(db_column='PunJurisdiccion', blank=True, null=True)  # Field name made lowercase.
    tiporegimen = models.SmallIntegerField(db_column='TipoRegimen')  # Field name made lowercase.
    puntipopadroniibb = models.SmallIntegerField(db_column='PunTipoPadronIIBB')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JurisdiccionTipoPadron'


class Jurisdiccionescmtmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion', blank=True, null=True)  # Field name made lowercase.
    punjurisdiccionib = models.IntegerField(db_column='PunJurisdiccionIB', blank=True, null=True)  # Field name made lowercase.
    exencion = models.BooleanField(db_column='Exencion', blank=True, null=True)  # Field name made lowercase.
    fechadesde = models.DateTimeField(db_column='FechaDesde', blank=True, null=True)  # Field name made lowercase.
    fechahasta = models.DateTimeField(db_column='FechaHasta', blank=True, null=True)  # Field name made lowercase.
    punconcepto = models.IntegerField(db_column='PunConcepto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JurisdiccionesCMTMP'


class Jurisdiccionesconceptosib(models.Model):
    punjurisdiccionib = models.IntegerField(db_column='PunJurisdiccionIB')  # Field name made lowercase.
    punconcepto = models.IntegerField(db_column='PunConcepto')  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=19, decimal_places=4)  # Field name made lowercase.
    codigoafip = models.CharField(db_column='CodigoAfip', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JurisdiccionesConceptosIB'


class Jurisdiccionesib(models.Model):
    punjurisdiccionib = models.AutoField(primary_key=True, db_column='PunJurisdiccionIB')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado')  # Field name made lowercase.
    porcentajenoinsc = models.DecimalField(db_column='PorcentajeNoInsc', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    minimoaretener = models.DecimalField(db_column='MinimoARetener', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    minimoretencion = models.DecimalField(db_column='MinimoRetencion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    codigoafip = models.CharField(db_column='CodigoAfip', max_length=3, blank=True, null=True)  # Field name made lowercase.
    usapadron = models.SmallIntegerField(db_column='UsaPadron', blank=True, null=True)  # Field name made lowercase.
    cuentapercepcionib = models.CharField(db_column='CuentaPercepcionIB', max_length=9, blank=True, null=True)  # Field name made lowercase.
    cuentaretencionib = models.CharField(db_column='CuentaRetencionIB', max_length=9, blank=True, null=True)  # Field name made lowercase.
    padronseparado = models.SmallIntegerField(db_column='PadronSeparado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JurisdiccionesIB'


class Lineasproduccion(models.Model):
    punlineaproduccion = models.AutoField(db_column='PunLineaProduccion', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LineasProduccion'


class Liquidaciondetalle(models.Model):
    cuit = models.CharField(db_column='CUIT', max_length=15, blank=True, null=True)  # Field name made lowercase.
    profesional = models.CharField(db_column='Profesional', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tipoiva = models.IntegerField(db_column='TipoIVA', blank=True, null=True)  # Field name made lowercase.
    codgan = models.IntegerField(db_column='CodGan', blank=True, null=True)  # Field name made lowercase.
    exento = models.DecimalField(db_column='Exento', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    gravado = models.DecimalField(db_column='Gravado', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    obrasocial = models.IntegerField(db_column='ObraSocial', blank=True, null=True)  # Field name made lowercase.
    punprofesional = models.IntegerField(db_column='PunProfesional', blank=True, null=True)  # Field name made lowercase.
    acredita = models.CharField(db_column='Acredita', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nroliquida = models.CharField(db_column='NroLiquida', max_length=8, blank=True, null=True)  # Field name made lowercase.
    poriva = models.DecimalField(db_column='PorIVa', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    retgan = models.DecimalField(db_column='RetGan', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punbanco = models.IntegerField(db_column='PunBanco', blank=True, null=True)  # Field name made lowercase.
    punchequera = models.IntegerField(db_column='PunChequera', blank=True, null=True)  # Field name made lowercase.
    nrocheque = models.IntegerField(db_column='NroCheque', blank=True, null=True)  # Field name made lowercase.
    fechacheque = models.DateTimeField(db_column='FechaCheque', blank=True, null=True)  # Field name made lowercase.
    fechadiferido = models.DateTimeField(db_column='FechaDiferido', blank=True, null=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda', blank=True, null=True)  # Field name made lowercase.
    fechaproceso = models.DateTimeField(db_column='FechaProceso', blank=True, null=True)  # Field name made lowercase.
    monto = models.DecimalField(db_column='Monto', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nroretigan = models.IntegerField(db_column='NroRetigan', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    saldo = models.DecimalField(db_column='Saldo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    retiva = models.DecimalField(db_column='RetIva', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    retib = models.DecimalField(db_column='RetIB', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nombreos = models.CharField(db_column='NombreOS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punprovincia = models.IntegerField(db_column='PunProvincia', blank=True, null=True)  # Field name made lowercase.
    importeretib = models.DecimalField(db_column='ImporteRetIB', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LiquidacionDetalle'


class Listaprecioarticulotmp(models.Model):
    idoperacion = models.IntegerField(db_column='idOperacion', blank=True, null=True)  # Field name made lowercase.
    punlista = models.IntegerField(db_column='punLista', blank=True, null=True)  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='punMoneda', blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='punArticulo', blank=True, null=True)  # Field name made lowercase.
    punprecio = models.IntegerField(db_column='PunPrecio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ListaPrecioArticuloTMP'


class Listaprecioarticulos(models.Model):
    punprecio = models.AutoField(primary_key=True, db_column='PunPrecio')  # Field name made lowercase.
    punlista = models.IntegerField(db_column='PunLista')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fechamodificacion = models.DateTimeField(db_column='FechaModificacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ListaPrecioArticulos'


class Listaprecioarticulosleo(models.Model):
    punprecio = models.IntegerField(db_column='PunPrecio')  # Field name made lowercase.
    punlista = models.IntegerField(db_column='PunLista')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ListaPrecioArticulosLeo'


class Listaprecioarticulosmal(models.Model):
    punprecio = models.AutoField(primary_key=True, db_column='PunPrecio')  # Field name made lowercase.
    punlista = models.IntegerField(db_column='PunLista')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ListaPrecioArticulosMal'


class Listaprecios(models.Model):
    punlista = models.AutoField(primary_key=True, db_column='PunLista')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    tipo = models.SmallIntegerField(db_column='Tipo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ListaPrecios'


class Localidadesnew(models.Model):
    punlocalidad = models.AutoField(primary_key=True, db_column='PunLocalidad')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    punlocalidadstarcom = models.IntegerField(db_column='PunLocalidadStarcom', blank=True, null=True)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    punprovincia = models.IntegerField(db_column='punProvincia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Localidadesnew'


class Log(models.Model):
    punusuario = models.IntegerField(db_column='PunUsuario')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    punaccion = models.IntegerField(db_column='PunAccion')  # Field name made lowercase.
    programa = models.CharField(db_column='Programa', max_length=100, blank=True, null=True)  # Field name made lowercase.
    puntero = models.IntegerField(db_column='Puntero', blank=True, null=True)  # Field name made lowercase.
    punteroc = models.CharField(db_column='PunteroC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tablapuntero = models.CharField(db_column='TablaPuntero', max_length=50, blank=True, null=True)  # Field name made lowercase.
    campopuntero = models.CharField(db_column='CampoPuntero', max_length=50, blank=True, null=True)  # Field name made lowercase.
    punorigen = models.IntegerField(db_column='PunOrigen', blank=True, null=True)  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa', blank=True, null=True)  # Field name made lowercase.
    punasiento = models.IntegerField(db_column='PunAsiento', blank=True, null=True)  # Field name made lowercase.
    storep = models.CharField(db_column='StoreP', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    detalle = models.CharField(db_column='Detalle', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    empresa = models.SmallIntegerField(db_column='Empresa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Log'


class Logacciones(models.Model):
    punaccion = models.IntegerField(db_column='PunAccion')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.
    adescripcion = models.CharField(db_column='ADescripcion', max_length=1)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LogAcciones'


class Logenvioreclamodeuda(models.Model):
    puncliente = models.IntegerField(db_column='PunCLiente', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LogEnvioReclamoDeuda'


class Logpedidostmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    cfecha = models.CharField(db_column='cFecha', max_length=10, blank=True, null=True)  # Field name made lowercase.
    hora = models.CharField(db_column='Hora', max_length=5, blank=True, null=True)  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='PunUsuario', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=500, blank=True, null=True)  # Field name made lowercase.
    punpedido = models.IntegerField(db_column='PunPedido', blank=True, null=True)  # Field name made lowercase.
    punitempedido = models.IntegerField(db_column='PunItemPedido', blank=True, null=True)  # Field name made lowercase.
    codigoarticulo = models.CharField(db_column='CodigoArticulo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    articulo = models.CharField(db_column='Articulo', max_length=500, blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    puncampo = models.IntegerField(db_column='PunCampo', blank=True, null=True)  # Field name made lowercase.
    dato = models.CharField(db_column='Dato', max_length=500, blank=True, null=True)  # Field name made lowercase.
    valoranterior = models.CharField(db_column='ValorAnterior', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    valornuevo = models.CharField(db_column='ValorNuevo', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    punvariacion = models.IntegerField(db_column='PunVariacion', blank=True, null=True)  # Field name made lowercase.
    camporelacionado = models.SmallIntegerField(db_column='CampoRelacionado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LogPedidosTMP'


class Logtextostmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion', blank=True, null=True)  # Field name made lowercase.
    texto = models.CharField(db_column='Texto', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LogTextosTMP'


class MailingcategoriaReportes(models.Model):
    puncategoria = models.OneToOneField('Mailingcategorias', models.DO_NOTHING, db_column='PunCategoria', primary_key=True)  # Field name made lowercase. The composite primary key (PunCategoria, PunReporte) found, that is not supported. The first column is selected.
    punreporte = models.ForeignKey('Mailingreportes', models.DO_NOTHING, db_column='PunReporte')  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MailingCategoria_Reportes'
        unique_together = (('puncategoria', 'punreporte'),)


class MailingcategoriaReportestmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    puncategoria = models.IntegerField(db_column='PunCategoria', blank=True, null=True)  # Field name made lowercase.
    punreporte = models.IntegerField(db_column='PunReporte', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MailingCategoria_ReportesTMP'


class MailingcategoriaUsuarioVendedores(models.Model):
    puncategoriausuario = models.IntegerField(db_column='PunCategoriaUsuario')  # Field name made lowercase.
    punvendedor = models.IntegerField(db_column='PunVendedor')  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MailingCategoria_Usuario_Vendedores'


class MailingcategoriaUsuarioVendedorestmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    puncategoriausuario = models.IntegerField(db_column='PunCategoriaUsuario', blank=True, null=True)  # Field name made lowercase.
    punvendedor = models.IntegerField(db_column='PunVendedor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MailingCategoria_Usuario_VendedoresTMP'


class MailingcategoriaUsuarios(models.Model):
    puncategoriausuario = models.AutoField(primary_key=True, db_column='PunCategoriaUsuario')  # Field name made lowercase.
    puncategoria = models.ForeignKey('Mailingcategorias', models.DO_NOTHING, db_column='PunCategoria')  # Field name made lowercase.
    punusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='PunUsuario', blank=True, null=True)  # Field name made lowercase.
    destinatario = models.CharField(db_column='Destinatario', max_length=50, blank=True, null=True)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MailingCategoria_Usuarios'
        unique_together = (('puncategoria', 'punusuario', 'destinatario'),)


class MailingcategoriaUsuariostmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion', blank=True, null=True)  # Field name made lowercase.
    idoperacion2 = models.IntegerField(db_column='IDOperacion2', blank=True, null=True)  # Field name made lowercase.
    puncategoria = models.IntegerField(db_column='PunCategoria', blank=True, null=True)  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='PunUsuario', blank=True, null=True)  # Field name made lowercase.
    destinatario = models.CharField(db_column='Destinatario', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MailingCategoria_UsuariosTMP'


class Mailingcategorias(models.Model):
    puncategoria = models.AutoField(db_column='PunCategoria', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    punperiodo = models.ForeignKey('Mailingperiodos', models.DO_NOTHING, db_column='PunPeriodo')  # Field name made lowercase.
    factorperiodo = models.SmallIntegerField(db_column='FactorPeriodo')  # Field name made lowercase.
    diames = models.SmallIntegerField(db_column='DiaMes', blank=True, null=True)  # Field name made lowercase.
    diasem = models.CharField(db_column='DiaSem', max_length=20, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=500, blank=True, null=True)  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='PunUsuario')  # Field name made lowercase.
    habilitado = models.SmallIntegerField(db_column='Habilitado')  # Field name made lowercase.
    fechainicio = models.DateTimeField(db_column='FechaInicio')  # Field name made lowercase.
    fechafin = models.DateTimeField(db_column='FechaFin', blank=True, null=True)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MailingCategorias'


class Mailingeventos(models.Model):
    punevento = models.AutoField(db_column='PunEvento', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MailingEventos'


class Mailingnotificaciones(models.Model):
    puncategoria = models.ForeignKey(Mailingcategorias, models.DO_NOTHING, db_column='PunCategoria')  # Field name made lowercase.
    punevento = models.ForeignKey(Mailingeventos, models.DO_NOTHING, db_column='PunEvento')  # Field name made lowercase.
    punusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='PunUsuario', blank=True, null=True)  # Field name made lowercase.
    destinatario = models.CharField(db_column='Destinatario', max_length=50, blank=True, null=True)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MailingNotificaciones'
        unique_together = (('puncategoria', 'punusuario', 'destinatario'),)


class Mailingnotificacionestmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion', blank=True, null=True)  # Field name made lowercase.
    puncategoria = models.IntegerField(db_column='PunCategoria', blank=True, null=True)  # Field name made lowercase.
    punevento = models.IntegerField(db_column='PunEvento', blank=True, null=True)  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='PunUsuario', blank=True, null=True)  # Field name made lowercase.
    destinatario = models.CharField(db_column='Destinatario', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MailingNotificacionesTMP'


class Mailingperiodos(models.Model):
    punperiodo = models.AutoField(db_column='PunPeriodo', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MailingPeriodos'


class Mailingreportes(models.Model):
    punreporte = models.AutoField(db_column='PunReporte', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    storedprocedure = models.CharField(db_column='StoredProcedure', max_length=50, blank=True, null=True)  # Field name made lowercase.
    templatexls = models.CharField(db_column='TemplateXLS', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MailingReportes'


class Maquina(models.Model):
    punmaquina = models.AutoField(db_column='PunMaquina', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=20)  # Field name made lowercase.
    codigobarras = models.CharField(db_column='CodigoBarras', max_length=50, blank=True, null=True)  # Field name made lowercase.
    punsector = models.IntegerField(db_column='PunSector')  # Field name made lowercase.
    punmodelo = models.IntegerField(db_column='PunModelo')  # Field name made lowercase.
    fechaingreso = models.DateTimeField(db_column='FechaIngreso')  # Field name made lowercase.
    fechaegreso = models.DateTimeField(db_column='FechaEgreso', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=255, blank=True, null=True)  # Field name made lowercase.
    critico = models.BooleanField(db_column='Critico')  # Field name made lowercase.
    fechacompra = models.DateTimeField(db_column='FechaCompra', blank=True, null=True)  # Field name made lowercase.
    fechaventa = models.DateTimeField(db_column='FechaVenta', blank=True, null=True)  # Field name made lowercase.
    valorcompra = models.DecimalField(db_column='ValorCompra', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valorventa = models.DecimalField(db_column='ValorVenta', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punmonedacompra = models.IntegerField(db_column='PunMonedaCompra', blank=True, null=True)  # Field name made lowercase.
    punmonedaventa = models.IntegerField(db_column='PunMonedaVenta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Maquina'


class Maquinamarca(models.Model):
    punmarca = models.AutoField(db_column='punMarca', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MaquinaMarca'


class Maquinamodelo(models.Model):
    punmodelo = models.AutoField(db_column='PunModelo', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punmarca = models.ForeignKey(Maquinamarca, models.DO_NOTHING, db_column='PunMarca', blank=True, null=True)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MaquinaModelo'


class Maquinamodelostmp(models.Model):
    punmodelo = models.IntegerField(db_column='PunModelo', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punmarca = models.IntegerField(db_column='PunMarca', blank=True, null=True)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    modoabm = models.IntegerField(db_column='ModoAbm', blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.BigIntegerField(db_column='idOperacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MaquinaModelosTMP'


class Maquinaoperacion(models.Model):
    punmaquinaoperacion = models.AutoField(db_column='PunMaquinaOperacion', primary_key=True)  # Field name made lowercase.
    punmaquina = models.IntegerField(db_column='PunMaquina')  # Field name made lowercase.
    punoperacion = models.ForeignKey('Operacion', models.DO_NOTHING, db_column='PunOperacion')  # Field name made lowercase.
    valorhora = models.DecimalField(db_column='ValorHora', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda', blank=True, null=True)  # Field name made lowercase.
    fechadesde = models.DateTimeField(db_column='FechaDesde')  # Field name made lowercase.
    fechahasta = models.DateTimeField(db_column='FechaHasta', blank=True, null=True)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MaquinaOperacion'


class Maquinaoperacionestmp(models.Model):
    punmaquinaoper = models.IntegerField(db_column='PunMaquinaOper', blank=True, null=True)  # Field name made lowercase.
    punmaquina = models.IntegerField(db_column='PunMaquina', blank=True, null=True)  # Field name made lowercase.
    punoperacion = models.IntegerField(db_column='PunOperacion', blank=True, null=True)  # Field name made lowercase.
    valorhora = models.DecimalField(db_column='ValorHora', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda', blank=True, null=True)  # Field name made lowercase.
    fechadesde = models.DateTimeField(db_column='FechaDesde', blank=True, null=True)  # Field name made lowercase.
    fechahasta = models.DateTimeField(db_column='FechaHasta', blank=True, null=True)  # Field name made lowercase.
    modoabm = models.IntegerField(db_column='ModoAbm', blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.BigIntegerField(db_column='idOperacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MaquinaOperacionesTMP'


class Mensaje(models.Model):
    punmensaje = models.AutoField(db_column='PunMensaje', primary_key=True)  # Field name made lowercase.
    mensaje = models.CharField(db_column='Mensaje', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    puntipoaviso = models.ForeignKey('Tipoaviso', models.DO_NOTHING, db_column='PunTipoAviso')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mensaje'


class Mensajedestinatario(models.Model):
    punmensaje = models.ForeignKey(Mensaje, models.DO_NOTHING, db_column='PunMensaje')  # Field name made lowercase.
    punusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='PunUsuario', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fechaleido = models.DateTimeField(db_column='FechaLeido', blank=True, null=True)  # Field name made lowercase.
    hostleido = models.CharField(db_column='HostLeido', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.ForeignKey('Hcstatusmensajedestinatario', models.DO_NOTHING, db_column='Status')  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MensajeDestinatario'
        unique_together = (('punmensaje', 'punusuario', 'email'),)


class Menu(models.Model):
    punmenu = models.IntegerField(db_column='PunMenu', primary_key=True)  # Field name made lowercase.
    punmenupadre = models.IntegerField(db_column='PunMenuPadre', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=60, blank=True, null=True)  # Field name made lowercase.
    permisos = models.IntegerField(db_column='Permisos', blank=True, null=True)  # Field name made lowercase.
    indice = models.SmallIntegerField(db_column='Indice', blank=True, null=True)  # Field name made lowercase.
    nombremenu = models.CharField(db_column='NombreMenu', max_length=60, blank=True, null=True)  # Field name made lowercase.
    nivel = models.IntegerField(db_column='Nivel', blank=True, null=True)  # Field name made lowercase.
    punsistema = models.IntegerField(db_column='PunSistema')  # Field name made lowercase.
    form = models.CharField(db_column='Form', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Menu'


class Menupermisosespeciales(models.Model):
    punitem = models.IntegerField(db_column='PunItem', primary_key=True)  # Field name made lowercase.
    punmenu = models.IntegerField(db_column='PunMenu')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MenuPermisosEspeciales'


class Menutmp(models.Model):
    idoperacion = models.IntegerField(db_column='IdOperacion', blank=True, null=True)  # Field name made lowercase.
    nivel = models.IntegerField(db_column='Nivel', blank=True, null=True)  # Field name made lowercase.
    punmenupadre = models.IntegerField(db_column='PunMenuPadre', blank=True, null=True)  # Field name made lowercase.
    nombremenupadre = models.CharField(db_column='NombreMenuPadre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    indicemenupadre = models.IntegerField(db_column='IndiceMenuPadre', blank=True, null=True)  # Field name made lowercase.
    punmenu = models.IntegerField(db_column='PunMenu', blank=True, null=True)  # Field name made lowercase.
    nombremenu = models.CharField(db_column='NombreMenu', max_length=100, blank=True, null=True)  # Field name made lowercase.
    indice = models.IntegerField(db_column='Indice', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    permisosusuario = models.IntegerField(db_column='PermisosUsuario', blank=True, null=True)  # Field name made lowercase.
    permisosmenu = models.IntegerField(db_column='PermisosMenu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MenuTMP'


class Menup(models.Model):
    punmenu = models.IntegerField(db_column='PunMenu')  # Field name made lowercase.
    punmenupadre = models.IntegerField(db_column='PunMenuPadre', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=60, blank=True, null=True)  # Field name made lowercase.
    permisos = models.IntegerField(db_column='Permisos', blank=True, null=True)  # Field name made lowercase.
    indice = models.SmallIntegerField(db_column='Indice', blank=True, null=True)  # Field name made lowercase.
    nombremenu = models.CharField(db_column='NombreMenu', max_length=60, blank=True, null=True)  # Field name made lowercase.
    nivel = models.IntegerField(db_column='Nivel', blank=True, null=True)  # Field name made lowercase.
    punsistema = models.IntegerField(db_column='PunSistema')  # Field name made lowercase.
    form = models.CharField(db_column='Form', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Menup'


class Minutosmaquina(models.Model):
    codigo = models.IntegerField(db_column='Codigo', blank=True, null=True)  # Field name made lowercase.
    punmaquina = models.IntegerField(db_column='PunMaquina', blank=True, null=True)  # Field name made lowercase.
    mes01 = models.IntegerField(db_column='Mes01', blank=True, null=True)  # Field name made lowercase.
    mes02 = models.IntegerField(db_column='Mes02', blank=True, null=True)  # Field name made lowercase.
    mes03 = models.IntegerField(db_column='Mes03', blank=True, null=True)  # Field name made lowercase.
    mes04 = models.IntegerField(db_column='Mes04', blank=True, null=True)  # Field name made lowercase.
    mes05 = models.IntegerField(db_column='Mes05', blank=True, null=True)  # Field name made lowercase.
    mes06 = models.IntegerField(db_column='Mes06', blank=True, null=True)  # Field name made lowercase.
    mes07 = models.IntegerField(db_column='Mes07', blank=True, null=True)  # Field name made lowercase.
    mes08 = models.IntegerField(db_column='Mes08', blank=True, null=True)  # Field name made lowercase.
    mes09 = models.IntegerField(db_column='Mes09', blank=True, null=True)  # Field name made lowercase.
    mes10 = models.IntegerField(db_column='Mes10', blank=True, null=True)  # Field name made lowercase.
    mes11 = models.IntegerField(db_column='Mes11', blank=True, null=True)  # Field name made lowercase.
    mes12 = models.IntegerField(db_column='Mes12', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MinutosMaquina'


class Modifcevencimientostmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDoperacion', blank=True, null=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunCOmprobante', blank=True, null=True)  # Field name made lowercase.
    fechavencimiento = models.DateTimeField(db_column='FechaVEncimiento', blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ModifCeVencimientosTMP'


class Modulos(models.Model):
    punmodulo = models.IntegerField(db_column='punModulo', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    valor = models.SmallIntegerField(db_column='Valor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Modulos'


class Monedas(models.Model):
    punmoneda = models.AutoField(primary_key=True, db_column='PunMoneda')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cuenta = models.CharField(db_column='Cuenta', max_length=9, blank=True, null=True)  # Field name made lowercase.
    impuestochq = models.SmallIntegerField(db_column='ImpuestoChq', blank=True, null=True)  # Field name made lowercase.
    cuentaff = models.CharField(db_column='CuentaFF', max_length=9, blank=True, null=True)  # Field name made lowercase.
    simbolo = models.CharField(db_column='Simbolo', max_length=5, blank=True, null=True)  # Field name made lowercase.
    afipcodigo = models.CharField(db_column='AFIPCodigo', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cuentadifcaja = models.CharField(db_column='CuentaDifCaja', max_length=9, blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    cuentavaloresdepositar = models.CharField(db_column='CuentaValoresDepositar', max_length=9, blank=True, null=True)  # Field name made lowercase.
    descripcionsingular = models.CharField(db_column='DescripcionSingular', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Monedas'


class Motivorecepcion(models.Model):
    punmotivo = models.AutoField(primary_key=True, db_column='PunMotivo')  # Field name made lowercase.
    motivo = models.CharField(db_column='Motivo', max_length=150)  # Field name made lowercase.
    puntipoot = models.IntegerField(db_column='PunTipoOT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MotivoRecepcion'


class Motivosanulacionremitos(models.Model):
    punmotivo = models.AutoField(primary_key=True, db_column='punMotivo')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MotivosAnulacionRemitos'


class Motivoscambiofecha(models.Model):
    punmotivo = models.AutoField(primary_key=True, db_column='punMotivo')  # Field name made lowercase.
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    borrado = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MotivosCambioFecha'


class Motivosdeventregas(models.Model):
    punmotivo = models.AutoField(primary_key=True, db_column='PunMotivo')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MotivosDevEntregas'


class Movercashflow(models.Model):
    idoperacion = models.IntegerField(db_column='IdOperacion')  # Field name made lowercase.
    puncashflow = models.IntegerField(db_column='PunCashFlow')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MoverCashflow'


class Nomencladorcot(models.Model):
    codigo = models.CharField(db_column='Codigo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    codigounidad = models.SmallIntegerField(db_column='CodigoUnidad', blank=True, null=True)  # Field name made lowercase.
    final = models.BooleanField(db_column='Final', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NomencladorCOT'


class Notaenvio(models.Model):
    punnotaenvio = models.AutoField(db_column='PunNotaEnvio', primary_key=True)  # Field name made lowercase.
    prefijo = models.CharField(db_column='Prefijo', max_length=4)  # Field name made lowercase.
    sufijo = models.CharField(db_column='Sufijo', max_length=8)  # Field name made lowercase.
    fechaalta = models.DateTimeField(db_column='FechaAlta')  # Field name made lowercase.
    fechaenvio = models.DateTimeField(db_column='FechaEnvio')  # Field name made lowercase.
    fechaentrega = models.DateTimeField(db_column='FechaEntrega')  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='PunProveedor')  # Field name made lowercase.
    punordenc = models.IntegerField(db_column='PunOrdenC', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    fecharecepcion = models.DateTimeField(db_column='FechaRecepcion', blank=True, null=True)  # Field name made lowercase.
    remitoprefijo = models.CharField(db_column='RemitoPrefijo', max_length=4, blank=True, null=True)  # Field name made lowercase.
    remitosufijo = models.CharField(db_column='RemitoSufijo', max_length=8, blank=True, null=True)  # Field name made lowercase.
    facturaletra = models.CharField(db_column='FacturaLetra', max_length=1, blank=True, null=True)  # Field name made lowercase.
    facturaprefijo = models.CharField(db_column='FacturaPrefijo', max_length=4, blank=True, null=True)  # Field name made lowercase.
    facturasufijo = models.CharField(db_column='FacturaSufijo', max_length=8, blank=True, null=True)  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    bultos = models.IntegerField(db_column='Bultos', blank=True, null=True)  # Field name made lowercase.
    peso = models.DecimalField(db_column='Peso', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punoperario = models.IntegerField(db_column='PunOperario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NotaEnvio'


class Notaenvioitem(models.Model):
    punitemne = models.AutoField(db_column='PunItemNE', primary_key=True)  # Field name made lowercase.
    punnotaenvio = models.ForeignKey(Notaenvio, models.DO_NOTHING, db_column='PunNotaEnvio')  # Field name made lowercase.
    item = models.SmallIntegerField(db_column='Item')  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT')  # Field name made lowercase.
    cantidadenviada = models.DecimalField(db_column='CantidadEnviada', max_digits=19, decimal_places=4)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    cantidadrecibida = models.DecimalField(db_column='CantidadRecibida', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidadscrap = models.DecimalField(db_column='CantidadScrap', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NotaEnvioItem'


class Notaenvioitemservicio(models.Model):
    punitemservicio = models.AutoField(db_column='PunItemServicio', primary_key=True)  # Field name made lowercase.
    punitemne = models.ForeignKey(Notaenvioitem, models.DO_NOTHING, db_column='PunItemNE')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4)  # Field name made lowercase.
    pununidad = models.IntegerField(db_column='PunUnidad')  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda', blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    punitemoc = models.IntegerField(db_column='PunItemOC', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    punoperacion = models.IntegerField(db_column='PunOperacion', blank=True, null=True)  # Field name made lowercase.
    cantidadrecibida = models.DecimalField(db_column='CantidadRecibida', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NotaEnvioItemServicio'


# class Numret(models.Model):
#     origen = models.CharField(db_column='Origen', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     puntero = models.FloatField(blank=True, null=True)
#     fecha_field = models.DateTimeField(db_column='Fecha ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     nro_retenci├│n = models.CharField(db_column='Nro Retenci├│n', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     importe = models.FloatField(db_column='Importe', blank=True, null=True)  # Field name made lowercase.
#     nro_retencion_nuevo = models.FloatField(db_column='Nro Retencion NUEVO', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     f7 = models.CharField(db_column='F7', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     nrook = models.CharField(db_column='NroOk', max_length=10, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'NumRet'


class Numeroscomprobante(models.Model):
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tipoabc = models.CharField(db_column='TipoABC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    prefijo = models.CharField(db_column='Prefijo', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sufijo = models.CharField(db_column='Sufijo', max_length=8, blank=True, null=True)  # Field name made lowercase.
    puntipomph = models.IntegerField(db_column='PunTipoMPH', blank=True, null=True)  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa', blank=True, null=True)  # Field name made lowercase.
    pundistribuidor = models.IntegerField(db_column='PunDistribuidor', blank=True, null=True)  # Field name made lowercase.
    desfacturaelectronica = models.CharField(db_column='DesFacturaElectronica', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descripcionimpresion = models.CharField(db_column='DescripcionImpresion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pun = models.AutoField(primary_key=True, )
    puntodeventa = models.SmallIntegerField(db_column='PuntoDeVenta', blank=True, null=True)  # Field name made lowercase.
    facturaelectronica = models.BooleanField(db_column='FacturaElectronica', blank=True, null=True)  # Field name made lowercase.
    puntipowebservice = models.SmallIntegerField(db_column='PunTipoWebService', blank=True, null=True)  # Field name made lowercase.
    reportname = models.CharField(db_column='ReportName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fce = models.BooleanField(db_column='FCE', blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NumerosComprobante'


class Ocfacturadas(models.Model):
    punordenc = models.IntegerField(db_column='PunOrdenC')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    punorigen = models.IntegerField(db_column='PunOrigen')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OCFacturadas'


class Ocitems(models.Model):
    punitemoc = models.AutoField(primary_key=True, db_column='PunItemOC')  # Field name made lowercase.
    punordenc = models.IntegerField(db_column='PunOrdenC')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    puninsumo = models.IntegerField(db_column='PunInsumo', blank=True, null=True)  # Field name made lowercase.
    punbys = models.IntegerField(db_column='PunByS', blank=True, null=True)  # Field name made lowercase.
    fechaentrega = models.DateTimeField(db_column='FechaEntrega')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4)  # Field name made lowercase.
    pununidad = models.IntegerField(db_column='PunUnidad')  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    punitempres = models.IntegerField(db_column='PunItemPres')  # Field name made lowercase.
    punpedidocliente = models.IntegerField(db_column='PunPedidoCliente', blank=True, null=True)  # Field name made lowercase.
    porciva = models.DecimalField(db_column='PorcIva', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    item = models.IntegerField(db_column='Item', blank=True, null=True)  # Field name made lowercase.
    fecharecepcionestimada = models.DateTimeField(db_column='FechaRecepcionEstimada', blank=True, null=True)  # Field name made lowercase.
    observacionitem = models.CharField(db_column='ObservacionItem', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    djai = models.CharField(db_column='DJAI', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fechaconfirmacion = models.DateTimeField(db_column='FechaConfirmacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OCItems'


class Ocitemstmp(models.Model):
    punitemoc = models.IntegerField(db_column='PunItemOC', blank=True, null=True)  # Field name made lowercase.
    punordenc = models.IntegerField(db_column='PunOrdenC', blank=True, null=True)  # Field name made lowercase.
    puninsumo = models.IntegerField(db_column='PunInsumo', blank=True, null=True)  # Field name made lowercase.
    punbys = models.IntegerField(db_column='PunByS', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pununidad = models.IntegerField(db_column='PunUnidad', blank=True, null=True)  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='idOperacion')  # Field name made lowercase.
    punitempres = models.IntegerField(db_column='punItemPres', blank=True, null=True)  # Field name made lowercase.
    porciva = models.DecimalField(db_column='porcIva', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punitemreq = models.IntegerField(db_column='punItemReq', blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='punMoneda', blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fechaentrega = models.DateTimeField(db_column='FechaEntrega', blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='punArticulo', blank=True, null=True)  # Field name made lowercase.
    punpedidocliente = models.IntegerField(db_column='punPedidoCliente', blank=True, null=True)  # Field name made lowercase.
    cantidadfaltante = models.DecimalField(db_column='CantidadFaltante', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    item = models.IntegerField(db_column='Item', blank=True, null=True)  # Field name made lowercase.
    fecharecepcionestimada = models.DateTimeField(db_column='FechaRecepcionEstimada', blank=True, null=True)  # Field name made lowercase.
    observacionitem = models.CharField(db_column='ObservacionItem', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    djai = models.CharField(db_column='DJAI', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fechaconfirmacion = models.DateTimeField(db_column='FechaConfirmacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OCItemsTMP'


class Ofsf(models.Model):
    cant = models.FloatField(db_column='CANT', blank=True, null=True)  # Field name made lowercase.
    cierre = models.CharField(db_column='CIERRE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    codalt = models.CharField(db_column='CODALT', max_length=16, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OFSF'


class Orden(models.Model):
    cant = models.FloatField(db_column='CANT', blank=True, null=True)  # Field name made lowercase.
    codalt = models.CharField(db_column='CODALT', max_length=16, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ORDEN'


class Otafilado(models.Model):
    punordent = models.IntegerField(db_column='PunOrdenT')  # Field name made lowercase.
    puntipopieza = models.IntegerField(db_column='PunTipoPieza')  # Field name made lowercase.
    puntiporeparacion = models.IntegerField(db_column='PunTipoReparacion')  # Field name made lowercase.
    confirmacionventas = models.BooleanField(db_column='ConfirmacionVentas')  # Field name made lowercase.
    punaccion = models.IntegerField(db_column='PunAccion', blank=True, null=True)  # Field name made lowercase.
    puncausaaccion = models.IntegerField(db_column='PunCausaAccion', blank=True, null=True)  # Field name made lowercase.
    punrecepcion = models.IntegerField(db_column='PunRecepcion', blank=True, null=True)  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    respuestaventas = models.SmallIntegerField(db_column='RespuestaVentas', blank=True, null=True)  # Field name made lowercase.
    puntipoafilado = models.IntegerField(db_column='PunTipoAfilado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTAfilado'


class Otafiladopiezas(models.Model):
    punordent = models.IntegerField(db_column='PunOrdenT')  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTAfiladoPiezas'


class Otafiladorecepcion(models.Model):
    punrecepcion = models.AutoField(primary_key=True, db_column='PunRecepcion')  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    prefijoremito = models.CharField(db_column='PrefijoRemito', max_length=4)  # Field name made lowercase.
    sufijoremito = models.CharField(db_column='SufijoRemito', max_length=8)  # Field name made lowercase.
    cantidadpiezas = models.DecimalField(db_column='CantidadPiezas', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punmotivo = models.IntegerField(db_column='PunMotivo')  # Field name made lowercase.
    prefijo = models.CharField(db_column='Prefijo', max_length=4)  # Field name made lowercase.
    sufijo = models.CharField(db_column='Sufijo', max_length=8)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    fechacumplimiento = models.DateTimeField(db_column='FechaCumplimiento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTAfiladoRecepcion'


class Otauxcriterio(models.Model):
    puncriterio = models.AutoField(primary_key=True, db_column='PunCriterio')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTAuxCriterio'


class Otauxcriteriodetalle(models.Model):
    puncriteriodet = models.AutoField(primary_key=True, db_column='PunCriterioDet')  # Field name made lowercase.
    puncriterio = models.IntegerField(db_column='PunCriterio')  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT')  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTAuxCriterioDetalle'


class Otauxcriteriodetalletmp(models.Model):
    idoperacion = models.IntegerField(db_column='IdOperacion')  # Field name made lowercase.
    puncriterio = models.IntegerField(db_column='PunCriterio')  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT')  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTAuxCriterioDetalleTMP'


class Otauxiliarcierre(models.Model):
    punordent = models.IntegerField(db_column='PunOrdenT', blank=True, null=True)  # Field name made lowercase.
    cantidadminutos = models.IntegerField(db_column='CantidadMinutos', blank=True, null=True)  # Field name made lowercase.
    fechacierre = models.DateTimeField(db_column='FechaCierre', blank=True, null=True)  # Field name made lowercase.
    puntero = models.IntegerField(db_column='Puntero', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTAuxiliarCierre'


class Otauxiliarcierrepablo(models.Model):
    punordent = models.IntegerField(db_column='PunOrdenT', blank=True, null=True)  # Field name made lowercase.
    cantidadminutos = models.IntegerField(db_column='CantidadMinutos', blank=True, null=True)  # Field name made lowercase.
    fechacierre = models.DateTimeField(db_column='FechaCierre', blank=True, null=True)  # Field name made lowercase.
    puntero = models.IntegerField(db_column='Puntero', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTAuxiliarCierrePablo'


class Otaviso(models.Model):
    punotaviso = models.AutoField(db_column='punOTAviso', primary_key=True)  # Field name made lowercase.
    puncausaaviso = models.IntegerField(db_column='PunCausaAviso', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    punitempedido = models.IntegerField(db_column='PunItemPedido', blank=True, null=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT', blank=True, null=True)  # Field name made lowercase.
    punsectordestino = models.IntegerField(db_column='PunSectorDestino', blank=True, null=True)  # Field name made lowercase.
    instante = models.DateTimeField(db_column='Instante', blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    punremitoitem = models.IntegerField(db_column='punRemitoitem', blank=True, null=True)  # Field name made lowercase.
    punrecepcion = models.IntegerField(db_column='punRecepcion', blank=True, null=True)  # Field name made lowercase.
    fecharechazo = models.DateTimeField(db_column='FechaRechazo', blank=True, null=True)  # Field name made lowercase.
    motivorechazo = models.CharField(db_column='MotivoRechazo', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    punusuariomodif = models.IntegerField(db_column='PunUsuarioModif', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTAviso'


class Otavisomodif(models.Model):
    punmodificacion = models.AutoField(db_column='PunModificacion', primary_key=True)  # Field name made lowercase.
    punotaviso = models.ForeignKey(Otaviso, models.DO_NOTHING, db_column='PunOTAviso', blank=True, null=True)  # Field name made lowercase.
    campo = models.CharField(db_column='Campo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    valoranterior = models.CharField(db_column='ValorAnterior', max_length=50, blank=True, null=True)  # Field name made lowercase.
    valornuevo = models.CharField(db_column='ValorNuevo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tipovalor = models.ForeignKey('Hctipovalor', models.DO_NOTHING, db_column='TipoValor', blank=True, null=True)  # Field name made lowercase.
    item = models.IntegerField(db_column='ITEM', blank=True, null=True)  # Field name made lowercase.
    idophlp = models.IntegerField(db_column='IDOPHLP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTAvisoModif'


class Otavisomodiftmp(models.Model):
    punmodificacion = models.IntegerField(db_column='PunModificacion', blank=True, null=True)  # Field name made lowercase.
    punotaviso = models.IntegerField(db_column='PunOTAviso', blank=True, null=True)  # Field name made lowercase.
    campo = models.CharField(db_column='Campo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    valoranterior = models.CharField(db_column='ValorAnterior', max_length=50, blank=True, null=True)  # Field name made lowercase.
    valornuevo = models.CharField(db_column='ValorNuevo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tipovalor = models.IntegerField(db_column='TipoValor', blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='idOperacion', blank=True, null=True)  # Field name made lowercase.
    item = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OTAvisoModifTMP'


class Otavisotmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    punotaviso = models.IntegerField(db_column='punOTAviso', blank=True, null=True)  # Field name made lowercase.
    puncausaaviso = models.IntegerField(db_column='PunCausaAviso', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    punitempedido = models.IntegerField(db_column='PunItemPedido', blank=True, null=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT', blank=True, null=True)  # Field name made lowercase.
    punsectordestino = models.IntegerField(db_column='PunSectorDestino', blank=True, null=True)  # Field name made lowercase.
    modoabm = models.SmallIntegerField(db_column='ModoABM')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTAvisoTMP'


class Otcantidades(models.Model):
    puncantidad = models.AutoField(db_column='PunCantidad', primary_key=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punreasignacionot = models.IntegerField(db_column='PunReasignacionOT', blank=True, null=True)  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='PunUsuario')  # Field name made lowercase.
    tipocantidad = models.IntegerField(db_column='TipoCantidad', blank=True, null=True)  # Field name made lowercase.
    punoperacion = models.IntegerField(db_column='PunOperacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTCantidades'


class Otcostocierre(models.Model):
    punordent = models.IntegerField(db_column='PunOrdenT', primary_key=True)  # Field name made lowercase. The composite primary key (PunOrdenT, PunTipoCosto) found, that is not supported. The first column is selected.
    puntipocosto = models.IntegerField(db_column='PunTipoCosto')  # Field name made lowercase.
    costo = models.DecimalField(db_column='Costo', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTCostoCierre'
        unique_together = (('punordent', 'puntipocosto'),)


class Otcostocierrebackup(models.Model):
    punordent = models.IntegerField(db_column='PunOrdenT')  # Field name made lowercase.
    puntipocosto = models.IntegerField(db_column='PunTipoCosto')  # Field name made lowercase.
    costo = models.DecimalField(db_column='Costo', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTCostoCierreBackUp'


class Otentrega(models.Model):
    punordent = models.IntegerField(db_column='PunOrdenT')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4)  # Field name made lowercase.
    pundeposito = models.IntegerField(db_column='PunDeposito')  # Field name made lowercase.
    puntero = models.AutoField(primary_key=True, db_column='Puntero')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTEntrega'


class Otmpsugerida(models.Model):
    punotmpsugerida = models.AutoField(primary_key=True, db_column='PunOTMPSugerida')  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT')  # Field name made lowercase. The composite primary key (PunOrdenT, PunArticulo) found, that is not supported. The first column is selected.
    punarticulo = models.ForeignKey(Articulos, models.DO_NOTHING, db_column='PunArticulo')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTMPSugerida'
        unique_together = (('punordent', 'punarticulo'),)


class Otmpsugeridatmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    punotmpsugerida = models.IntegerField(db_column='PunOTMPSugerida', blank=True, null=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT', blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.
    modoabm = models.SmallIntegerField(db_column='ModoABM')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTMPSugeridaTMP'


class Otmateriaprimaasignada(models.Model):
    punasignacion = models.AutoField(primary_key=True, db_column='PunAsignacion')  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT')  # Field name made lowercase.
    punarticuloasignado = models.IntegerField(db_column='PunArticuloAsignado', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pununidad = models.IntegerField(db_column='PunUnidad', blank=True, null=True)  # Field name made lowercase.
    pundeposito = models.IntegerField(db_column='PunDeposito', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    punordentorigen = models.IntegerField(db_column='PunOrdenTOrigen', blank=True, null=True)  # Field name made lowercase.
    punoporigen = models.IntegerField(db_column='PunOPOrigen', blank=True, null=True)  # Field name made lowercase.
    costo = models.DecimalField(db_column='Costo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda', blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punremitoitem = models.IntegerField(db_column='PunRemitoItem', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=512, blank=True, null=True)  # Field name made lowercase.
    punmovimientostock = models.IntegerField(db_column='PunMovimientoStock', blank=True, null=True)  # Field name made lowercase.
    puntipompse = models.IntegerField(db_column='PunTipoMPSE', blank=True, null=True)  # Field name made lowercase.
    recomendar = models.BooleanField(db_column='Recomendar', blank=True, null=True)  # Field name made lowercase.
    modoabm = models.SmallIntegerField(db_column='ModoABM', blank=True, null=True)  # Field name made lowercase.
    punreasignacionot = models.IntegerField(db_column='PunReasignacionOT', blank=True, null=True)  # Field name made lowercase.
    cantidadcomenzada = models.DecimalField(db_column='CantidadComenzada', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidaddescontada = models.DecimalField(db_column='CantidadDescontada', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTMateriaPrimaAsignada'


class Otmateriaprimaasignadatmp(models.Model):
    idoperacion = models.IntegerField(db_column='IdOperacion')  # Field name made lowercase.
    punid = models.AutoField(primary_key=True, db_column='PunId')  # Field name made lowercase.
    punasignacion = models.IntegerField(db_column='PunAsignacion', blank=True, null=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT')  # Field name made lowercase.
    punarticuloasignado = models.IntegerField(db_column='PunArticuloAsignado', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pununidad = models.IntegerField(db_column='PunUnidad', blank=True, null=True)  # Field name made lowercase.
    pundeposito = models.IntegerField(db_column='PunDeposito', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    punordentorigen = models.IntegerField(db_column='PunOrdenTOrigen', blank=True, null=True)  # Field name made lowercase.
    punoporigen = models.IntegerField(db_column='PunOPOrigen', blank=True, null=True)  # Field name made lowercase.
    costo = models.DecimalField(db_column='Costo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda', blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punremitoitem = models.IntegerField(db_column='PunRemitoItem', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=512, blank=True, null=True)  # Field name made lowercase.
    punmovimientostock = models.IntegerField(db_column='PunMovimientoStock', blank=True, null=True)  # Field name made lowercase.
    puntipompse = models.IntegerField(db_column='PunTipoMPSE', blank=True, null=True)  # Field name made lowercase.
    recomendar = models.BooleanField(db_column='Recomendar', blank=True, null=True)  # Field name made lowercase.
    modoabm = models.SmallIntegerField(db_column='ModoABM', blank=True, null=True)  # Field name made lowercase.
    punreasignacionot = models.IntegerField(db_column='PunReasignacionOT', blank=True, null=True)  # Field name made lowercase.
    cantidadbaja = models.DecimalField(db_column='CantidadBaja', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidadcomenzada = models.DecimalField(db_column='CantidadComenzada', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTMateriaPrimaAsignadaTMP'


class Otoperacion(models.Model):
    punotoperacion = models.AutoField(db_column='PunOTOperacion', primary_key=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT')  # Field name made lowercase.
    punoperacion = models.ForeignKey('Operacion', models.DO_NOTHING, db_column='PunOperacion')  # Field name made lowercase.
    orden = models.IntegerField(db_column='Orden')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTOperacion'
        unique_together = (('punordent', 'punoperacion', 'orden'),)


class Otoperaciontmp(models.Model):
    punotoperacion = models.IntegerField(db_column='PunOTOperacion', blank=True, null=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT', blank=True, null=True)  # Field name made lowercase.
    punoperacion = models.IntegerField(db_column='PunOperacion')  # Field name made lowercase.
    orden = models.IntegerField(db_column='Orden')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=250, blank=True, null=True)  # Field name made lowercase.
    modoabm = models.IntegerField(db_column='ModoAbm')  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTOperacionTMP'


class Ototrocosto(models.Model):
    puncosto = models.AutoField(db_column='PunCosto', primary_key=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255)  # Field name made lowercase.
    costounitario = models.DecimalField(db_column='CostoUnitario', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4)  # Field name made lowercase.
    pununidad = models.IntegerField(db_column='PunUnidad', blank=True, null=True)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTOtroCosto'


class Otpropiedad(models.Model):
    punordent = models.IntegerField(db_column='PunOrdenT')  # Field name made lowercase.
    punpropiedad = models.IntegerField(db_column='PunPropiedad')  # Field name made lowercase.
    valor = models.CharField(db_column='Valor', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTPropiedad'


class Otreasignacion(models.Model):
    punreasignacionot = models.AutoField(primary_key=True, db_column='PunReasignacionOT')  # Field name made lowercase.
    punordentorigen = models.IntegerField(db_column='PunOrdenTOrigen')  # Field name made lowercase.
    punordentdestino = models.IntegerField(db_column='PunOrdenTDestino')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    cantidadreasignada = models.DecimalField(db_column='CantidadReasignada', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cantidadcomenzada = models.DecimalField(db_column='CantidadComenzada', max_digits=19, decimal_places=4)  # Field name made lowercase.
    nroreasignacion = models.IntegerField(db_column='NroReasignacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTReasignacion'


class Otreasignacioncosto(models.Model):
    punreasignacionot = models.IntegerField(db_column='PunReasignacionOT')  # Field name made lowercase.
    tipocosto = models.IntegerField(db_column='TipoCosto')  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    costo = models.DecimalField(db_column='Costo', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTReasignacionCosto'


class Otreasignacionservicio(models.Model):
    punreasignacionot = models.IntegerField(db_column='PunReasignacionOT')  # Field name made lowercase.
    punitemservicio = models.IntegerField(db_column='PunItemServicio')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTReasignacionServicio'


class Otremito(models.Model):
    punremitoot = models.AutoField(primary_key=True, db_column='PunRemitoOT')  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT')  # Field name made lowercase.
    prefijo = models.CharField(db_column='Prefijo', max_length=4)  # Field name made lowercase.
    sufijo = models.CharField(db_column='Sufijo', max_length=8)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4)  # Field name made lowercase.
    pununidad = models.IntegerField(db_column='PunUnidad')  # Field name made lowercase.
    punprvremitoitem = models.IntegerField(db_column='PunPRVRemitoItem', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OTRemito'


class Operacion(models.Model):
    punoperacion = models.AutoField(db_column='PunOperacion', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=10)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    codigobarras = models.CharField(db_column='CodigoBarras', max_length=50, blank=True, null=True)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Operacion'


class Operacionaduanaimportestmp(models.Model):
    puntipoimporte = models.IntegerField(db_column='punTipoImporte', blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    puncomprobantepago = models.IntegerField(db_column='punComprobantePago', blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='idOperacion', blank=True, null=True)  # Field name made lowercase.
    punoperacionaduana = models.IntegerField(db_column='punOperacionAduana', blank=True, null=True)  # Field name made lowercase.
    punjurisdiccion = models.IntegerField(db_column='PunJurisdiccion', blank=True, null=True)  # Field name made lowercase.
    numeroret = models.CharField(db_column='NumeroRet', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OperacionAduanaImportesTMP'


class Operacionrubroarticulo(models.Model):
    punopra = models.AutoField(db_column='PunOPRA', primary_key=True)  # Field name made lowercase.
    punoperacion = models.IntegerField(db_column='PunOperacion')  # Field name made lowercase.
    punrubro = models.IntegerField(db_column='PunRubro', blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=255, blank=True, null=True)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado')  # Field name made lowercase.
    orden = models.IntegerField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OperacionRubroArticulo'


class Operacionrubroarticulotmp(models.Model):
    punopra = models.IntegerField(db_column='PunOPRA', blank=True, null=True)  # Field name made lowercase.
    punoperacion = models.IntegerField(db_column='PunOperacion', blank=True, null=True)  # Field name made lowercase.
    punrubro = models.IntegerField(db_column='PunRubro', blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.BigIntegerField(db_column='idOperacion', blank=True, null=True)  # Field name made lowercase.
    modoabm = models.IntegerField(db_column='Modoabm', blank=True, null=True)  # Field name made lowercase.
    orden = models.IntegerField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OperacionRubroArticuloTMP'


class Operacionesaduana(models.Model):
    punoperacionaduana = models.IntegerField(db_column='PunOperacionAduana')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    nrodespacho = models.CharField(db_column='NroDespacho', max_length=40, blank=True, null=True)  # Field name made lowercase.
    punaduana = models.SmallIntegerField(db_column='PunAduana', blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda', blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pundespachante = models.IntegerField(db_column='PunDespachante', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    punproveedor = models.IntegerField(blank=True, null=True)
    fechaembarquereal = models.DateTimeField(db_column='FechaEmbarqueReal', blank=True, null=True)  # Field name made lowercase.
    valorfobtotal = models.DecimalField(db_column='ValorFobTotal', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pundivisa = models.IntegerField(db_column='PunDivisa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OperacionesAduana'


class Operacionesaduanaimportes(models.Model):
    punoperacionaduana = models.IntegerField(db_column='PunOperacionAduana')  # Field name made lowercase.
    puntipoimporte = models.IntegerField(db_column='PunTipoImporte')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    puncomprobantepago = models.IntegerField(db_column='PunComprobantePago', blank=True, null=True)  # Field name made lowercase.
    punjurisdiccion = models.IntegerField(db_column='PunJurisdiccion', blank=True, null=True)  # Field name made lowercase.
    numeroret = models.CharField(db_column='NumeroRet', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OperacionesAduanaImportes'


class Operario(models.Model):
    punoperario = models.AutoField(db_column='PunOperario', primary_key=True)  # Field name made lowercase.
    nrolegajo = models.CharField(db_column='NroLegajo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fechabaja = models.DateTimeField(db_column='FechaBaja', blank=True, null=True)  # Field name made lowercase.
    valorhora = models.DecimalField(db_column='ValorHora', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda', blank=True, null=True)  # Field name made lowercase.
    fechaalta = models.DateTimeField(db_column='FechaAlta', blank=True, null=True)  # Field name made lowercase.
    puncategoria = models.IntegerField(db_column='PunCategoria', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Operario'


class Ordentrabajo(models.Model):
    punordent = models.IntegerField(db_column='PunOrdenT')  # Field name made lowercase.
    puntipoot = models.IntegerField(db_column='PunTipoOT')  # Field name made lowercase.
    prefijo = models.CharField(db_column='Prefijo', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sufijo = models.CharField(db_column='Sufijo', max_length=8, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    punitempedido = models.IntegerField(db_column='PunItemPedido', blank=True, null=True)  # Field name made lowercase.
    cantidadpedida = models.DecimalField(db_column='CantidadPedida', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidadafabricar = models.DecimalField(db_column='CantidadAFabricar', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidadequivalente = models.DecimalField(db_column='CantidadEquivalente', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidadcomenzada = models.DecimalField(db_column='CantidadComenzada', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidadterminada = models.DecimalField(db_column='CantidadTerminada', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidadentregada = models.DecimalField(db_column='CantidadEntregada', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pununidad = models.IntegerField(db_column='PunUnidad', blank=True, null=True)  # Field name made lowercase.
    pununidadalternativa = models.IntegerField(db_column='PunUnidadAlternativa', blank=True, null=True)  # Field name made lowercase.
    fechaentrega = models.DateTimeField(db_column='FechaEntrega', blank=True, null=True)  # Field name made lowercase.
    fechaentregadeposito = models.DateTimeField(db_column='FechaEntregaDeposito', blank=True, null=True)  # Field name made lowercase.
    fechacierre = models.DateTimeField(db_column='FechaCierre', blank=True, null=True)  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda', blank=True, null=True)  # Field name made lowercase.
    punplanocliente = models.IntegerField(db_column='PunPlanoCliente', blank=True, null=True)  # Field name made lowercase.
    punplanosinpar = models.IntegerField(db_column='PunPlanoSinPar', blank=True, null=True)  # Field name made lowercase.
    msgproduccion = models.TextField(db_column='msgProduccion', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    observacioncierre = models.TextField(db_column='ObservacionCierre', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    punremitoitem = models.IntegerField(db_column='punRemitoitem', blank=True, null=True)  # Field name made lowercase.
    cantidadascrap = models.IntegerField(db_column='CantidadASCRAP', blank=True, null=True)  # Field name made lowercase.
    cantidadreasignada = models.IntegerField(db_column='CantidadReasignada', blank=True, null=True)  # Field name made lowercase.
    fechaterminada = models.DateTimeField(db_column='FechaTerminada', blank=True, null=True)  # Field name made lowercase.
    fechaanulacion = models.DateTimeField(db_column='FechaAnulacion', blank=True, null=True)  # Field name made lowercase.
    punlistacostocierre = models.IntegerField(db_column='PunListaCostoCierre', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=500, blank=True, null=True)  # Field name made lowercase.
    punlistaventacierre = models.IntegerField(db_column='PunListaVentaCierre', blank=True, null=True)  # Field name made lowercase.
    punrecepcion = models.IntegerField(db_column='PunRecepcion', blank=True, null=True)  # Field name made lowercase.
    codigo = models.IntegerField(blank=True, null=True)
    observaciones = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cantidadot = models.DecimalField(db_column='CantidadOT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    visto = models.SmallIntegerField(db_column='Visto', blank=True, null=True)  # Field name made lowercase.
    devolucion = models.SmallIntegerField(db_column='Devolucion', blank=True, null=True)  # Field name made lowercase.
    fechavisto = models.DateTimeField(db_column='FechaVisto', blank=True, null=True)  # Field name made lowercase.
    fechadevolucion = models.DateTimeField(db_column='FechaDevolucion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrdenTrabajo'


class OrdentrabajoOrg(models.Model):
    punordent = models.AutoField(primary_key=True, db_column='PunOrdenT')  # Field name made lowercase.
    puntipoot = models.IntegerField(db_column='PunTipoOT')  # Field name made lowercase.
    prefijo = models.CharField(db_column='Prefijo', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sufijo = models.CharField(db_column='Sufijo', max_length=8, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    punitempedido = models.IntegerField(db_column='PunItemPedido', blank=True, null=True)  # Field name made lowercase.
    cantidadpedida = models.DecimalField(db_column='CantidadPedida', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidadafabricar = models.DecimalField(db_column='CantidadAFabricar', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidadequivalente = models.DecimalField(db_column='CantidadEquivalente', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidadcomenzada = models.DecimalField(db_column='CantidadComenzada', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidadterminada = models.DecimalField(db_column='CantidadTerminada', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidadentregada = models.DecimalField(db_column='CantidadEntregada', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pununidad = models.IntegerField(db_column='PunUnidad', blank=True, null=True)  # Field name made lowercase.
    pununidadalternativa = models.IntegerField(db_column='PunUnidadAlternativa', blank=True, null=True)  # Field name made lowercase.
    fechaentrega = models.DateTimeField(db_column='FechaEntrega', blank=True, null=True)  # Field name made lowercase.
    fechaentregadeposito = models.DateTimeField(db_column='FechaEntregaDeposito', blank=True, null=True)  # Field name made lowercase.
    fechacierre = models.DateTimeField(db_column='FechaCierre', blank=True, null=True)  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda', blank=True, null=True)  # Field name made lowercase.
    punplanocliente = models.IntegerField(db_column='PunPlanoCliente', blank=True, null=True)  # Field name made lowercase.
    punplanosinpar = models.IntegerField(db_column='PunPlanoSinPar', blank=True, null=True)  # Field name made lowercase.
    msgproduccion = models.TextField(db_column='msgProduccion', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    observacioncierre = models.TextField(db_column='ObservacionCierre', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    punremitoitem = models.IntegerField(db_column='punRemitoitem', blank=True, null=True)  # Field name made lowercase.
    cantidadascrap = models.IntegerField(db_column='CantidadASCRAP', blank=True, null=True)  # Field name made lowercase.
    cantidadreasignada = models.IntegerField(db_column='CantidadReasignada', blank=True, null=True)  # Field name made lowercase.
    fechaterminada = models.DateTimeField(db_column='FechaTerminada', blank=True, null=True)  # Field name made lowercase.
    fechaanulacion = models.DateTimeField(db_column='FechaAnulacion', blank=True, null=True)  # Field name made lowercase.
    punlistacostocierre = models.IntegerField(db_column='PunListaCostoCierre', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=500, blank=True, null=True)  # Field name made lowercase.
    punlistaventacierre = models.IntegerField(db_column='PunListaVentaCierre', blank=True, null=True)  # Field name made lowercase.
    punrecepcion = models.IntegerField(db_column='PunRecepcion', blank=True, null=True)  # Field name made lowercase.
    codigo = models.IntegerField(blank=True, null=True)
    observaciones = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cantidadot = models.DecimalField(db_column='CantidadOT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    visto = models.SmallIntegerField(db_column='Visto', blank=True, null=True)  # Field name made lowercase.
    devolucion = models.SmallIntegerField(db_column='Devolucion', blank=True, null=True)  # Field name made lowercase.
    fechavisto = models.DateTimeField(db_column='FechaVisto', blank=True, null=True)  # Field name made lowercase.
    fechadevolucion = models.DateTimeField(db_column='FechaDevolucion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrdenTrabajo_org'


class Ordenescompra(models.Model):
    punordenc = models.AutoField(db_column='PunOrdenC', primary_key=True)  # Field name made lowercase.
    nroordenc = models.IntegerField(db_column='NroOrdenC')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='PunProveedor')  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    puncondicionpago = models.IntegerField(db_column='PunCondicionPago', blank=True, null=True)  # Field name made lowercase.
    seguimientovto = models.SmallIntegerField(db_column='SeguimientoVto')  # Field name made lowercase.
    punoperacionaduana = models.IntegerField(db_column='PunOperacionAduana', blank=True, null=True)  # Field name made lowercase.
    observacion = models.TextField(db_column='Observacion', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'OrdenesCompra'


class Ordenescompraold(models.Model):
    punordenc = models.AutoField(primary_key=True, db_column='PunOrdenC')  # Field name made lowercase.
    nroordenc = models.IntegerField(db_column='NroOrdenC')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='PunProveedor')  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    puncondicionpago = models.IntegerField(db_column='PunCondicionPago', blank=True, null=True)  # Field name made lowercase.
    seguimientovto = models.SmallIntegerField(db_column='SeguimientoVto')  # Field name made lowercase.
    punoperacionaduana = models.IntegerField(db_column='PunOperacionAduana', blank=True, null=True)  # Field name made lowercase.
    observacion = models.TextField(db_column='Observacion', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'OrdenesCompraOLD'


class Ordenescompratmp(models.Model):
    punordenc = models.IntegerField(db_column='punOrdenC', blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='idOperacion', blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OrdenesCompraTMP'


class OrdenescompraBkp(models.Model):
    punordenc = models.AutoField(primary_key=True, db_column='PunOrdenC')  # Field name made lowercase.
    nroordenc = models.IntegerField(db_column='NroOrdenC')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='PunProveedor')  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    puncondicionpago = models.IntegerField(db_column='PunCondicionPago', blank=True, null=True)  # Field name made lowercase.
    seguimientovto = models.SmallIntegerField(db_column='SeguimientoVto')  # Field name made lowercase.
    punoperacionaduana = models.IntegerField(db_column='PunOperacionAduana', blank=True, null=True)  # Field name made lowercase.
    observacion = models.TextField(db_column='Observacion', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'OrdenesCompra_BKP'


class Pasajeorden(models.Model):
    codigo = models.CharField(db_column='CODIGO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    fecha_alta = models.DateTimeField(db_column='FECHA ALTA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cliente = models.CharField(db_column='CLIENTE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    descli = models.CharField(db_column='DESCLI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    descri = models.CharField(db_column='DESCRI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cant_fabricar = models.DecimalField(db_column='CANT#FABRICAR', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    plazo = models.DateTimeField(db_column='PLAZO', blank=True, null=True)  # Field name made lowercase.
    puntipoot = models.IntegerField(db_column='PUNTIPOOT', blank=True, null=True)  # Field name made lowercase.
    pedido = models.IntegerField(db_column='PEDIDO', blank=True, null=True)  # Field name made lowercase.
    codalt = models.CharField(db_column='CODALT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cant = models.IntegerField(db_column='CANT', blank=True, null=True)  # Field name made lowercase.
    otroscostos = models.DecimalField(db_column='OTROSCOSTOS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PASAJEORDEN'


class Planosarmado(models.Model):
    punarmado = models.AutoField(primary_key=True, db_column='PunArmado')  # Field name made lowercase.
    punrubro = models.IntegerField(db_column='PunRubro', blank=True, null=True)  # Field name made lowercase.
    punconcepto = models.IntegerField(db_column='PunConcepto', blank=True, null=True)  # Field name made lowercase.
    posicion = models.IntegerField(db_column='Posicion', blank=True, null=True, db_comment='Numero que identifica la posic')  # Field name made lowercase.
    inspeccion = models.IntegerField(db_column='Inspeccion', blank=True, null=True, db_comment='Inspecci├│n=0 NO se inspecciona')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PLANOSArmado'


class Planosconceptos(models.Model):
    punconcepto = models.AutoField(primary_key=True, db_column='PunConcepto')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True, db_comment='Detalle de los nombres de los ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PLANOSConceptos'


class Planosfinal(models.Model):
    punplano = models.AutoField(primary_key=True, db_column='PunPlano')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    punarmado = models.IntegerField(db_column='PunArmado', blank=True, null=True)  # Field name made lowercase.
    valor = models.CharField(db_column='Valor', max_length=50, blank=True, null=True, db_comment='Valor de la cota')  # Field name made lowercase.
    inspeccion = models.IntegerField(db_column='Inspeccion', blank=True, null=True, db_comment='Inspeccion=0 NO se inspecciona')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PLANOSFinal'


class Prodepositos(models.Model):
    pundeposito = models.AutoField(db_column='PunDeposito', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punprovincia = models.IntegerField(db_column='PunProvincia')  # Field name made lowercase.
    telefonos = models.CharField(db_column='Telefonos', max_length=100, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    pundistribuidor = models.IntegerField(db_column='PunDistribuidor')  # Field name made lowercase.
    tipo = models.SmallIntegerField(db_column='Tipo')  # Field name made lowercase.
    puncalipso = models.CharField(max_length=10, blank=True, null=True)
    puntipompse = models.ForeignKey('Hctipompse', models.DO_NOTHING, db_column='PunTipoMPSE', blank=True, null=True)  # Field name made lowercase.
    interno = models.SmallIntegerField(db_column='Interno', blank=True, null=True)  # Field name made lowercase.
    puntipostock = models.SmallIntegerField(db_column='PunTipoStock', blank=True, null=True)  # Field name made lowercase.
    codigopostal = models.CharField(db_column='CodigoPostal', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRODepositos'


class Promotivosmovistock(models.Model):
    punmotivo = models.AutoField(primary_key=True, db_column='PunMotivo')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150)  # Field name made lowercase.
    puntipomovimiento = models.CharField(db_column='PunTipomovimiento', max_length=10, blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado')  # Field name made lowercase.
    clasifxmovim = models.BooleanField(db_column='ClasifXmovim', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROMotivosMoviStock'


class Prvactividadfce(models.Model):
    punactividad = models.IntegerField(db_column='PunActividad', primary_key=True)  # Field name made lowercase. The composite primary key (PunActividad, FechaDesde) found, that is not supported. The first column is selected.
    fechadesde = models.DateTimeField(db_column='FechaDesde')  # Field name made lowercase.
    fechahasta = models.DateTimeField(db_column='FechaHasta', blank=True, null=True)  # Field name made lowercase.
    importeminimo = models.DecimalField(db_column='ImporteMinimo', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVActividadFCE'
        unique_together = (('punactividad', 'fechadesde'),)


class Prvactividades(models.Model):
    punactividad = models.AutoField(primary_key=True, db_column='PunActividad')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVActividades'


class Prvcalificaciones(models.Model):
    puncalificacion = models.AutoField(primary_key=True, db_column='PunCalificacion')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVCalificaciones'


class Prvcodigosiva(models.Model):
    puniva = models.IntegerField(db_column='PunIVA')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    porcretencion = models.DecimalField(db_column='PorcRetencion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porcincumplimiento = models.DecimalField(db_column='PorcIncumplimiento', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVCodigosIVA'


class Prvcomprobantecondiciones(models.Model):
    puncondicion = models.IntegerField(db_column='PunCondicion')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    diasdesde = models.SmallIntegerField(db_column='DiasDesde', blank=True, null=True)  # Field name made lowercase.
    diashasta = models.SmallIntegerField(db_column='DiasHasta', blank=True, null=True)  # Field name made lowercase.
    porcentaje = models.FloatField(db_column='Porcentaje', blank=True, null=True)  # Field name made lowercase.
    descuentointeres = models.SmallIntegerField(db_column='DescuentoInteres')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVComprobanteCondiciones'


class Prvcomprobantecondicionestmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    puncondicion = models.IntegerField(db_column='PunCondicion', blank=True, null=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    diasdesde = models.SmallIntegerField(db_column='DiasDesde', blank=True, null=True)  # Field name made lowercase.
    diashasta = models.SmallIntegerField(db_column='DiasHasta', blank=True, null=True)  # Field name made lowercase.
    porcentaje = models.FloatField(db_column='Porcentaje', blank=True, null=True)  # Field name made lowercase.
    descuentointeres = models.SmallIntegerField(db_column='DescuentoInteres')  # Field name made lowercase.
    modoabm = models.SmallIntegerField(db_column='ModoABM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVComprobanteCondicionesTMP'


class Prvcomprobantecuentas(models.Model):
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    cuenta = models.CharField(db_column='Cuenta', max_length=9)  # Field name made lowercase.
    punplancuentas = models.IntegerField(db_column='PunPlanCuentas')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    leyenda = models.CharField(db_column='Leyenda', max_length=100, blank=True, null=True)  # Field name made lowercase.
    puncentrocosto = models.IntegerField(db_column='PunCentroCosto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVComprobanteCuentas'


class Prvcomprobantecuentastmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    cuenta = models.CharField(db_column='Cuenta', max_length=9)  # Field name made lowercase.
    punplancuentas = models.IntegerField(db_column='PunPlanCuentas')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    leyenda = models.CharField(db_column='Leyenda', max_length=100, blank=True, null=True)  # Field name made lowercase.
    abm = models.CharField(db_column='ABM', max_length=1)  # Field name made lowercase.
    puncentrocosto = models.IntegerField(db_column='PunCentroCosto', blank=True, null=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT', blank=True, null=True)  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    punsubcliente = models.IntegerField(db_column='PunSubcliente', blank=True, null=True)  # Field name made lowercase.
    idoperacion2 = models.IntegerField(db_column='IDOperacion2', blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='punMoneda', blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVComprobanteCuentasTMP'


class Prvcomprobanteimportes(models.Model):
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    punreferencia = models.IntegerField(db_column='PunReferencia')  # Field name made lowercase.
    puntipoimporte = models.IntegerField(db_column='PunTipoImporte')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    numeroret = models.CharField(db_column='NumeroRet', max_length=20, blank=True, null=True)  # Field name made lowercase.
    punjurisdiccion = models.IntegerField(db_column='PunJurisdiccion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVComprobanteImportes'


class Prvcomprobanteimportestmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    puntipoimporte = models.IntegerField(db_column='PunTipoImporte')  # Field name made lowercase.
    punreferencia = models.IntegerField(db_column='PunReferencia', blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    numeroret = models.CharField(db_column='NumeroRet', max_length=20, blank=True, null=True)  # Field name made lowercase.
    punjurisdiccion = models.IntegerField(db_column='PunJurisdiccion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVComprobanteImportesTMP'


class Prvcomprobantevencimientos(models.Model):
    punproveedor = models.IntegerField(db_column='PunProveedor')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    punreferencia = models.IntegerField(db_column='PunReferencia')  # Field name made lowercase.
    fechavto = models.DateTimeField(db_column='FechaVto')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVComprobanteVencimientos'


class Prvcomprobantevencimientostmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    fechavto = models.DateTimeField(db_column='FechaVto')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    abm = models.CharField(db_column='ABM', max_length=1)  # Field name made lowercase.
    punreferencia = models.IntegerField(db_column='PunReferencia', blank=True, null=True)  # Field name made lowercase.
    fechaorig = models.DateTimeField(db_column='FechaOrig', blank=True, null=True)  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='PunProveedor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVComprobanteVencimientosTMP'


class Prvcomprobantes(models.Model):
    puncomprobante = models.AutoField(primary_key=True, db_column='PunComprobante')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    tipoabc = models.CharField(db_column='TipoABC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=2, blank=True, null=True)  # Field name made lowercase.
    prefijo = models.CharField(db_column='Prefijo', max_length=5, blank=True, null=True)  # Field name made lowercase.
    sufijo = models.CharField(db_column='Sufijo', max_length=8, blank=True, null=True)  # Field name made lowercase.
    punasiento = models.IntegerField(db_column='PunAsiento')  # Field name made lowercase.
    observacioncomp = models.CharField(db_column='ObservacionComp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tiponcnd = models.SmallIntegerField(db_column='TipoNCND', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='PunProveedor')  # Field name made lowercase.
    punusuario = models.SmallIntegerField(db_column='PunUsuario', blank=True, null=True)  # Field name made lowercase.
    tipoimputacion = models.SmallIntegerField(db_column='TipoImputacion', blank=True, null=True)  # Field name made lowercase.
    puntipoiva = models.IntegerField(db_column='PunTipoIVA', blank=True, null=True)  # Field name made lowercase.
    fechacontab = models.DateTimeField(db_column='FechaContab', blank=True, null=True)  # Field name made lowercase.
    punagrupado = models.IntegerField(db_column='PunAgrupado', blank=True, null=True)  # Field name made lowercase.
    fechaingreso = models.DateTimeField(db_column='FechaIngreso', blank=True, null=True)  # Field name made lowercase.
    punactividadganancias = models.IntegerField(db_column='PunActividadGanancias', blank=True, null=True)  # Field name made lowercase.
    pungasto = models.IntegerField(db_column='PunGasto', blank=True, null=True)  # Field name made lowercase.
    puncai = models.IntegerField(db_column='PunCAI', blank=True, null=True)  # Field name made lowercase.
    controladorfiscal = models.SmallIntegerField(db_column='ControladorFiscal', blank=True, null=True)  # Field name made lowercase.
    afiptipocomprobante = models.IntegerField(db_column='AFIPTipoComprobante', blank=True, null=True)  # Field name made lowercase.
    punconceptoib = models.IntegerField(db_column='PunConceptoIB', blank=True, null=True)  # Field name made lowercase.
    punprocesoautomatico = models.IntegerField(db_column='PunProcesoAutomatico', blank=True, null=True)  # Field name made lowercase.
    cargamanual = models.SmallIntegerField(db_column='CargaManual', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVComprobantes'


class Prvcomprobantesapagar(models.Model):
    punproveedor = models.IntegerField(db_column='PunProveedor')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    fechavto = models.DateTimeField(db_column='FechaVto')  # Field name made lowercase.
    saldocomprobante = models.DecimalField(db_column='SaldoComprobante', max_digits=19, decimal_places=4)  # Field name made lowercase.
    importeapagar = models.DecimalField(db_column='ImporteAPagar', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importedescuento = models.DecimalField(db_column='ImporteDescuento', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importeinteres = models.DecimalField(db_column='ImporteInteres', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importeretencioniva = models.DecimalField(db_column='ImporteRetencionIVA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    puncondicion = models.IntegerField(db_column='PunCondicion', blank=True, null=True)  # Field name made lowercase.
    importereduccioniva = models.DecimalField(db_column='ImporteReduccionIVA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porcretencioniva = models.DecimalField(db_column='PorcRetencionIVA', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    porcreduccion = models.DecimalField(db_column='PorcReduccion', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    importeretencionrg1784 = models.DecimalField(db_column='ImporteRetencionRG1784', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importereduccionrg1784 = models.DecimalField(db_column='ImporteReduccionRG1784', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porcretencionrg1784 = models.DecimalField(db_column='PorcRetencionRG1784', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porcreduccionrg1784 = models.DecimalField(db_column='PorcReduccionRG1784', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importeretganm = models.DecimalField(db_column='ImporteRetGanM', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVComprobantesAPagar'


class Prvcomprobantesapagartmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    idoperacion2 = models.IntegerField(db_column='IDOperacion2', blank=True, null=True)  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='PunProveedor')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa', blank=True, null=True)  # Field name made lowercase.
    fechavto = models.DateTimeField(db_column='FechaVto', blank=True, null=True)  # Field name made lowercase.
    saldocomprobante = models.DecimalField(db_column='SaldoComprobante', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importeapagar = models.DecimalField(db_column='ImporteAPagar', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importedescuento = models.DecimalField(db_column='ImporteDescuento', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importeinteres = models.DecimalField(db_column='ImporteInteres', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importeretencioniva = models.DecimalField(db_column='ImporteRetencionIVA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    puncondicion = models.IntegerField(db_column='PunCondicion', blank=True, null=True)  # Field name made lowercase.
    importereduccioniva = models.DecimalField(db_column='ImporteReduccionIVA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porcretencioniva = models.DecimalField(db_column='PorcRetencionIVA', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    porcreduccion = models.DecimalField(db_column='PorcReduccion', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVComprobantesAPagarTMP'


class Prvcomprobantestmp(models.Model):
    tipoabc = models.CharField(db_column='TipoABC', max_length=1)  # Field name made lowercase.
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=2)  # Field name made lowercase.
    prefijo = models.CharField(db_column='Prefijo', max_length=5, blank=True, null=True)  # Field name made lowercase.
    sufijo = models.CharField(db_column='Sufijo', max_length=8)  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='IdOperacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVComprobantesTMP'


class Prvcuentacorriente(models.Model):
    punproveedor = models.IntegerField(db_column='PunProveedor')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    punreferencia = models.IntegerField(db_column='PunReferencia')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punmoneda = models.SmallIntegerField(db_column='PunMoneda')  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4)  # Field name made lowercase.
    observacioncc = models.CharField(db_column='ObservacionCC', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVCuentaCorriente'


class Prvdgiretencionesm(models.Model):
    punretencionganm = models.AutoField(primary_key=True, db_column='punRetencionGanM')  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='punProveedor', blank=True, null=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='punComprobante', blank=True, null=True)  # Field name made lowercase.
    importeretencion = models.DecimalField(db_column='ImporteRetencion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punganancias = models.IntegerField(db_column='punGanancias', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVDGIRetencionesM'


class Prvdetallepago(models.Model):
    punagrupado = models.IntegerField(db_column='PunAgrupado')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    punorigen = models.IntegerField(db_column='PunOrigen')  # Field name made lowercase.
    punorigenagrupado = models.IntegerField(db_column='PunOrigenAgrupado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVDetallePago'


class Prvdgicontribucionespat(models.Model):
    punretencion = models.AutoField(primary_key=True, db_column='punRetencion')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='punComprobante', blank=True, null=True)  # Field name made lowercase.
    puncomprobantepago = models.IntegerField(db_column='punComprobantePago', blank=True, null=True)  # Field name made lowercase.
    importebase = models.DecimalField(db_column='ImporteBase', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importeretencion = models.DecimalField(db_column='ImporteRetencion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tasa = models.DecimalField(db_column='Tasa', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nroretencion = models.CharField(db_column='NroRetencion', max_length=16, blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(blank=True, null=True)
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    porcreduccion = models.DecimalField(db_column='porcReduccion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importereduccion = models.DecimalField(db_column='ImporteReduccion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVDgiContribucionesPat'


class Prvdgiganancias(models.Model):
    punganancias = models.AutoField(primary_key=True, db_column='PunGanancias')  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='PunProveedor')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    tasa = models.DecimalField(db_column='Tasa', max_digits=5, decimal_places=2)  # Field name made lowercase.
    minimonoimponible = models.DecimalField(db_column='MinimoNoImponible', max_digits=9, decimal_places=2)  # Field name made lowercase.
    acumulado = models.DecimalField(db_column='Acumulado', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    importeretencion = models.DecimalField(db_column='ImporteRetencion', max_digits=9, decimal_places=2)  # Field name made lowercase.
    retencionesefectuadas = models.DecimalField(db_column='RetencionesEfectuadas', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nroganancias = models.CharField(db_column='NroGanancias', max_length=20, blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado')  # Field name made lowercase.
    pungeneracion = models.IntegerField(db_column='PunGeneracion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVDgiGanancias'


class Prvdgiiva(models.Model):
    punretencioniva = models.AutoField(primary_key=True, db_column='PunRetencionIVA')  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='PunProveedor')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    importeretencion = models.DecimalField(db_column='ImporteRetencion', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcentajeretencion = models.DecimalField(db_column='PorcentajeRetencion', max_digits=5, decimal_places=2)  # Field name made lowercase.
    importereduccion = models.DecimalField(db_column='ImporteReduccion', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    puncomprobantepago = models.IntegerField(db_column='PunComprobantePago', blank=True, null=True)  # Field name made lowercase.
    nroretencioniva = models.CharField(db_column='NroRetencionIva', max_length=16, blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado')  # Field name made lowercase.
    pungeneracion = models.IntegerField(db_column='PunGeneracion', blank=True, null=True)  # Field name made lowercase.
    porcentajereduccion = models.DecimalField(db_column='PorcentajeReduccion', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVDgiIVA'


class Prvdgiretencionesib(models.Model):
    punretencionib = models.AutoField(primary_key=True, db_column='PunRetencionIB')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    base = models.DecimalField(db_column='Base', max_digits=19, decimal_places=4)  # Field name made lowercase.
    retencion = models.DecimalField(db_column='Retencion', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punjurisdiccionib = models.IntegerField(db_column='PunJurisdiccionIB')  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado')  # Field name made lowercase.
    nroretencionib = models.CharField(db_column='NroRetencionIB', max_length=20, blank=True, null=True)  # Field name made lowercase.
    punconceptoib = models.IntegerField(db_column='PunConceptoIB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVDgiRetencionesIB'


class Prvfondofijocomprobantesapagar(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion', blank=True, null=True)  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='PunProveedor')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    fechavto = models.DateTimeField(db_column='FechaVto')  # Field name made lowercase.
    saldocomprobante = models.DecimalField(db_column='SaldoComprobante', max_digits=19, decimal_places=4)  # Field name made lowercase.
    importeapagar = models.DecimalField(db_column='ImporteAPagar', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importedescuento = models.DecimalField(db_column='ImporteDescuento', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importeinteres = models.DecimalField(db_column='ImporteInteres', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importeretencioniva = models.DecimalField(db_column='ImporteRetencionIVA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    puncondicion = models.IntegerField(db_column='PunCondicion', blank=True, null=True)  # Field name made lowercase.
    importereduccioniva = models.DecimalField(db_column='ImporteReduccionIVA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porcretencioniva = models.DecimalField(db_column='PorcRetencionIVA', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    porcreduccion = models.DecimalField(db_column='PorcReduccion', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVFondoFijoComprobantesAPagar'


class Prvgastos(models.Model):
    pungasto = models.AutoField(primary_key=True, db_column='PunGasto')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    prefijo = models.CharField(db_column='Prefijo', max_length=4)  # Field name made lowercase.
    sufijo = models.CharField(db_column='Sufijo', max_length=8)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    cotizacion = models.FloatField(db_column='Cotizacion')  # Field name made lowercase.
    punasiento = models.IntegerField(db_column='PunAsiento')  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    punorigen = models.SmallIntegerField(db_column='PunOrigen')  # Field name made lowercase.
    numero = models.IntegerField(db_column='Numero', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVGastos'


class Prvnhcomprobanteimportes(models.Model):
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    punreferencia = models.IntegerField(db_column='PunReferencia')  # Field name made lowercase.
    puntipoimporte = models.IntegerField(db_column='PunTipoImporte')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcentaje = models.FloatField(db_column='Porcentaje', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVNHComprobanteImportes'


class Prvnhcomprobantes(models.Model):
    puncomprobante = models.AutoField(primary_key=True, db_column='PunComprobante')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    tipoabc = models.CharField(db_column='TipoABC', max_length=1)  # Field name made lowercase.
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=2)  # Field name made lowercase.
    prefijo = models.CharField(db_column='Prefijo', max_length=5, blank=True, null=True)  # Field name made lowercase.
    sufijo = models.CharField(db_column='Sufijo', max_length=8)  # Field name made lowercase.
    punasiento = models.IntegerField(db_column='PunAsiento')  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='PunProveedor')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    pungasto = models.IntegerField(db_column='PunGasto', blank=True, null=True)  # Field name made lowercase.
    puncai = models.IntegerField(db_column='PunCAI', blank=True, null=True)  # Field name made lowercase.
    controladorfiscal = models.SmallIntegerField(db_column='ControladorFiscal', blank=True, null=True)  # Field name made lowercase.
    afiptipocomprobante = models.IntegerField(db_column='AFIPTipoComprobante')  # Field name made lowercase.
    fechacomprobante = models.DateTimeField(db_column='FechaComprobante', blank=True, null=True)  # Field name made lowercase.
    punprocesoautomatico = models.IntegerField(db_column='PunProcesoAutomatico', blank=True, null=True)  # Field name made lowercase.
    cargamanual = models.SmallIntegerField(db_column='CargaManual', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVNHComprobantes'


class Prvnhcomprobantestmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    idoperacion2 = models.IntegerField(db_column='IDOperacion2', blank=True, null=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    tipoabc = models.CharField(db_column='TipoABC', max_length=1)  # Field name made lowercase.
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=2)  # Field name made lowercase.
    prefijo = models.CharField(db_column='Prefijo', max_length=5, blank=True, null=True)  # Field name made lowercase.
    sufijo = models.CharField(db_column='Sufijo', max_length=8)  # Field name made lowercase.
    punasiento = models.IntegerField(db_column='PunAsiento', blank=True, null=True)  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='PunProveedor')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    pungasto = models.IntegerField(db_column='PunGasto', blank=True, null=True)  # Field name made lowercase.
    importecuota = models.DecimalField(db_column='ImporteCuota', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    modoabm = models.SmallIntegerField(db_column='ModoABM', blank=True, null=True)  # Field name made lowercase.
    puncai = models.IntegerField(db_column='PunCAI', blank=True, null=True)  # Field name made lowercase.
    fechacomprobante = models.DateTimeField(db_column='FechaComprobante', blank=True, null=True)  # Field name made lowercase.
    controladorfiscal = models.SmallIntegerField(db_column='ControladorFiscal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVNHComprobantesTMP'


class Prvnhcuentacorriente(models.Model):
    punproveedor = models.IntegerField(db_column='PunProveedor')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    punreferencia = models.IntegerField(db_column='PunReferencia')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punmoneda = models.SmallIntegerField(db_column='PunMoneda')  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVNHCuentaCorriente'


class Prvnhnumeroscai(models.Model):
    puncai = models.AutoField(primary_key=True, db_column='PunCAI')  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='PunProveedor')  # Field name made lowercase.
    numerocai = models.CharField(db_column='NumeroCAI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fechavto = models.DateTimeField(db_column='FechaVto')  # Field name made lowercase.
    fechavtoant = models.DateTimeField(db_column='FechaVtoAnt', blank=True, null=True)  # Field name made lowercase.
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tipoabc = models.CharField(db_column='TipoABC', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVNHNumerosCAI'


class Prvnhproveedores(models.Model):
    punproveedor = models.AutoField(primary_key=True, db_column='PunProveedor')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100)  # Field name made lowercase.
    puntipoiva = models.IntegerField(db_column='PunTipoIva')  # Field name made lowercase.
    cuit = models.CharField(db_column='Cuit', max_length=14, blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    puncentro = models.IntegerField(db_column='PunCentro', blank=True, null=True)  # Field name made lowercase.
    punjurisdiccionib = models.IntegerField(db_column='punJurisdiccionIB', blank=True, null=True)  # Field name made lowercase.
    codigoretencioniva = models.IntegerField(db_column='CodigoRetencionIVA', blank=True, null=True)  # Field name made lowercase.
    codigopercepcioniva = models.IntegerField(db_column='CodigoPercepcionIVA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVNHProveedores'


class Prvnumeroscai(models.Model):
    puncai = models.AutoField(primary_key=True, db_column='PunCAI')  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='PunProveedor')  # Field name made lowercase.
    numerocai = models.CharField(db_column='NumeroCAI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fechavto = models.DateTimeField(db_column='FechaVto')  # Field name made lowercase.
    fechavtoant = models.DateTimeField(db_column='FechaVtoAnt', blank=True, null=True)  # Field name made lowercase.
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tipoabc = models.CharField(db_column='TipoABC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tipoclave = models.IntegerField(db_column='TipoClave', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVNumerosCAI'


class Prvpagos(models.Model):
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    puntipopago = models.IntegerField(db_column='PunTipoPago')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punbanco = models.IntegerField(db_column='PunBanco', blank=True, null=True)  # Field name made lowercase.
    nrocheque = models.IntegerField(db_column='NroCheque', blank=True, null=True)  # Field name made lowercase.
    punorigen = models.IntegerField(db_column='PunOrigen', blank=True, null=True)  # Field name made lowercase.
    puncomprobanteasociado = models.IntegerField(db_column='PunComprobanteAsociado', blank=True, null=True)  # Field name made lowercase.
    punpago = models.AutoField(primary_key=True, db_column='PunPago')  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=2, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    puncomprobanteorigen = models.IntegerField(db_column='punComprobanteOrigen', blank=True, null=True)  # Field name made lowercase.
    cotizacionsinredondear = models.DecimalField(db_column='CotizacionSinRedondear', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVPagos'


class Prvpagosnoretiene(models.Model):
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVPagosNoRetiene'


class Prvparametrosganancias1(models.Model):
    punganancias = models.IntegerField(db_column='PunGanancias')  # Field name made lowercase.
    porcentajeconcuit = models.FloatField(db_column='PorcentajeConCUIT')  # Field name made lowercase.
    porcentajesincuit = models.FloatField(db_column='PorcentajeSinCUIT')  # Field name made lowercase.
    minimonoimponible = models.DecimalField(db_column='MinimoNoImponible', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVParametrosGanancias1'


class Prvparametrosganancias2(models.Model):
    minimo = models.DecimalField(db_column='Minimo', max_digits=19, decimal_places=4)  # Field name made lowercase.
    maximo = models.DecimalField(db_column='Maximo', max_digits=19, decimal_places=4)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcentaje = models.FloatField(db_column='Porcentaje')  # Field name made lowercase.
    minimonoimponible = models.DecimalField(db_column='MinimoNoImponible', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punganancias = models.IntegerField(db_column='PunGanancias', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVParametrosGanancias2'


class Prvparametrosganancias2Tmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    minimo = models.DecimalField(db_column='Minimo', max_digits=19, decimal_places=4)  # Field name made lowercase.
    maximo = models.DecimalField(db_column='Maximo', max_digits=19, decimal_places=4)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcentaje = models.FloatField(db_column='Porcentaje')  # Field name made lowercase.
    minimonoimponible = models.DecimalField(db_column='MinimoNoImponible', max_digits=19, decimal_places=4)  # Field name made lowercase.
    modo = models.IntegerField(db_column='Modo', blank=True, null=True)  # Field name made lowercase.
    punganancias = models.IntegerField(db_column='PunGanancias', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVParametrosGanancias2TMP'


class Prvparametrosganancias3(models.Model):
    punganancias = models.IntegerField(db_column='PunGanancias')  # Field name made lowercase.
    porcentajepago = models.FloatField(db_column='PorcentajePago')  # Field name made lowercase.
    porcentajeretencion = models.FloatField(db_column='PorcentajeRetencion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVParametrosGanancias3'


class Prvproveedoractganancias(models.Model):
    punproveedor = models.IntegerField(db_column='PunProveedor')  # Field name made lowercase.
    punactividadganancias = models.SmallIntegerField(db_column='PunActividadGanancias', blank=True, null=True)  # Field name made lowercase.
    puntipoactganancias = models.SmallIntegerField(db_column='PunTipoActGanancias', blank=True, null=True)  # Field name made lowercase.
    reduccionretganancias = models.DecimalField(db_column='ReduccionRetGanancias', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fechavtoganancias = models.DateTimeField(db_column='FechaVtoGanancias', blank=True, null=True)  # Field name made lowercase.
    punactividad = models.IntegerField(db_column='PunActividad', blank=True, null=True)  # Field name made lowercase.
    cuenta = models.CharField(db_column='Cuenta', max_length=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVProveedorActGanancias'


class Prvproveedoractgananciastmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='PunProveedor', blank=True, null=True)  # Field name made lowercase.
    punactividadganancias = models.SmallIntegerField(db_column='PunActividadGanancias', blank=True, null=True)  # Field name made lowercase.
    puntipoactganancias = models.SmallIntegerField(db_column='PunTipoActGanancias', blank=True, null=True)  # Field name made lowercase.
    reduccionretganancias = models.DecimalField(db_column='ReduccionRetGanancias', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fechavtoganancias = models.DateTimeField(db_column='FechaVtoGanancias', blank=True, null=True)  # Field name made lowercase.
    punactividad = models.IntegerField(db_column='PunActividad', blank=True, null=True)  # Field name made lowercase.
    cuenta = models.CharField(db_column='Cuenta', max_length=9, blank=True, null=True)  # Field name made lowercase.
    punactividadgananciasant = models.IntegerField(db_column='PunActividadGananciasANT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVProveedorActGananciasTMP'


class Prvproveedores(models.Model):
    punproveedor = models.AutoField(primary_key=True, db_column='PunProveedor')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=120, blank=True, null=True)  # Field name made lowercase.
    localidad = models.CharField(db_column='Localidad', max_length=50, blank=True, null=True)  # Field name made lowercase.
    punprovincia = models.SmallIntegerField(db_column='PunProvincia', blank=True, null=True)  # Field name made lowercase.
    punpais = models.SmallIntegerField(db_column='PunPais', blank=True, null=True)  # Field name made lowercase.
    codigopostal = models.CharField(db_column='CodigoPostal', max_length=15, blank=True, null=True)  # Field name made lowercase.
    telefonos = models.CharField(db_column='Telefonos', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    puntipoiva = models.IntegerField(db_column='PunTipoIva')  # Field name made lowercase.
    puntipodocumento = models.IntegerField(db_column='PunTipoDocumento', blank=True, null=True)  # Field name made lowercase.
    cuit = models.CharField(db_column='Cuit', max_length=14, blank=True, null=True)  # Field name made lowercase.
    numeroib = models.CharField(db_column='numeroIB', max_length=14, blank=True, null=True)  # Field name made lowercase.
    nrodocumento = models.IntegerField(db_column='NroDocumento', blank=True, null=True)  # Field name made lowercase.
    agenteretencioniva = models.SmallIntegerField(db_column='AgenteRetencionIVA')  # Field name made lowercase.
    expreso = models.SmallIntegerField(db_column='Expreso', blank=True, null=True)  # Field name made lowercase.
    puncalificacion = models.IntegerField(db_column='PunCalificacion', blank=True, null=True)  # Field name made lowercase.
    fechaalta = models.DateTimeField(db_column='FechaAlta', blank=True, null=True)  # Field name made lowercase.
    reduccionretiva = models.DecimalField(db_column='ReduccionRetIVA', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fechavtoiva = models.DateTimeField(db_column='FechaVtoIVA', blank=True, null=True)  # Field name made lowercase.
    formulario576 = models.SmallIntegerField(db_column='Formulario576')  # Field name made lowercase.
    verificariva = models.SmallIntegerField(db_column='VerificarIVA')  # Field name made lowercase.
    fechavtoverificacion = models.DateTimeField(db_column='FechaVtoVerificacion', blank=True, null=True)  # Field name made lowercase.
    puniva = models.SmallIntegerField(db_column='PunIVA', blank=True, null=True)  # Field name made lowercase.
    formularioddjj = models.SmallIntegerField(db_column='FormularioDDJJ')  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    tiporetencion = models.SmallIntegerField(db_column='TipoRetencion', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    exterior = models.SmallIntegerField(db_column='Exterior', blank=True, null=True)  # Field name made lowercase.
    punconventa = models.IntegerField(db_column='PunConVenta', blank=True, null=True)  # Field name made lowercase.
    pymes = models.SmallIntegerField(db_column='Pymes')  # Field name made lowercase.
    noapto = models.SmallIntegerField(db_column='NoApto', blank=True, null=True)  # Field name made lowercase.
    punjurisdiccionib = models.IntegerField(db_column='PunJurisdiccionIB', blank=True, null=True)  # Field name made lowercase.
    retencionib = models.SmallIntegerField(db_column='RetencionIB', blank=True, null=True)  # Field name made lowercase.
    notomariva = models.SmallIntegerField(db_column='NoTomarIVA', blank=True, null=True)  # Field name made lowercase.
    punrecorrido = models.IntegerField(db_column='PunRecorrido', blank=True, null=True)  # Field name made lowercase.
    porcreduccionrg1784 = models.DecimalField(db_column='PorcReduccionRG1784', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fechavtoreduccionrg1784 = models.DateTimeField(db_column='FechaVtoReduccionRG1784', blank=True, null=True)  # Field name made lowercase.
    empleador = models.SmallIntegerField(db_column='Empleador', blank=True, null=True)  # Field name made lowercase.
    punactividadganancias = models.IntegerField(db_column='PunActividadGanancias', blank=True, null=True)  # Field name made lowercase.
    nroingresosbrutos = models.CharField(db_column='NroIngresosBrutos', max_length=15, blank=True, null=True)  # Field name made lowercase.
    percepcioniva = models.SmallIntegerField(db_column='PercepcionIVA', blank=True, null=True)  # Field name made lowercase.
    codigoretencioniva = models.IntegerField(db_column='CodigoRetencionIVA', blank=True, null=True)  # Field name made lowercase.
    codigopercepcioniva = models.IntegerField(db_column='CodigoPercepcionIVA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVProveedores'


class Prvproveedoresacumulados(models.Model):
    punproveedor = models.IntegerField(db_column='PunProveedor')  # Field name made lowercase.
    pagosmes = models.SmallIntegerField(db_column='PagosMes', blank=True, null=True)  # Field name made lowercase.
    pagosanio = models.SmallIntegerField(db_column='PagosAnio', blank=True, null=True)  # Field name made lowercase.
    acumuladopagos = models.DecimalField(db_column='AcumuladoPagos', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    acumuladoretencion = models.DecimalField(db_column='AcumuladoRetencion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa', blank=True, null=True)  # Field name made lowercase.
    punactividadganancias = models.IntegerField(db_column='PunActividadGanancias', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(primary_key=True, )

    class Meta:
        managed = False
        db_table = 'PRVProveedoresAcumulados'


class Prvproveedoresib(models.Model):
    punproveedor = models.IntegerField(db_column='PunProveedor')  # Field name made lowercase.
    punconceptoib = models.IntegerField(db_column='PunConceptoIB')  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVProveedoresIB'


class Prvreferenciastmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    punreferencia = models.IntegerField(db_column='PunReferencia')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    abm = models.CharField(db_column='ABM', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importeconcotizacion = models.DecimalField(db_column='ImporteConCotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVReferenciasTMP'


class Prvremitoitems(models.Model):
    punremitoitem = models.AutoField(primary_key=True, db_column='PunRemitoItem')  # Field name made lowercase.
    punremito = models.IntegerField(db_column='PunRemito')  # Field name made lowercase.
    punitemoc = models.IntegerField(db_column='PunItemOC', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punitemservicio = models.IntegerField(db_column='PunItemServicio', blank=True, null=True)  # Field name made lowercase.
    cantidadtotal = models.DecimalField(db_column='CantidadTotal', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidadtotalscrap = models.DecimalField(db_column='CantidadTotalScrap', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVRemitoItems'


class Prvremitos(models.Model):
    punremito = models.AutoField(primary_key=True, db_column='PunRemito')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='PunProveedor')  # Field name made lowercase.
    prefijo = models.CharField(db_column='Prefijo', max_length=4)  # Field name made lowercase.
    sufijo = models.CharField(db_column='Sufijo', max_length=8)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    punoperacionaduana = models.IntegerField(db_column='PunOperacionAduana', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVRemitos'


class Prvremitosfacturados(models.Model):
    puncomprobante = models.IntegerField(db_column='punComprobante', blank=True, null=True)  # Field name made lowercase.
    punremitoitem = models.IntegerField(db_column='punRemitoItem', blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVRemitosFacturados'


class Prvremitostmp(models.Model):
    idoperacion = models.IntegerField(db_column='idOperacion', blank=True, null=True)  # Field name made lowercase.
    punremito = models.IntegerField(db_column='punRemito', blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVRemitosTMP'


class Prvtipoactganancias(models.Model):
    puntipoactividad = models.SmallIntegerField(db_column='PunTipoActividad')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRVTipoActGanancias'


class Padroniibb(models.Model):
    punitem = models.AutoField(primary_key=True, db_column='PunItem')  # Field name made lowercase.
    fechapublicacion = models.DateTimeField(db_column='FechaPublicacion')  # Field name made lowercase.
    fechadesde = models.DateTimeField(db_column='FechaDesde')  # Field name made lowercase.
    fechahasta = models.DateTimeField(db_column='FechaHasta')  # Field name made lowercase.
    cuit = models.CharField(db_column='Cuit', max_length=15)  # Field name made lowercase.
    tipocontribuyente = models.CharField(db_column='TipoContribuyente', max_length=1)  # Field name made lowercase.
    alicuotapercepcion = models.DecimalField(db_column='AlicuotaPercepcion', max_digits=19, decimal_places=4)  # Field name made lowercase.
    alicuotaretencion = models.DecimalField(db_column='AlicuotaRetencion', max_digits=19, decimal_places=4)  # Field name made lowercase.
    nrogrupopercepcion = models.CharField(db_column='NroGrupoPercepcion', max_length=2)  # Field name made lowercase.
    nrogruporetencion = models.CharField(db_column='NroGrupoRetencion', max_length=2)  # Field name made lowercase.
    punjurisdiccion = models.IntegerField(db_column='PunJurisdiccion', blank=True, null=True)  # Field name made lowercase.
    tiporegimen = models.SmallIntegerField(db_column='TipoRegimen', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PadronIIBB'


class Padroniibbtmp(models.Model):
    idoperacion = models.IntegerField(db_column='IdOperacion', blank=True, null=True)  # Field name made lowercase.
    fechapublicacion = models.CharField(db_column='FechaPublicacion', max_length=8, blank=True, null=True)  # Field name made lowercase.
    fechadesde = models.CharField(db_column='FechaDesde', max_length=8, blank=True, null=True)  # Field name made lowercase.
    fechahasta = models.CharField(db_column='FechaHasta', max_length=8, blank=True, null=True)  # Field name made lowercase.
    cuit = models.CharField(db_column='Cuit', max_length=15, blank=True, null=True)  # Field name made lowercase.
    tipocontribuyente = models.CharField(db_column='TipoContribuyente', max_length=1, blank=True, null=True)  # Field name made lowercase.
    marcaab = models.CharField(db_column='MarcaAB', max_length=1, blank=True, null=True)  # Field name made lowercase.
    marcacambio = models.CharField(db_column='MarcaCambio', max_length=1, blank=True, null=True)  # Field name made lowercase.
    alicuotapercepcion = models.CharField(db_column='AlicuotaPercepcion', max_length=10, blank=True, null=True)  # Field name made lowercase.
    alicuotaretencion = models.CharField(db_column='AlicuotaRetencion', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nrogrupopercepcion = models.CharField(db_column='NroGrupoPercepcion', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nrogruporetencion = models.CharField(db_column='NroGrupoRetencion', max_length=2, blank=True, null=True)  # Field name made lowercase.
    punjurisdiccion = models.IntegerField(db_column='PunJurisdiccion', blank=True, null=True)  # Field name made lowercase.
    tiporegimen = models.SmallIntegerField(db_column='TipoRegimen', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PadronIIBBTmp'


class Pagoefectivotmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    idoperacion2 = models.IntegerField(db_column='IDOperacion2', blank=True, null=True)  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa', blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importepesos = models.DecimalField(db_column='ImportePesos', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PagoEfectivoTMP'


class Pagofondofijotmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    idoperacion2 = models.IntegerField(db_column='IDOperacion2', blank=True, null=True)  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa', blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PagoFondoFijoTMP'


class Parametrosgenerales(models.Model):
    punparametro = models.AutoField(primary_key=True, db_column='PunParametro')  # Field name made lowercase.
    etiqueta = models.CharField(db_column='Etiqueta', max_length=30)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255)  # Field name made lowercase.
    valornumerico = models.DecimalField(db_column='ValorNumerico', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valorcaracter = models.CharField(db_column='ValorCaracter', max_length=255, blank=True, null=True)  # Field name made lowercase.
    valorfecha = models.DateTimeField(db_column='ValorFecha', blank=True, null=True)  # Field name made lowercase.
    valorboolean = models.SmallIntegerField(db_column='ValorBoolean', blank=True, null=True)  # Field name made lowercase.
    valortexto = models.TextField(db_column='ValorTexto', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tipovalor = models.IntegerField(db_column='TipoValor', blank=True, null=True)  # Field name made lowercase.
    storedproc = models.CharField(db_column='StoredProc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    spbusquedatabla = models.CharField(db_column='SPBusquedaTabla', max_length=50, blank=True, null=True)  # Field name made lowercase.
    campoadditem = models.CharField(db_column='CampoAddItem', max_length=30, blank=True, null=True)  # Field name made lowercase.
    campoitemdata = models.CharField(db_column='CampoItemData', max_length=30, blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ParametrosGenerales'


class Partediario(models.Model):
    punpartediario = models.AutoField(db_column='punParteDiario', primary_key=True)  # Field name made lowercase.
    punoperario = models.ForeignKey(Operario, models.DO_NOTHING, db_column='punOperario', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(blank=True, null=True)
    borrado = models.BooleanField(blank=True, null=True)
    ingreso = models.BooleanField(db_column='Ingreso', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ParteDiario'


class Partediarioitem(models.Model):
    punpartediarioitem = models.AutoField(db_column='PunParteDiarioItem', primary_key=True)  # Field name made lowercase.
    punpartediario = models.ForeignKey(Partediario, models.DO_NOTHING, db_column='PunParteDiario', blank=True, null=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT', blank=True, null=True)  # Field name made lowercase.
    punmaquina = models.IntegerField(db_column='PunMaquina', blank=True, null=True)  # Field name made lowercase.
    punoperacion = models.ForeignKey(Operacion, models.DO_NOTHING, db_column='PunOperacion', blank=True, null=True)  # Field name made lowercase.
    horainicio = models.DateTimeField(db_column='HoraInicio', blank=True, null=True)  # Field name made lowercase.
    horafin = models.DateTimeField(db_column='HoraFin', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    horaoperariocosto = models.DecimalField(db_column='HoraOperarioCosto', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    horaoperariopunmoneda = models.IntegerField(db_column='HoraOperarioPunMoneda', blank=True, null=True)  # Field name made lowercase.
    horaoperariocotizacion = models.DecimalField(db_column='HoraOperarioCotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    horamaquinacosto = models.DecimalField(db_column='HoraMaquinaCosto', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    horamaquinapunmoneda = models.DecimalField(db_column='HoraMaquinaPunMoneda', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    horamaquinacotizacion = models.DecimalField(db_column='HoraMaquinaCotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    minutos = models.IntegerField(blank=True, null=True)
    punreasignacionot = models.IntegerField(db_column='PunReasignacionOT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ParteDiarioItem'


class Partediarioitemstmp(models.Model):
    punpartediarioitem = models.IntegerField(db_column='PunParteDiarioItem', blank=True, null=True)  # Field name made lowercase.
    punpartediario = models.IntegerField(db_column='PunParteDiario', blank=True, null=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT', blank=True, null=True)  # Field name made lowercase.
    punmaquina = models.IntegerField(db_column='PunMaquina', blank=True, null=True)  # Field name made lowercase.
    punoperacion = models.IntegerField(db_column='PunOperacion', blank=True, null=True)  # Field name made lowercase.
    horainicio = models.DateTimeField(db_column='HoraInicio', blank=True, null=True)  # Field name made lowercase.
    horafin = models.DateTimeField(db_column='HoraFin', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    modoabm = models.IntegerField(db_column='ModoABM', blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='IdOperacion', blank=True, null=True)  # Field name made lowercase.
    minutos = models.IntegerField(db_column='Minutos', blank=True, null=True)  # Field name made lowercase.
    horaoperariocosto = models.DecimalField(db_column='HoraOperarioCosto', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    horaoperariopunmoneda = models.IntegerField(db_column='HoraOperarioPunMoneda', blank=True, null=True)  # Field name made lowercase.
    horaoperariocotizacion = models.DecimalField(db_column='HoraOperarioCotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    horamaquinacosto = models.DecimalField(db_column='HoraMaquinaCosto', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    horamaquinapunmoneda = models.IntegerField(db_column='HoraMaquinaPunMoneda', blank=True, null=True)  # Field name made lowercase.
    horamaquinacotizacion = models.DecimalField(db_column='HoraMaquinaCotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punreasignacionot = models.IntegerField(db_column='PunReasignacionOT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ParteDiarioItemsTMP'


class Percepcionesibtmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion', blank=True, null=True)  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    punjurisdiccionib = models.IntegerField(db_column='PunJurisdiccionIB', blank=True, null=True)  # Field name made lowercase.
    porcentajepercepcionib = models.DecimalField(db_column='PorcentajePercepcionIB', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importepercibido = models.DecimalField(db_column='ImportePercibido', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    minimoapercibir = models.DecimalField(db_column='MinimoAPercibir', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PercepcionesIBTMP'


class Piibbpercepcionesnctmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    puntipoimporte = models.IntegerField(db_column='PunTipoImporte')  # Field name made lowercase.
    punreferencia = models.IntegerField(db_column='PunReferencia', blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    numeroret = models.CharField(db_column='NumeroRet', max_length=20, blank=True, null=True)  # Field name made lowercase.
    punjurisdiccion = models.IntegerField(db_column='PunJurisdiccion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PiibbPercepcionesNCTMP'


class Planocliente(models.Model):
    punplanocliente = models.AutoField(db_column='PunPlanoCliente', primary_key=True)  # Field name made lowercase.
    punarticulo = models.ForeignKey(Articulos, models.DO_NOTHING, db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=20, blank=True, null=True)  # Field name made lowercase.
    revision = models.CharField(db_column='Revision', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fecharevision = models.DateTimeField(db_column='FechaRevision', blank=True, null=True)  # Field name made lowercase.
    vigente = models.BooleanField(db_column='Vigente', blank=True, null=True)  # Field name made lowercase.
    punplanosinpar = models.IntegerField(db_column='PunPlanoSinPar', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlanoCliente'


class Planoclientetmp(models.Model):
    idoperacion = models.IntegerField(db_column='IdOperacion')  # Field name made lowercase.
    punplanocliente = models.IntegerField(db_column='PunPlanoCliente', blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=20, blank=True, null=True)  # Field name made lowercase.
    revision = models.CharField(db_column='Revision', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fecharevision = models.DateTimeField(db_column='FechaRevision', blank=True, null=True)  # Field name made lowercase.
    vigente = models.BooleanField(db_column='Vigente', blank=True, null=True)  # Field name made lowercase.
    punplanosinpar = models.IntegerField(db_column='PunPlanoSinPar', blank=True, null=True)  # Field name made lowercase.
    modoabm = models.IntegerField(db_column='ModoABM')  # Field name made lowercase.
    nuevo = models.CharField(db_column='Nuevo', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlanoClienteTMP'


class Planospclitmp(models.Model):
    punplanocliente = models.IntegerField(db_column='PunPlanoCliente', blank=True, null=True)  # Field name made lowercase.
    punplanosinpar = models.IntegerField(db_column='PunPlanoSinPar', blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.BigIntegerField(db_column='IdOperacion', blank=True, null=True)  # Field name made lowercase.
    modoabm = models.IntegerField(db_column='ModoAbm', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlanoSPCLITmp'


class Planosinpar(models.Model):
    punplanosinpar = models.AutoField(db_column='punPlanoSinPar', primary_key=True)  # Field name made lowercase.
    punarticulo = models.ForeignKey(Articulos, models.DO_NOTHING, db_column='punArticulo', blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=20, blank=True, null=True)  # Field name made lowercase.
    revision = models.CharField(db_column='Revision', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fecharevision = models.DateTimeField(db_column='FechaRevision', blank=True, null=True)  # Field name made lowercase.
    vigente = models.BooleanField(db_column='Vigente', blank=True, null=True)  # Field name made lowercase.
    archivo = models.CharField(db_column='Archivo', max_length=250, blank=True, null=True)  # Field name made lowercase.
    usar = models.CharField(db_column='Usar', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nuevo = models.CharField(db_column='Nuevo', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlanoSinPar'


class Planosinpartmp(models.Model):
    idoperacion = models.IntegerField(db_column='IdOperacion')  # Field name made lowercase.
    punplanosinpar = models.IntegerField(db_column='punPlanoSinPar', blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='punArticulo', blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=20, blank=True, null=True)  # Field name made lowercase.
    revision = models.CharField(db_column='Revision', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fecharevision = models.DateTimeField(db_column='FechaRevision', blank=True, null=True)  # Field name made lowercase.
    vigente = models.BooleanField(db_column='Vigente', blank=True, null=True)  # Field name made lowercase.
    archivo = models.CharField(db_column='Archivo', max_length=250, blank=True, null=True)  # Field name made lowercase.
    modoabm = models.IntegerField(db_column='ModoABM', blank=True, null=True)  # Field name made lowercase.
    usar = models.CharField(db_column='Usar', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nuevo = models.CharField(db_column='Nuevo', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlanoSinParTMP'


class Posicionarancelariatmp(models.Model):
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    posicion = models.CharField(db_column='Posicion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PosicionArancelariaTMP'


class Presupuestoitemtmp(models.Model):
    idoperacion = models.IntegerField(db_column='idOperacion', blank=True, null=True)  # Field name made lowercase.
    puninsumo = models.IntegerField(db_column='PunInsumo', blank=True, null=True)  # Field name made lowercase.
    punbys = models.IntegerField(db_column='punByS', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    pununidad = models.IntegerField(db_column='punUnidad', blank=True, null=True)  # Field name made lowercase.
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    punitempres = models.IntegerField(db_column='punItemPres', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    porciva = models.DecimalField(db_column='porcIva', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    punpedidocliente = models.IntegerField(db_column='punPedidoCliente', blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='punMoneda', blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='punArticulo', blank=True, null=True)  # Field name made lowercase.
    fechaentrega = models.DateTimeField(db_column='FechaEntrega', blank=True, null=True)  # Field name made lowercase.
    importacion = models.SmallIntegerField(db_column='Importacion', blank=True, null=True)  # Field name made lowercase.
    item = models.IntegerField(db_column='Item', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PresupuestoItemTMP'


class Presupuestoitems(models.Model):
    punitempres = models.AutoField(primary_key=True, db_column='PunItemPres')  # Field name made lowercase.
    punpresupuesto = models.IntegerField(db_column='PunPresupuesto')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    puninsumo = models.IntegerField(db_column='PunInsumo', blank=True, null=True)  # Field name made lowercase.
    punbys = models.IntegerField(db_column='PunByS', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4)  # Field name made lowercase.
    pununidad = models.IntegerField(db_column='PunUnidad')  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda', blank=True, null=True)  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porciva = models.DecimalField(db_column='PorcIva', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fechaentrega = models.DateTimeField(db_column='FechaEntrega', blank=True, null=True)  # Field name made lowercase.
    punpedidocliente = models.IntegerField(db_column='PunPedidoCliente', blank=True, null=True)  # Field name made lowercase.
    importacion = models.SmallIntegerField(db_column='Importacion', blank=True, null=True)  # Field name made lowercase.
    item = models.IntegerField(db_column='Item', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PresupuestoItems'


class Presupuestoproveedor(models.Model):
    punpresupuesto = models.IntegerField(db_column='punPresupuesto', blank=True, null=True)  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='punProveedor', blank=True, null=True)  # Field name made lowercase.
    nombreprv = models.CharField(db_column='NombrePRV', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telefonoprv = models.CharField(db_column='telefonoPRV', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PresupuestoProveedor'


class Presupuestoproveedortmp(models.Model):
    idoperacion = models.IntegerField(db_column='idOperacion', blank=True, null=True)  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='punProveedor', blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50, blank=True, null=True)
    telefonos = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PresupuestoProveedorTMP'


class Presupuestotmp(models.Model):
    idoperacion = models.IntegerField(db_column='idOperacion', blank=True, null=True)  # Field name made lowercase.
    idoperacion2 = models.IntegerField(db_column='idOperacion2', blank=True, null=True)  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='punProveedor', blank=True, null=True)  # Field name made lowercase.
    nombreprv = models.CharField(db_column='nombrePRV', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telefonoprv = models.CharField(db_column='telefonoPRV', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nropresupuesto = models.IntegerField(db_column='NroPresupuesto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PresupuestoTMP'


class Presupuestos(models.Model):
    punpresupuesto = models.AutoField(primary_key=True, db_column='PunPresupuesto')  # Field name made lowercase.
    nropresupuesto = models.IntegerField(db_column='NroPresupuesto')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='PunProveedor', blank=True, null=True)  # Field name made lowercase.
    nombreprv = models.CharField(db_column='NombrePRV', max_length=150, blank=True, null=True)  # Field name made lowercase.
    telefonoprv = models.CharField(db_column='TelefonoPRV', max_length=80, blank=True, null=True)  # Field name made lowercase.
    nropresupuestoprv = models.IntegerField(db_column='NroPresupuestoPRV', blank=True, null=True)  # Field name made lowercase.
    puncondicionpago = models.IntegerField(db_column='PunCondicionPago', blank=True, null=True)  # Field name made lowercase.
    fechavto = models.DateTimeField(db_column='FechaVto', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Presupuestos'


class Previsioncomprobantes(models.Model):
    punprevision = models.IntegerField(db_column='PunPrevision')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    punorigen = models.SmallIntegerField(db_column='PunOrigen')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrevisionComprobantes'


class Previsionescashflow(models.Model):
    punprevision = models.AutoField(primary_key=True, db_column='PunPrevision')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    tipoingresoegreso = models.SmallIntegerField(db_column='TipoIngresoEgreso')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    fechavto = models.DateTimeField(db_column='FechaVto')  # Field name made lowercase.
    puntipoprevision = models.IntegerField(db_column='PunTipoPrevision')  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=255, blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda', blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.FloatField(db_column='Cotizacion', blank=True, null=True)  # Field name made lowercase.
    puncashflow = models.IntegerField(db_column='PunCashFlow', blank=True, null=True)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrevisionesCashFlow'


class Previsionestmp(models.Model):
    idoperacion = models.IntegerField(db_column='IdOperacion')  # Field name made lowercase.
    punprevision = models.IntegerField(db_column='PunPrevision')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='punMOneda', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PrevisionesTMP'


class Promediohistorico(models.Model):
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.
    punmaquina = models.IntegerField(db_column='PunMaquina')  # Field name made lowercase.
    punoperacion = models.IntegerField(db_column='PunOperacion')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4)  # Field name made lowercase.
    horas = models.DecimalField(db_column='Horas', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PromedioHistorico'


class Propiedad(models.Model):
    punpropiedad = models.AutoField(db_column='PunPropiedad', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', unique=True, max_length=100)  # Field name made lowercase.
    puntipodato = models.ForeignKey('Hctipodato', models.DO_NOTHING, db_column='PunTipoDato')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Propiedad'


class Provincias(models.Model):
    punprovincia = models.AutoField(db_column='PunProvincia', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado')  # Field name made lowercase.
    codigodgi = models.IntegerField(db_column='CodigoDGI', blank=True, null=True)  # Field name made lowercase.
    punpais = models.IntegerField(db_column='PunPais', blank=True, null=True)  # Field name made lowercase.
    padronseparado = models.SmallIntegerField(db_column='PadronSeparado', blank=True, null=True)  # Field name made lowercase.
    codigoarba = models.CharField(db_column='CodigoARBA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    obligacot = models.BooleanField(db_column='ObligaCOT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Provincias'


class Provinciasjurisdicciones(models.Model):
    punprovincia = models.IntegerField(db_column='PunProvincia')  # Field name made lowercase.
    punjurisdiccionib = models.IntegerField(db_column='PunJurisdiccionIB')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProvinciasJurisdicciones'


class Rg3685Presentaciones(models.Model):
    punpresentacion = models.AutoField(primary_key=True, db_column='PunPresentacion')  # Field name made lowercase.
    fechadesde = models.DateTimeField(db_column='FechaDesde', blank=True, null=True)  # Field name made lowercase.
    fechahasta = models.DateTimeField(db_column='FechaHasta', blank=True, null=True)  # Field name made lowercase.
    secuencia = models.SmallIntegerField(db_column='Secuencia')  # Field name made lowercase.
    numero = models.SmallIntegerField(db_column='Numero')  # Field name made lowercase.
    prorratearcf = models.CharField(db_column='ProrratearCF', max_length=1)  # Field name made lowercase.
    creditofiscalcomputable = models.SmallIntegerField(db_column='CreditoFiscalComputable', blank=True, null=True)  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    importecfcomputable = models.DecimalField(db_column='ImporteCFComputable', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importecfcomputablead = models.DecimalField(db_column='ImporteCFComputableAD', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importecfcomputableprorrateo = models.DecimalField(db_column='ImporteCFComputableProrrateo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importecfnocomputable = models.DecimalField(db_column='ImporteCFNOComputable', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importecfcontribss = models.DecimalField(db_column='ImporteCFContribSS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importecfcomputablecontribss = models.DecimalField(db_column='ImporteCFComputableContribSS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RG3685Presentaciones'


class Reclamodeuda(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion', blank=True, null=True)  # Field name made lowercase.
    seleccionado = models.SmallIntegerField(db_column='Seleccionado', blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    razonsocial = models.CharField(db_column='RazonSocial', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.SmallIntegerField(db_column='PunMoneda', blank=True, null=True)  # Field name made lowercase.
    deudavencida = models.DecimalField(db_column='DeudaVencida', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    deudaavencer = models.DecimalField(db_column='DeudaAVencer', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    diaspromediovencido = models.IntegerField(db_column='DiasPromedioVencido', blank=True, null=True)  # Field name made lowercase.
    diaspromedioavencer = models.IntegerField(db_column='DiasPromedioAVencer', blank=True, null=True)  # Field name made lowercase.
    totaldeuda = models.DecimalField(db_column='TotalDeuda', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totaldeudaenpesos = models.DecimalField(db_column='TotalDeudaEnPesos', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pendientedeimputar = models.DecimalField(db_column='PendienteDeImputar', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ultimoenvio = models.CharField(db_column='UltimoEnvio', max_length=20, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(primary_key=True, db_column='ID')  # Field name made lowercase.
    cantidadmonedas = models.SmallIntegerField(db_column='CantidadMonedas', blank=True, null=True)  # Field name made lowercase.
    seleccion = models.SmallIntegerField(blank=True, null=True)
    fechaoriginal = models.DateTimeField(db_column='FechaOriginal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReclamoDeuda'


class Reclamodeudadetalle(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion', blank=True, null=True)  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PuNCliente', blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda', blank=True, null=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    fechaemision = models.DateTimeField(db_column='FechaEmision', blank=True, null=True)  # Field name made lowercase.
    fechavencimiento = models.DateTimeField(db_column='FechaVencimiento', blank=True, null=True)  # Field name made lowercase.
    dias = models.IntegerField(db_column='Dias', blank=True, null=True)  # Field name made lowercase.
    adeudado = models.DecimalField(db_column='Adeudado', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    adeudadoenpesos = models.DecimalField(db_column='AdeudadoEnPesos', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punvendedor = models.IntegerField(db_column='PunVendedor', blank=True, null=True)  # Field name made lowercase.
    punsucursal = models.IntegerField(db_column='PunSucursal', blank=True, null=True)  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID', blank=True, primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReclamoDeudaDetalle'


class Reclamodeudapendientedeimputar(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion', blank=True, null=True)  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    punvendedor = models.IntegerField(db_column='PunVendedor', blank=True, null=True)  # Field name made lowercase.
    punsucursal = models.IntegerField(db_column='PunSucursal', blank=True, null=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda', blank=True, null=True)  # Field name made lowercase.
    saldo = models.DecimalField(db_column='Saldo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    saldoenpesos = models.DecimalField(db_column='SaldoEnPesos', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReclamoDeudaPendienteDeImputar'


class Recorridos(models.Model):
    punrecorrido = models.AutoField(primary_key=True, db_column='PunRecorrido')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=80, blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Recorridos'


class Referenciastmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion', blank=True, null=True)  # Field name made lowercase.
    punnuevareferencia = models.IntegerField(db_column='PunNuevaReferencia', blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReferenciasTMP'


class Remitoitemdistridepositotmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDoperacion', blank=True, null=True)  # Field name made lowercase.
    punitemoc = models.IntegerField(db_column='PunItemOC', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    pundeposito = models.IntegerField(db_column='PunDeposito', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RemitoItemDistriDepositoTMP'


class Remitotransporte(models.Model):
    punremitotransporte = models.AutoField(primary_key=True, db_column='PunRemitoTransporte')  # Field name made lowercase.
    prefijo = models.CharField(db_column='Prefijo', max_length=4)  # Field name made lowercase.
    sufijo = models.CharField(db_column='Sufijo', max_length=8)  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='PunProveedor')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    valordeclarado = models.CharField(db_column='ValorDeclarado', max_length=50)  # Field name made lowercase.
    pesocarga = models.CharField(db_column='PesoCarga', max_length=50)  # Field name made lowercase.
    detallecarga = models.TextField(db_column='DetalleCarga', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fechaentrega = models.DateTimeField(db_column='FechaEntrega', blank=True, null=True)  # Field name made lowercase.
    puntiporesponsableentrega = models.IntegerField(db_column='PunTipoResponsableEntrega', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    paquetes = models.CharField(db_column='Paquetes', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nropaquete = models.CharField(db_column='NroPaquete', max_length=8, blank=True, null=True)  # Field name made lowercase.
    puntero = models.IntegerField(blank=True, null=True)
    puncliente = models.IntegerField(db_column='PunCliente')  # Field name made lowercase.
    etiquetas = models.IntegerField(db_column='Etiquetas')  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RemitoTransporte'


class Remitotransportecarga(models.Model):
    punremitotransporte = models.IntegerField(db_column='PunRemitoTransporte')  # Field name made lowercase.
    puntipocarga = models.IntegerField(db_column='PunTipoCarga')  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RemitoTransporteCarga'


class Rentabilidadbase(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion', blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importefacturado = models.DecimalField(db_column='ImporteFacturado', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dtoprontopago = models.DecimalField(db_column='DtoProntoPago', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valorfob = models.DecimalField(db_column='ValorFOB', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punmonedafob = models.IntegerField(db_column='PunMonedaFOB', blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    punreferencia = models.IntegerField(db_column='PunReferencia', blank=True, null=True)  # Field name made lowercase.
    coeficiente = models.FloatField(blank=True, null=True)
    importeoi = models.DecimalField(db_column='ImporteOI', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    puncomprobanteoi = models.IntegerField(db_column='puncomprobanteOI', blank=True, null=True)  # Field name made lowercase.
    importeconiva = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    puncliente = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    punsucursal = models.IntegerField(db_column='punSucursal', blank=True, null=True)  # Field name made lowercase.
    nroot = models.CharField(db_column='NroOT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cantidadot = models.DecimalField(db_column='CantidadOT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    costouniot = models.DecimalField(db_column='CostoUniOT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT', blank=True, null=True)  # Field name made lowercase.
    ordenot = models.SmallIntegerField(db_column='OrdenOT', blank=True, null=True)  # Field name made lowercase.
    cantidadcomprob = models.DecimalField(db_column='CantidadComprob', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tipocbiovta = models.DecimalField(db_column='TipoCbioVta', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tipocbiocosto = models.DecimalField(db_column='TipoCbioCosto', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valorfoboriginal = models.DecimalField(db_column='ValorFOBOriginal', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    costouniotoriginal = models.DecimalField(db_column='CostoUniOTOriginal', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RentabilidadBase'


class Reporteparametros(models.Model):
    reporteoriginal = models.CharField(db_column='ReporteOriginal', max_length=150)  # Field name made lowercase.
    nombreparametro = models.CharField(db_column='NombreParametro', max_length=150)  # Field name made lowercase.
    tipo = models.IntegerField(db_column='Tipo')  # Field name made lowercase.
    orden = models.IntegerField(db_column='Orden')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReporteParametros'


class Reportes(models.Model):
    reporteoriginal = models.CharField(db_column='ReporteOriginal', max_length=150)  # Field name made lowercase.
    reportecr10 = models.CharField(db_column='ReporteCR10', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Reportes'


class Retenciongananciatmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=20)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa', blank=True, null=True)  # Field name made lowercase.
    puntiporetencion = models.IntegerField(db_column='PunTipoRetencion', blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='punMoneda', blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RetencionGananciaTMP'


class Retencioniva(models.Model):
    punoi = models.IntegerField(db_column='PunOI')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    numerocertificado = models.CharField(db_column='NumeroCertificado', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RetencionIVA'


class Rubrosarticulos(models.Model):
    punrubro = models.AutoField(db_column='PunRubro', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=4)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado')  # Field name made lowercase.
    puntipoot = models.IntegerField(db_column='PunTipoOT', blank=True, null=True)  # Field name made lowercase.
    generaot = models.BooleanField(db_column='GeneraOT', blank=True, null=True)  # Field name made lowercase.
    excluirderentabilidad = models.SmallIntegerField(db_column='ExcluirDeRentabilidad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RubrosArticulos'


class Rubrosarticulosdescuentos(models.Model):
    punrubro = models.IntegerField(db_column='PunRubro')  # Field name made lowercase.
    descuento = models.DecimalField(db_column='Descuento', max_digits=19, decimal_places=4)  # Field name made lowercase.
    orden = models.SmallIntegerField(db_column='Orden')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RubrosArticulosDescuentos'


class Rubrosarticulosdescuentostmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    descuento = models.DecimalField(db_column='Descuento', max_digits=19, decimal_places=4)  # Field name made lowercase.
    orden = models.SmallIntegerField(db_column='Orden')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RubrosArticulosDescuentosTMP'


class Rubrosbys(models.Model):
    punrubro = models.AutoField(primary_key=True, db_column='PunRubro')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=4)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RubrosByS'


class Rubrosinsumos(models.Model):
    punrubro = models.AutoField(primary_key=True, db_column='PunRubro')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=4)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RubrosInsumos'


class Smatmp(models.Model):
    punmovimiento = models.IntegerField(db_column='PunMovimiento')  # Field name made lowercase.
    pundeposito = models.IntegerField(db_column='PunDeposito')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    puntipomovimiento = models.IntegerField(db_column='PunTipoMovimiento')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punremitoitemventa = models.IntegerField(db_column='PunRemitoItemVenta', blank=True, null=True)  # Field name made lowercase.
    punremitoitemcompra = models.IntegerField(db_column='PunRemitoItemCompra', blank=True, null=True)  # Field name made lowercase.
    punmotivo = models.IntegerField(db_column='PunMotivo', blank=True, null=True)  # Field name made lowercase.
    nroordent = models.CharField(db_column='NroOrdenT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    punremitotransferencia = models.IntegerField(db_column='PunRemitoTransferencia', blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='IdOperacion', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punmovimientoencabezado = models.IntegerField(db_column='PunMovimientoEncabezado', blank=True, null=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT', blank=True, null=True)  # Field name made lowercase.
    punot = models.IntegerField(db_column='PunOT', blank=True, null=True)  # Field name made lowercase.
    tipostock = models.SmallIntegerField(db_column='TipoStock', blank=True, null=True)  # Field name made lowercase.
    punordentorig = models.IntegerField(db_column='PunOrdenTOrig', blank=True, null=True)  # Field name made lowercase.
    orden = models.IntegerField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SMATmp'


class Sectordiaslaborables(models.Model):
    pundialaboral = models.AutoField(db_column='PunDiaLaboral', primary_key=True)  # Field name made lowercase.
    punsector = models.ForeignKey('Sectores', models.DO_NOTHING, db_column='PunSector')  # Field name made lowercase.
    pundia = models.ForeignKey(Diasemana, models.DO_NOTHING, db_column='PunDia')  # Field name made lowercase.
    punturno = models.ForeignKey('Turnos', models.DO_NOTHING, db_column='PunTurno')  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SectorDiasLaborables'


class Sectordiaslaborablestmp(models.Model):
    pundialaboral = models.IntegerField(db_column='PunDiaLaboral', blank=True, null=True)  # Field name made lowercase.
    punsector = models.IntegerField(db_column='PunSector', blank=True, null=True)  # Field name made lowercase.
    pundia = models.IntegerField(db_column='PunDia', blank=True, null=True)  # Field name made lowercase.
    punturno = models.IntegerField(db_column='PunTurno', blank=True, null=True)  # Field name made lowercase.
    modoabm = models.IntegerField(db_column='ModoAbm', blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='idOperacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SectorDiasLaborablesTmp'


class Sectordiasnolaborables(models.Model):
    pundianolaboral = models.AutoField(db_column='PunDiaNoLaboral', primary_key=True)  # Field name made lowercase.
    punsector = models.ForeignKey('Sectores', models.DO_NOTHING, db_column='PunSector')  # Field name made lowercase.
    fechadesde = models.DateTimeField(db_column='FechaDesde')  # Field name made lowercase.
    fechahasta = models.DateTimeField(db_column='FechaHasta', blank=True, null=True)  # Field name made lowercase.
    motivo = models.CharField(db_column='Motivo', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SectorDiasNoLaborables'


class Sectordiasnolaborablestmp(models.Model):
    pundianolaboral = models.IntegerField(db_column='PunDiaNoLaboral', blank=True, null=True)  # Field name made lowercase.
    punsector = models.IntegerField(db_column='PunSector', blank=True, null=True)  # Field name made lowercase.
    fechadesde = models.DateTimeField(db_column='FechaDesde', blank=True, null=True)  # Field name made lowercase.
    fechahasta = models.DateTimeField(db_column='FechaHasta', blank=True, null=True)  # Field name made lowercase.
    motivo = models.CharField(db_column='Motivo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modoabm = models.IntegerField(db_column='ModoABM', blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.BigIntegerField(db_column='idOperacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SectorDiasNoLaborablesTMP'


class Sectores(models.Model):
    punsector = models.AutoField(db_column='PunSector', primary_key=True)  # Field name made lowercase.
    simbolo = models.CharField(db_column='Simbolo', max_length=5)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sectores'


class Sinfinleo(models.Model):
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    precio = models.FloatField(db_column='Precio', blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda', blank=True, null=True)  # Field name made lowercase.
    punlistaprecio = models.IntegerField(db_column='PunListaPrecio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SinFinLeo'


class Sistema(models.Model):
    punsistema = models.AutoField(db_column='punSistema', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    archivoexe = models.CharField(db_column='ArchivoExe', max_length=100, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sistema'


class Stockarticulos(models.Model):
    pundeposito = models.IntegerField(db_column='PunDeposito', primary_key=True)  # Field name made lowercase. The composite primary key (PunDeposito, PunArticulo) found, that is not supported. The first column is selected.
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.
    stock = models.DecimalField(db_column='Stock', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StockArticulos'
        unique_together = (('pundeposito', 'punarticulo'),)


class Stockbase(models.Model):
    pun = models.AutoField(primary_key=True, db_column='Pun')  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='IdOperacion', blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    punpedido = models.IntegerField(db_column='PunPedido', blank=True, null=True)  # Field name made lowercase.
    punitempedido = models.IntegerField(db_column='PunItemPedido', blank=True, null=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT', blank=True, null=True)  # Field name made lowercase.
    nroordent = models.CharField(db_column='NroOrdenT', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cantidadpedida = models.DecimalField(db_column='CantidadPedida', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidadenviada = models.DecimalField(db_column='CantidadEnviada', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidadafabricar = models.DecimalField(db_column='CantidadAFabricar', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidadcomenzada = models.DecimalField(db_column='CantidadComenzada', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidadafabricarreal = models.DecimalField(db_column='CantidadAFabricarReal', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidadascrap = models.DecimalField(db_column='CantidadASCRAP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidadreasignada = models.DecimalField(db_column='CantidadReasignada', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidadreasignadarecibida = models.DecimalField(db_column='CantidadReasignadaRecibida', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidadentregada = models.DecimalField(db_column='CantidadEntregada', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    faltaentregar = models.DecimalField(db_column='FaltaEntregar', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    stock = models.DecimalField(db_column='Stock', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    stockexcedente = models.DecimalField(db_column='StockExcedente', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    orden = models.SmallIntegerField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StockBase'


class Stockmovimientoarticuloencabezado(models.Model):
    punmovimientoencabezado = models.AutoField(primary_key=True, db_column='PunMovimientoEncabezado')  # Field name made lowercase.
    prefijo = models.CharField(db_column='Prefijo', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sufijo = models.CharField(db_column='Sufijo', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StockMovimientoArticuloEncabezado'


class Stockmovimientoarticulotmp(models.Model):
    idoperacion2 = models.IntegerField(db_column='idOperacion2', blank=True, null=True)  # Field name made lowercase.
    pundeposito = models.IntegerField(db_column='punDeposito', blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='punArticulo', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    puntipomovimiento = models.IntegerField(db_column='punTipoMovimiento', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punremitoitemventa = models.IntegerField(db_column='PunRemitoItemVenta', blank=True, null=True)  # Field name made lowercase.
    punremitoitemcompra = models.IntegerField(db_column='PunRemitoItemCompra', blank=True, null=True)  # Field name made lowercase.
    punmotivo = models.IntegerField(db_column='PunMotivo', blank=True, null=True)  # Field name made lowercase.
    nroordent = models.CharField(db_column='NroOrdenT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    punremitotransferencia = models.IntegerField(db_column='PunRemitoTransferencia', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT', blank=True, null=True)  # Field name made lowercase.
    generaot = models.SmallIntegerField(db_column='GeneraOT', blank=True, null=True)  # Field name made lowercase.
    requierepedido = models.SmallIntegerField(db_column='RequierePedido', blank=True, null=True)  # Field name made lowercase.
    puntero = models.AutoField(primary_key=True, )

    class Meta:
        managed = False
        db_table = 'StockMovimientoArticuloTMP'


class Stockmovimientoinsumoencabezado(models.Model):
    punmovimientoencabezado = models.AutoField(primary_key=True, db_column='punMovimientoEncabezado')  # Field name made lowercase.
    prefijo = models.CharField(db_column='Prefijo', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sufijo = models.CharField(db_column='Sufijo', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StockMovimientoInsumoEncabezado'


class Stockmovimientorelaciontmp(models.Model):
    pun = models.AutoField(primary_key=True, db_column='Pun')  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    puntero = models.IntegerField(db_column='Puntero')  # Field name made lowercase.
    punmovimientostock = models.IntegerField(db_column='PunMovimientoStock')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StockMovimientoRelacionTMP'


class Stockmovimientosarticulos(models.Model):
    punmovimiento = models.AutoField(primary_key=True, db_column='PunMovimiento')  # Field name made lowercase.
    pundeposito = models.IntegerField(db_column='PunDeposito')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    puntipomovimiento = models.IntegerField(db_column='PunTipoMovimiento')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punremitoitemventa = models.IntegerField(db_column='PunRemitoItemVenta', blank=True, null=True)  # Field name made lowercase.
    punremitoitemcompra = models.IntegerField(db_column='PunRemitoItemCompra', blank=True, null=True)  # Field name made lowercase.
    punmotivo = models.IntegerField(db_column='PunMotivo', blank=True, null=True)  # Field name made lowercase.
    nroordent = models.CharField(db_column='NroOrdenT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    punremitotransferencia = models.IntegerField(db_column='PunRemitoTransferencia', blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='IdOperacion', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punmovimientoencabezado = models.IntegerField(db_column='PunMovimientoEncabezado', blank=True, null=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT', blank=True, null=True)  # Field name made lowercase.
    tipostock = models.SmallIntegerField(db_column='TipoStock', blank=True, null=True)  # Field name made lowercase.
    punmovimientoorigen = models.IntegerField(db_column='PunMovimientoOrigen', blank=True, null=True)  # Field name made lowercase.
    punremitoitemcompraanterior = models.IntegerField(db_column='PunRemitoItemCompraAnterior', blank=True, null=True)  # Field name made lowercase.
    momento = models.DateTimeField(db_column='Momento', blank=True, null=True)  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='PunUsuario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StockMovimientosArticulos'


class Stockmovimientosinsumos(models.Model):
    pundeposito = models.IntegerField(db_column='PunDeposito')  # Field name made lowercase.
    puninsumo = models.IntegerField(db_column='PunInsumo')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    puntipomovimiento = models.IntegerField(db_column='PunTipoMovimiento')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punremitoitemventa = models.IntegerField(db_column='PunRemitoItemVenta', blank=True, null=True)  # Field name made lowercase.
    punremitoitemcompra = models.IntegerField(db_column='PunRemitoItemCompra', blank=True, null=True)  # Field name made lowercase.
    punmotivo = models.IntegerField(db_column='PunMotivo', blank=True, null=True)  # Field name made lowercase.
    punremitotransferencia = models.IntegerField(db_column='PunRemitoTransferencia', blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='IdOperacion', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punmovimientoencabezado = models.IntegerField(db_column='punMovimientoEncabezado', blank=True, null=True)  # Field name made lowercase.
    momento = models.DateTimeField(db_column='Momento', blank=True, null=True)  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='PunUsuario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StockMovimientosInsumos'


class Subclasificacionarticulos(models.Model):
    punsubclasificacion = models.AutoField(primary_key=True, db_column='PunSubClasificacion')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    emaildestinatario = models.CharField(db_column='emailDestinatario', max_length=100, blank=True, null=True)  # Field name made lowercase.
    emailreplyto = models.CharField(db_column='emailReplyTo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    emailccopy = models.CharField(db_column='emailCCopy', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SubClasificacionArticulos'


class Subzonas(models.Model):
    punsubzona = models.AutoField(primary_key=True, db_column='PunSubZona')  # Field name made lowercase.
    punzona = models.IntegerField(db_column='PunZona')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SubZonas'


class Sucursales(models.Model):
    punsucursal = models.AutoField(primary_key=True, db_column='punSucursal')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sucursales'


class T540(models.Model):
    puncomprobante = models.IntegerField(db_column='PUNCOMPROBANTE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T540'


class T547(models.Model):
    puncomprobante = models.IntegerField(db_column='PUNCOMPROBANTE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T547'


class Tccomprobantes(models.Model):
    puntccomprobante = models.AutoField(db_column='PunTCComprobante', primary_key=True)  # Field name made lowercase.
    puntarjeta = models.IntegerField(db_column='PunTarjeta')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    punorigen = models.SmallIntegerField(db_column='PunOrigen')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cuotas = models.SmallIntegerField(db_column='Cuotas')  # Field name made lowercase.
    cuotaspagas = models.SmallIntegerField(db_column='CuotasPagas', blank=True, null=True)  # Field name made lowercase.
    nrocupon = models.CharField(db_column='NroCupon', max_length=15, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCComprobantes'


class Tccomprobantestmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion', blank=True, null=True)  # Field name made lowercase.
    idoperacion2 = models.IntegerField(db_column='IDOperacion2', blank=True, null=True)  # Field name made lowercase.
    puntccomprobante = models.IntegerField(db_column='PunTCComprobante', blank=True, null=True)  # Field name made lowercase.
    puntarjeta = models.IntegerField(db_column='PunTarjeta', blank=True, null=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    punorigen = models.SmallIntegerField(db_column='PunOrigen', blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cuotas = models.IntegerField(db_column='Cuotas', blank=True, null=True)  # Field name made lowercase.
    cuotaspagas = models.SmallIntegerField(db_column='CuotasPagas', blank=True, null=True)  # Field name made lowercase.
    nrocupon = models.CharField(db_column='NroCupon', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCComprobantesTMP'


class Tcconceptos(models.Model):
    punconcepto = models.SmallAutoField(db_column='PunConcepto', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    cuenta = models.CharField(db_column='Cuenta', max_length=9)  # Field name made lowercase.
    conceptogravado = models.BooleanField(db_column='ConceptoGravado', blank=True, null=True)  # Field name made lowercase.
    porcentajeiva = models.DecimalField(db_column='PorcentajeIVA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    informarensubdiario = models.SmallIntegerField(db_column='InformarEnSubdiario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCConceptos'


class Tcresumen(models.Model):
    puntcresumen = models.AutoField(db_column='PunTCResumen', primary_key=True)  # Field name made lowercase.
    puntarjeta = models.IntegerField(db_column='PunTarjeta')  # Field name made lowercase.
    nroresumen = models.CharField(db_column='NroResumen', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    fechavto = models.DateTimeField(db_column='FechaVto')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    saldoanterior = models.DecimalField(db_column='SaldoAnterior', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punasiento = models.IntegerField(db_column='PunAsiento')  # Field name made lowercase.
    puncomprobanteoe = models.IntegerField(db_column='PunComprobanteOE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCResumen'


class Tcresumencargos(models.Model):
    puntcresumencargo = models.AutoField(db_column='PunTCResumenCargo', primary_key=True)  # Field name made lowercase.
    puntcresumen = models.IntegerField(db_column='PunTCResumen')  # Field name made lowercase.
    punconcepto = models.SmallIntegerField(db_column='PunConcepto')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    iva = models.DecimalField(db_column='Iva', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porcentajeiva = models.DecimalField(db_column='PorcentajeIva', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCResumenCargos'


class Tcresumencargostmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion', blank=True, null=True)  # Field name made lowercase.
    puntcresumencargo = models.IntegerField(db_column='PunTCResumenCargo', blank=True, null=True)  # Field name made lowercase.
    puntcresumen = models.IntegerField(db_column='PunTCResumen', blank=True, null=True)  # Field name made lowercase.
    punconcepto = models.SmallIntegerField(db_column='PunConcepto', blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    iva = models.DecimalField(db_column='Iva', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porcentajeiva = models.DecimalField(db_column='PorcentajeIva', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(primary_key=True, db_column='Id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCResumenCargosTMP'


class Tcresumendetalle(models.Model):
    puntcresumendetalle = models.AutoField(db_column='PunTCResumenDetalle', primary_key=True)  # Field name made lowercase.
    puntcresumen = models.IntegerField(db_column='PunTCResumen')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    puntccomprobante = models.IntegerField(db_column='PunTCComprobante', blank=True, null=True)  # Field name made lowercase.
    cuota = models.SmallIntegerField(db_column='Cuota', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    comprobante = models.CharField(db_column='Comprobante', max_length=30, blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cuenta = models.CharField(db_column='Cuenta', max_length=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCResumenDetalle'


class Tcresumendetalletmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion', blank=True, null=True)  # Field name made lowercase.
    tipo = models.SmallIntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    puntccomprobante = models.IntegerField(db_column='PunTcComprobante', blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cuota = models.IntegerField(db_column='Cuota', blank=True, null=True)  # Field name made lowercase.
    puntcresumendetalle = models.IntegerField(db_column='PunTCResumenDetalle', blank=True, null=True)  # Field name made lowercase.
    puntcresumen = models.IntegerField(db_column='PunTCResumen', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    comprobante = models.CharField(db_column='Comprobante', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cuenta = models.CharField(db_column='Cuenta', max_length=9, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(primary_key=True, db_column='Id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCResumenDetalleTMP'


class Tcresumenpago(models.Model):
    puntcresumen = models.IntegerField(db_column='PunTCResumen')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    saldoafavor = models.DecimalField(db_column='SaldoAFavor', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TCResumenPago'


class Tctarjetas(models.Model):
    puntarjeta = models.AutoField(db_column='PunTarjeta', primary_key=True)  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    bancoemisor = models.CharField(db_column='BancoEmisor', max_length=80)  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=20)  # Field name made lowercase.
    fechavto = models.DateTimeField(db_column='FechaVto', blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    cuit = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TCTarjetas'


class Tmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion', blank=True, null=True)  # Field name made lowercase.
    fechadesde = models.CharField(db_column='FechaDesde', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fechahasta = models.CharField(db_column='FechaHasta', max_length=20, blank=True, null=True)  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    punvendedor = models.IntegerField(db_column='PunVendedor', blank=True, null=True)  # Field name made lowercase.
    pundistribuidor = models.IntegerField(db_column='PunDistribuidor', blank=True, null=True)  # Field name made lowercase.
    punrubro = models.IntegerField(db_column='PunRubro', blank=True, null=True)  # Field name made lowercase.
    tiporemito = models.SmallIntegerField(db_column='TipoRemito', blank=True, null=True)  # Field name made lowercase.
    endeposito = models.SmallIntegerField(db_column='EnDeposito', blank=True, null=True)  # Field name made lowercase.
    tipofecha = models.SmallIntegerField(db_column='TipoFecha', blank=True, null=True)  # Field name made lowercase.
    ppunlineaproduccion = models.IntegerField(db_column='ppunLineaProduccion', blank=True, null=True)  # Field name made lowercase.
    porigen = models.IntegerField(db_column='pOrigen', blank=True, null=True)  # Field name made lowercase.
    pclientesinactivos = models.IntegerField(db_column='pClientesInactivos', blank=True, null=True)  # Field name made lowercase.
    ppunsucursal = models.IntegerField(db_column='ppunSucursal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMP'


class Tmpproc(models.Model):
    spid = models.SmallIntegerField()
    kpid = models.SmallIntegerField()
    blocked = models.SmallIntegerField()
    waittype = models.TextField()  # This field type is a guess.
    waittime = models.IntegerField()
    lastwaittype = models.CharField(max_length=32)
    waitresource = models.CharField(max_length=256)
    dbid = models.SmallIntegerField()
    uid = models.SmallIntegerField()
    cpu = models.IntegerField()
    physical_io = models.BigIntegerField()
    memusage = models.IntegerField()
    login_time = models.DateTimeField()
    last_batch = models.DateTimeField()
    ecid = models.SmallIntegerField()
    open_tran = models.SmallIntegerField()
    status = models.CharField(max_length=30)
    sid = models.TextField()  # This field type is a guess.
    hostname = models.CharField(max_length=128)
    program_name = models.CharField(max_length=128)
    hostprocess = models.CharField(max_length=8)
    cmd = models.CharField(max_length=16)
    nt_domain = models.CharField(max_length=128)
    nt_username = models.CharField(max_length=128)
    net_address = models.CharField(max_length=12)
    net_library = models.CharField(max_length=12)
    loginame = models.CharField(max_length=128)
    context_info = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'TMPProc'


class Tmpremitos(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion', blank=True, null=True)  # Field name made lowercase.
    fechadesde = models.CharField(db_column='FechaDesde', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fechahasta = models.CharField(db_column='FechaHasta', max_length=20, blank=True, null=True)  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    punvendedor = models.IntegerField(db_column='PunVendedor', blank=True, null=True)  # Field name made lowercase.
    pundistribuidor = models.IntegerField(db_column='PunDistribuidor', blank=True, null=True)  # Field name made lowercase.
    punrubro = models.IntegerField(db_column='PunRubro', blank=True, null=True)  # Field name made lowercase.
    tiporemito = models.SmallIntegerField(db_column='TipoRemito', blank=True, null=True)  # Field name made lowercase.
    endeposito = models.SmallIntegerField(db_column='EnDeposito', blank=True, null=True)  # Field name made lowercase.
    tipofecha = models.SmallIntegerField(db_column='TipoFecha', blank=True, null=True)  # Field name made lowercase.
    ppunlineaproduccion = models.IntegerField(db_column='ppunLineaProduccion', blank=True, null=True)  # Field name made lowercase.
    porigen = models.IntegerField(db_column='pOrigen', blank=True, null=True)  # Field name made lowercase.
    pclientesinactivos = models.IntegerField(db_column='pClientesInactivos', blank=True, null=True)  # Field name made lowercase.
    ppunsucursal = models.IntegerField(db_column='ppunSucursal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TMPREMITOS'


class Tabempresas(models.Model):
    punempresa = models.IntegerField(db_column='PunEmpresa', blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    oe = models.CharField(db_column='OE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    punasiento = models.IntegerField(db_column='PunAsiento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TabEmpresas'


class Tabla1(models.Model):
    puntero = models.AutoField(primary_key=True)
    dato = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tabla1'


class Tablaansi(models.Model):
    caracter = models.CharField(db_column='Caracter', primary_key=True, max_length=1)  # Field name made lowercase.
    codigo = models.IntegerField(db_column='Codigo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TablaANSI'


class Tablasexportacion(models.Model):
    tabla = models.CharField(db_column='Tabla', max_length=50, blank=True, null=True)  # Field name made lowercase.
    campoexcluido = models.CharField(db_column='CampoExcluido', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mensaje = models.CharField(db_column='Mensaje', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TablasExportacion'


class Tablasmaestras(models.Model):
    punmaestra = models.AutoField(primary_key=True, db_column='PunMaestra')  # Field name made lowercase.
    nombretabla = models.CharField(db_column='NombreTabla', max_length=128)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    spselect = models.CharField(db_column='SPSelect', max_length=100)  # Field name made lowercase.
    spinsert = models.CharField(db_column='SPInsert', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spupdate = models.CharField(db_column='SPUpdate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    spdelete = models.CharField(db_column='SPDelete', max_length=100, blank=True, null=True)  # Field name made lowercase.
    campopuntero = models.CharField(db_column='CampoPuntero', max_length=100)  # Field name made lowercase.
    campodescripcion = models.CharField(db_column='CampoDescripcion', max_length=100)  # Field name made lowercase.
    spselrel = models.CharField(db_column='SPSelRel', max_length=100, blank=True, null=True)  # Field name made lowercase.
    campopunrelacionado = models.CharField(db_column='CampoPunRelacionado', max_length=100, blank=True, null=True)  # Field name made lowercase.
    campodescriprelacionado = models.CharField(db_column='CampoDescripRelacionado', max_length=100, blank=True, null=True)  # Field name made lowercase.
    campocodigoalter = models.CharField(db_column='CampoCodigoAlter', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TablasMaestras'


class Table1(models.Model):
    p = models.AutoField(primary_key=True, db_column='P')  # Field name made lowercase.
    d = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Table1'


class Temporal(models.Model):
    punpedido = models.IntegerField(db_column='PunPedido')  # Field name made lowercase.
    simbolo = models.CharField(db_column='Simbolo', max_length=5, blank=True, null=True)  # Field name made lowercase.
    moneda = models.CharField(db_column='Moneda', max_length=100, blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Temporal'


class Timeout(models.Model):
    procedurename = models.CharField(db_column='ProcedureName', primary_key=True, max_length=128)  # Field name made lowercase.
    timeout = models.IntegerField(db_column='TimeOut')  # Field name made lowercase.
    ultimaejecucion = models.DateTimeField(db_column='UltimaEjecucion')  # Field name made lowercase.
    ultimotiempoejecucion = models.DateTimeField(db_column='UltimoTiempoEjecucion', blank=True, null=True)  # Field name made lowercase.
    maximotiempoejecucion = models.DateTimeField(db_column='MaximoTiempoEjecucion', blank=True, null=True)  # Field name made lowercase.
    promediotiempoejecucion = models.DateTimeField(db_column='PromedioTiempoEjecucion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TimeOut'


class Tipoafilado(models.Model):
    puntipoafilado = models.AutoField(db_column='PunTipoAfilado', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=10)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoAfilado'


class Tipoaviso(models.Model):
    puntipoaviso = models.IntegerField(db_column='PunTipoAviso', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    activo = models.BooleanField(db_column='Activo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoAviso'


class Tipocomprobantes(models.Model):
    puntipocomprobante = models.AutoField(primary_key=True, db_column='PunTipoComprobante')  # Field name made lowercase.
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=2)  # Field name made lowercase.
    punagrupado = models.IntegerField(db_column='PunAgrupado')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=120)  # Field name made lowercase.
    tipocomprobanteref = models.CharField(db_column='TipoComprobanteRef', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoComprobantes'


class Tipodocumentos(models.Model):
    puntipodocumento = models.IntegerField(db_column='PunTipoDocumento')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoDocumentos'


class Tipohorarios(models.Model):
    puntipohorario = models.AutoField(primary_key=True, db_column='PunTipoHorario')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150)  # Field name made lowercase.
    borrado = models.IntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoHorarios'


class Tipoimportes(models.Model):
    puntipoimporte = models.IntegerField(db_column='PunTipoImporte')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    punagrupado = models.IntegerField(db_column='PunAgrupado', blank=True, null=True)  # Field name made lowercase.
    impuesto = models.BooleanField(db_column='Impuesto', blank=True, null=True)  # Field name made lowercase.
    codigoafip = models.CharField(db_column='CodigoAfip', max_length=3, blank=True, null=True)  # Field name made lowercase.
    punrg3685 = models.IntegerField(db_column='PunRG3685', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoImportes'


class Tipomensajesfacturacion(models.Model):
    puntipomensaje = models.AutoField(primary_key=True, db_column='PunTipoMensaje')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoMensajesFacturacion'


class Tiponcnd(models.Model):
    puntiponcnd = models.AutoField(primary_key=True, db_column='PunTipoNCND')  # Field name made lowercase.
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=2)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    hardcode = models.SmallIntegerField(db_column='HardCode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoNCND'


class Tipoot(models.Model):
    puntipoot = models.AutoField(primary_key=True, db_column='PunTipoOT')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    prefijo = models.CharField(db_column='Prefijo', max_length=4, blank=True, null=True)  # Field name made lowercase.
    numeracionunica = models.BooleanField(db_column='NumeracionUnica')  # Field name made lowercase.
    puntipoorigen = models.IntegerField(db_column='PunTipoOrigen')  # Field name made lowercase.
    cierre_pedido = models.BooleanField(db_column='Cierre_Pedido')  # Field name made lowercase.
    cierre_costos = models.BooleanField(db_column='Cierre_Costos')  # Field name made lowercase.
    cierre_precio = models.BooleanField(db_column='Cierre_Precio')  # Field name made lowercase.
    planos = models.BooleanField(db_column='Planos')  # Field name made lowercase.
    requiereplanosinpar = models.BooleanField(db_column='RequierePlanoSinPar', blank=True, null=True)  # Field name made lowercase.
    requiereplanocliente = models.BooleanField(db_column='RequierePlanoCliente', blank=True, null=True)  # Field name made lowercase.
    incluirlistsemi = models.BooleanField(db_column='IncluirListSemi', blank=True, null=True)  # Field name made lowercase.
    puntipootreporte = models.IntegerField(db_column='PunTipoOTReporte', blank=True, null=True)  # Field name made lowercase.
    cantidadcomenzadaautomatica = models.BooleanField(db_column='CantidadComenzadaAutomatica', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoOT'


class TipootOrg(models.Model):
    puntipoot = models.AutoField(db_column='PunTipoOT', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    prefijo = models.CharField(db_column='Prefijo', max_length=4, blank=True, null=True)  # Field name made lowercase.
    numeracionunica = models.BooleanField(db_column='NumeracionUnica')  # Field name made lowercase.
    puntipoorigen = models.ForeignKey('Hctipoorigenot', models.DO_NOTHING, db_column='PunTipoOrigen')  # Field name made lowercase.
    cierre_pedido = models.BooleanField(db_column='Cierre_Pedido')  # Field name made lowercase.
    cierre_costos = models.BooleanField(db_column='Cierre_Costos')  # Field name made lowercase.
    cierre_precio = models.BooleanField(db_column='Cierre_Precio')  # Field name made lowercase.
    planos = models.BooleanField(db_column='Planos')  # Field name made lowercase.
    requiereplanosinpar = models.BooleanField(db_column='RequierePlanoSinPar', blank=True, null=True)  # Field name made lowercase.
    requiereplanocliente = models.BooleanField(db_column='RequierePlanoCliente', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoOT Org'


class Tipootreporte(models.Model):
    puntipootreporte = models.AutoField(primary_key=True, db_column='PunTipoOTReporte')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    reporte = models.CharField(db_column='Reporte', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoOTReporte'


class Tipoottmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    idoperacion2 = models.IntegerField(db_column='IDOperacion2')  # Field name made lowercase.
    puntipoot = models.IntegerField(db_column='PunTipoOT', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    prefijo = models.CharField(db_column='Prefijo', max_length=4, blank=True, null=True)  # Field name made lowercase.
    numeracionunica = models.BooleanField(db_column='NumeracionUnica')  # Field name made lowercase.
    puntipoorigen = models.IntegerField(db_column='PunTipoOrigen')  # Field name made lowercase.
    cierre_pedido = models.BooleanField(db_column='Cierre_Pedido')  # Field name made lowercase.
    cierre_costos = models.BooleanField(db_column='Cierre_Costos')  # Field name made lowercase.
    cierre_precio = models.BooleanField(db_column='Cierre_Precio')  # Field name made lowercase.
    requiereplanosinpar = models.BooleanField(db_column='RequierePlanoSinPar')  # Field name made lowercase.
    requiereplanocliente = models.BooleanField(db_column='RequierePlanoCliente')  # Field name made lowercase.
    modoabm = models.SmallIntegerField(db_column='ModoABM', blank=True, null=True)  # Field name made lowercase.
    incluirlistsemi = models.BooleanField(db_column='IncluirListSemi', blank=True, null=True)  # Field name made lowercase.
    puntipootreporte = models.IntegerField(db_column='PunTipoOTReporte', blank=True, null=True)  # Field name made lowercase.
    cantidadcomenzadaautomatica = models.BooleanField(db_column='CantidadComenzadaAutomatica', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoOTTMP'


class TipootRubrotmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    punrubro = models.IntegerField(db_column='PunRubro')  # Field name made lowercase.
    modoabm = models.SmallIntegerField(db_column='ModoABM')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoOT_RubroTMP'


class Tipoorigen(models.Model):
    punorigen = models.IntegerField(db_column='PunOrigen')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoOrigen'


class Tipopago(models.Model):
    puntipopago = models.IntegerField(db_column='PunTipoPago')  # Field name made lowercase.
    etiqueta = models.CharField(db_column='Etiqueta', max_length=4)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tipopagocaja = models.SmallIntegerField(db_column='TipoPagoCaja', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoPago'


class Tipopieza(models.Model):
    puntipopieza = models.AutoField(db_column='PunTipoPieza', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', unique=True, max_length=100)  # Field name made lowercase.
    punrubro = models.IntegerField(db_column='PunRubro', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoPieza'


class Tipopiezapropiedad(models.Model):
    puntipopieza = models.ForeignKey(Tipopieza, models.DO_NOTHING, db_column='PunTipoPieza')  # Field name made lowercase.
    punpropiedad = models.ForeignKey(Propiedad, models.DO_NOTHING, db_column='PunPropiedad')  # Field name made lowercase.
    orden = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TipoPiezaPropiedad'


class Tiporemito(models.Model):
    puntiporemito = models.IntegerField(db_column='PunTipoRemito')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoRemito'


class Tiporeparacion(models.Model):
    puntiporeparacion = models.AutoField(primary_key=True, db_column='PunTipoReparacion')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoReparacion'


class Tiporesponsables(models.Model):
    puntiporesponsable = models.AutoField(primary_key=True, db_column='PunTipoResponsable')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.
    tabla = models.CharField(db_column='Tabla', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sp = models.CharField(db_column='SP', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoResponsables'


class Tiporetenciones(models.Model):
    puntiporetencion = models.IntegerField(db_column='PunTipoRetencion')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    cuenta = models.CharField(db_column='Cuenta', max_length=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoRetenciones'


class Tipostock(models.Model):
    puntipostock = models.SmallAutoField(primary_key=True, db_column='PunTipoStock')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=5)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoStock'


class Tiposiva(models.Model):
    puntipoiva = models.IntegerField(db_column='PunTipoIVA')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    abreviado = models.CharField(db_column='Abreviado', max_length=2, blank=True, null=True)  # Field name made lowercase.
    afipcodigo = models.IntegerField(db_column='AFIPCodigo', blank=True, null=True)  # Field name made lowercase.
    codigoiibb = models.IntegerField(db_column='CodigoIIBB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TiposIVA'


class Tiposprevision(models.Model):
    puntipoprevision = models.AutoField(primary_key=True, db_column='PunTipoPrevision')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tipoingresoegreso = models.SmallIntegerField(db_column='TipoIngresoEgreso')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TiposPrevision'


class Turnos(models.Model):
    punturno = models.AutoField(db_column='PunTurno', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.
    horaentrada = models.DateTimeField(db_column='HoraEntrada')  # Field name made lowercase.
    horasalida = models.DateTimeField(db_column='HoraSalida')  # Field name made lowercase.
    tiempodescanso = models.IntegerField(db_column='TiempoDescanso', blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Turnos'


class Unidades(models.Model):
    pununidad = models.AutoField(db_column='PunUnidad', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modificado = models.CharField(db_column='Modificado', max_length=1, blank=True, null=True)  # Field name made lowercase.
    codigoafip = models.CharField(db_column='CodigoAfip', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Unidades'


class Unidadesmedida(models.Model):
    pununidadmedida = models.AutoField(primary_key=True, db_column='PunUnidadMedida')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    codigoafip = models.CharField(db_column='CodigoAfip', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UnidadesMedida'


class Userlogin(models.Model):
    punusuario = models.IntegerField(db_column='PunUsuario', blank=True, null=True)  # Field name made lowercase.
    net_address = models.CharField(db_column='Net_Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    login_time = models.DateTimeField(db_column='Login_time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserLogin'


class Usuariopermisomenutmp(models.Model):
    idoperacion = models.IntegerField(db_column='Idoperacion')  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='punUsuario', blank=True, null=True)  # Field name made lowercase.
    punmenu = models.IntegerField(db_column='punMenu', blank=True, null=True)  # Field name made lowercase.
    permisos = models.IntegerField(db_column='Permisos', blank=True, null=True)  # Field name made lowercase.
    fechainserted = models.DateTimeField(db_column='FechaInserted')  # Field name made lowercase.
    modoabm = models.IntegerField(db_column='ModoABM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UsuarioPermisoMenuTMP'


class Usuariopermisosespeciales(models.Model):
    punusuario = models.OneToOneField('Usuarios', models.DO_NOTHING, db_column='PunUsuario', primary_key=True)  # Field name made lowercase. The composite primary key (PunUsuario, PunItem) found, that is not supported. The first column is selected.
    punitem = models.ForeignKey(Menupermisosespeciales, models.DO_NOTHING, db_column='PunItem')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UsuarioPermisosEspeciales'
        unique_together = (('punusuario', 'punitem'),)


class Usuariopermisosespecialestmp(models.Model):
    punusuario = models.IntegerField(db_column='punUsuario', blank=True, null=True)  # Field name made lowercase.
    punitem = models.IntegerField(db_column='punItem', blank=True, null=True)  # Field name made lowercase.
    modoabm = models.IntegerField(db_column='ModoABM', blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UsuarioPermisosEspecialesTMP'


class Usuariosistema(models.Model):
    punusuario = models.OneToOneField('Usuarios', models.DO_NOTHING, db_column='punUsuario', primary_key=True)  # Field name made lowercase. The composite primary key (punUsuario, punSistema) found, that is not supported. The first column is selected.
    punsistema = models.ForeignKey(Sistema, models.DO_NOTHING, db_column='punSistema')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UsuarioSistema'
        unique_together = (('punusuario', 'punsistema'),)


class Usuariosistematmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='PunUsuario', blank=True, null=True)  # Field name made lowercase.
    punsistema = models.IntegerField(db_column='PunSistema', blank=True, null=True)  # Field name made lowercase.
    modoabm = models.SmallIntegerField(db_column='ModoABM')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UsuarioSistemaTMP'


class Usuarios(models.Model):
    punusuario = models.AutoField(db_column='PunUsuario', primary_key=True)  # Field name made lowercase.
    puncentro = models.IntegerField(db_column='PunCentro')  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=100)  # Field name made lowercase.
    nombres = models.CharField(db_column='Nombres', max_length=100)  # Field name made lowercase.
    tipodocumento = models.IntegerField(db_column='TipoDocumento', blank=True, null=True)  # Field name made lowercase.
    nrodocumento = models.IntegerField(db_column='NroDocumento', blank=True, null=True)  # Field name made lowercase.
    fechaalta = models.DateTimeField(db_column='FechaAlta')  # Field name made lowercase.
    fechabaja = models.DateTimeField(db_column='FechaBaja', blank=True, null=True)  # Field name made lowercase.
    cuentausuario = models.CharField(db_column='CuentaUsuario', max_length=100)  # Field name made lowercase.
    fechatimereport = models.DateTimeField(db_column='FechaTimeReport', blank=True, null=True)  # Field name made lowercase.
    pundepartamento = models.IntegerField(db_column='PunDepartamento', blank=True, null=True)  # Field name made lowercase.
    cadete = models.BooleanField(db_column='Cadete', blank=True, null=True)  # Field name made lowercase.
    externo = models.SmallIntegerField(db_column='Externo', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=15, blank=True, null=True)  # Field name made lowercase.
    punvendedor = models.IntegerField(db_column='PunVendedor', blank=True, null=True)  # Field name made lowercase.
    pundistribuidor = models.IntegerField(db_column='PunDistribuidor', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    punsector = models.ForeignKey(Sectores, models.DO_NOTHING, db_column='PunSector', blank=True, null=True)  # Field name made lowercase.
    superusuario = models.BooleanField(db_column='SuperUsuario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usuarios'


class Usuariospermisosmenu(models.Model):
    punusuario = models.OneToOneField(Usuarios, models.DO_NOTHING, db_column='PunUsuario', primary_key=True)  # Field name made lowercase. The composite primary key (PunUsuario, PunMenu) found, that is not supported. The first column is selected.
    punmenu = models.ForeignKey(Menu, models.DO_NOTHING, db_column='PunMenu')  # Field name made lowercase.
    permisos = models.IntegerField(db_column='Permisos')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UsuariosPermisosMenu'
        unique_together = (('punusuario', 'punmenu'),)


class Vencimientoscai(models.Model):
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=2)  # Field name made lowercase.
    tipoabc = models.CharField(db_column='TipoABC', max_length=1)  # Field name made lowercase.
    prefijodesde = models.CharField(db_column='PrefijoDesde', max_length=4)  # Field name made lowercase.
    sufijodesde = models.CharField(db_column='SufijoDesde', max_length=8)  # Field name made lowercase.
    prefijohasta = models.CharField(db_column='PrefijoHasta', max_length=4)  # Field name made lowercase.
    sufijohasta = models.CharField(db_column='SufijoHasta', max_length=8)  # Field name made lowercase.
    fechavto = models.DateTimeField(db_column='FechaVto')  # Field name made lowercase.
    prefijoultimo = models.CharField(db_column='PrefijoUltimo', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sufijoultimo = models.CharField(db_column='SufijoUltimo', max_length=8, blank=True, null=True)  # Field name made lowercase.
    status = models.BooleanField(db_column='Status')  # Field name made lowercase.
    numerocai = models.CharField(db_column='NumeroCAI', max_length=14, blank=True, null=True)  # Field name made lowercase.
    numnerocai = models.CharField(db_column='NumneroCAI', max_length=14, blank=True, null=True)  # Field name made lowercase.
    talonarioanulado = models.SmallIntegerField(db_column='TalonarioAnulado', blank=True, null=True)  # Field name made lowercase.
    sufijoanuladodesde = models.CharField(db_column='SufijoAnuladoDesde', max_length=8, blank=True, null=True)  # Field name made lowercase.
    sufijoanuladohasta = models.CharField(db_column='SufijoAnuladoHasta', max_length=8, blank=True, null=True)  # Field name made lowercase.
    punvencimiento = models.AutoField(primary_key=True, db_column='PunVencimiento')  # Field name made lowercase.
    conproximotalonario = models.SmallIntegerField(db_column='ConProximoTalonario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VencimientosCAI'


class Vendedorrubro(models.Model):
    punvendedor = models.IntegerField(db_column='PunVendedor', primary_key=True)  # Field name made lowercase. The composite primary key (PunVendedor, PunRubro) found, that is not supported. The first column is selected.
    punrubro = models.ForeignKey(Rubrosarticulos, models.DO_NOTHING, db_column='PunRubro')  # Field name made lowercase.
    tipocomision = models.SmallIntegerField(db_column='TipoComision')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VendedorRubro'
        unique_together = (('punvendedor', 'punrubro'),)


class Vendedorrubrotmp(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion')  # Field name made lowercase.
    punrubro = models.IntegerField(db_column='PunRubro')  # Field name made lowercase.
    tipocomision = models.SmallIntegerField(db_column='TipoComision')  # Field name made lowercase.
    modoabm = models.SmallIntegerField(db_column='ModoABM')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VendedorRubroTMP'


class Vendedores(models.Model):
    punvendedor = models.AutoField(db_column='PunVendedor', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=150)  # Field name made lowercase.
    telefonos = models.CharField(db_column='Telefonos', max_length=100, blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado')  # Field name made lowercase.
    codigo = models.CharField(max_length=5, blank=True, null=True)
    cobranzaespecial = models.DecimalField(db_column='CobranzaEspecial', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cobranzastandard = models.DecimalField(db_column='CobranzaStandard', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ventaespecial = models.DecimalField(db_column='VentaEspecial', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ventastandard = models.DecimalField(db_column='VentaStandard', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pununidadnegocio = models.IntegerField(db_column='punUnidadNegocio', blank=True, null=True)  # Field name made lowercase.
    punsucursal = models.IntegerField(db_column='punSucursal', blank=True, null=True)  # Field name made lowercase.
    punusuarioasociado = models.IntegerField(db_column='PunUsuarioAsociado', blank=True, null=True)  # Field name made lowercase.
    emailcustomer = models.CharField(db_column='EmailCustomer', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vendedores'


class Zonas(models.Model):
    punzona = models.AutoField(primary_key=True, db_column='PunZona')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=2)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado')  # Field name made lowercase.
    padronseparado = models.SmallIntegerField(db_column='PadronSeparado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Zonas'


# class Artic(models.Model):
#     punrubro = models.FloatField(db_column='PunRubro', blank=True, null=True)  # Field name made lowercase.
#     codigo = models.CharField(db_column='Codigo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     descripci├│n = models.CharField(db_column='Descripci├│n', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     punlineaproduccion = models.FloatField(blank=True, null=True)
#     punfamilia = models.FloatField(blank=True, null=True)
#     pungrupo = models.FloatField(blank=True, null=True)
#     origen = models.FloatField(blank=True, null=True)
#     tipo = models.FloatField(blank=True, null=True)
#     cuentacompra = models.FloatField(blank=True, null=True)
#     cuentaventa = models.FloatField(blank=True, null=True)
#     pununidad = models.FloatField(blank=True, null=True)
#     stockminimo = models.FloatField(db_column='StockMinimo', blank=True, null=True)  # Field name made lowercase.
#     stockcritico = models.FloatField(db_column='StockCritico', blank=True, null=True)  # Field name made lowercase.
#     stockmaximo = models.FloatField(db_column='StockMaximo', blank=True, null=True)  # Field name made lowercase.
#     alicuotaiva = models.FloatField(db_column='AlicuotaIVA', blank=True, null=True)  # Field name made lowercase.
#     borrado = models.FloatField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
#     enfabricacion = models.FloatField(db_column='EnFabricacion', blank=True, null=True)  # Field name made lowercase.
#     tiemporeposicion = models.FloatField(db_column='TiempoReposicion', blank=True, null=True)  # Field name made lowercase.
#     generastock = models.FloatField(db_column='GeneraStock', blank=True, null=True)  # Field name made lowercase.
#     peso = models.CharField(db_column='Peso', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     pununidadalternativa = models.FloatField(db_column='PunUnidadAlternativa', blank=True, null=True)  # Field name made lowercase.
#     coeficiente = models.FloatField(db_column='Coeficiente', blank=True, null=True)  # Field name made lowercase.
#     puntipoot = models.FloatField(db_column='PunTipoOT', blank=True, null=True)  # Field name made lowercase.
#     puntipompse = models.FloatField(db_column='PunTipoMPSE', blank=True, null=True)  # Field name made lowercase.
#     unidadesporenvase = models.FloatField(db_column='UnidadesporEnvase', blank=True, null=True)  # Field name made lowercase.
#     f26 = models.CharField(db_column='F26', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     f27 = models.CharField(db_column='F27', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     precio_fob_field = models.FloatField(db_column='Precio FOB (Ôé¼)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     punmoneda = models.FloatField(blank=True, null=True)
#     precio_fob_nac_field = models.FloatField(db_column='Precio FOB+NAC (Ôé¼)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     punmoneda1 = models.FloatField(blank=True, null=True)
#     precio_m├¡nimo_field = models.FloatField(db_column='Precio m├¡nimo (Ôé¼)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     punmoneda2 = models.FloatField(blank=True, null=True)
#     precio_de_lista_131_field = models.FloatField(db_column='Precio de lista 131 (Ôé¼)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     punmoneda3 = models.FloatField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = '_Artic'


class Cuitsfce(models.Model):
    cuit = models.CharField(db_column='CUIT', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_CUITSFCE'


class Gclistaprecioarticulos1(models.Model):
    punprecio = models.AutoField(primary_key=True, db_column='PunPrecio')  # Field name made lowercase.
    punlista = models.IntegerField(db_column='PunLista')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fechamodificacion = models.DateTimeField(db_column='FechaModificacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_GCListaPrecioArticulos1'


class Gclistaprecioarticulos40(models.Model):
    punprecio = models.AutoField(primary_key=True, db_column='PunPrecio')  # Field name made lowercase.
    punlista = models.IntegerField(db_column='PunLista')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fechamodificacion = models.DateTimeField(db_column='FechaModificacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_GCListaPrecioArticulos40'


class Gclistaprecioarticulos42(models.Model):
    punprecio = models.AutoField(primary_key=True, db_column='PunPrecio')  # Field name made lowercase.
    punlista = models.IntegerField(db_column='PunLista')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fechamodificacion = models.DateTimeField(db_column='FechaModificacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_GCListaPrecioArticulos42'


class Gclistaprecios40(models.Model):
    punlista = models.AutoField(primary_key=True, db_column='PunLista')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    tipo = models.SmallIntegerField(db_column='Tipo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_GCListaPrecios40'


class Gclistaprecios41(models.Model):
    punlista = models.AutoField(primary_key=True, db_column='PunLista')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    tipo = models.SmallIntegerField(db_column='Tipo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_GCListaPrecios41'


class Gclistaprecios42(models.Model):
    punlista = models.AutoField(primary_key=True, db_column='PunLista')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    tipo = models.SmallIntegerField(db_column='Tipo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_GCListaPrecios42'


class Gcvencimientosarreglados(models.Model):
    punreferenciacc = models.IntegerField(db_column='punreferenciaCC')  # Field name made lowercase.
    puncomprobantecc = models.IntegerField(db_column='puncomprobanteCC')  # Field name made lowercase.
    importectacte = models.DecimalField(db_column='ImporteCtaCte', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punreferenciaci = models.IntegerField(db_column='punreferenciaCI')  # Field name made lowercase.
    puncomprobanteci = models.IntegerField(db_column='puncomprobanteCI')  # Field name made lowercase.
    importeimportes = models.DecimalField(db_column='ImporteImportes', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punreferenciacv = models.IntegerField(db_column='punreferenciaCV')  # Field name made lowercase.
    puncomprobantecv = models.IntegerField(db_column='puncomprobanteCV')  # Field name made lowercase.
    importevencimientos = models.DecimalField(db_column='ImporteVencimientos', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_GCVencimientosArreglados'


class Gcddjjagua(models.Model):
    punproveedor = models.IntegerField(db_column='PunProveedor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_GcDDJJAgua'


class Gcddjjbancos(models.Model):
    punproveedor = models.IntegerField(db_column='PunProveedor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_GcDDJJBancos'


class Gcddjjdelexterior(models.Model):
    punproveedor = models.IntegerField(db_column='PunProveedor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_GcDDJJDelExterior'


class Gcddjjgas(models.Model):
    punproveedor = models.IntegerField(db_column='PunProveedor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_GcDDJJGas'


class Gcddjjluz(models.Model):
    punproveedor = models.IntegerField(db_column='PunProveedor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_GcDDJJLuz'


class Gcddjjproveedores(models.Model):
    punproveedor = models.IntegerField(db_column='PunProveedor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_GcDDJJProveedores'


class Gcddjjtelefono(models.Model):
    punproveedor = models.IntegerField(db_column='PunProveedor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_GcDDJJTelefono'


class Gclogpedidos(models.Model):
    punpedido = models.IntegerField(db_column='PunPedido', blank=True, null=True)  # Field name made lowercase.
    veces = models.IntegerField(db_column='Veces', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_GcLogPedidos'


class Gcsmodifart(models.Model):
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    codigoalternativo = models.CharField(db_column='CodigoAlternativo', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_GcsModifArt'


class Insertados(models.Model):
    punlista = models.IntegerField(db_column='PunLista')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fechamodificacion = models.DateTimeField(db_column='FechaModificacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_Insertados'


class Lpmqlp(models.Model):
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.
    stocksinot = models.DecimalField(db_column='StockSINOT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    stock = models.DecimalField(db_column='Stock', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_LPMQLP'


# class Lista(models.Model):
#     rubro = models.CharField(db_column='Rubro', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     pun = models.IntegerField(db_column='Pun', blank=True, null=True)  # Field name made lowercase.
#     c├│digo = models.CharField(db_column='C├│digo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     descripci├│n_field = models.CharField(db_column='descripci├│n ', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     caracteristicas_adicionales_field = models.CharField(db_column='caracteristicas adicionales ', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

#     class Meta:
#         managed = False
#         db_table = '_Lista'


class Om(models.Model):
    punasignacion = models.IntegerField(db_column='PunAsignacion', blank=True, null=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT', blank=True, null=True)  # Field name made lowercase.
    punarticuloasignado = models.IntegerField(db_column='PunArticuloAsignado', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pununidad = models.IntegerField(db_column='PunUnidad', blank=True, null=True)  # Field name made lowercase.
    pundeposito = models.IntegerField(db_column='PunDeposito', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    punordentorigen = models.IntegerField(db_column='PunOrdenTOrigen', blank=True, null=True)  # Field name made lowercase.
    punoporigen = models.IntegerField(db_column='PunOPOrigen', blank=True, null=True)  # Field name made lowercase.
    costo = models.DecimalField(db_column='Costo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda', blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punremitoitem = models.IntegerField(db_column='PunRemitoItem', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=512, blank=True, null=True)  # Field name made lowercase.
    punmovimientostock = models.IntegerField(db_column='PunMovimientoStock', blank=True, null=True)  # Field name made lowercase.
    puntipompse = models.IntegerField(db_column='PunTipoMPSE', blank=True, null=True)  # Field name made lowercase.
    recomendar = models.BooleanField(db_column='Recomendar', blank=True, null=True)  # Field name made lowercase.
    modoabm = models.SmallIntegerField(db_column='ModoABM', blank=True, null=True)  # Field name made lowercase.
    punreasignacionot = models.IntegerField(db_column='PunReasignacionOT', blank=True, null=True)  # Field name made lowercase.
    cantidadcomenzada = models.DecimalField(db_column='CantidadComenzada', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidaddescontada = models.DecimalField(db_column='CantidadDescontada', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_OM'


class Othoraoperariocorregida(models.Model):
    punordent = models.IntegerField()
    prefijo = models.CharField(max_length=4, blank=True, null=True)
    sufijo = models.CharField(max_length=8, blank=True, null=True)
    punpartediario = models.IntegerField(db_column='punParteDiario')  # Field name made lowercase.
    punoperario = models.IntegerField(db_column='punOperario', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(blank=True, null=True)
    borrado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_OTHoraOperarioCorregida'


class Partediarioitemactualizado(models.Model):
    punpartediarioitem = models.IntegerField(db_column='PunParteDiarioItem')  # Field name made lowercase.
    punpartediario = models.IntegerField(db_column='PunParteDiario', blank=True, null=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT', blank=True, null=True)  # Field name made lowercase.
    punmaquina = models.IntegerField(db_column='PunMaquina', blank=True, null=True)  # Field name made lowercase.
    punoperacion = models.IntegerField(db_column='PunOperacion', blank=True, null=True)  # Field name made lowercase.
    horainicio = models.DateTimeField(db_column='HoraInicio', blank=True, null=True)  # Field name made lowercase.
    horafin = models.DateTimeField(db_column='HoraFin', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    horaoperariocosto = models.DecimalField(db_column='HoraOperarioCosto', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    horaoperariopunmoneda = models.IntegerField(db_column='HoraOperarioPunMoneda', blank=True, null=True)  # Field name made lowercase.
    horaoperariocotizacion = models.DecimalField(db_column='HoraOperarioCotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    horamaquinacosto = models.DecimalField(db_column='HoraMaquinaCosto', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    horamaquinapunmoneda = models.DecimalField(db_column='HoraMaquinaPunMoneda', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    horamaquinacotizacion = models.DecimalField(db_column='HoraMaquinaCotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    minutos = models.IntegerField(blank=True, null=True)
    punreasignacionot = models.IntegerField(db_column='PunReasignacionOT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_ParteDiarioItemActualizado'


class Partediarioitemactualizado2(models.Model):
    punpartediarioitem = models.AutoField(primary_key=True, db_column='PunParteDiarioItem')  # Field name made lowercase.
    punpartediario = models.IntegerField(db_column='PunParteDiario', blank=True, null=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT', blank=True, null=True)  # Field name made lowercase.
    punmaquina = models.IntegerField(db_column='PunMaquina', blank=True, null=True)  # Field name made lowercase.
    punoperacion = models.IntegerField(db_column='PunOperacion', blank=True, null=True)  # Field name made lowercase.
    horainicio = models.DateTimeField(db_column='HoraInicio', blank=True, null=True)  # Field name made lowercase.
    horafin = models.DateTimeField(db_column='HoraFin', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    horaoperariocosto = models.DecimalField(db_column='HoraOperarioCosto', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    horaoperariopunmoneda = models.IntegerField(db_column='HoraOperarioPunMoneda', blank=True, null=True)  # Field name made lowercase.
    horaoperariocotizacion = models.DecimalField(db_column='HoraOperarioCotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    horamaquinacosto = models.DecimalField(db_column='HoraMaquinaCosto', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    horamaquinapunmoneda = models.DecimalField(db_column='HoraMaquinaPunMoneda', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    horamaquinacotizacion = models.DecimalField(db_column='HoraMaquinaCotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    minutos = models.IntegerField(blank=True, null=True)
    punreasignacionot = models.IntegerField(db_column='PunReasignacionOT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_ParteDiarioItemActualizado2'


class Periodomanoobre(models.Model):
    fechadesde = models.DateTimeField(blank=True, null=True)
    importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_PeriodoManoObre'


class Gcarticulosstockcero(models.Model):
    field_codigorubro = models.CharField(db_column='_CodigoRubro', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_codigoarticulo = models.CharField(db_column='_CodigoArticulo', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_descripcion = models.CharField(db_column='_descripcion', max_length=1000, blank=True, null=True)  # Field renamed because it started with '_'.
    field_stock = models.IntegerField(db_column='_stock', blank=True, null=True)  # Field renamed because it started with '_'.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    punrubro = models.IntegerField(db_column='PunRubro', blank=True, null=True)  # Field name made lowercase.
    stocksinpar = models.DecimalField(db_column='StockSinpar', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    stocknuevo = models.DecimalField(db_column='StockNUEVO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_gcArticulosStockCERO'


class Gcclidiferenciacambioimportes08092020(models.Model):
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    punreferencia = models.IntegerField(db_column='PunReferencia')  # Field name made lowercase.
    puntipoimporte = models.IntegerField(db_column='PunTipoImporte')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    puncomprobantencnd = models.IntegerField(db_column='PunComprobanteNCND', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_gcCLIDiferenciaCambioImportes08092020'


class Gccomprasrg3685(models.Model):
    tipo = models.CharField(db_column='Tipo', max_length=5, blank=True, null=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    iva = models.DecimalField(db_column='Iva', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_gcCOMPRASRG3685'


class Gcconcuentasasientosautomaticos(models.Model):
    punplancuentas = models.IntegerField(db_column='PunPlanCuentas')  # Field name made lowercase.
    etiqueta = models.CharField(db_column='Etiqueta', max_length=20)  # Field name made lowercase.
    cuenta = models.CharField(db_column='Cuenta', max_length=9, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_gcCONCuentasAsientosAutomaticos'


class Gccarterachequestk29410(models.Model):
    puncheque = models.AutoField(primary_key=True, db_column='PunCheque')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    nrocheque = models.CharField(db_column='NroCheque', max_length=20)  # Field name made lowercase.
    punbancoemisor = models.IntegerField(db_column='PunBancoEmisor')  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    fechaemision = models.DateTimeField(db_column='FechaEmision')  # Field name made lowercase.
    fechacheque = models.DateTimeField(db_column='FechaCheque')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    puncomprobanteorigen = models.IntegerField(db_column='PunComprobanteOrigen', blank=True, null=True)  # Field name made lowercase.
    puncomprobantedestino = models.IntegerField(db_column='PunComprobanteDestino', blank=True, null=True)  # Field name made lowercase.
    punbancodeposito = models.IntegerField(db_column='PunBancoDeposito', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    fechastatus = models.DateTimeField(db_column='FechaStatus', blank=True, null=True)  # Field name made lowercase.
    clearing = models.SmallIntegerField(db_column='Clearing')  # Field name made lowercase.
    pundestino = models.IntegerField(db_column='PunDestino', blank=True, null=True)  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    puncomprobanterechazo = models.IntegerField(db_column='PunComprobanteRechazo', blank=True, null=True)  # Field name made lowercase.
    fechaingreso = models.DateTimeField(db_column='FechaIngreso', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=255, blank=True, null=True)  # Field name made lowercase.
    punmotivorechazo = models.IntegerField(db_column='PunMotivoRechazo', blank=True, null=True)  # Field name made lowercase.
    noalaorden = models.SmallIntegerField(db_column='NoALaOrden', blank=True, null=True)  # Field name made lowercase.
    aforo = models.SmallIntegerField(db_column='Aforo', blank=True, null=True)  # Field name made lowercase.
    punorigen = models.IntegerField(db_column='PunOrigen')  # Field name made lowercase.
    punasiento = models.IntegerField(db_column='PunAsiento')  # Field name made lowercase.
    puncaja = models.IntegerField(db_column='PunCaja', blank=True, null=True)  # Field name made lowercase.
    fechaoriginalchq = models.DateTimeField(db_column='FechaOriginalChq', blank=True, null=True)  # Field name made lowercase.
    cuitemisor = models.CharField(db_column='CuitEmisor', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_gcCarterachequesTk29410'


class Gccliclientesencctk27956(models.Model):
    puncliente = models.IntegerField(db_column='PunCliente')  # Field name made lowercase.
    fechaalta = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_gcCliCLientesENCCTK27956'


class Gccliclientesenlogtk27956(models.Model):
    puncliente = models.IntegerField(db_column='PunCliente')  # Field name made lowercase.
    fechaalta = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_gcCliCLientesENLOGTK27956'


class Gccliclientesotrostk27956(models.Model):
    puncliente = models.IntegerField(db_column='PunCliente')  # Field name made lowercase.
    fechaalta = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_gcCliCLientesOTROSTK27956'


class Gccomparacionsaldos(models.Model):
    punreferencia = models.IntegerField(db_column='PuNReferencia', blank=True, null=True)  # Field name made lowercase.
    saldoctacte = models.DecimalField(db_column='SaldoCtaCte', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    saldoimportes = models.DecimalField(db_column='SaldoImportes', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    saldovencimientos = models.DecimalField(db_column='SaldoVencimientos', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_gcComparacionSaldos'


class Gcconsulta(models.Model):
    punmenu = models.IntegerField(db_column='PunMenu', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    accion = models.CharField(db_column='Accion', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sp = models.CharField(max_length=8000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_gcConsulta'


class Gcfadolarescomparacionsaldos(models.Model):
    punreferencia = models.IntegerField(db_column='PuNReferencia', blank=True, null=True)  # Field name made lowercase.
    saldoctacte = models.DecimalField(db_column='SaldoCtaCte', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    saldoimportes = models.DecimalField(db_column='SaldoImportes', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    saldovencimientos = models.DecimalField(db_column='SaldoVencimientos', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_gcFADolaresComparacionSaldos'


class Gcfadolaresimportes(models.Model):
    punreferencia = models.IntegerField(db_column='PuNReferencia', blank=True, null=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importepesos = models.DecimalField(db_column='ImportePesos', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_gcFADolaresImportes'


class Gcfacturasvencimientosmal(models.Model):
    puncomprobantefa = models.IntegerField(db_column='puncomprobanteFA', blank=True, null=True)  # Field name made lowercase.
    tipocomprobantefa = models.CharField(db_column='TipoComprobanteFA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tipoabcfa = models.CharField(db_column='TipoABCFA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    prefijofa = models.CharField(db_column='prefijoFA', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sufijofa = models.CharField(db_column='SufijoFA', max_length=8, blank=True, null=True)  # Field name made lowercase.
    fechavtofa = models.DateTimeField(db_column='FechaVtoFA', blank=True, null=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(blank=True, null=True)
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tipoabc = models.CharField(db_column='TipoABC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    prefijo = models.CharField(max_length=4, blank=True, null=True)
    sufijo = models.CharField(db_column='Sufijo', max_length=8, blank=True, null=True)  # Field name made lowercase.
    punreferencia = models.IntegerField(db_column='PunReferencia', blank=True, null=True)  # Field name made lowercase.
    fechavto = models.DateTimeField(db_column='FechaVto', blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_gcFacturasVencimientosMal'


class Gclibroivadigitalcomprasexcluidas(models.Model):
    puncomprobante = models.IntegerField(db_column='PunCOmprobante', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_gcLibroIvaDigitalCOmprasExcluidas'


class Gcmenu682(models.Model):
    punusuario = models.IntegerField(db_column='PunUsuario')  # Field name made lowercase.
    punmenu = models.IntegerField(db_column='PunMenu')  # Field name made lowercase.
    permisos = models.IntegerField(db_column='Permisos')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_gcMenu682'


class Gcncsincashflow(models.Model):
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_gcNcSinCashflow'


class Gcprvproveedoresacumuladosconrepetidos(models.Model):
    punproveedor = models.IntegerField(db_column='PunProveedor')  # Field name made lowercase.
    pagosmes = models.SmallIntegerField(db_column='PagosMes', blank=True, null=True)  # Field name made lowercase.
    pagosanio = models.SmallIntegerField(db_column='PagosAnio', blank=True, null=True)  # Field name made lowercase.
    acumuladopagos = models.DecimalField(db_column='AcumuladoPagos', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    acumuladoretencion = models.DecimalField(db_column='AcumuladoRetencion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa', blank=True, null=True)  # Field name made lowercase.
    punactividadganancias = models.IntegerField(db_column='PunActividadGanancias', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(primary_key=True, )

    class Meta:
        managed = False
        db_table = '_gcPRVProveedoresAcumuladosconrepetidos'


class Gcpermisoscotizacionestk30808(models.Model):
    punusuario = models.IntegerField(db_column='PunUsuario')  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=100)  # Field name made lowercase.
    nombres = models.CharField(db_column='Nombres', max_length=100)  # Field name made lowercase.
    permisos = models.IntegerField(db_column='Permisos')  # Field name made lowercase.
    cuentausuario = models.CharField(db_column='CuentaUsuario', max_length=100)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_gcPermisosCotizacionesTK30808'


class Gcprvcomprobantestk30203(models.Model):
    punproveedor = models.IntegerField(db_column='PunProveedor')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100)  # Field name made lowercase.
    afiptipocomprobante = models.IntegerField(db_column='AFIPTipoComprobante', blank=True, null=True)  # Field name made lowercase.
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tipoabc = models.CharField(db_column='TipoABC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    punreferencia = models.IntegerField(db_column='PunReferencia')  # Field name made lowercase.
    puntipoimporte = models.IntegerField(db_column='PunTipoImporte')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    numeroret = models.CharField(db_column='NumeroRet', max_length=20, blank=True, null=True)  # Field name made lowercase.
    punjurisdiccion = models.IntegerField(db_column='PunJurisdiccion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_gcPrvCOmprobantesTk30203'


class Gctemp1(models.Model):
    punusuario = models.IntegerField(db_column='PunUsuario', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    accion = models.CharField(db_column='Accion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    programa = models.CharField(db_column='Programa', max_length=100, blank=True, null=True)  # Field name made lowercase.
    puntero = models.IntegerField(db_column='Puntero', blank=True, null=True)  # Field name made lowercase.
    punorigen = models.IntegerField(db_column='PunOrigen', blank=True, null=True)  # Field name made lowercase.
    tablapuntero = models.CharField(db_column='TablaPuntero', max_length=100, blank=True, null=True)  # Field name made lowercase.
    campopuntero = models.CharField(db_column='CampoPuntero', max_length=100, blank=True, null=True)  # Field name made lowercase.
    detalle = models.CharField(db_column='Detalle', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa', blank=True, null=True)  # Field name made lowercase.
    empresa = models.CharField(db_column='Empresa', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punasiento = models.IntegerField(db_column='PunAsiento', blank=True, null=True)  # Field name made lowercase.
    nroasiento = models.IntegerField(db_column='NroAsiento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_gcTemp1'


class Gcusuariopermisosespecialesadmin(models.Model):
    punusuario = models.IntegerField(db_column='PunUsuario')  # Field name made lowercase.
    punitem = models.IntegerField(db_column='PunItem')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_gcUsuarioPermisosEspecialesAdmin'


class Gcusuariospermisosmenuadmin(models.Model):
    punusuario = models.IntegerField(db_column='PunUsuario')  # Field name made lowercase.
    punmenu = models.IntegerField(db_column='PunMenu')  # Field name made lowercase.
    permisos = models.IntegerField(db_column='Permisos')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_gcUsuariosPermisosMenuAdmin'


class Gcvencimientosticket30673(models.Model):
    codigo = models.CharField(max_length=8, blank=True, null=True)
    puncliente = models.IntegerField(db_column='PunCliente')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=2)  # Field name made lowercase.
    tipoabc = models.CharField(db_column='TipoABC', max_length=1)  # Field name made lowercase.
    prefijo = models.CharField(db_column='Prefijo', max_length=4)  # Field name made lowercase.
    sufijo = models.CharField(db_column='Sufijo', max_length=8)  # Field name made lowercase.
    fecha = models.DateTimeField()
    ctaimporte = models.DecimalField(db_column='CtaImporte', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fechavto = models.DateTimeField(db_column='FechaVto')  # Field name made lowercase.
    vtoimporte = models.DecimalField(db_column='VtoImporte', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_gcVencimientosTicket30673'


class Gcarticulos23042021(models.Model):
    punarticulo = models.AutoField(primary_key=True, db_column='PunArticulo')  # Field name made lowercase.
    punrubro = models.IntegerField(db_column='PunRubro')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150)  # Field name made lowercase.
    punlineaproduccion = models.IntegerField(db_column='PunLineaProduccion')  # Field name made lowercase.
    punfamilia = models.IntegerField(db_column='PunFamilia')  # Field name made lowercase.
    pungrupo = models.IntegerField(db_column='PunGrupo')  # Field name made lowercase.
    origen = models.SmallIntegerField(db_column='Origen')  # Field name made lowercase.
    tipo = models.SmallIntegerField(db_column='Tipo')  # Field name made lowercase.
    cuentacompra = models.CharField(db_column='CuentaCompra', max_length=9, blank=True, null=True)  # Field name made lowercase.
    cuentaventa = models.CharField(db_column='CuentaVenta', max_length=9, blank=True, null=True)  # Field name made lowercase.
    pununidad = models.IntegerField(db_column='PunUnidad')  # Field name made lowercase.
    stockminimo = models.DecimalField(db_column='StockMinimo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    stockcritico = models.DecimalField(db_column='StockCritico', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    stockmaximo = models.DecimalField(db_column='StockMaximo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    alicuotaiva = models.IntegerField(db_column='AlicuotaIVA')  # Field name made lowercase.
    codigobarras = models.CharField(db_column='CodigoBarras', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ubicacionfisica = models.CharField(db_column='UbicacionFisica', max_length=10, blank=True, null=True)  # Field name made lowercase.
    codigoalternativo = models.CharField(db_column='CodigoAlternativo', max_length=16, blank=True, null=True)  # Field name made lowercase.
    critico = models.SmallIntegerField(db_column='Critico', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=255, blank=True, null=True)  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    enfabricacion = models.DecimalField(db_column='EnFabricacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    consumopromedio = models.DecimalField(db_column='ConsumoPromedio', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tiemporeposicion = models.DecimalField(db_column='TiempoReposicion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    caractadicionales = models.CharField(db_column='CaractAdicionales', max_length=255, blank=True, null=True)  # Field name made lowercase.
    generastock = models.BooleanField(db_column='GeneraStock')  # Field name made lowercase.
    peso = models.DecimalField(db_column='Peso', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pununidadalternativa = models.IntegerField(db_column='PunUnidadAlternativa', blank=True, null=True)  # Field name made lowercase.
    coeficiente = models.DecimalField(db_column='Coeficiente', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    puntipoot = models.IntegerField(db_column='PunTipoOT', blank=True, null=True)  # Field name made lowercase.
    punplanosinparvigente = models.IntegerField(db_column='PunPlanoSinParVigente', blank=True, null=True)  # Field name made lowercase.
    posicionarancelaria = models.CharField(db_column='PosicionArancelaria', max_length=50, blank=True, null=True)  # Field name made lowercase.
    puntipompse = models.IntegerField(db_column='PunTipoMPSE', blank=True, null=True)  # Field name made lowercase.
    unidadesporenvase = models.IntegerField(db_column='UnidadesPorEnvase', blank=True, null=True)  # Field name made lowercase.
    unidadreferenciafe = models.CharField(db_column='UnidadReferenciaFE', max_length=6, blank=True, null=True)  # Field name made lowercase.
    codigofe = models.CharField(db_column='CodigoFE', max_length=14, blank=True, null=True)  # Field name made lowercase.
    pununidadmedidafe = models.IntegerField(db_column='PunUnidadMedidaFE', blank=True, null=True)  # Field name made lowercase.
    codigobonofiscal = models.CharField(db_column='CodigoBonoFiscal', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cotcodigo = models.CharField(db_column='COTCodigo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cotcodigounidad = models.SmallIntegerField(db_column='COTCodigoUnidad', blank=True, null=True)  # Field name made lowercase.
    cotobligatorio = models.BooleanField(db_column='COTObligatorio', blank=True, null=True)  # Field name made lowercase.
    punsubclasificacion = models.IntegerField(db_column='PunSubClasificacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_gcarticulos23042021'


class Gcconplancuentas(models.Model):
    punplancuentas = models.IntegerField(db_column='PunPlanCuentas')  # Field name made lowercase.
    cuenta = models.CharField(db_column='Cuenta', max_length=9)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    aceptamovimientos = models.SmallIntegerField(db_column='AceptaMovimientos', blank=True, null=True)  # Field name made lowercase.
    puntipocuenta = models.SmallIntegerField(db_column='PunTipoCuenta', blank=True, null=True)  # Field name made lowercase.
    cuentasumariza = models.CharField(db_column='CuentaSumariza', max_length=9, blank=True, null=True)  # Field name made lowercase.
    cuentadistribuible = models.SmallIntegerField(db_column='CuentaDistribuible')  # Field name made lowercase.
    ajustaporinflacion = models.SmallIntegerField(db_column='AjustaPorInflacion', blank=True, null=True)  # Field name made lowercase.
    cuentaqueajusta = models.CharField(db_column='CuentaQueAjusta', max_length=9, blank=True, null=True)  # Field name made lowercase.
    cuentaajusteinflacion = models.CharField(db_column='CuentaAjusteInflacion', max_length=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_gcconplancuentas'


class Gcscli(models.Model):
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    punstatus = models.SmallIntegerField(db_column='PunStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_gcsCli'


class Gcsclistatuscambiados(models.Model):
    puncliente = models.IntegerField(db_column='PunCliente')  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_gcsCliStatusCambiados'


class Gcscliven(models.Model):
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    punvendedor = models.IntegerField(db_column='PunVendedor', blank=True, null=True)  # Field name made lowercase.
    predeterminado = models.BooleanField(db_column='Predeterminado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_gcsCliVen'


class Gcsaldos(models.Model):
    reporte = models.CharField(max_length=10, blank=True, null=True)
    puncliente = models.IntegerField(blank=True, null=True)
    codigo = models.CharField(max_length=20, blank=True, null=True)
    nombre = models.CharField(db_column='Nombre', max_length=200, blank=True, null=True)  # Field name made lowercase.
    saldo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_gcsaldos'


class Gcsartmodificados(models.Model):
    codigo = models.CharField(db_column='Codigo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150)  # Field name made lowercase.
    codigoalternativo = models.CharField(db_column='CodigoAlternativo', max_length=16, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_gcsartmodificados'


class Rentabilidadbasebup(models.Model):
    idoperacion = models.IntegerField(db_column='IDOperacion', blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importefacturado = models.DecimalField(db_column='ImporteFacturado', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dtoprontopago = models.DecimalField(db_column='DtoProntoPago', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valorfob = models.DecimalField(db_column='ValorFOB', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punmonedafob = models.IntegerField(db_column='PunMonedaFOB', blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    punreferencia = models.IntegerField(db_column='PunReferencia', blank=True, null=True)  # Field name made lowercase.
    coeficiente = models.FloatField(blank=True, null=True)
    importeoi = models.DecimalField(db_column='ImporteOI', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    puncomprobanteoi = models.IntegerField(db_column='puncomprobanteOI', blank=True, null=True)  # Field name made lowercase.
    importeconiva = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    puncliente = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    punsucursal = models.IntegerField(db_column='punSucursal', blank=True, null=True)  # Field name made lowercase.
    nroot = models.CharField(db_column='NroOT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cantidadot = models.DecimalField(db_column='CantidadOT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    costouniot = models.DecimalField(db_column='CostoUniOT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT', blank=True, null=True)  # Field name made lowercase.
    ordenot = models.SmallIntegerField(db_column='OrdenOT', blank=True, null=True)  # Field name made lowercase.
    cantidadcomprob = models.DecimalField(db_column='CantidadComprob', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_rentabilidadbaseBUP'


class Adesc(models.Model):
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adesc'


class ApptestExamplemodel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'appTest_examplemodel'


class ApptestProducto(models.Model):
    nombre = models.CharField(max_length=255)
    calidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'appTest_producto'


class ApptestProducts(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.BooleanField()
    image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'appTest_products'


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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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


class Auxprvcomprobantes(models.Model):
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    fechavto = models.DateTimeField(db_column='FechaVto', blank=True, null=True)  # Field name made lowercase.
    saldo = models.DecimalField(db_column='Saldo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='PunProveedor', blank=True, null=True)  # Field name made lowercase.
    importeapagar = models.DecimalField(db_column='ImporteAPagar', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importedescuento = models.DecimalField(db_column='ImporteDescuento', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importeinteres = models.DecimalField(db_column='ImporteInteres', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importeretencioniva = models.DecimalField(db_column='ImporteRetencionIVA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tipoabc = models.CharField(db_column='TipoABC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    prefijo = models.CharField(db_column='Prefijo', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sufijo = models.CharField(db_column='Sufijo', max_length=8, blank=True, null=True)  # Field name made lowercase.
    simbolo = models.CharField(db_column='Simbolo', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=200, blank=True, null=True)  # Field name made lowercase.
    puncondicion = models.IntegerField(db_column='PunCondicion', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    formulario576 = models.SmallIntegerField(db_column='Formulario576', blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa', blank=True, null=True)  # Field name made lowercase.
    empresa = models.CharField(db_column='Empresa', max_length=100, blank=True, null=True)  # Field name made lowercase.
    actividad = models.CharField(db_column='Actividad', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda', blank=True, null=True)  # Field name made lowercase.
    punactividadganancias = models.IntegerField(db_column='PunActividadGanancias', blank=True, null=True)  # Field name made lowercase.
    punconceptoib = models.IntegerField(db_column='PunConceptoIB', blank=True, null=True)  # Field name made lowercase.
    conceptodescripcion = models.CharField(db_column='ConceptoDescripcion', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auxPrvComprobantes'


class Auxiliaresimpl(models.Model):
    punordent = models.IntegerField(db_column='PunOrdenT', blank=True, null=True)  # Field name made lowercase.
    puntipoot = models.IntegerField(db_column='PunTipoOT', blank=True, null=True)  # Field name made lowercase.
    prefijo = models.CharField(db_column='Prefijo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sufijo = models.CharField(db_column='Sufijo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fecha = models.CharField(db_column='Fecha', max_length=20, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    fechaentrega = models.CharField(db_column='FechaEntrega', max_length=20, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auxiliaresimpl'


class Calab(models.Model):
    punarticulo = models.IntegerField(blank=True, null=True)
    codigo = models.IntegerField(blank=True, null=True)
    borrado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calab'


class Cliclientesbk(models.Model):
    puncliente = models.AutoField(primary_key=True, db_column='PunCliente')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=150)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    entrecalles = models.CharField(db_column='EntreCalles', max_length=150, blank=True, null=True)  # Field name made lowercase.
    telefonos = models.CharField(db_column='Telefonos', max_length=150, blank=True, null=True)  # Field name made lowercase.
    codigopostal = models.CharField(db_column='CodigoPostal', max_length=20, blank=True, null=True)  # Field name made lowercase.
    punpais = models.SmallIntegerField(db_column='PunPais', blank=True, null=True)  # Field name made lowercase.
    punprovincia = models.SmallIntegerField(db_column='PunProvincia', blank=True, null=True)  # Field name made lowercase.
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punzona = models.IntegerField(db_column='PunZona', blank=True, null=True)  # Field name made lowercase.
    punsubzona = models.IntegerField(db_column='PunSubZona', blank=True, null=True)  # Field name made lowercase.
    tiporecorrido = models.CharField(db_column='TipoRecorrido', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lugarentrega = models.CharField(db_column='LugarEntrega', max_length=150, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    punactividad = models.SmallIntegerField(db_column='PunActividad', blank=True, null=True)  # Field name made lowercase.
    fechaalta = models.DateTimeField(db_column='FechaAlta', blank=True, null=True)  # Field name made lowercase.
    puntipoiva = models.IntegerField(db_column='PunTipoIVA', blank=True, null=True)  # Field name made lowercase.
    puntipodocumento = models.IntegerField(db_column='PunTipoDocumento', blank=True, null=True)  # Field name made lowercase.
    cuit = models.CharField(db_column='Cuit', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nrodocumento = models.IntegerField(db_column='NroDocumento', blank=True, null=True)  # Field name made lowercase.
    punjurisdiccionib = models.SmallIntegerField(db_column='PunJurisdiccionIB', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    punclasificacion = models.IntegerField(db_column='PunClasificacion', blank=True, null=True)  # Field name made lowercase.
    delexterior = models.SmallIntegerField(db_column='DelExterior', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    credito = models.DecimalField(db_column='Credito', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punlistaprecio = models.IntegerField(db_column='PunListaPrecio', blank=True, null=True)  # Field name made lowercase.
    percepcioniva = models.SmallIntegerField(db_column='PercepcionIva', blank=True, null=True)  # Field name made lowercase.
    tipocliente = models.SmallIntegerField(db_column='TipoCliente')  # Field name made lowercase.
    punrecorrido = models.IntegerField(db_column='PunRecorrido', blank=True, null=True)  # Field name made lowercase.
    punmonedafactura = models.IntegerField(db_column='PunMonedaFactura', blank=True, null=True)  # Field name made lowercase.
    puncondicionventa = models.IntegerField(db_column='PunCondicionVenta', blank=True, null=True)  # Field name made lowercase.
    percepcionib = models.SmallIntegerField(db_column='PercepcionIB', blank=True, null=True)  # Field name made lowercase.
    distribuidor = models.SmallIntegerField(db_column='Distribuidor', blank=True, null=True)  # Field name made lowercase.
    punleyenda = models.IntegerField(blank=True, null=True)
    zonafranca = models.SmallIntegerField(db_column='ZonaFranca', blank=True, null=True)  # Field name made lowercase.
    preciounitario = models.SmallIntegerField(db_column='PrecioUnitario', blank=True, null=True)  # Field name made lowercase.
    subtotal = models.SmallIntegerField(db_column='SubTotal', blank=True, null=True)  # Field name made lowercase.
    netomercaderia = models.SmallIntegerField(db_column='NetoMercaderia', blank=True, null=True)  # Field name made lowercase.
    leyendatipocambio = models.SmallIntegerField(db_column='LeyendaTipoCambio', blank=True, null=True)  # Field name made lowercase.
    leyendatipocambio2 = models.SmallIntegerField(db_column='LeyendaTipoCambio2', blank=True, null=True)  # Field name made lowercase.
    nombrefantasia = models.CharField(db_column='NombreFantasia', max_length=150, blank=True, null=True)  # Field name made lowercase.
    web = models.CharField(db_column='Web', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cliclientesbk'


class Clidevolucionitempablo(models.Model):
    pundevolucionitem = models.AutoField(primary_key=True, db_column='PunDevolucionItem')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4)  # Field name made lowercase.
    preciooriginal = models.DecimalField(db_column='PrecioOriginal', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcentajeiva = models.DecimalField(db_column='PorcentajeIVA', max_digits=19, decimal_places=4)  # Field name made lowercase.
    orden = models.SmallIntegerField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.
    bonificacion = models.DecimalField(db_column='Bonificacion', max_digits=19, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clidevolucionitemPablo'


class Clidiferenciacambioimportesaux(models.Model):
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    punreferencia = models.IntegerField(db_column='PunReferencia')  # Field name made lowercase.
    puntipoimporte = models.IntegerField(db_column='PunTipoImporte')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clidiferenciacambioimportesaux'


class Descuent(models.Model):
    cliente = models.CharField(max_length=6)
    rubro = models.CharField(max_length=10)
    descuento = models.DecimalField(max_digits=6, decimal_places=2)
    cantidad = models.DecimalField(max_digits=9, decimal_places=2)
    detalle = models.CharField(max_length=30)
    detdes = models.CharField(max_length=34)
    desccant = models.DecimalField(max_digits=9, decimal_places=2)
    descuento1 = models.DecimalField(max_digits=5, decimal_places=2)
    descuento2 = models.DecimalField(max_digits=5, decimal_places=2)
    descuento3 = models.DecimalField(max_digits=5, decimal_places=2)
    descuento4 = models.DecimalField(max_digits=5, decimal_places=2)
    descuento5 = models.DecimalField(max_digits=5, decimal_places=2)
    precio = models.DecimalField(max_digits=12, decimal_places=3)
    pago = models.CharField(max_length=2)
    rango = models.CharField(max_length=2)
    lista = models.CharField(max_length=1)
    canmin = models.DecimalField(max_digits=9, decimal_places=2)
    canmax = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'descuent'


class Dif(models.Model):
    punorden = models.AutoField(primary_key=True, db_column='PunOrden')  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    dia = models.IntegerField(db_column='Dia', blank=True, null=True)  # Field name made lowercase.
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=3, blank=True, null=True)  # Field name made lowercase.
    comprobante = models.CharField(db_column='Comprobante', max_length=20, blank=True, null=True)  # Field name made lowercase.
    comprobanteorden = models.CharField(db_column='ComprobanteOrden', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nrocomprobante = models.CharField(db_column='NroComprobante', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tipoabc = models.CharField(db_column='TipoABC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    proveedor = models.CharField(db_column='Proveedor', max_length=120, blank=True, null=True)  # Field name made lowercase.
    cuit = models.CharField(db_column='CUIT', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gravado = models.DecimalField(db_column='Gravado', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    iva = models.DecimalField(db_column='Iva', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    exentoynoresp = models.DecimalField(db_column='ExentoYNoResp', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    respmonotributo = models.DecimalField(db_column='RespMonotributo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    percepcioniva = models.DecimalField(db_column='PercepcionIVA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    percepcionib = models.DecimalField(db_column='PercepcionIB', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totgral = models.DecimalField(db_column='TotGral', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    orden = models.IntegerField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa', blank=True, null=True)  # Field name made lowercase.
    punproveedor = models.IntegerField(db_column='PunProveedor', blank=True, null=True)  # Field name made lowercase.
    tipoprov = models.SmallIntegerField(db_column='TipoProv', blank=True, null=True)  # Field name made lowercase.
    puntipoiva = models.IntegerField(db_column='PunTipoIVA', blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    iva2 = models.DecimalField(db_column='IVA2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ib = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dif'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class Dtproperties(models.Model):
    objectid = models.IntegerField(blank=True, null=True)
    property = models.CharField(max_length=64)
    value = models.CharField(max_length=255, blank=True, null=True)
    uvalue = models.CharField(max_length=255, blank=True, null=True)
    lvalue = models.BinaryField(blank=True, null=True)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dtproperties'
        unique_together = (('id', 'property'),)


class Fuckhorn(models.Model):
    punarticulo = models.IntegerField(blank=True, null=True)
    codigo = models.CharField(max_length=255, blank=True, null=True)
    codigoalternativo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fuckhorn'


class GcActualizararticulos(models.Model):
    punarticulo = models.IntegerField(db_column='PunARticulo', blank=True, null=True)  # Field name made lowercase.
    descripcionnueva = models.CharField(db_column='DescripcionNueva', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gc_ActualizarArticulos'


class GcArticulospreciosduplicados(models.Model):
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.
    punlista = models.IntegerField(db_column='PunLista')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gc_ArticulosPreciosDuplicados'


class GcListaprecioarticulosborrados(models.Model):
    punprecio = models.IntegerField(db_column='PunPrecio')  # Field name made lowercase.
    punlista = models.IntegerField(db_column='PunLista')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fechamodificacion = models.DateTimeField(db_column='FechaModificacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gc_ListaPrecioArticulosBORRADOS'


class Gcs2(models.Model):
    puntero = models.IntegerField(db_column='Puntero')  # Field name made lowercase.
    punremito = models.IntegerField(db_column='PunRemito', blank=True, null=True)  # Field name made lowercase.
    codigocot = models.CharField(db_column='CodigoCOT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    punhojarutacot = models.IntegerField(db_column='PunHojaRutaCOT', blank=True, null=True)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gcs2'


class Gcsagregados(models.Model):
    punremito = models.IntegerField(db_column='PunRemito')  # Field name made lowercase.
    punhojarutacot = models.IntegerField(db_column='PunHojaRutaCOT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gcsAgregados'


class Gcsbonif(models.Model):
    puncliente = models.FloatField(db_column='punCliente', blank=True, null=True)  # Field name made lowercase.
    codcliente = models.FloatField(db_column='CodCliente', blank=True, null=True)  # Field name made lowercase.
    descliente = models.CharField(db_column='Descliente', max_length=255, blank=True, null=True)  # Field name made lowercase.
    punrubro = models.FloatField(db_column='punRubro', blank=True, null=True)  # Field name made lowercase.
    codrubro = models.CharField(db_column='CodRubro', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desrubro = models.CharField(db_column='DesRubro', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pungrupo = models.FloatField(db_column='punGrupo', blank=True, null=True)  # Field name made lowercase.
    codgrupo = models.CharField(db_column='CodGrupo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desgrupo = models.CharField(db_column='DesGrupo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    punfamilia = models.FloatField(db_column='punFamilia', blank=True, null=True)  # Field name made lowercase.
    codfamilia = models.CharField(db_column='CodFamilia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desfamilia = models.CharField(db_column='DesFamilia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.FloatField(db_column='punArticulo', blank=True, null=True)  # Field name made lowercase.
    codarticulo = models.CharField(db_column='CodArticulo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desarticulo = models.CharField(db_column='DesArticulo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bonif01 = models.FloatField(db_column='Bonif01', blank=True, null=True)  # Field name made lowercase.
    bonif02 = models.FloatField(db_column='Bonif02', blank=True, null=True)  # Field name made lowercase.
    bonif03 = models.FloatField(db_column='Bonif03', blank=True, null=True)  # Field name made lowercase.
    bonif04 = models.FloatField(db_column='Bonif04', blank=True, null=True)  # Field name made lowercase.
    bonif05 = models.FloatField(db_column='Bonif05', blank=True, null=True)  # Field name made lowercase.
    bonif06 = models.FloatField(db_column='Bonif06', blank=True, null=True)  # Field name made lowercase.
    bonif07 = models.FloatField(db_column='Bonif07', blank=True, null=True)  # Field name made lowercase.
    bonif08 = models.FloatField(db_column='Bonif08', blank=True, null=True)  # Field name made lowercase.
    bonif09 = models.FloatField(db_column='Bonif09', blank=True, null=True)  # Field name made lowercase.
    bonif10 = models.FloatField(db_column='Bonif10', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gcsBonif'


class Gcsclientes(models.Model):
    puncliente = models.FloatField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    codigo = models.FloatField(db_column='Codigo', blank=True, null=True)  # Field name made lowercase.
    nomnbre = models.CharField(db_column='Nomnbre', max_length=255, blank=True, null=True)  # Field name made lowercase.
    punlocalidad = models.FloatField(db_column='PunLocalidad', blank=True, null=True)  # Field name made lowercase.
    punprovincia = models.FloatField(db_column='PunProvincia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gcsClientes'


class Gcsclientes20140414(models.Model):
    puncliente = models.AutoField(primary_key=True, db_column='PunCliente')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=150)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    entrecalles = models.CharField(db_column='EntreCalles', max_length=150, blank=True, null=True)  # Field name made lowercase.
    telefonos = models.CharField(db_column='Telefonos', max_length=150, blank=True, null=True)  # Field name made lowercase.
    codigopostal = models.CharField(db_column='CodigoPostal', max_length=20, blank=True, null=True)  # Field name made lowercase.
    punpais = models.SmallIntegerField(db_column='PunPais', blank=True, null=True)  # Field name made lowercase.
    punprovincia = models.SmallIntegerField(db_column='PunProvincia', blank=True, null=True)  # Field name made lowercase.
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punzona = models.IntegerField(db_column='PunZona', blank=True, null=True)  # Field name made lowercase.
    punsubzona = models.IntegerField(db_column='PunSubZona', blank=True, null=True)  # Field name made lowercase.
    tiporecorrido = models.CharField(db_column='TipoRecorrido', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lugarentrega = models.CharField(db_column='LugarEntrega', max_length=150, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    punactividad = models.SmallIntegerField(db_column='PunActividad', blank=True, null=True)  # Field name made lowercase.
    fechaalta = models.DateTimeField(db_column='FechaAlta', blank=True, null=True)  # Field name made lowercase.
    puntipoiva = models.IntegerField(db_column='PunTipoIVA', blank=True, null=True)  # Field name made lowercase.
    puntipodocumento = models.IntegerField(db_column='PunTipoDocumento', blank=True, null=True)  # Field name made lowercase.
    cuit = models.CharField(db_column='Cuit', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nrodocumento = models.IntegerField(db_column='NroDocumento', blank=True, null=True)  # Field name made lowercase.
    punjurisdiccionib = models.SmallIntegerField(db_column='PunJurisdiccionIB', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    punclasificacion = models.IntegerField(db_column='PunClasificacion', blank=True, null=True)  # Field name made lowercase.
    delexterior = models.SmallIntegerField(db_column='DelExterior', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    credito = models.DecimalField(db_column='Credito', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punlistaprecio = models.IntegerField(db_column='PunListaPrecio', blank=True, null=True)  # Field name made lowercase.
    percepcioniva = models.SmallIntegerField(db_column='PercepcionIva', blank=True, null=True)  # Field name made lowercase.
    tipocliente = models.SmallIntegerField(db_column='TipoCliente')  # Field name made lowercase.
    punrecorrido = models.IntegerField(db_column='PunRecorrido', blank=True, null=True)  # Field name made lowercase.
    punmonedafactura = models.IntegerField(db_column='PunMonedaFactura', blank=True, null=True)  # Field name made lowercase.
    puncondicionventa = models.IntegerField(db_column='PunCondicionVenta', blank=True, null=True)  # Field name made lowercase.
    percepcionib = models.SmallIntegerField(db_column='PercepcionIB', blank=True, null=True)  # Field name made lowercase.
    distribuidor = models.SmallIntegerField(db_column='Distribuidor', blank=True, null=True)  # Field name made lowercase.
    punleyenda = models.IntegerField(blank=True, null=True)
    zonafranca = models.SmallIntegerField(db_column='ZonaFranca', blank=True, null=True)  # Field name made lowercase.
    preciounitario = models.SmallIntegerField(db_column='PrecioUnitario', blank=True, null=True)  # Field name made lowercase.
    subtotal = models.SmallIntegerField(db_column='SubTotal', blank=True, null=True)  # Field name made lowercase.
    netomercaderia = models.SmallIntegerField(db_column='NetoMercaderia', blank=True, null=True)  # Field name made lowercase.
    leyendatipocambio = models.SmallIntegerField(db_column='LeyendaTipoCambio', blank=True, null=True)  # Field name made lowercase.
    leyendatipocambio2 = models.SmallIntegerField(db_column='LeyendaTipoCambio2', blank=True, null=True)  # Field name made lowercase.
    nombrefantasia = models.CharField(db_column='NombreFantasia', max_length=150, blank=True, null=True)  # Field name made lowercase.
    web = models.CharField(db_column='Web', max_length=150, blank=True, null=True)  # Field name made lowercase.
    servicioafilado = models.SmallIntegerField(db_column='ServicioAfilado', blank=True, null=True)  # Field name made lowercase.
    emailfactura = models.CharField(db_column='EMailFactura', max_length=500, blank=True, null=True)  # Field name made lowercase.
    idimpositivo = models.CharField(db_column='IDImpositivo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    punlocalidad = models.IntegerField(db_column='PunLocalidad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gcsClientes20140414'


class Gcsclientes4(models.Model):
    punclientes = models.FloatField(db_column='PunClientes', blank=True, null=True)  # Field name made lowercase.
    punlocalidad = models.FloatField(db_column='PunLocalidad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gcsClientes4'


class Gcslocalidades(models.Model):
    punlocalidad = models.FloatField(db_column='PunLocalidad', blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=255, blank=True, null=True)  # Field name made lowercase.
    punprovincia = models.FloatField(db_column='PunProvincia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gcsLocalidades'


class Gcslocalidades20140414(models.Model):
    punlocalidad = models.AutoField(primary_key=True, db_column='PunLocalidad')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    punlocalidadstarcom = models.IntegerField(db_column='PunLocalidadStarcom', blank=True, null=True)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    punprovincia = models.IntegerField(db_column='punProvincia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gcsLocalidades20140414'


class Gcslocalidades4(models.Model):
    punlocalidad = models.FloatField(db_column='PunLocalidad', blank=True, null=True)  # Field name made lowercase.
    punprovincia = models.FloatField(db_column='PunProvincia', blank=True, null=True)  # Field name made lowercase.
    localidad = models.CharField(db_column='Localidad', max_length=255, blank=True, null=True)  # Field name made lowercase.
    f4 = models.CharField(db_column='F4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    f5 = models.CharField(db_column='F5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    f6 = models.CharField(db_column='F6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    f7 = models.CharField(db_column='F7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    f8 = models.CharField(db_column='F8', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gcsLocalidades4'


class Gcsprvproveedoresacumulados(models.Model):
    punproveedor = models.IntegerField(db_column='PunProveedor')  # Field name made lowercase.
    pagosmes = models.SmallIntegerField(db_column='PagosMes', blank=True, null=True)  # Field name made lowercase.
    pagosanio = models.SmallIntegerField(db_column='PagosAnio', blank=True, null=True)  # Field name made lowercase.
    acumuladopagos = models.DecimalField(db_column='AcumuladoPagos', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    acumuladoretencion = models.DecimalField(db_column='AcumuladoRetencion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa', blank=True, null=True)  # Field name made lowercase.
    punactividadganancias = models.IntegerField(db_column='PunActividadGanancias', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gcsPRVProveedoresAcumulados'


class Gcsprovincias(models.Model):
    punprovincia = models.IntegerField(db_column='PunProvincia')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado')  # Field name made lowercase.
    codigodgi = models.IntegerField(db_column='CodigoDGI', blank=True, null=True)  # Field name made lowercase.
    punpais = models.IntegerField(db_column='PunPais', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gcsProvincias'


class Gcsprovincias20140414(models.Model):
    punprovincia = models.AutoField(primary_key=True, db_column='PunProvincia')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado')  # Field name made lowercase.
    codigodgi = models.IntegerField(db_column='CodigoDGI', blank=True, null=True)  # Field name made lowercase.
    punpais = models.IntegerField(db_column='PunPais', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gcsProvincias20140414'


class Gcsprovincias4(models.Model):
    punprovincia = models.FloatField(db_column='PunProvincia', blank=True, null=True)  # Field name made lowercase.
    provincia = models.CharField(db_column='Provincia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coddgi = models.FloatField(db_column='CodDGI', blank=True, null=True)  # Field name made lowercase.
    punpais = models.FloatField(db_column='PunPais', blank=True, null=True)  # Field name made lowercase.
    f5 = models.CharField(db_column='F5', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gcsProvincias4'


class GcsBonificaciones(models.Model):
    puncliente = models.IntegerField(db_column='punCliente', blank=True, null=True)  # Field name made lowercase.
    codcliente = models.CharField(db_column='CodCliente', max_length=8, blank=True, null=True)  # Field name made lowercase.
    descliente = models.CharField(db_column='Descliente', max_length=150, blank=True, null=True)  # Field name made lowercase.
    punrubro = models.IntegerField(db_column='punRubro', blank=True, null=True)  # Field name made lowercase.
    codrubro = models.CharField(db_column='CodRubro', max_length=4, blank=True, null=True)  # Field name made lowercase.
    desrubro = models.CharField(db_column='DesRubro', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pungrupo = models.IntegerField(db_column='punGrupo', blank=True, null=True)  # Field name made lowercase.
    codgrupo = models.CharField(db_column='CodGrupo', max_length=4, blank=True, null=True)  # Field name made lowercase.
    desgrupo = models.CharField(db_column='DesGrupo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punfamilia = models.IntegerField(db_column='punFamilia', blank=True, null=True)  # Field name made lowercase.
    codfamilia = models.CharField(db_column='CodFamilia', max_length=4, blank=True, null=True)  # Field name made lowercase.
    desfamilia = models.CharField(db_column='DesFamilia', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='punArticulo', blank=True, null=True)  # Field name made lowercase.
    codarticulo = models.CharField(db_column='CodArticulo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    desarticulo = models.CharField(db_column='DesArticulo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    boniforden01 = models.DecimalField(db_column='BonifOrden01', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    boniforden02 = models.DecimalField(db_column='BonifOrden02', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    boniforden03 = models.DecimalField(db_column='BonifOrden03', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    boniforden04 = models.DecimalField(db_column='BonifOrden04', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    boniforden05 = models.DecimalField(db_column='BonifOrden05', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    boniforden06 = models.DecimalField(db_column='BonifOrden06', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    boniforden07 = models.DecimalField(db_column='BonifOrden07', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    boniforden08 = models.DecimalField(db_column='BonifOrden08', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    boniforden09 = models.DecimalField(db_column='BonifOrden09', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    boniforden10 = models.DecimalField(db_column='BonifOrden10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gcs_Bonificaciones'


class GcsMovstockpunart2528(models.Model):
    punmovimiento = models.AutoField(primary_key=True, db_column='PunMovimiento')  # Field name made lowercase.
    pundeposito = models.IntegerField(db_column='PunDeposito')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    puntipomovimiento = models.IntegerField(db_column='PunTipoMovimiento')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punremitoitemventa = models.IntegerField(db_column='PunRemitoItemVenta', blank=True, null=True)  # Field name made lowercase.
    punremitoitemcompra = models.IntegerField(db_column='PunRemitoItemCompra', blank=True, null=True)  # Field name made lowercase.
    punmotivo = models.IntegerField(db_column='PunMotivo', blank=True, null=True)  # Field name made lowercase.
    nroordent = models.CharField(db_column='NroOrdenT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    punremitotransferencia = models.IntegerField(db_column='PunRemitoTransferencia', blank=True, null=True)  # Field name made lowercase.
    idoperacion = models.IntegerField(db_column='IdOperacion', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punmovimientoencabezado = models.IntegerField(db_column='PunMovimientoEncabezado', blank=True, null=True)  # Field name made lowercase.
    punordent = models.IntegerField(db_column='PunOrdenT', blank=True, null=True)  # Field name made lowercase.
    tipostock = models.SmallIntegerField(db_column='TipoStock', blank=True, null=True)  # Field name made lowercase.
    punmovimientoorigen = models.IntegerField(db_column='PunMovimientoOrigen', blank=True, null=True)  # Field name made lowercase.
    punremitoitemcompraanterior = models.IntegerField(db_column='PunRemitoItemCompraAnterior', blank=True, null=True)  # Field name made lowercase.
    momento = models.DateTimeField(db_column='Momento', blank=True, null=True)  # Field name made lowercase.
    punusuario = models.IntegerField(db_column='PunUsuario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gcs_MovStockPunArt2528'


class GcsOe(models.Model):
    puncomprobante = models.IntegerField(db_column='PunComprobante')  # Field name made lowercase.
    puntipopago = models.IntegerField(db_column='PunTipoPago')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda')  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4)  # Field name made lowercase.
    punbanco = models.IntegerField(db_column='PunBanco', blank=True, null=True)  # Field name made lowercase.
    nrocheque = models.IntegerField(db_column='NroCheque', blank=True, null=True)  # Field name made lowercase.
    punorigen = models.IntegerField(db_column='PunOrigen', blank=True, null=True)  # Field name made lowercase.
    puncomprobanteasociado = models.IntegerField(db_column='PunComprobanteAsociado', blank=True, null=True)  # Field name made lowercase.
    punpago = models.AutoField(primary_key=True, db_column='PunPago')  # Field name made lowercase.
    borrado = models.SmallIntegerField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=2, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    puncomprobanteorigen = models.IntegerField(db_column='punComprobanteOrigen', blank=True, null=True)  # Field name made lowercase.
    cotizacionsinredondear = models.DecimalField(db_column='CotizacionSinRedondear', max_digits=12, decimal_places=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gcs_OE'


class GcsOt(models.Model):
    punordent = models.IntegerField(db_column='PunOrdent', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gcs_OT'


class GcsRemitoscot(models.Model):
    punhojaruta = models.IntegerField(db_column='PunHojaRuta', blank=True, null=True)  # Field name made lowercase.
    statuscot = models.SmallIntegerField(db_column='StatusCOT', blank=True, null=True)  # Field name made lowercase.
    fechasalida = models.DateTimeField(db_column='FechaSalida', blank=True, null=True)  # Field name made lowercase.
    punresponsable = models.IntegerField(db_column='PunResponsable', blank=True, null=True)  # Field name made lowercase.
    punhojarutacot = models.IntegerField(db_column='PunHojaRutaCOT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gcs_RemitosCOT'


class Gcs_Articulos(models.Model):
    puntero = models.FloatField(blank=True, null=True)
    descripcion = models.CharField(db_column='Descripcion', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gcs_articulos'


class GcsFf(models.Model):
    punvendedor = models.IntegerField(db_column='punVendedor', blank=True, null=True)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='punComprobante', blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    importesinimpuestos = models.DecimalField(db_column='ImporteSinImpuestos', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gcs_ff'


class Gcsbonif20130506(models.Model):
    puncliente = models.FloatField(db_column='punCliente', blank=True, null=True)  # Field name made lowercase.
    codcliente = models.CharField(db_column='CodCliente', max_length=255, blank=True, null=True)  # Field name made lowercase.
    descliente = models.CharField(db_column='Descliente', max_length=255, blank=True, null=True)  # Field name made lowercase.
    punrubro = models.FloatField(db_column='punRubro', blank=True, null=True)  # Field name made lowercase.
    codrubro = models.CharField(db_column='CodRubro', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desrubro = models.CharField(db_column='DesRubro', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pungrupo = models.FloatField(db_column='punGrupo', blank=True, null=True)  # Field name made lowercase.
    codgrupo = models.CharField(db_column='CodGrupo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desgrupo = models.CharField(db_column='DesGrupo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    punfamilia = models.FloatField(db_column='punFamilia', blank=True, null=True)  # Field name made lowercase.
    codfamilia = models.CharField(db_column='CodFamilia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desfamilia = models.CharField(db_column='DesFamilia', max_length=255, blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.FloatField(db_column='punArticulo', blank=True, null=True)  # Field name made lowercase.
    codarticulo = models.CharField(db_column='CodArticulo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desarticulo = models.CharField(db_column='DesArticulo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bonif01 = models.FloatField(db_column='Bonif01', blank=True, null=True)  # Field name made lowercase.
    bonif02 = models.FloatField(db_column='Bonif02', blank=True, null=True)  # Field name made lowercase.
    bonif03 = models.FloatField(db_column='Bonif03', blank=True, null=True)  # Field name made lowercase.
    bonif04 = models.FloatField(db_column='Bonif04', blank=True, null=True)  # Field name made lowercase.
    bonif05 = models.FloatField(db_column='Bonif05', blank=True, null=True)  # Field name made lowercase.
    bonif06 = models.FloatField(db_column='Bonif06', blank=True, null=True)  # Field name made lowercase.
    bonif07 = models.FloatField(db_column='Bonif07', blank=True, null=True)  # Field name made lowercase.
    bonif08 = models.FloatField(db_column='Bonif08', blank=True, null=True)  # Field name made lowercase.
    bonif09 = models.FloatField(db_column='Bonif09', blank=True, null=True)  # Field name made lowercase.
    bonif10 = models.FloatField(db_column='Bonif10', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gcsbonif20130506'


class Gcsbonifbk(models.Model):
    fechaproceso = models.DateTimeField(db_column='FechaProceso')  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente')  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    punrubro = models.IntegerField(db_column='PunRubro', blank=True, null=True)  # Field name made lowercase.
    orden = models.SmallIntegerField(db_column='Orden')  # Field name made lowercase.
    descuento = models.DecimalField(db_column='Descuento', max_digits=19, decimal_places=4)  # Field name made lowercase.
    pungrupo = models.IntegerField(db_column='punGrupo', blank=True, null=True)  # Field name made lowercase.
    punfamilia = models.IntegerField(db_column='punFamilia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gcsbonifbk'


class Gcscashflow20121102(models.Model):
    puncashflow = models.AutoField(primary_key=True, db_column='PunCashflow')  # Field name made lowercase.
    punempresa = models.IntegerField(db_column='PunEmpresa')  # Field name made lowercase.
    fechavto = models.DateTimeField(db_column='FechaVto')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4)  # Field name made lowercase.
    tipoingresoegreso = models.SmallIntegerField(db_column='TipoIngresoEgreso')  # Field name made lowercase.
    punorigen = models.IntegerField(db_column='PunOrigen')  # Field name made lowercase.
    punclienteproveedor = models.IntegerField(db_column='PunClienteProveedor', blank=True, null=True)  # Field name made lowercase.
    punreferenciacashflow = models.IntegerField(db_column='PunReferenciaCashflow', blank=True, null=True)  # Field name made lowercase.
    realestimado = models.SmallIntegerField(db_column='RealEstimado')  # Field name made lowercase.
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=2)  # Field name made lowercase.
    puncomprobante = models.IntegerField(db_column='PunComprobante', blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.SmallIntegerField(db_column='PunMoneda')  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4)  # Field name made lowercase.
    fechavtooriginal = models.DateTimeField(db_column='FechaVtoOriginal', blank=True, null=True)  # Field name made lowercase.
    punreferencia = models.IntegerField(db_column='PunReferencia', blank=True, null=True)  # Field name made lowercase.
    tiporeferencia = models.CharField(db_column='TipoReferencia', max_length=2, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gcscashflow20121102'


class Gcscliclientesant(models.Model):
    puncliente = models.AutoField(primary_key=True, db_column='PunCliente')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=150)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    entrecalles = models.CharField(db_column='EntreCalles', max_length=150, blank=True, null=True)  # Field name made lowercase.
    telefonos = models.CharField(db_column='Telefonos', max_length=150, blank=True, null=True)  # Field name made lowercase.
    codigopostal = models.CharField(db_column='CodigoPostal', max_length=20, blank=True, null=True)  # Field name made lowercase.
    punpais = models.SmallIntegerField(db_column='PunPais', blank=True, null=True)  # Field name made lowercase.
    punprovincia = models.SmallIntegerField(db_column='PunProvincia', blank=True, null=True)  # Field name made lowercase.
    localidad = models.CharField(db_column='Localidad', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punzona = models.IntegerField(db_column='PunZona', blank=True, null=True)  # Field name made lowercase.
    punsubzona = models.IntegerField(db_column='PunSubZona', blank=True, null=True)  # Field name made lowercase.
    tiporecorrido = models.CharField(db_column='TipoRecorrido', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lugarentrega = models.CharField(db_column='LugarEntrega', max_length=150, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=150, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    punactividad = models.SmallIntegerField(db_column='PunActividad', blank=True, null=True)  # Field name made lowercase.
    fechaalta = models.DateTimeField(db_column='FechaAlta', blank=True, null=True)  # Field name made lowercase.
    puntipoiva = models.IntegerField(db_column='PunTipoIVA', blank=True, null=True)  # Field name made lowercase.
    puntipodocumento = models.IntegerField(db_column='PunTipoDocumento', blank=True, null=True)  # Field name made lowercase.
    cuit = models.CharField(db_column='Cuit', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nrodocumento = models.IntegerField(db_column='NroDocumento', blank=True, null=True)  # Field name made lowercase.
    punjurisdiccionib = models.SmallIntegerField(db_column='PunJurisdiccionIB', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    punclasificacion = models.IntegerField(db_column='PunClasificacion', blank=True, null=True)  # Field name made lowercase.
    delexterior = models.SmallIntegerField(db_column='DelExterior', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    credito = models.DecimalField(db_column='Credito', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punlistaprecio = models.IntegerField(db_column='PunListaPrecio', blank=True, null=True)  # Field name made lowercase.
    percepcioniva = models.SmallIntegerField(db_column='PercepcionIva', blank=True, null=True)  # Field name made lowercase.
    tipocliente = models.SmallIntegerField(db_column='TipoCliente')  # Field name made lowercase.
    punrecorrido = models.IntegerField(db_column='PunRecorrido', blank=True, null=True)  # Field name made lowercase.
    punmonedafactura = models.IntegerField(db_column='PunMonedaFactura', blank=True, null=True)  # Field name made lowercase.
    puncondicionventa = models.IntegerField(db_column='PunCondicionVenta', blank=True, null=True)  # Field name made lowercase.
    percepcionib = models.SmallIntegerField(db_column='PercepcionIB', blank=True, null=True)  # Field name made lowercase.
    distribuidor = models.SmallIntegerField(db_column='Distribuidor', blank=True, null=True)  # Field name made lowercase.
    punleyenda = models.IntegerField(blank=True, null=True)
    zonafranca = models.SmallIntegerField(db_column='ZonaFranca', blank=True, null=True)  # Field name made lowercase.
    preciounitario = models.SmallIntegerField(db_column='PrecioUnitario', blank=True, null=True)  # Field name made lowercase.
    subtotal = models.SmallIntegerField(db_column='SubTotal', blank=True, null=True)  # Field name made lowercase.
    netomercaderia = models.SmallIntegerField(db_column='NetoMercaderia', blank=True, null=True)  # Field name made lowercase.
    leyendatipocambio = models.SmallIntegerField(db_column='LeyendaTipoCambio', blank=True, null=True)  # Field name made lowercase.
    leyendatipocambio2 = models.SmallIntegerField(db_column='LeyendaTipoCambio2', blank=True, null=True)  # Field name made lowercase.
    nombrefantasia = models.CharField(db_column='NombreFantasia', max_length=150, blank=True, null=True)  # Field name made lowercase.
    web = models.CharField(db_column='Web', max_length=150, blank=True, null=True)  # Field name made lowercase.
    servicioafilado = models.SmallIntegerField(db_column='ServicioAfilado', blank=True, null=True)  # Field name made lowercase.
    emailfactura = models.CharField(db_column='EMailFactura', max_length=500, blank=True, null=True)  # Field name made lowercase.
    idimpositivo = models.CharField(db_column='IDImpositivo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    punlocalidad = models.IntegerField(db_column='PunLocalidad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gcscliclientesant'


class Gcscotnom(models.Model):
    cot = models.FloatField(db_column='COT', blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.FloatField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gcscotnom'


class Gcscotnom2(models.Model):
    cot = models.CharField(db_column='COT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.CharField(db_column='PunArticulo', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gcscotnom2'


class Gcsti20140207(models.Model):
    punreferencia = models.IntegerField()
    saldo = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gcsti20140207'


class Hcaccionafilado(models.Model):
    punaccion = models.IntegerField(db_column='PunAccion')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcAccionAfilado'


class Hcafiptipostributo(models.Model):
    codigoafip = models.CharField(db_column='CodigoAFIP', max_length=3, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcAfipTiposTributo'


class Hcalicuotaiva(models.Model):
    punalicuotaiva = models.AutoField(primary_key=True, db_column='punAlicuotaIva')  # Field name made lowercase.
    alicuota = models.DecimalField(max_digits=19, decimal_places=4)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    codigoafip = models.CharField(db_column='CodigoAfip', max_length=3, blank=True, null=True)  # Field name made lowercase.
    codigoafiprg3685 = models.CharField(db_column='CodigoAfipRG3685', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcAlicuotaIva'


class Hcconmodulos(models.Model):
    punmodulo = models.IntegerField(db_column='PunModulo', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcCONModulos'


class Hcconceptos(models.Model):
    punconcepto = models.IntegerField(db_column='PunConcepto')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcConceptos'


class Hcconceptosib(models.Model):
    punconcepto = models.AutoField(primary_key=True, db_column='PunConcepto')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcConceptosIB'


class Hccondicionvta(models.Model):
    puncondicion = models.SmallIntegerField(db_column='PunCondicion')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcCondicionVta'


class Hcdescripciongrupo(models.Model):
    pundescripciongrupo = models.SmallIntegerField(db_column='PunDescripcionGrupo')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcDescripcionGrupo'


class Hcestadomodifpedidoitem(models.Model):
    estadomodifitem = models.SmallIntegerField(db_column='EstadoModifItem', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcEstadoModifPedidoItem'


class Hcfcetransmision(models.Model):
    puntransmision = models.IntegerField(db_column='PunTransmision', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcFCETransmision'


class Hcformaspago(models.Model):
    puncondicionventa = models.AutoField(db_column='PunCondicionVenta', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=120)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    contraentrega = models.SmallIntegerField(db_column='ContraEntrega', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcFormasPago'


class Hcformaspagodias(models.Model):
    puncondicionventa = models.IntegerField(db_column='PunCondicionVenta')  # Field name made lowercase.
    dias = models.IntegerField(db_column='Dias')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcFormasPagoDias'


class Hcidiomas(models.Model):
    punidioma = models.SmallIntegerField(db_column='PunIdioma')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcIdiomas'


class Hcincoterms(models.Model):
    punincoterm = models.SmallIntegerField(db_column='PunIncoterm')  # Field name made lowercase.
    codigoafip = models.CharField(db_column='CodigoAfip', max_length=4)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcIncoterms'


class Hckmsrecorrido(models.Model):
    puntero = models.IntegerField(db_column='Puntero', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dias = models.SmallIntegerField(db_column='Dias', blank=True, null=True)  # Field name made lowercase.
    solicitarvto = models.BooleanField(db_column='SolicitarVto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcKmsRecorrido'


class Hclibroivaexcluirproveedor(models.Model):
    punproveedor = models.IntegerField(db_column='PunProveedor', blank=True, null=True)  # Field name made lowercase.
    accion = models.SmallIntegerField(db_column='Accion', blank=True, null=True)  # Field name made lowercase.
    despachante = models.SmallIntegerField(db_column='Despachante', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcLibroIvaExcluirProveedor'


class Hclogtablas(models.Model):
    puncampo = models.AutoField(primary_key=True, db_column='PunCampo')  # Field name made lowercase.
    tabla = models.CharField(db_column='Tabla', max_length=100, blank=True, null=True)  # Field name made lowercase.
    campo = models.CharField(db_column='Campo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tipodato = models.CharField(db_column='TipoDato', max_length=100, blank=True, null=True)  # Field name made lowercase.
    campodescripcion = models.CharField(db_column='CampoDescripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tablarelacionada = models.CharField(db_column='TablaRelacionada', max_length=100, blank=True, null=True)  # Field name made lowercase.
    punterotablarelacion = models.CharField(db_column='PunteroTablaRelacion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    campotablarelacion = models.CharField(db_column='CampoTablaRelacion', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcLogTablas'


class Hcmes(models.Model):
    mes = models.IntegerField(db_column='Mes', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcMes'


class Hcmodoabm(models.Model):
    modoabm = models.SmallIntegerField(db_column='ModoABM')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcModoABM'


class Hcotcausaaviso(models.Model):
    puncausaaviso = models.IntegerField(db_column='PunCausaAviso', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=20, blank=True, null=True)  # Field name made lowercase.
    punsector = models.IntegerField(db_column='PunSector', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcOTCausaAviso'


class Hcopcionalesafip(models.Model):
    id = models.IntegerField(primary_key=True, db_column='Id')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=512)  # Field name made lowercase.
    fechadesde = models.DateTimeField(db_column='FechaDesde')  # Field name made lowercase.
    fechahasta = models.DateTimeField(db_column='FechaHasta', blank=True, null=True)  # Field name made lowercase.
    tipovalor = models.IntegerField(db_column='TipoValor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcOpcionalesAFIP'


class Hcorigenarticulo(models.Model):
    punorigenarticulo = models.IntegerField(db_column='PunOrigenArticulo', unique=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.
    datosimportacion = models.BooleanField(db_column='DatosImportacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcOrigenArticulo'


class Hcpermisos(models.Model):
    permiso = models.IntegerField(db_column='Permiso', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    enum = models.CharField(db_column='Enum', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcPermisos'


class Hcplanoaccion(models.Model):
    punplanoaccion = models.IntegerField(db_column='punPlanoAccion', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcPlanoAccion'


class Hcprioridades(models.Model):
    prioridad = models.IntegerField(db_column='Prioridad')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcPrioridades'


class Hcpuntosdeventa(models.Model):
    puntodeventa = models.SmallIntegerField(db_column='PuntoDeVenta')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcPuntosDeVenta'


class Hcrutinas(models.Model):
    punrutina = models.IntegerField(db_column='PunRutina')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcRutinas'


class Hcsituacionib(models.Model):
    punsituacioniibb = models.SmallIntegerField(db_column='PunSituacionIIBB', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcSituacionIB'


class Hcstatusarticulo(models.Model):
    punstatus = models.IntegerField(db_column='PunStatus')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcStatusArticulo'


class Hcstatusbienes(models.Model):
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcStatusBienes'


class Hcstatuscliremitos(models.Model):
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcStatusCLIRemitos'


class Hcstatuscot(models.Model):
    statuscot = models.SmallIntegerField(db_column='StatusCOT', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcStatusCOT'


class Hcstatuscheque(models.Model):
    punstatuscheque = models.IntegerField()
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'hcStatusCheque'


class Hcstatuschequera(models.Model):
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcStatusChequera'


class Hcstatuscliente(models.Model):
    punstatus = models.SmallIntegerField(db_column='PunStatus', unique=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado')  # Field name made lowercase.
    semaforo = models.CharField(db_column='Semaforo', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcStatusCliente'


class Hcstatuscontactos(models.Model):
    punstatus = models.IntegerField(db_column='PunStatus', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcStatusContactos'


class Hcstatusextractos(models.Model):
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcStatusExtractos'


class Hcstatusitemoc(models.Model):
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcStatusItemOC'


class Hcstatusitempres(models.Model):
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcStatusItemPres'


class Hcstatuslistaprecios(models.Model):
    punstatus = models.IntegerField(db_column='punStatus', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hcStatusListaPrecios'


class Hcstatusmaquinas(models.Model):
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcStatusMaquinas'


class Hcstatusmensajedestinatario(models.Model):
    status = models.AutoField(db_column='Status', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcStatusMensajeDestinatario'


class Hcstatusne(models.Model):
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.
    pun = models.AutoField(primary_key=True, db_column='Pun')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcStatusNE'


class Hcstatusoc(models.Model):
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcStatusOC'


class Hcstatusot(models.Model):
    status = models.IntegerField(db_column='Status', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    permiteaviso = models.BooleanField(db_column='PermiteAviso')  # Field name made lowercase.
    materiaprima = models.BooleanField(db_column='MateriaPrima', blank=True, null=True)  # Field name made lowercase.
    otroscostos = models.BooleanField(db_column='OtrosCostos', blank=True, null=True)  # Field name made lowercase.
    partediario = models.BooleanField(db_column='ParteDiario', blank=True, null=True)  # Field name made lowercase.
    cierre = models.BooleanField(db_column='Cierre', blank=True, null=True)  # Field name made lowercase.
    reasignacion = models.BooleanField(db_column='Reasignacion', blank=True, null=True)  # Field name made lowercase.
    terminar = models.BooleanField(blank=True, null=True)
    anular = models.BooleanField(blank=True, null=True)
    modificar = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hcStatusOT'


class Hcstatusotaviso(models.Model):
    status = models.IntegerField(db_column='Status', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcStatusOTAviso'


class Hcstatusotrecepcion(models.Model):
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=80)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcStatusOTRecepcion'


class Hcstatuspedido(models.Model):
    punstatus = models.IntegerField(db_column='PunStatus')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.
    abreviado = models.CharField(db_column='Abreviado', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcStatusPedido'


class Hcstatuspresupuesto(models.Model):
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcStatusPresupuesto'


class Hcstatusproveedores(models.Model):
    punstatus = models.SmallIntegerField(db_column='PunStatus')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcStatusProveedores'


class Hcstatusremito(models.Model):
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hcStatusRemito'


class Hcstatustccomprobantes(models.Model):
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcStatusTCComprobantes'


class Hcsumatoriagastosint(models.Model):
    punitem = models.SmallIntegerField(db_column='PunItem')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcSumatoriaGastosInt'


class Hctipoarticulo(models.Model):
    puntipoarticulo = models.IntegerField(db_column='PunTipoArticulo', unique=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcTipoArticulo'


class Hctipoavisodeuda(models.Model):
    punavisodeuda = models.SmallIntegerField(db_column='PunAvisoDeuda', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcTipoAvisoDeuda'


class Hctipocarga(models.Model):
    puntipocarga = models.AutoField(primary_key=True, db_column='PunTipoCarga')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcTipoCarga'


class Hctipoclientefce(models.Model):
    puntipoclientefce = models.SmallIntegerField(db_column='PunTipoClienteFCE', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcTipoClienteFCE'


class Hctipocosto(models.Model):
    puntipocosto = models.AutoField(primary_key=True, db_column='PunTipoCosto')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcTipoCosto'


class Hctipodato(models.Model):
    puntipodato = models.AutoField(db_column='PunTipoDato', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcTipoDato'


class Hctipodeposito(models.Model):
    puntipodeposito = models.AutoField(primary_key=True, db_column='PunTipoDeposito')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcTipoDeposito'


class Hctipoexportacion(models.Model):
    puntipoexportacion = models.SmallIntegerField(db_column='PunTipoExportacion')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcTipoExportacion'


class Hctipoimporteaduana(models.Model):
    puntipoimporte = models.AutoField(primary_key=True, db_column='PunTipoImporte')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.
    pedirporcentaje = models.SmallIntegerField(db_column='PedirPorcentaje')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcTipoImporteAduana'


class Hctipoinsumo(models.Model):
    puntipoinsumo = models.IntegerField(db_column='PunTipoInsumo')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcTipoInsumo'


class Hctipolistaprecios(models.Model):
    puntipo = models.IntegerField(db_column='punTipo', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hcTipoListaPrecios'


class Hctipomph(models.Model):
    puntipo = models.SmallIntegerField(db_column='PunTipo')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcTipoMPH'


class Hctipompse(models.Model):
    puntipompse = models.IntegerField(db_column='punTipoMPSE', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcTipoMPSE'


class Hctipomovstock(models.Model):
    puntipomovimiento = models.AutoField(primary_key=True, db_column='PunTipoMovimiento')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.
    multiplicador = models.IntegerField(db_column='Multiplicador', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcTipoMovStock'


class Hctipoorigenot(models.Model):
    puntipoorigen = models.AutoField(db_column='PunTipoOrigen', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcTipoOrigenOT'


class Hctipopadroniibb(models.Model):
    puntipopadroniibb = models.SmallIntegerField(db_column='PunTipoPadronIIBB')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=80)  # Field name made lowercase.
    monotributo = models.BooleanField(db_column='Monotributo', blank=True, null=True)  # Field name made lowercase.
    orden = models.SmallIntegerField(db_column='Orden', blank=True, null=True)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcTipoPadronIIBB'


class Hctipoprocesamientofe(models.Model):
    puntipoprocesamiento = models.SmallIntegerField(db_column='PunTipoProcesamiento')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcTipoProcesamientoFE'


class Hctiporegimeniibb(models.Model):
    tiporegimen = models.SmallIntegerField(db_column='TipoRegimen', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcTipoRegimenIIBB'


class Hctiporesponsableentrega(models.Model):
    puntiporesponsableentrega = models.IntegerField(db_column='punTipoResponsableEntrega', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    cuit = models.CharField(db_column='CUIT', max_length=13, blank=True, null=True)  # Field name made lowercase.
    patente = models.CharField(db_column='Patente', max_length=10, blank=True, null=True)  # Field name made lowercase.
    patenteacoplado = models.CharField(db_column='PatenteAcoplado', max_length=10, blank=True, null=True)  # Field name made lowercase.
    avisoalcliente = models.BooleanField(db_column='AvisoAlCliente', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcTipoResponsableEntrega'


class Hctipovalidacionitemsremito(models.Model):
    puntipovalidacion = models.IntegerField(db_column='PunTipoValidacion', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcTipoValidacionItemsRemito'


class Hctipovalor(models.Model):
    tipovalor = models.IntegerField(db_column='TipoValor', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcTipoValor'


class Hctiposcliente(models.Model):
    tipocliente = models.IntegerField(db_column='TipoCliente')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcTiposCliente'


class Hcunidadescot(models.Model):
    codigo = models.SmallIntegerField(db_column='Codigo', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcUnidadesCOT'


class Hcwebservice(models.Model):
    puntipowebservice = models.SmallIntegerField(db_column='PunTipoWebService')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.
    punestructura = models.IntegerField(db_column='PunEstructura', blank=True, null=True)  # Field name made lowercase.
    punestructuraresultado = models.IntegerField(db_column='PunEstructuraResultado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcWebService'


class Hcwebserviceestructuras(models.Model):
    puntipowebservice = models.IntegerField(db_column='PunTipoWebService', blank=True, null=True)  # Field name made lowercase.
    etiquetaestructura = models.CharField(db_column='EtiquetaEstructura', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tiporegistro = models.SmallIntegerField(db_column='TipoRegistro', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hcWebServiceEstructuras'


class Hctipocompinforme(models.Model):
    puntipoinforme = models.IntegerField(db_column='punTipoInforme', blank=True, null=True)  # Field name made lowercase.
    tipocomp = models.CharField(db_column='TipoComp', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hctipocompinforme'


class Lleno(models.Model):
    punarticulo = models.IntegerField(blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    punmoneda = models.IntegerField(blank=True, null=True)
    codigoalternativo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lleno'


class Lleno1(models.Model):
    punarticulo = models.IntegerField(blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    punmoneda = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lleno1'


class Localidades(models.Model):
    punlocalidad = models.AutoField(primary_key=True, db_column='PunLocalidad')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    punlocalidadstarcom = models.IntegerField(db_column='PunLocalidadStarcom', blank=True, null=True)  # Field name made lowercase.
    borrado = models.BooleanField(db_column='Borrado', blank=True, null=True)  # Field name made lowercase.
    punprovincia = models.IntegerField(db_column='punProvincia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'localidades'


class Otbackup(models.Model):
    punordent = models.IntegerField(db_column='PunOrdenT')  # Field name made lowercase.
    puntipoot = models.IntegerField(db_column='PunTipoOT')  # Field name made lowercase.
    prefijo = models.CharField(db_column='Prefijo', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sufijo = models.CharField(db_column='Sufijo', max_length=8, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    puncliente = models.IntegerField(db_column='PunCliente', blank=True, null=True)  # Field name made lowercase.
    punarticulo = models.IntegerField(db_column='PunArticulo', blank=True, null=True)  # Field name made lowercase.
    punitempedido = models.IntegerField(db_column='PunItemPedido', blank=True, null=True)  # Field name made lowercase.
    cantidadpedida = models.DecimalField(db_column='CantidadPedida', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidadafabricar = models.DecimalField(db_column='CantidadAFabricar', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidadequivalente = models.DecimalField(db_column='CantidadEquivalente', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidadcomenzada = models.DecimalField(db_column='CantidadComenzada', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidadterminada = models.DecimalField(db_column='CantidadTerminada', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidadentregada = models.DecimalField(db_column='CantidadEntregada', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pununidad = models.IntegerField(db_column='PunUnidad', blank=True, null=True)  # Field name made lowercase.
    pununidadalternativa = models.IntegerField(db_column='PunUnidadAlternativa', blank=True, null=True)  # Field name made lowercase.
    fechaentrega = models.DateTimeField(db_column='FechaEntrega', blank=True, null=True)  # Field name made lowercase.
    fechaentregadeposito = models.DateTimeField(db_column='FechaEntregaDeposito', blank=True, null=True)  # Field name made lowercase.
    fechacierre = models.DateTimeField(db_column='FechaCierre', blank=True, null=True)  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    punmoneda = models.IntegerField(db_column='PunMoneda', blank=True, null=True)  # Field name made lowercase.
    punplanocliente = models.IntegerField(db_column='PunPlanoCliente', blank=True, null=True)  # Field name made lowercase.
    punplanosinpar = models.IntegerField(db_column='PunPlanoSinPar', blank=True, null=True)  # Field name made lowercase.
    msgproduccion = models.TextField(db_column='msgProduccion', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    observacioncierre = models.CharField(db_column='ObservacionCierre', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    punremitoitem = models.IntegerField(db_column='punRemitoitem', blank=True, null=True)  # Field name made lowercase.
    cantidadascrap = models.IntegerField(db_column='CantidadASCRAP', blank=True, null=True)  # Field name made lowercase.
    cantidadreasignada = models.IntegerField(db_column='CantidadReasignada', blank=True, null=True)  # Field name made lowercase.
    fechaterminada = models.DateTimeField(db_column='FechaTerminada', blank=True, null=True)  # Field name made lowercase.
    fechaanulacion = models.DateTimeField(db_column='FechaAnulacion', blank=True, null=True)  # Field name made lowercase.
    punlistacostocierre = models.IntegerField(db_column='PunListaCostoCierre', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=500, blank=True, null=True)  # Field name made lowercase.
    punlistaventacierre = models.IntegerField(db_column='PunListaVentaCierre', blank=True, null=True)  # Field name made lowercase.
    punrecepcion = models.IntegerField(db_column='PunRecepcion', blank=True, null=True)  # Field name made lowercase.
    codigo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'otbackup'


class Otentregabup(models.Model):
    punordent = models.IntegerField(db_column='PunOrdenT')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4)  # Field name made lowercase.
    pundeposito = models.IntegerField(db_column='PunDeposito')  # Field name made lowercase.
    puntero = models.AutoField(primary_key=True, db_column='Puntero')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'otentregabup'


class Paises(models.Model):
    punpais = models.AutoField(db_column='PUNPAIS', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=100)
    borrado = models.BooleanField()
    codigoafip = models.CharField(db_column='CodigoAfip', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paises'


class Prueba1(models.Model):
    punarticulo = models.IntegerField(blank=True, null=True)
    fob = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    monfob = models.IntegerField(blank=True, null=True)
    fobnac = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    monfobnac = models.IntegerField(blank=True, null=True)
    codigoalternativo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prueba1'


class Prueba1B(models.Model):
    punarticulo = models.IntegerField(blank=True, null=True)
    codigo = models.CharField(max_length=255, blank=True, null=True)
    codigoalternativo = models.CharField(max_length=255, blank=True, null=True)
    fob = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    monfob = models.IntegerField(blank=True, null=True)
    fobnac = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    monfobnac = models.IntegerField(blank=True, null=True)
    pl125 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    monpl125 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prueba1b'


class Prueba1C(models.Model):
    punarticulo = models.IntegerField(blank=True, null=True)
    codigo = models.CharField(max_length=255, blank=True, null=True)
    codigoalternativo = models.CharField(max_length=255, blank=True, null=True)
    fob = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    monfob = models.IntegerField(blank=True, null=True)
    fobnac = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    monfobnac = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prueba1c'


class Prueba1D(models.Model):
    punarticulo = models.IntegerField(blank=True, null=True)
    codigo = models.CharField(max_length=255, blank=True, null=True)
    codigoalternativo = models.CharField(max_length=255, blank=True, null=True)
    fob = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    monfob = models.IntegerField(blank=True, null=True)
    fobnac = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    monfobnac = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prueba1d'


class Prvremitoitemstmp(models.Model):
    idoperacion = models.IntegerField(db_column='IdOperacion', blank=True, null=True)  # Field name made lowercase.
    punitemoc = models.IntegerField(db_column='punItemOC', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    puncentro = models.IntegerField(db_column='PunCentro', blank=True, null=True)  # Field name made lowercase.
    completado = models.SmallIntegerField(db_column='Completado', blank=True, null=True)  # Field name made lowercase.
    idoperacion2 = models.IntegerField(db_column='idOperacion2', blank=True, null=True)  # Field name made lowercase.
    punaccionot = models.IntegerField(db_column='punAccionOT', blank=True, null=True)  # Field name made lowercase.
    pundeposito = models.IntegerField(db_column='PunDeposito', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prvRemitoItemsTMP'


class Prvremitosfacturadospld(models.Model):
    puncomprobante = models.IntegerField(db_column='punComprobante', blank=True, null=True)  # Field name made lowercase.
    punremitoitem = models.IntegerField(db_column='punRemitoItem', blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cotizacion = models.DecimalField(db_column='Cotizacion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prvremitosfacturadosPLD'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class T1(models.Model):
    tipocomprobante = models.CharField(db_column='TipoComprobante', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tipoabc = models.CharField(db_column='TipoABC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    gravado = models.DecimalField(db_column='Gravado', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    iva = models.DecimalField(db_column='Iva', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    exentoynoresp = models.DecimalField(db_column='ExentoYNoResp', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    respmonotributo = models.DecimalField(db_column='RespMonotributo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    percepcioniva = models.DecimalField(db_column='PercepcionIVA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    percepcionib = models.DecimalField(db_column='PercepcionIB', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totgral = models.DecimalField(db_column='TotGral', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't1'


class Tempcarga(models.Model):
    codigo = models.CharField(db_column='CODIGO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    remito = models.CharField(db_column='REMITO', max_length=35, blank=True, null=True)  # Field name made lowercase.
    remitotr = models.CharField(db_column='REMITOTR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ubica = models.FloatField(db_column='UBICA', blank=True, null=True)  # Field name made lowercase.
    recorre = models.FloatField(db_column='RECORRE', blank=True, null=True)  # Field name made lowercase.
    descli = models.CharField(db_column='DESCLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='FECHA', blank=True, null=True)  # Field name made lowercase.
    npaq = models.CharField(db_column='NPAQ', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bulto = models.FloatField(db_column='BULTO', blank=True, null=True)  # Field name made lowercase.
    paquete = models.FloatField(db_column='PAQUETE', blank=True, null=True)  # Field name made lowercase.
    caja = models.FloatField(db_column='CAJA', blank=True, null=True)  # Field name made lowercase.
    esqueleto = models.FloatField(db_column='ESQUELETO', blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='VALOR', blank=True, null=True)  # Field name made lowercase.
    peso = models.FloatField(db_column='PESO', blank=True, null=True)  # Field name made lowercase.
    expre = models.CharField(db_column='EXPRE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cuit = models.CharField(db_column='CUIT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    iva = models.CharField(db_column='IVA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    local = models.CharField(db_column='LOCAL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    entrega = models.CharField(db_column='ENTREGA', max_length=70, blank=True, null=True)  # Field name made lowercase.
    ivacli = models.CharField(db_column='IVACLI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    loccli = models.CharField(db_column='LOCCLI', max_length=40, blank=True, null=True)  # Field name made lowercase.
    dircli = models.CharField(db_column='DIRCLI', max_length=70, blank=True, null=True)  # Field name made lowercase.
    procli = models.CharField(db_column='PROCLI', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cucli = models.CharField(db_column='CUCLI', max_length=13, blank=True, null=True)  # Field name made lowercase.
    codi = models.CharField(db_column='CODI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    notas = models.FloatField(db_column='NOTAS', blank=True, null=True)  # Field name made lowercase.
    cp = models.CharField(db_column='CP', max_length=7, blank=True, null=True)  # Field name made lowercase.
    ubica1 = models.FloatField(db_column='UBICA1', blank=True, null=True)  # Field name made lowercase.
    recorre1 = models.FloatField(db_column='RECORRE1', blank=True, null=True)  # Field name made lowercase.
    ubiind = models.FloatField(db_column='UBIIND', blank=True, null=True)  # Field name made lowercase.
    recoind = models.FloatField(db_column='RECOIND', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tempCARGA'


class Tempexpreso(models.Model):
    codigo = models.CharField(db_column='CODIGO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    descri = models.CharField(db_column='DESCRI', max_length=40, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='DIRECCION', max_length=70, blank=True, null=True)  # Field name made lowercase.
    localidad = models.CharField(db_column='LOCALIDAD', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cpo = models.CharField(db_column='CPO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='TELEFONO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cuit = models.CharField(db_column='CUIT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    iva = models.CharField(db_column='IVA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ubicacion = models.FloatField(db_column='UBICACION', blank=True, null=True)  # Field name made lowercase.
    obs = models.TextField(db_column='OBS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tempExpreso'


class Tmpcartera(models.Model):
    puncheque = models.IntegerField(db_column='PunCheque', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpcartera'


#--------------------------------------------------------------------------------- EDICION DE MODELO DOCUMENTOS
class Documentos(models.Model):
    pundocumento = models.IntegerField(db_column='PunDocumento', primary_key=True)  # Field name made lowercase.
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