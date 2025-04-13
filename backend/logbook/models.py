from django.db import models

class AuditLog(models.Model):
    audit_id = models.AutoField(primary_key=True)
    table_name = models.TextField(blank=True, null=True)
    operation = models.TextField(blank=True, null=True)
    changed_at = models.DateTimeField(blank=True, null=True)
    record_id = models.IntegerField(blank=True, null=True)
    changed_by = models.TextField(blank=True, null=True)
    old_data = models.JSONField(blank=True, null=True)
    new_data = models.JSONField(blank=True, null=True)

    class Meta:
        db_table = 'audit_log'

    def __str__(self):
        return f"Change in {self.table_name} by {self.changed_by}"


class ConfigAudit(models.Model):
    audit_id = models.AutoField(primary_key=True)
    tail_number = models.CharField(max_length=50, blank=True, null=True)
    config_date = models.DateField(blank=True, null=True)
    technician_name = models.TextField(blank=True, null=True)
    supervisor_name = models.TextField(blank=True, null=True)
    change_time = models.DateTimeField(blank=True, null=True)
    operation = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'config_audit'

    def __str__(self):
        return f"Audit {self.audit_id} - {self.tail_number}"


class ConfigControl(models.Model):
    tail_number = models.ForeignKey('Uav', models.DO_NOTHING, db_column='tail_number', blank=True, null=True)
    payload_type = models.TextField(blank=True, null=True)
    battery_type = models.TextField(blank=True, null=True)
    config_date = models.DateField(blank=True, null=True)
    technician_name = models.TextField(blank=True, null=True)
    supervisor_name = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'config_control'

    def __str__(self):
        return f"Config on {self.tail_number    } at {self.config_date}"
class Lru(models.Model):
    lru_item = models.CharField(max_length=50, blank=True, null=True)
    serial_number = models.CharField(max_length=100, blank=True, null=True)
    assembly_date = models.DateField(blank=True, null=True)
    assembler_name = models.CharField(max_length=100, blank=True, null=True)
    item_hours = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    tail_number = models.ForeignKey('Uav', models.DO_NOTHING, db_column='tail_number', blank=True, null=True)

    class Meta:
        db_table = 'lru'

    def __str__(self):
        return f"{self.lru_item} - {self.serial_number}"


class Malfunction(models.Model):
    malfunction_id = models.AutoField(primary_key=True)
    malfunction_open_date = models.DateField()
    technician_name = models.CharField(max_length=100)
    malfunction_description = models.TextField()
    action_repair_description = models.TextField(blank=True, null=True)
    malfunction_closed_date = models.DateField(blank=True, null=True)
    technician_signature = models.TextField(blank=True, null=True)
    supervisor_signature = models.TextField(blank=True, null=True)
    tail_number = models.ForeignKey('Uav', models.DO_NOTHING, db_column='tail_number', blank=True, null=True)

    class Meta:
        db_table = 'malfunction'

    def __str__(self):
        return f"Malfunction #{self.malfunction_id} - {self.tail_number}"


class Permit(models.Model):
    malfunction = models.ForeignKey(Malfunction, models.DO_NOTHING)
    permit_description = models.TextField()
    validity = models.TextField(blank=True, null=True)
    technician_signature = models.TextField(blank=True, null=True)
    closing_date = models.DateField()

    class Meta:
        db_table = 'permit'

    def __str__(self):
        return f"Permit for malfunction #{self.malfunction_id}"


class Sort(models.Model):
    sort_id = models.AutoField(primary_key=True)
    tail_number = models.ForeignKey('Uav', models.DO_NOTHING, db_column='tail_number')
    flight_number = models.IntegerField(blank=True, null=True)
    sort_purpose = models.TextField(blank=True, null=True)
    battery_id = models.CharField(max_length=50, blank=True, null=True)
    battery_takeoff_voltage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    payload1_type = models.CharField(max_length=100, blank=True, null=True)
    payload1_id = models.CharField(max_length=100, blank=True, null=True)
    payload2_type = models.CharField(max_length=100, blank=True, null=True)
    payload2_id = models.CharField(max_length=100, blank=True, null=True)
    pcu_id = models.CharField(max_length=100, blank=True, null=True)
    pgcs_type = models.CharField(max_length=100, blank=True, null=True)
    flight_configuration_addons = models.TextField(blank=True, null=True)
    launcher_type = models.CharField(max_length=100, blank=True, null=True)
    launcher_id = models.CharField(max_length=100, blank=True, null=True)
    internal_pilot_name = models.CharField(max_length=100, blank=True, null=True)
    technician_name = models.CharField(max_length=100, blank=True, null=True)
    takeoff_time = models.TimeField(blank=True, null=True)
    landing_time = models.TimeField(blank=True, null=True)
    sort_total_time = models.DurationField(blank=True, null=True)
    landing_battery_voltage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    landing_accuracy = models.CharField(max_length=50, blank=True, null=True)
    malfunction = models.BooleanField(blank=True, null=True)
    manager_name = models.TextField(blank=True, null=True)
    permits_check = models.BooleanField(blank=True, null=True)
    pre_mission_check = models.BooleanField(blank=True, null=True)
    pre_mission_check_time = models.TimeField(blank=True, null=True)
    pre_mission_check_name = models.TextField(blank=True, null=True)
    site = models.TextField(blank=True, null=True)
    flight_date = models.DateField(blank=True, null=True)
    after_flight_check_time = models.TimeField(blank=True, null=True)
    after_flight_check_name = models.TextField(blank=True, null=True)
    after_flight_check_date = models.DateField(blank=True, null=True)
    after_flight_check_passed = models.BooleanField(blank=True, null=True)
    uav_hours_current = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    uav_hours_today = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    uav_hours_total = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sorties_current = models.IntegerField(blank=True, null=True)
    sorties_today = models.IntegerField(blank=True, null=True)
    sorties_total = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'sort'

    def __str__(self):
        return f"Sort #{self.sort_id} - {self.tail_number}"


class Uav(models.Model):
    tail_number = models.CharField(primary_key=True, max_length=50)
    model = models.TextField(blank=True, null=True)
    manufacturing_date = models.DateField(blank=True, null=True)
    frequency = models.IntegerField(blank=True, null=True)
    uav_hours = models.IntegerField(blank=True, null=True)
    rata = models.DateField(blank=True, null=True)
    lru_items = models.JSONField(blank=True, null=True)

    class Meta:
        db_table = 'uav'

    def __str__(self):
        return self.tail_number


class UavBalanceControl(models.Model):
    tail_number = models.ForeignKey(Uav, models.DO_NOTHING, db_column='tail_number')
    empty_weight = models.FloatField(blank=True, null=True)
    right_winglet = models.TextField(blank=True, null=True)
    left_winglet = models.TextField(blank=True, null=True)
    nose = models.TextField(blank=True, null=True)
    other = models.TextField(blank=True, null=True)
    technician_name = models.TextField(blank=True, null=True)
    date = models.DateField()

    class Meta:
        db_table = 'uav_balance_control'
        unique_together = (('tail_number', 'date'),)

    def __str__(self):
        return f"Balance - {self.tail_number} ({self.date})"


class UavVersions(models.Model):
    tail_number = models.ForeignKey(Uav, models.DO_NOTHING, db_column='tail_number', blank=True, null=True)
    fcc_version = models.TextField(blank=True, null=True)
    fcc_crc_version = models.TextField(blank=True, null=True)
    fcc_prog_size_version = models.TextField(blank=True, null=True)
    dvr_version = models.TextField(blank=True, null=True)
    dvr_crc_version = models.TextField(blank=True, null=True)
    dvr_prog_size_version = models.TextField(blank=True, null=True)
    last_updated = models.DateField(blank=True, null=True)
    technician_name = models.TextField(blank=True, null=True)
    supervisor_name = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'uav_versions'

    def __str__(self):
        return f"Versions - {self.tail_number}"


class UavWeightsControl(models.Model):
    tail_number = models.ForeignKey(Uav, models.DO_NOTHING, db_column='tail_number', blank=True, null=True)
    fuselage_weight = models.IntegerField(blank=True, null=True)
    right_wing_weight = models.IntegerField(blank=True, null=True)
    left_wing_weight = models.IntegerField(blank=True, null=True)
    right_winglet_weight = models.IntegerField(blank=True, null=True)
    left_winglet_weight = models.IntegerField(blank=True, null=True)
    technician_name = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'uav_weights_control'

    def __str__(self):
        return f"Weight - {self.tail_number} ({self.date})"
