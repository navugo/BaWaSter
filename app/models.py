from django.db import models


# Create your models here.
class Ballast(models.Model):
    name = models.CharField(max_length=20)
    maxVolume = models.DecimalField(max_digits=6, decimal_places=2)
    maxSounding = models.DecimalField(max_digits=4, decimal_places=2)
    LCStart = models.DecimalField(max_digits=5, decimal_places=2)
    LCEnd = models.DecimalField(max_digits=5, decimal_places=2)
    TCStart = models.DecimalField(max_digits=5, decimal_places=2)
    TCEnd = models.DecimalField(max_digits=5, decimal_places=2)
    VCStart = models.DecimalField(max_digits=5, decimal_places=2)
    VCEnd = models.DecimalField(max_digits=5, decimal_places=2)

    # All ballast on board must be inserted + Sea

    def __str__(self):
        return str(self.name) + ' (' + str(self.maxVolume) + 'm³)'


class Pump(models.Model):
    name = models.CharField(max_length=20)
    rate = models.DecimalField(max_digits=6, decimal_places=2)
    lastRateTest = models.DateTimeField()
    available = models.BooleanField()

    # Put all ballast possible pumps + Gravity

    def __str__(self):
        return str(self.name) + ' (' + str(self.rate) + 'm³)'


class Quantity(models.Model):
    ballast = models.ForeignKey(Ballast, on_delete=models.CASCADE)
    isClean = models.BooleanField()
    quantity = models.DecimalField('Quantity inside', max_digits=6,
                                   decimal_places=2)
    unpumpable = models.DecimalField(max_digits=6, decimal_places=2)
    # Sourced from more Unfavorable ? Or most quantity ?
    sourceTxt = models.CharField(max_length=20)
    sourceLat = models.DecimalField(max_digits=8,
                                    decimal_places=6)  # decimal degree
    sourceLong = models.DecimalField(max_digits=9, decimal_places=6)
    salinity = models.DecimalField(max_digits=4, decimal_places=2)
    # Mixing may be used for the renewal factor (clean / not clean) ?
    mixing = models.DecimalField('Mixing Ration', max_digits=5,
                                 decimal_places=4)


    def __str__(self):
        return str(self.ballast) + ' (' + str(self.maxVolume) + 'm³)'


class Movements(models.Model):
    dateTimeUTC = models.DateTimeField()
    timeZone = models.DecimalField(max_digits=3, decimal_places=1)
    locationTxT = models.CharField(max_length=20)
    locationLat = models.DecimalField(max_digits=8,
                                      decimal_places=6)  # decimal degree
    locationLong = models.DecimalField(max_digits=9, decimal_places=6)
    density = models.DecimalField(max_digits=6, decimal_places=5)
    temperature = models.IntegerField()
    salinity = models.DecimalField(max_digits=4, decimal_places=2)
    pumpUsed = models.ForeignKey(Pump, on_delete=models.CASCADE)
    ballastFrom = models.ForeignKey(Ballast, on_delete=models.CASCADE)
    ballastTo = models.ForeignKey(Ballast, on_delete=models.CASCADE,
                                  related_name="movements_ballastTo")
    # ballastFrom et ballastTo makes a many to many connection
    quantity = models.DecimalField('Quantity transferred', max_digits=6,
                                   decimal_places=2)
    distance = models.DecimalField('Distance from shore', max_digits=5,
                                   decimal_places=1)
    depth = models.IntegerField()
    speed = models.DecimalField(max_digits=5, decimal_places=1)
    isBWTS = models.BooleanField()
    comment = models.CharField(max_length=200)
