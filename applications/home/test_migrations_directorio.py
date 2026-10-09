from django.db import connection
from django.db.migrations.executor import MigrationExecutor
from django.test import TransactionTestCase


class DirectorioMigrationTests(TransactionTestCase):
    reset_sequences = True

    def test_empresa_historica_conserva_pk_slug_relaciones_y_se_publica(self):
        executor = MigrationExecutor(connection)
        executor.migrate([('home', '0086_historia_preferencias_grabacion')])
        old_apps = executor.loader.project_state([('home', '0086_historia_preferencias_grabacion')]).apps
        TipoEmpresa = old_apps.get_model('home', 'TipoEmpresa')
        Empresa = old_apps.get_model('home', 'Empresa')
        User = old_apps.get_model('auth', 'User')
        Favorito = old_apps.get_model('home', 'Favorito')
        Valoracion = old_apps.get_model('home', 'Valoracion')
        tipo = TipoEmpresa.objects.create(nombre='Restaurante')
        usuario = User.objects.create(username='historico')
        empresa = Empresa.objects.create(
            id=987, nombre_de_la_empresa='Negocio histórico', nombreUrl='negocio-historico',
            tipo_empresa=tipo, propietario_sitio_web=usuario,
        )
        Favorito.objects.create(usuario=usuario, empresa=empresa)
        Valoracion.objects.create(usuario=usuario, empresa=empresa, puntuacion=5)

        executor = MigrationExecutor(connection)
        executor.migrate([('home', '0090_auditar_importaciones_fase1')])
        new_apps = executor.loader.project_state([('home', '0090_auditar_importaciones_fase1')]).apps
        EmpresaNueva = new_apps.get_model('home', 'Empresa')
        FavoritoNuevo = new_apps.get_model('home', 'Favorito')
        ValoracionNueva = new_apps.get_model('home', 'Valoracion')
        migrada = EmpresaNueva.objects.get(pk=987)
        self.assertEqual(migrada.nombreUrl, 'negocio-historico')
        self.assertEqual(migrada.propietario_sitio_web_id, usuario.pk)
        self.assertEqual(migrada.estado_publicacion, 'published')
        self.assertEqual(migrada.tipo_perfil, 'business')
        self.assertIsNone(migrada.identificador_externo)
        self.assertTrue(FavoritoNuevo.objects.filter(empresa_id=987, usuario_id=usuario.pk).exists())
        self.assertTrue(ValoracionNueva.objects.filter(empresa_id=987, usuario_id=usuario.pk, puntuacion=5).exists())
