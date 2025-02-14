from django.db import models

from django.contrib.auth.models import User

class Sleep(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    oura_id = models.CharField(max_length=255)
    average_breath = models.FloatField(null=True, blank=True)
    average_heart_rate = models.FloatField(null=True, blank=True)
    average_hrv = models.IntegerField(null=True, blank=True)
    awake_time = models.IntegerField(null=True, blank=True)
    bedtime_end = models.DateTimeField()
    bedtime_start = models.DateTimeField()
    day = models.DateField()
    deep_sleep_duration = models.IntegerField(null=True, blank=True)
    efficiency = models.IntegerField(null=True, blank=True)
    latency = models.IntegerField(null=True, blank=True)
    light_sleep_duration = models.IntegerField(null=True, blank=True)
    low_battery_alert = models.BooleanField()
    lowest_heart_rate = models.IntegerField(null=True, blank=True)
    movement_30_sec = models.CharField(max_length=255, blank=True)
    period = models.IntegerField()
    readiness_score_delta = models.IntegerField(null=True, blank=True)
    rem_sleep_duration = models.IntegerField(null=True, blank=True)
    restless_periods =models.IntegerField(null=True, blank=True)
    sleep_phase_5_min = models.CharField(max_length=255, blank=True)
    sleep_score_delta = models.IntegerField(null=True, blank=True)
    time_in_bed = models.IntegerField()
    total_sleep_duration = models.IntegerField(null=True, blank=True)

class Sample(models.Model):
    interval = models.FloatField()
    timestamp = models.DateTimeField()
    
    class Meta:
        abstract = True

class SampleItem(models.Model):
    # Index for this item in the parent Sample object.
    index = models.IntegerField()
    item = models.FloatField(null=True, blank=True)
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)

class SleepHeartRateSample(Sample):
    sleep = models.OneToOneField(Sleep, on_delete=models.CASCADE, primary_key=True)

class SleepHRVSample(Sample):
    sleep = models.OneToOneField(Sleep, on_delete=models.CASCADE, primary_key=True)

class SleepAlgorithmVersion(models.Model):
    V1 = "v1"
    V2 = "v2"
    SLEEP_ALGORITHM_CHOICES = {
            V1: "v1",
            V2: "v2",
    }
    version = models.CharField(max_length=10,
                               choices=SLEEP_ALGORITHM_CHOICES,
                               default=V2)
    sleep = models.OneToOneField(Sleep, on_delete=models.CASCADE, primary_key=True)

class ReadinessContributors(models.Model):
    activity_balance= models.IntegerField(null=True, blank=True)
    body_temperature= models.IntegerField(null=True, blank=True)
    hrv_balance= models.IntegerField(null=True, blank=True)
    previous_day_activity= models.IntegerField(null=True, blank=True)
    previous_night= models.IntegerField(null=True, blank=True)
    recovery_index= models.IntegerField(null=True, blank=True)
    resting_heart_rate= models.IntegerField(null=True, blank=True)
    sleep_balance= models.IntegerField(null=True, blank=True)
    summary = models.OneToOneField(ReadinessSummary, on_delete=models.CASCADE, primary_key=True)

class ReadinessSummary(models.Model):
    contributors = ReadinessContributors
    score = models.IntegerField(null=True, blank=True)
    temperature_deviation = models.FloatField(null=True, blank=True)
    temperature_trend_deviation = models.FloatField(null=True, blank=True)
    sleep = models.OneToOneField(Sleep, on_delete=models.CASCADE, primary_key=True)

