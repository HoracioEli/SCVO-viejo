from django.db import models

# Create your models here.

class Poliza(models.Model):
    poliza = models.CharField(max_length=20)
    asegurado = models.CharField(max_length=200)
    CUIT = models.CharField(max_length=20)
    fecha= models.DateField()


    def __str__(self):
        #para self.fecha quiero que devuelve con formato dia-mes-anio   
        return self.poliza + ' ' + self.asegurado + "- " + self.fecha.strftime("%d-%m-%Y")
    
class Empleado(models.Model):
    nombre = models.CharField(max_length=200)
    CUIL = models.CharField(max_length=20)
    #llave foranea id del modelo Poliza
    id_poliza = models.ForeignKey(Poliza, on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.id) + ' ' + self.nombre + ' ' + self.CUIL