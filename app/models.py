from django.db import models


class Ballast(models.Model):
    """Ballast designs a table containing all ballasts information. Location,
    sounding height, volume and name.
    For transfer purpose, it has also to contain a entry called 'sea', to allow
    loading or discharging water to or from the ship."""
    name = models.CharField(max_length=20)
    maxVolume = models.DecimalField(max_digits=6, decimal_places=2)
    # actualVolume and isClean are to avoid any additional search in database.
    actualVolume = models.DecimalField(max_digits=6, decimal_places=2)
    isClean = models.BooleanField()
    maxSounding = models.DecimalField(max_digits=4, decimal_places=2)
    LCStart = models.DecimalField(max_digits=5, decimal_places=2,
                                  null=True, blank=True)
    LCEnd = models.DecimalField(max_digits=5, decimal_places=2,
                                null=True, blank=True)
    TCStart = models.DecimalField(max_digits=5, decimal_places=2,
                                  null=True, blank=True)
    TCEnd = models.DecimalField(max_digits=5, decimal_places=2,
                                null=True, blank=True)
    VCStart = models.DecimalField(max_digits=5, decimal_places=2,
                                  null=True, blank=True)
    VCEnd = models.DecimalField(max_digits=5, decimal_places=2,
                                null=True, blank=True)

    def __str__(self):
        return str(self.name) + ' [capacity: ' +\
               str(self.maxVolume) + ' m³]'


class Pump(models.Model):
    """Pump designs a table containing all means of loading/discharging
    ballasts. It includes of course Ballast pumps, but also Fire pumps, eductor
    and any kind of transfer like 'by gravity'."""
    name = models.CharField(max_length=20)
    flowRate = models.DecimalField(max_digits=6, decimal_places=2,
                                   null=True, blank=True)
    flowRateTestDate = models.DateTimeField(null=True, blank=True)
    available = models.BooleanField()

    def __str__(self):
        return str(self.name) + ' [' +\
               str(self.flowRate) + ' m³/h]'


class TransferType(models.Model):
    """Direction designs a table containing all sorts of transfer, pump in, pump
    out, exchange of water, stripping, transfer, overflow, ..."""
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Record(models.Model):
    """Record designs a table recording movement of all quantities of
    water in any ballast."""
    ballast = models.ForeignKey(Ballast, on_delete=models.CASCADE)
    startDateTimeUTC = models.DateTimeField()
    startTxt = models.CharField(max_length=20)
    startLat = models.DecimalField(max_digits=8,
                                   decimal_places=6,  # decimal degree
                                   null=True, blank=True)
    startLong = models.DecimalField(max_digits=9, decimal_places=6,
                                    null=True, blank=True)
    quantityInBallastStart = models.DecimalField(max_digits=6,
                                                 decimal_places=2)
    stopDateTimeUTC = models.DateTimeField()
    stopTxt = models.CharField(max_length=20)
    stopLat = models.DecimalField(max_digits=8,
                                  decimal_places=6,  # decimal degree
                                  null=True, blank=True)
    stopLong = models.DecimalField(max_digits=9, decimal_places=6,
                                   null=True, blank=True)
    quantityInBallastStop = models.DecimalField(max_digits=6,
                                                decimal_places=2)
    timeZone = models.DecimalField(max_digits=3, decimal_places=1)
    transferType = models.ForeignKey(TransferType, on_delete=models.CASCADE)
    transferredBy = models.ManyToManyField(Pump)
    transferredQuantity = models.DecimalField(max_digits=6,
                                              decimal_places=2)
    isInUseBWTS = models.BooleanField()
    isClean = models.BooleanField()
    unpumpable = models.DecimalField(max_digits=6, decimal_places=2,
                                     null=True, blank=True)
    ballastFromTo = models.ForeignKey(Ballast, on_delete=models.CASCADE,
                                      related_name="record_ballastFromTo")
    density = models.DecimalField(max_digits=6, decimal_places=5)
    temperature = models.IntegerField()
    salinity = models.DecimalField(max_digits=4, decimal_places=2)
    comment = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.ballast) + ' [actual volume: ' +\
               str(self.quantityInBallastStop) + ' m³]'
